import urllib.parse

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
