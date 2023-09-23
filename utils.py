import urllib.parse

def wasup():
    return 'greetings friend ;)'


def generate_session_key_url(api_key: str):
    return "https://api.icicidirect.com/apiuser/login?api_key="+urllib.parse.quote_plus(api_key)

def load_secrets(filename: str):
    secrets = open(filename).read()
    
