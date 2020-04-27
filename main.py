# line_bot_api = LineBotApi('YOUR_CHANNEL_ACCESS_TOKEN')
# handler = WebhookHandler('YOUR_CHANNEL_SECRET')

# line_bot_api = LineBotApi('LAGLgywVNICYZhq4SB+3c72vkOEuWOWLbCawayERvcyNd/dl3h7mb8AWCS0dRysBG8l7hnWlToADsXkxmu8srSTIesT2Pld0u8YUMNeswCDkYBhPcykNVChnE84kerKfR7Xt5o1CfYmOFu3Vzru19gdB04t89/1O/w1cDnyilFU=')
# handler = WebhookHandler('0ba65702ffed4d5de3887078e07b88ba')

from flask import Flask, request, abort
import os

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

line_bot_api = LineBotApi('LAGLgywVNICYZhq4SB+3c72vkOEuWOWLbCawayERvcyNd/dl3h7mb8AWCS0dRysBG8l7hnWlToADsXkxmu8srSTIesT2Pld0u8YUMNeswCDkYBhPcykNVChnE84kerKfR7Xt5o1CfYmOFu3Vzru19gdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('0ba65702ffed4d5de3887078e07b88ba')

@app.route("/")
def hello_world():
    return "hello world!"

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
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))

if __name__ == "__main__":
#    app.run()
    port = int(os.getenv("PORT"))
    app.run(host="0.0.0.0", port=port)