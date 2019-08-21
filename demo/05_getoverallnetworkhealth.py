import requests
import json
import datetime
import time

from kikuta_def import *

from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

if __name__ == "__main__":
    print("===", "Get Overall Network Health", "===")
    dtstr = input("調査対象日時を入力してください yyyy-mm-dd hh:mm:ss ： ")
    dt = datetime.datetime.strptime(dtstr, '%Y-%m-%d %H:%M:%S')
    unixtime = str(round(dt.timestamp() * 1000))
    auth_token = get_token(DNAC_URL, DNAC_USER, DNAC_PASSWORD)
    get_overallnwhealth(auth_token, DNAC_URI, unixtime)

