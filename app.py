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
import requests,json

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
    if mtext == '新北市天氣' or mtext == '新北市' or mtext == '新北':
        NewTaipeiCity(event)
    elif mtext == '台北市天氣' or mtext == '台北市' or mtext == '台北':
         TaipeiCity(event)
    elif mtext == '桃園市天氣' or mtext == '桃園市' or mtext == '桃園':
        TaoyuanCity(event)
    elif mtext == '新竹縣天氣' or mtext == '新竹市' or mtext == '新竹':
        HsinchuCity(event)
    elif mtext == '基隆市天氣' or mtext == '基隆市' or mtext == '基隆':
        Keelung(event)
    elif mtext == '宜蘭縣天氣' or mtext == '宜蘭市' or mtext == '宜蘭':
        Yilan(event)
    elif mtext == '苗栗縣天氣' or mtext == '苗栗市' or mtext == '苗栗':
        MiaoliCounty(event)
    elif mtext == '台中市天氣' or mtext == '台中市' or mtext == '台中':
        Taichung(event)
    elif mtext == '南投縣天氣' or mtext == '南投縣' or mtext == '南投':
        NantouCounty(event)
    elif mtext == '彰化縣天氣' or mtext == '彰化縣' or mtext == '彰化':
        ChanghuaCounty(event)
    elif mtext == '花蓮縣天氣' or mtext == '花蓮縣' or mtext == '花蓮':
        HualienCounty(event)
    elif mtext == '雲林縣天氣' or mtext == '雲林縣' or mtext == '雲林':
        YunlinCounty(event)
    elif mtext == '嘉義縣天氣' or mtext == '嘉義縣' or mtext == '嘉義':
        ChiayiCounty(event)
    elif mtext == '台南市天氣' or mtext == '台南市' or mtext == '台南':
        TainanCity(event)
    elif mtext == '高雄市天氣' or mtext == '高雄市' or mtext == '高雄':
        kaohsiungcity(event)
    elif mtext == '台東縣天氣' or mtext=='台東縣' or mtext=='臺東縣' or mtext=='臺東' or mtext=='臺東縣天氣':
        TaitungCounty(event)
    elif mtext == '屏東縣天氣' or mtext=='屏東縣'or mtext=='屏東':
        PingtungCounty(event)
        
        
         
        
        
        
        
        
        
   
   
   
        


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

def TaipeiCity(event):
    try:
        response = requests.get('https://opendata.cwb.gov.tw/fileapi/v1/opendataapi/F-C0032-009?Authorization=CWB-841EC847-824A-4A8E-AAC6-606D738A546F&downloadType=WEB&format=JSON')
    
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
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='讀取發生錯誤！'))
def TaoyuanCity(event):
    try:
        response = requests.get('https://opendata.cwb.gov.tw/fileapi/v1/opendataapi/F-C0032-022?Authorization=CWB-841EC847-824A-4A8E-AAC6-606D738A546F&downloadType=WEB&format=JSON')
    
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
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='讀取發生錯誤！'))
def  HsinchuCity(event):
    try:
        response = requests.get('https://opendata.cwb.gov.tw/fileapi/v1/opendataapi/F-C0032-023?Authorization=CWB-841EC847-824A-4A8E-AAC6-606D738A546F&downloadType=WEB&format=JSON')
    
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
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='讀取發生錯誤！'))

def Keelung(event):
    try:
        response = requests.get('https://opendata.cwb.gov.tw/fileapi/v1/opendataapi/F-C0032-011?Authorization=CWB-841EC847-824A-4A8E-AAC6-606D738A546F&downloadType=WEB&format=JSON')
    
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
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='讀取發生錯誤！'))

def Yilan(event):
    try:
        response = requests.get('https://opendata.cwb.gov.tw/fileapi/v1/opendataapi/F-C0032-013?Authorization=CWB-841EC847-824A-4A8E-AAC6-606D738A546F&downloadType=WEB&format=JSON')
    
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
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='讀取發生錯誤！'))
        
def MiaoliCounty(event):
    try:
        response = requests.get('https://opendata.cwb.gov.tw/fileapi/v1/opendataapi/F-C0032-020?Authorization=CWB-841EC847-824A-4A8E-AAC6-606D738A546F&downloadType=WEB&format=JSON')
    
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
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='讀取發生錯誤！'))

def Taichung(event):
    try:
        response = requests.get('https://opendata.cwb.gov.tw/fileapi/v1/opendataapi/F-C0032-021?Authorization=CWB-841EC847-824A-4A8E-AAC6-606D738A546F&downloadType=WEB&format=JSON')
    
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
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='讀取發生錯誤！'))
        
def NantouCounty(event):
    try:
        response = requests.get('https://opendata.cwb.gov.tw/fileapi/v1/opendataapi/F-C0032-026?Authorization=CWB-841EC847-824A-4A8E-AAC6-606D738A546F&downloadType=WEB&format=JSON')

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
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='讀取發生錯誤！'))

def ChanghuaCounty(event):
    try:
        response = requests.get('https://opendata.cwb.gov.tw/fileapi/v1/opendataapi/F-C0032-028?Authorization=CWB-841EC847-824A-4A8E-AAC6-606D738A546F&downloadType=WEB&format=JSON')

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
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='讀取發生錯誤！'))


def HualienCounty(event):
    try:
        response = requests.get('https://opendata.cwb.gov.tw/fileapi/v1/opendataapi/F-C0032-012?Authorization=CWB-841EC847-824A-4A8E-AAC6-606D738A546F&downloadType=WEB&format=JSON')

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
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='讀取發生錯誤！'))

def YunlinCounty(event):
    try:
        response = requests.get('https://opendata.cwb.gov.tw/fileapi/v1/opendataapi/F-C0032-029?Authorization=CWB-841EC847-824A-4A8E-AAC6-606D738A546F&downloadType=WEB&format=JSON')

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
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='讀取發生錯誤！'))
        
        
        
def  ChiayiCounty(event):
    try:
        response = requests.get('https://opendata.cwb.gov.tw/fileapi/v1/opendataapi/F-C0032-018?Authorization=CWB-841EC847-824A-4A8E-AAC6-606D738A546F&downloadType=WEB&format=JSON')

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
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='讀取發生錯誤！'))

def TainanCity(event):
    try:
        response = requests.get('https://opendata.cwb.gov.tw/fileapi/v1/opendataapi/F-C0032-016?Authorization=CWB-841EC847-824A-4A8E-AAC6-606D738A546F&downloadType=WEB&format=JSON')

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
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='讀取發生錯誤！'))


def  kaohsiungcity(event):
    try:
        
        response = requests.get('https://opendata.cwb.gov.tw/fileapi/v1/opendataapi/F-C0032-017?Authorization=CWB-841EC847-824A-4A8E-AAC6-606D738A546F&downloadType=WEB&format=JSON')
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
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='讀取發生錯誤！'))
        

def TaitungCounty(event):
    try:
        response = requests.get('https://opendata.cwb.gov.tw/fileapi/v1/opendataapi/F-C0032-027?Authorization=CWB-841EC847-824A-4A8E-AAC6-606D738A546F&downloadType=WEB&format=JSON')

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
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='讀取發生錯誤！'))
        
def PingtungCounty(event):
    try:
        response = requests.get('https://opendata.cwb.gov.tw/fileapi/v1/opendataapi/F-C0032-025?Authorization=CWB-841EC847-824A-4A8E-AAC6-606D738A546F&downloadType=WEB&format=JSON')

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
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='讀取發生錯誤！'))


if __name__ == "__main__":
    app.run()
