import flask
import requests.exceptions
from flask import request
import os
from bot import Bot, QuoteBot, ImageProcessingBot

app = flask.Flask(__name__)

TELEGRAM_TOKEN = os.environ['TELEGRAM_TOKEN']
TELEGRAM_APP_URL = os.environ['TELEGRAM_APP_URL']


@app.route('/', methods=['GET'])
def index():
    return 'Ok'


@app.route(f'/{TELEGRAM_TOKEN}/', methods=['POST'])
def webhook():
    try:
        req = request.get_json()
        print(req['message'])
        bot.handle_message(req['message']) # in case of stuck need to comment this line
        return 'Ok'
    except requests.exceptions.RequestException as e:
        print(e)


if __name__ == "__main__":
    bot = ImageProcessingBot(TELEGRAM_TOKEN, TELEGRAM_APP_URL)
    app.run(host='0.0.0.0', port=8443)
