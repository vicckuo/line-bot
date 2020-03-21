from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, StickerSendMessage, ImageSendMessage
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

	if '瑞藝' in msg:
		r = '臭臭師傅之王'
	elif '重錡' in msg:
		r = '臭臭'
	elif '小乖' in msg:
		r = '臭臭'	
	elif '明軒' in msg:
		r = '8+9'
	elif '禹豪' in msg:
		r = '水上'	
	elif '宜正' in msg:
		r = '柯有倫'
	elif '宥騰' in msg:
		r = '87'
	elif '沅丞' in msg:
		r = '智障腦包喜憨兒狗一條'	
	elif '峻豪' in msg:
		r = '帥'
	elif 'Vic' in msg:
		r = '帥'
	elif 'vic' in msg:
		r = '帥'	
	elif '邁耳音樂' in msg:
		r = 'https://easy4music.com 好聽~推起來'
	elif '飛機錡' in msg:
		image_message = ImageSendMessage(
   			 original_content_url='https://upload.cc/i1/2020/03/21/ojfc8h.jpeg',
   			 preview_image_url='https://upload.cc/i1/2020/03/21/ojfc8h.jpeg'
		)

		line_bot_api.reply_message(
        event.reply_token,
        image_message)
        r = '智力偏弱'
		return 


	line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=r))


if __name__ == "__main__":
    app.run()