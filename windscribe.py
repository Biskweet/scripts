import requests
import json
import dotenv
import os

dotenv.load_dotenv(".env")


HEADERS = {
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0"
}


s = requests.Session()
s.headers.update(HEADERS)

# Fake website request
login_req = s.get("https://windscribe.com/login")

# Now let's obtain the CSRF token
csrf_req = s.post("https://res.windscribe.com/res/logintoken")
csrf_data = json.loads(csrf_req.text)

# looks like
# {'csrf_token': '8580b1028025b7c0d1864be349a3d5a975818476', 'csrf_time': 1710589909}

payload = {
    "login": 1,
    "upgrade": 0,
    "csrf_time": csrf_data["csrf_time"],
    "csrf_token": csrf_data["csrf_token"],
    "username": os.environ["WINDSCRIBE_USERNAME"],
    "password": os.environ["WINDSCRIBE_PASSWORD"],
    "code": ''
}

