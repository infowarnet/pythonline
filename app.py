# encoding: utf-8
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

line_bot_api = LineBotApi('B7oxrv0hrFJrAgUq1Nf6n4p62FqEL5CL1YdHg7RHVaCLyXRQSEdivjwI9V8YeFtl+RQgRTi/9+wI/LOSwj/N6wwfiP+xqe9pe0IvzWqjLpBGduZ6fLPz9HHzV9xQsIbYcGXZhU5cbTYsLPDj87i6tQdB04t89/1O/w1cDnyilFU=') #Your Channel Access Token
handler = WebhookHandler('617d7b0b19d905d2fcb57215546acbfd') #Your Channel Secret

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
        abort(400)

    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_text_message(event):
    text = event.message.text #message from user

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=text)) #reply the same message from user
    

import os
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=os.environ['PORT'])
