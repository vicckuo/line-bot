from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
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
	line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run()