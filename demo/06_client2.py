import requests
import json
import datetime
import time

from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


DNAC_URL = 'https://10.71.130.60'
DNAC_USER = 'admin'
DNAC_PASSWORD = 'C1sco12345!'

def get_token(url, user, password):
    api_call = '/api/system/v1/auth/token'
    url += api_call
    response = requests.post(url=url, auth=(user, password), verify=False).json()
    return response["Token"]

def get_clientdetail(url, auth_token, unixtime, macaddr):
    assurl = url + '/dna/assurance/home#mac/' + macaddr
    api_call = '/dna/intent/api/v1/client-detail'
    url += api_call
    querystring = {"timestamp":unixtime, "macAddress":macaddr}
    headers = {
        'X-Auth-Token':auth_token,
        'Content-Type': "application/json",
        '__runsync': "true",
        '__timeout': "30",
        '__persistbapioutput': "true",
        }
    response = requests.request("GET", url, headers=headers, params=querystring, verify=False).json()
    print("=== 調査結果は... ===")
    time.sleep(2)
    #print("合計ヘルススコア(100点)：", response['detail'])
    print("合計ヘルススコア(100点)：", response['detail']['healthScore'][0]['score'] *10)
    print(" +オンボーディングヘルススコア：", response['detail']['healthScore'][1]['score'] *10)
    print(" +接続状況ヘルススコア：", response['detail']['healthScore'][2]['score'] *10)
    print("===", "スコアが100点未満の場合は、以下URLから調査できます", "===")
    print(assurl)
    print("=== THANK YOU ===")

    #print(response['detail']['healthScore'][0]['reason'])
    #print(response['detail']['healthScore'][1]['reason'])
    #print(response['detail']['healthScore'][2]['reason'])

if __name__ == "__main__":
    print("===", "端末健康診断アプリ0.1", "===")
    macaddr = input("端末のMACアドレスを入力してください： ")
    dtstr = input("日時を入力してください yyyy-mm-dd hh:mm:ss ： ")
    dt = datetime.datetime.strptime(dtstr, '%Y-%m-%d %H:%M:%S')
    unixtime = str(round(dt.timestamp() * 1000))
    auth_token = get_token(DNAC_URL, DNAC_USER, DNAC_PASSWORD)
    get_clientdetail(DNAC_URL, auth_token, unixtime, macaddr)
