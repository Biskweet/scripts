import os
import time
from bs4 import BeautifulSoup

import gspread
from google.oauth2.service_account import Credentials
import dotenv
import requests

dotenv.load_dotenv()

allowed_float_chars = "1234567890."


scopes = [ "https://www.googleapis.com/auth/spreadsheets" ]
creds = Credentials.from_service_account_file("gsheet_auth.json", scopes=scopes)
client = gspread.authorize(creds)

sheet_id = os.environ["SHEET_ID"]
workbook = client.open_by_key(sheet_id)

sheet = workbook.worksheet("Sheet1")

err_counter = 0

print("Running...")

while True:
    try:
        response = requests.get(os.environ["YGG_PUB_ACCOUNT"])
        if response.status_code >= 300:
            raise Exception()
        
        soup = BeautifulSoup(response.text, "html.parser")
        upload = soup.select(".card-footer strong:first-child")[0]
        download = soup.select(".card-footer strong:last-child")[0]

        upload_val = ''.join(filter(lambda char: char in allowed_float_chars, upload.text))
        download_val = ''.join(filter(lambda char: char in allowed_float_chars, download.text))

        sheet.update_acell("F5", upload_val)
        sheet.update_acell("G5", download_val)
        
    except:
        err_counter += 1
        if err_counter % 10 == 0:
            os.system('python3 /home/warning.py "Could not access yggtorrent for auto-update"')


    time.sleep(60 * 60 * 6)
