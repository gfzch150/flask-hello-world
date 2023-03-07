from flask import Flask, request, abort
import requests,json
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

line_bot_api = LineBotApi('DLMk1UwEwqi/umvpTBiZhwzfhZa8d7qsINjyPMl45eZNqapiuBmHJkyLO1HzGXGHqBl3CJkOqcJ2fCqLvltmCnySfNJmu5dMLoGByOnpCJlltP8DYI1Siuqy+2MZTWQBvgRJhTqjkt1k1VTV6IKI4QdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('5b1538f847a42fc9542c6531401b2384')


@app.route("/", methods=['POST'])
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
    mtext = event.message.text
    if mtext == '新北市天氣'or mtext =='新北市':
        NewTaipeiCity(event)
   
        
        
         
        
        
        
        
        
        
   
   
   
        


def NewTaipeiCity(event):
    try:
        response = requests.get('https://opendata.cwb.gov.tw/fileapi/v1/opendataapi/F-C0032-010?Authorization=CWB-841EC847-824A-4A8E-AAC6-606D738A546F&downloadType=WEB&format=JSON')
    
        # 將回應的 JSON 資料轉換成 Python 字典
        data = json.loads(response.text)
        location = data['cwbopendata']['dataset']['parameterSet']['parameter']
        for i in range(1,2):
            c = location[i]['parameterValue']
        message = [
            TextSendMessage(text = c)
   
         ]
        
        
       
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='讀取錯誤！'))





if __name__ == "__main__":
    app.run()
