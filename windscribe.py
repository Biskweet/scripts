import requests as r
import json


HEADERS = {
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0"
}

# Fake website request
login_req = r.get("https://windscribe.com/login", headers=HEADERS)

# Now let's obtain the CSRF token
csrf_req = r.post("https://res.windscribe.com/res/logintoken", headers=HEADERS)
csrf_data = json.loads(csrf_req.text)

