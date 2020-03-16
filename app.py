from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, StickerSendMessage
)

app = Flask(__name__)

line_bot_api = LineBotApi('X4NcBXr1LHwNIYFlwwM4Wl1eMoOKsG1V9a3MDkpUtunbwZ5t9Wt4VlhuaFHbg1YYWzzp5nuuJR3FFKxFijiOK5zRF3URUu8sIigFsqd4xWyaRMpyjel68ipPAH9F7M43V9dRTIpdP8Hy9a0wUPpDhgdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('cf0d3d8dd8a692a737e177e7a421c3bc')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
	msg = event.message.text
	r = '很抱歉，您說甚麼'

	if '給我貼圖' in msg:
		sticker_message = StickerSendMessage(
   			package_id='1',
    		sticker_id='1'
		)

		line_bot_api.reply_message(
        event.reply_token,
        sticker_message)
		return 

	if msg in ['hi', 'Hi']:
		r = '嗨'
	elif msg == '你吃飯了嗎':
		r = '還沒'
	elif msg == '你是誰':
		r = '我是Vic的機器人，我bb是大王'
	elif '訂位' in msg:
		r = '您想訂位嗎，是嗎?'


	line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=r))


if __name__ == "__main__":
    app.run()