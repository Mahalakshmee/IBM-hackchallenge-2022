import telebot
import requests
from bs4 import BeautifulSoup
bot_token = '5692968574:AAF6ftuVirseGFVeO07bG9WCiXtmPco0I0k'

bot = telebot.TeleBot(token=bot_token)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message,'Welcome!')

def code(data,message):
    URL = data
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

    page = requests.get(URL, headers=headers)

    soup1 = BeautifulSoup(page.content, "html.parser")

    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")
    try:
        title = soup2.find(id='productTitle').get_text()
        title = title.strip()
        title = title.replace(" ", "-")
        title = title.replace(".", "-")
        title = title.replace("(", "")
        title = title.replace(")", "")
        title = title.replace("/", "-")
        title = title.replace(",", "")
        title =  title.lower()
        print(title)
        url1 = 'https://pricehistoryapp.com/product/'
        url = f"{url1}{title}"
        user_agent = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0',
        }
        response = requests.get(url = url, headers = user_agent )
        soup = BeautifulSoup(response.content, 'lxml')

        new = soup.find_all('div',{'class': 'content-width mx-auto px-3'})
        def strip_html_tag(new):
            soup = BeautifulSoup(new,"html.parser")
            stripped_text = soup.get_text()
            return stripped_text
        bot.reply_to(message,strip_html_tag(str(new)))
    except AttributeError:
        print("ID: -")


@bot.message_handler(commands=['url'])
def send_welcome(message):
    data= message.text
    data=message.text.replace("/url","")
    print(data)
    code(data,message)
    

bot.polling()