import urllib
import datetime
import pandas as pd
import yfinance as yf
import os
import zipfile

def wasup():
    return 'greetings friend ;)'

def get_daily_zipfile():
    url = 'https://directlink.icicidirect.com/NewSecurityMaster/SecurityMaster.zip'
    timestamp = convDateYf_obj2str(datetime.datetime.now())
    if not os.path.exists('./data/daily_master_files/{}'.format(timestamp)):
        os.makedirs('./data/daily_master_files/{}'.format(timestamp))
    if not os.path.exists('./data/daily_master_files/{}/SecurityMaster.zip'.format(timestamp)):
        print('downloading file...')
        try:
            urllib.request.urlretrieve(url,'./data/daily_master_files/{}/SecurityMaster.zip'.format(timestamp))
            print('file downloaded!')
        except Exception as e:
            print('failed to get daily master file from {} on {} with error {}'.format(url,timestamp,e))
        print('extracting file...')
        with zipfile.ZipFile('./data/daily_master_files/{}/SecurityMaster.zip'.format(timestamp),'r') as f:
            f.extractall('./data/daily_master_files/{}'.format(timestamp))
            print('all done!')
    else:
        print('daily master file for todays date already exists!')

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

def convDateBrz_str2obj(input_date):
    return datetime.datetime.strptime(input_date, "%d:%m:%Y:%H:%M:%S")

def convDateBrz_obj2iso8601(input_date):
    return (input_date - datetime.timedelta(hours=5, minutes=30)).strftime("%Y-%m-%dT%H:%M:%S") + '.000Z'


#breeze.get_historical_data_v2(interval="1minute", from_date= "2022-08-15T07:00:00.000Z",to_date= "2022-08-17T07:00:00.000Z", stock_code="NIFTY", exchange_code="NSE",product_type="options",expiry_date="2022-09-29T07:00:00.000Z", right="call", strike_price="")
