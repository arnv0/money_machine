#!/usr/bin/env python3

from utils import *
from breeze_connect import BreezeConnect
import datetime
import yfinance as yf
import pandas as pd

secrets = load_config('secrets.cfg')
API_KEY = secrets['API_KEY']
SECRET_KEY = secrets['SECRET_KEY']
API_SESSION = secrets['API_SESSION']



if __name__ == '__main__':
    print(wasup())
    breeze = BreezeConnect(api_key=API_KEY)
    print('login here to generate generate a session key:',generate_session_key_url(API_KEY))
    try:
        breeze.generate_session(api_secret=SECRET_KEY,session_token=API_SESSION)
        print('session begun at: {}'.format(datetime.datetime.now().strftime("%d:%m:%y:%H:%M:%S")))
    except Exception as e:
        print('failed to generate session: {}'.format(e))


    try:
        breeze.ws_connect()
        print('websocket connected successfully!')
    except Exception as e:
        print('websocket failed: ',e)


    breeze.on_ticks = on_tick

    # todo;
    def test_subscribe():
        breeze.subscribe_feeds(exchange_code="NSE",
        stock_code="NIFTY",
        product_type="futures",
        expiry_date="",
        strike_price="",
        right="",
        get_exchange_quotes=True,
        get_market_depth=False)

    def test_unsubscribe():
        breeze.unsubscribe_feeds(exchange_code="NSE",
        stock_code="NIFTY",
        product_type="futures",
        expiry_date="",
        strike_price="",
        right="",
        get_exchange_quotes=True,
        get_market_depth=False)
