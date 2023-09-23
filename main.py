#!/usr/bin/env python3

from utils import *
from breeze_connect import BreezeConnect
import datetime



if __name__ == '__main__':
    print(wasup())
    breeze = BreezeConnect(api_key=API_KEY)
    print('login here to generate generate a session key:',generate_session_key_url(API_KEY))
    try:
        breeze.generate_session(api_secret=SECRET_KEY,session_token=API_SESSION)
        print('session begun at: {}'.format(datetime.datetime.now().strftime("%d:%m:%y:%H:%M:%S")))
    except Exception as e:
        print('failed to generate session: {}'.format(e))
