import requests
import json
from kikuta_def import *

from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

auth_token = get_token(DNAC_URL, DNAC_USER, DNAC_PASSWORD)
get_devicelist(auth_token, DNAC_URI)
