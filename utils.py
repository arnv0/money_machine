import urllib.parse
import datetime
import pandas as pd

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

def convDate_str2obj(input_date):
    return datetime.datetime.strptime(input_date, "%d:%m:%Y:%H:%M:%S")

def convDate_obj2iso8601(input_date):
    return (input_date - datetime.timedelta(hours=5, minutes=30)).strftime("%Y-%m-%dT%H:%M:%S") + '.000Z'

def options_getHistData(breezeObj, interval, tickerSym, exchangeCode, fromDate, toDate, expDate, right, strikePrice):
    intervals_dict = {"1second":1,"1minute":60,"5minute":300,"30minute":1800,"1day":86400}
    timeA = datetime.datetime.strptime(fromDate, "%d:%m:%Y:%H:%M:%S")
    timeB = datetime.datetime.strptime(toDate, "%d:%m:%Y:%H:%M:%S")
    candles_rem = 0
    if timeA > timeB:
        raise Exception('error: fromDate is later than toDate!')
    deltaTime = timeB - timeA
    num_candles = deltaTime.total_seconds() // intervals_dict[interval]
    if num_candles < 1:
        raise Exception('error: Date/Time range too small!!')
    elif num_candles > 1000:
        candles_rem = num_candles -1000
        print('total candles requested: ',num_candles)
    try:
        result = breezeObj.get_historical_data(interval,
            from_date=convDate(fromDate),to_date=convDate(toDate),
            stock_code=tickerSym,
            exchange_code=exchangeCode,
            product_type='options',
            expiry_date=expDate,
            right=right,
            strike_price=strikePrice)
        if len(result['Success']) == 0:
            print('failed to retrieve data')
            print(result)
        else:
            return (result['Success'],candles_rem)
    except Exception as err:
        print('failed to get data with error: ',err)
        return result

#breeze.get_historical_data_v2(interval="1minute", from_date= "2022-08-15T07:00:00.000Z",to_date= "2022-08-17T07:00:00.000Z", stock_code="NIFTY", exchange_code="NSE",product_type="options",expiry_date="2022-09-29T07:00:00.000Z", right="call", strike_price="")
