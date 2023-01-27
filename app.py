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
        test(event)
        
   
   
        
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
if __name__ == "__main__":
    app.run()
