import urllib.parse
import datetime
import pandas as pd
import yfinance as yf

def wasup():
    return 'greetings friend ;)'


def generate_session_key_url(api_key: str):
    return "https://api.icicidirect.com/apiuser/login?api_key="+urllib.parse.quote_plus(api_key)

def load_config(filename: str, split_by='='):
    dict = {}
    secrets = open(filename).read()
    secrets = secrets.split('\n')
    secrets.remove('')
    for secret in secrets:
        a, b = secret.split(split_by)
        dict[a] = b
    return dict

#breeze callback
def on_tick(ticks):
    print("\ntick: {}\n".format(ticks))


def convDateYf_str2obj(input_date):
    return datetime.datetime.strptime(input_date,'%Y-%m-%d')

def convDateYf_obj2str(input_obj):
    return datetime.datetime.strftime(input_obj,'%Y-%m-%d')

#breeze.get_historical_data_v2(interval="1minute", from_date= "2022-08-15T07:00:00.000Z",to_date= "2022-08-17T07:00:00.000Z", stock_code="NIFTY", exchange_code="NSE",product_type="options",expiry_date="2022-09-29T07:00:00.000Z", right="call", strike_price="")
