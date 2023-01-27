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
import requests
from bs4 import BeautifulSoup
app = Flask(__name__)

line_bot_api = LineBotApi('DLMk1UwEwqi/umvpTBiZhwzfhZa8d7qsINjyPMl45eZNqapiuBmHJkyLO1HzGXGHqBl3CJkOqcJ2fCqLvltmCnySfNJmu5dMLoGByOnpCJlltP8DYI1Siuqy+2MZTWQBvgRJhTqjkt1k1VTV6IKI4QdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('5b1538f847a42fc9542c6531401b2384')


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
    mtext = event.message.text
    if mtext == '鉅亨':
        sendUse(event)
    elif mtext == '工商時報' or mtext =='t':
        sendcommercial(event)
    elif mtext == '天氣':
        sendUse(event)
    
        
   
   
        
def sendUse(event):
    try:
        base = "https://news.cnyes.com"
        url  = "https://news.cnyes.com/news/cat/headline"
        re   = requests.get(url)
        content = ""
        soup = BeautifulSoup(re.text, "html.parser")
        data = soup.find_all("a", {"class": "_1Zdp"})
        for index, d in enumerate(data):
           if index <6:
            title = d.text
            href  = base + d.get("href")
            content += "{}\n{}\n".format(title, href) #格式化函數
            
            message =  content
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=message))
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='家裡死人'))
def sendcommercial(event):
    try:
        
        url  = "https://ctee.com.tw"
        re   = requests.get(url)
        content = ""
        soup = BeautifulSoup(re.text, "html.parser")
        data = soup.find_all("a", {"class": "post-title post-url"})
        for index, d in enumerate(data):
           if index <6:
            title = d.text
            href  =   d.get("href")
            content += "{}\n{}\n".format(title, href) #格式化函數
            
            message =  content
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=message))
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='家裡死人'))
def sendUse(event):
    try:
        content = ''
        url = 'https://opendata.cwb.gov.tw/fileapi/v1/opendataapi/F-C0032-001?Authorization=CWB-841EC847-824A-4A8E-AAC6-606D738A546F&downloadType=WEB&format=JSON'
        data = requests.get(url)   # 取得 JSON 檔案的內容為文字
        data_json = data.json()    # 轉換成 JSON 格式
        location = data_json['cwbopendata']['dataset']['location']
        for i in location:
            city = i['locationName']    # 縣市名稱
            wx8 = i['weatherElement'][0]['time'][0]['parameter']['parameterName']    # 天氣現象
            maxt8 = i['weatherElement'][1]['time'][0]['parameter']['parameterName']  # 最高溫
            mint8 = i['weatherElement'][2]['time'][0]['parameter']['parameterName']  # 最低溫
            ci8 = i['weatherElement'][3]['time'][0]['parameter']['parameterName']    # 舒適度
            pop8 = i['weatherElement'][4]['time'][0]['parameter']['parameterName']   # 降雨機率
            t  = f'{city}未來 8 小時{wx8}，最高溫 {maxt8} 度，最低溫 {mint8} 度，降雨機率 {pop8} %'
            content += "{}\n".format(t) #格式化函數
            message = content
            
            
        
           
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=message))
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='家裡死人'))
if __name__ == "__main__":
    app.run()
