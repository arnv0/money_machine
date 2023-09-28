#!/usr/bin/env python3

from utils import *
from breeze_connect import BreezeConnect
import datetime

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

    def histDataFetcher(from_date,interval, ticker,exchange):
        intervals_dict = {"1second":1,"1minute":60,"5minute":300,"30minute":1800,"1day":86400}
        MAX_CANDLES = 1000
        now = datetime.datetime.now()
        fromDateObj = convDate_str2obj(from_date)
        candlesToGet = (now-fromDateObj).total_seconds() // intervals_dict[interval]
        flag = 0
        final_results = []
        while candlesToGet > 0:
            result = breeze.get_historical_data_v2(interval=interval,
            from_date = convDate_obj2iso8601(fromDateObj),
            to_date = convDate_obj2iso8601(now),
            stock_code = "NIFTY",
            exchange_code = "NSE",
            product_type = "",
            expiry_date = "",
            right = "",
            strike_price = "")
            if len(result['Success']) == 0:
                print('0 candles was returned!')
                return None
            candlesToGet -= len(result['Success'])
            fromDateObj += datetime.timedelta(seconds=1000*intervals_dict[interval])
            final_results += result['Success']
        return final_results
