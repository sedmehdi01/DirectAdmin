import requests

def createUser(session,domain,username,password):

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

    session.headers.update(headers)

    changeURL=BASE_URL+'CMD_EMAIL_POP'

    data={

        'fakeusernameremembered':'',

        'fakepasswordremembered':'',

        'action':'create',

        'domain':'sendnews.top',

        'user':'{}'.format(username),

        'email':'{}@{}'.format(username,domain),

        'passwd':'{}'.format(password),

        'passwd2':'{}'.format(password),

        'quota':'50',

        'limit':'',

        'create':'Create'

    }

    session.post(changeURL, data=data)
