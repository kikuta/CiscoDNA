import requests
import json

from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

DNAC_URL = 'https://<ip>/api'
DNAC_URI = 'https://<ip>'
DNAC_USER = '<user>'
DNAC_PASSWORD = '<pass>'

def get_token(url, user, password):
    api_call = '/system/v1/auth/token'
    url += api_call
    response = requests.post(url=url, auth=(user, password), verify=False).json()
    return response["Token"]

def get_devicelist(token, url):
    api_call = '/api/v1/network-device'
    url += api_call
    headers = {'X-Auth-Token':token}
    response = requests.request('GET', url, headers=headers, verify=False).json()
    return json.dumps(response['response'])
    print(json.dumps(response['response'], indent=4))

def get_devicelist_filtered(token, url):
    api_call = '/dna/intent/api/v1/network-device'
    url += api_call
    headers = {'X-Auth-Token':token}
    response = requests.request('GET', url, headers=headers, verify=False).json()
    print(json.dumps(response['response'], indent=4))
    for device in response['response']:
        print('--------')
        print(device['hostname'])
        print(device['softwareVersion'])
        print(device['serialNumber'])

def get_deviceconfigall(token, url):
    api_call = '/dna/intent/api/v1/network-device/config'
    url += api_call
    headers = {'X-Auth-Token':token}
    response = requests.request('GET', url, headers=headers, verify=False).json()
    print(json.dumps(response['response'], indent=4))

def get_enterprisessid(token, url):
    api_call = '/dna/intent/api/v1/enterprise-ssid'
    url += api_call
    headers = {'X-Auth-Token':token}
    response = requests.request('GET', url, headers=headers, verify=False).json()
    print(json.dumps(response, indent=4))
    #print(response)

def get_overallnwhealth(token, url, unixtime):
    api_call = '/dna/intent/api/v1/network-health'
    url += api_call
    url += '?timestamp='
    url += unixtime
    headers = {'X-Auth-Token':token}
    response = requests.request('GET', url, headers=headers, verify=False).json()
    print(json.dumps(response, indent=4))

def get_scheduledtasks(token, url):
    api_call = '/v1/scheduled-job'
    url += api_call
    headers = {'X-Auth-Token':token}
    response = requests.request('GET', url, headers=headers, verify=False).json()
    print(json.dumps(response['response'][0]))

def get_tasks(token, url):
    api_call = '/v1/task'
    url += api_call
    headers = {'X-Auth-Token':token}
    response = requests.request('GET', url, headers=headers, verify=False).json()
    #print(type(response['response']))
    #print(len(response['response']))
    print(json.dumps(response['response']))

def get_clientdetail(token, url, macaddr, unixtime):
    api_call = '/dna/intent/api/v1/client-detail'
    url += api_call
    headers = {
      'X-Auth-Token':token,
      'Content-Type':'application/json',
      '__runsync': "true",
      '__timeout': "30",
      '__persistbapioutput': "true",
    }
    querystring = {
      "timestamp":unixtime,
      "macAddress":macaddr,
    }
    response = requests.request("GET", url, headers=headers, params=querystring, verify=False).json()
    print(json.dumps(response))
