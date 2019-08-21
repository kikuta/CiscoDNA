import requests
import json

from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

DNAC_URL = 'https://10.71.130.60/api'
DNAC_USER = 'admin'
DNAC_PASSWORD = 'C1sco12345!'

def get_token(url, user, password):
    api_call = '/system/v1/auth/token'
    url += api_call
    response = requests.post(url=url, auth=(user, password), verify=False).json()

    print(response["Token"])
    return response["Token"]

get_token(DNAC_URL, DNAC_USER, DNAC_PASSWORD)

