from __future__ import print_function
import requests
import json
import datetime
import time
import sys
import json
import logging
from argparse import ArgumentParser
from kikuta_def import *

from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def show_templates(token, url):
    api_call = '/dna/intent/api/v1/template-programmer/template'
    url += api_call
    headers = {'X-Auth-Token':token}
    print("Available Templates:")
    response = requests.request('GET', url, headers=headers, verify=False).json()
    print(json.dumps(response, indent=4))
    #print ('\n'.joinsorted([ '  {0}/{1}'.format(project['projectName'], project['name']) for project in result])))

def get_template_id(fqtn):
    parts = fqtn.split("/")
    projectName = parts[0]
    templateName = parts[1]
    print ('Looking for: {0}/{1}'.format(projectName, templateName))
    result = get_url("template-programmer/template")

    max = 0
    id = 0
    for project in result:
        if project['projectName'] == projectName and project['name'] == templateName:
            # look for latest version

            for v in project['versionsInfo']:
                #if v['version'] > max:
                if int(v['version']) > max:
                    max = int(v['version'])
                    id = v['id']
    return id,max

def execute(id, reqparams, device, params, doForce):
    #parts = deviceParams.split(';')
    #device = parts[0]

    #params = json.loads(parts[1])
    print ("\nExecuting template on:{0}, with Params:{1}".format(device,params))

    # need to check device params to make sure all present
    payload = {
    "templateId": id,
    "forcePushTemplate" : doForce,
    "targetInfo": [
     {

        "id": device,
        "type": "MANAGED_DEVICE_IP",
        "params": json.loads(params)
        }
     ]
    }
    print ("payload", payload)
    return post_and_wait("template-programmer/template/deploy", payload)

if __name__ == "__main__":
    auth_token = get_token(DNAC_URL, DNAC_USER, DNAC_PASSWORD)
    show_templates(auth_token, DNAC_URI)
