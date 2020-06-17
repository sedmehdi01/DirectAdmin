import requests

def login(domain,username,password):
    BASE_URL = "http://{}:2222/".format(domain)

    USER_AGENT='Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0'

    session = requests.Session()

    session.headers = {'user-agent':USER_AGENT,'Referer':BASE_URL}

    headers = {

        "Host": "{}:2222".format(domain),

        "Accept": "*/*",

        "Accept-Language": "en-US,en;q=0.5",

        "Accept-Encoding": "gzip, deflate",

        "Connection": "close",

    }
    LOGIN_URL = BASE_URL + "CMD_LOGIN"

    session = requests.Session()

    session.headers = {'user-agent':USER_AGENT,'Referer':LOGIN_URL}



    session.get(BASE_URL)

    login_data = {'referer':'/','username':'{}'.format(username),'password':'{}'.format(password)}



    session.post(LOGIN_URL, data=login_data)



    return(session)
