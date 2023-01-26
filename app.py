from flask import Flask
app = Flask(__name__)
from linebot import  LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage, FlexSendMessage
import requests

line_bot_api = LineBotApi('DLMk1UwEwqi/umvpTBiZhwzfhZa8d7qsINjyPMl45eZNqapiuBmHJkyLO1HzGXGHqBl3CJkOqcJ2fCqLvltmCnySfNJmu5dMLoGByOnpCJlltP8DYI1Siuqy+2MZTWQBvgRJhTqjkt1k1VTV6IKI4QdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('5b1538f847a42fc9542c6531401b2384')

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'
