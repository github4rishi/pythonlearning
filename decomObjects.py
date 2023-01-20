#! /usr/bin/python3
 
'''

Author      : Bharat Khaneja (bharat.khaneja@oracle.com)
Version     : 1.2
Purpose     : Mark the Servers as Decommissioned in Asset & CMDB

Note(s):
* Auth for WS-API & ASSET has been removed. Please add the same in main function.
* To be used only by GBUCS Compute Provisioning Team.

'''

import requests
from urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
import json
import sys
import argparse
from datetime import datetime

def get_objects_cmdb(objectName,auth):
    url = "https://ws-api.oracleindustry.com/api?obj=cmdb.item&action=query"
    payload = {
            "data": {
                    "query": "name = {}".format(objectName)
        },
            "options": {
                    "relationships.level": 1
            }
    }
    headers = {
      'Accept': 'application/json',
      'Content-Type': 'application/json',
      'Authorization': auth
    }
 
    retry_value = 0
    while retry_value < 3:
        retry_value += 1
        try:
            response = requests.request("POST", url, headers=headers, data=json.dumps(payload))
 
            if response.status_code == 200 and response.json()['success'] == True:
                if 'cmdb.item' in response.json()['data']:
                    if response.json()['data']['cmdb.item'][0]["name"].lower() == objectName.lower():
                        oem_route = response.json()['data']['cmdb.item'][0]['properties']['monitor_inst_id']
                        name = response.json()['data']['cmdb.item'][0]["name"]    # We will be passing exact name to the Monitoring Suspension Function so that case sensitivity is taken care
                    else:
                        output_json = {"Error" : "Input Object name do not match with the Object name in the WS API Query Response -- "+str(response.text)}
                        return output_json
                        
                else:                   
                    output_json = {"Error" : "Object not found in CMDB/WS API response. Return do not contain the field cmdb.item -- "+str(response.text)}
                    return output_json
                    
                output_json = {"oem_route":oem_route,"name":name}
                return output_json
               
            else:
                raise Exception ("Not a valid response from WS API -- " + str(response.text))
                            
        except Exception as e:
            if retry_value < 3:
                continue
            else:
                output_json = {"Error" : "We got error in WS API CMDB Query Endpoint -- "+str(e)}
                return output_json

def decom_objects_cmdb(auth,oem_route,objectName,objectType,cx,emailAddress):
    if objectType == "bsn":
        object_type = "generic_system"
    elif objectType == "server":
        object_type = "host"
    else:
        output_json = {"error" : "objectType should be bsn or server. Exiting!!"}
        print(json.dumps(output_json,indent=2))
        sys.exit(1)
    
    payload = {
                "data": {
                    "cmdb.item": [{
                        "name": objectName,
                        "type": object_type,
                        "properties": {
                            "Decommissioned": "Yes",
                            "Customer_Lifecycle_Status": "Decommissioned"
                        }
                    }]
                },
                "options": {
                    "route": oem_route,
                    "account": str(emailAddress),
                    "cx-ref_no": cx,
                    "account-type": "API"

                }
    }
    
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': auth
    }
 
    url = 'https://ws-api.oracleindustry.com/api?action=update&obj=cmdb.item'
    response = requests.request("POST", url, headers=headers, data=json.dumps(payload))
    return response.json()
 
def get_asset_token(auth):
    url = "https://idcs-9dc693e80d9b469480d7afe00e743931.identity.oraclecloud.com/oauth2/v1/token"
    payload='scope=AssetMgmt.rest.public&grant_type=client_credentials'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': auth
    }
    try:
        response = requests.request("POST", url, headers=headers, data=payload, verify=False)
        return response.json()['access_token']
    except Exception as e:
        output_json = {"error": "Unable to obtain the Asset Token", "error_message":str(e)}
        print(json.dumps(output_json,indent=2))
        sys.exit(1)

def get_objects_asset(objectName,token):
    url = "https://am-gbucs.oracleindustry.com/assetmgmt/search?pageNumber=1&pageSize=50"
    payload = json.dumps({
        "component": [
            {
                "name": objectName,
                "source_system": "DATA-PRIORITY"                
            }
        ]
    })
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': token
    }
    try:
        response = requests.request("POST", url, headers=headers, data=payload, verify=False)
        data =  response.json()['component'][0]
    except Exception as e:
        output_json = {"error" : "Unable to get the Object {} details from Asset".format(objectName),'error_message':response.text}
        return output_json        
 
    if len(data) == 0:
        output_json = {"error" : "Object {} details not found in Asset".format(objectName),'error_message':response.text}
        return output_json        
 
    return {"name":data['name'], "dp_id":data['id'], "status":data['status']}

def decom_objects_asset(dp_id,token):
    url = "https://am-gbucs.oracleindustry.com/assetmgmt/workflow/lifecycle"
    payload = json.dumps({
        "id": dp_id,
        "status": "DECOMMISSIONED",
        "occurred_at": datetime.utcnow().isoformat()[:-3]+'Z'
    })
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload, verify=False)
    if response.status_code == 200:
        output_json = {"Lifecycle Update Message": "Success"}
        return output_json
    else:
        output_json = {"error": "Request cannot be processed", "error_message":str(response.text)}
        return output_json

def get_arguments():
    parser = argparse.ArgumentParser(description="Mark the servers as Decommissioned in CMDB & ASSET")
    parser.add_argument("-f", "--file", dest="file",help="Please add a file which contains the Object Names (BSN Names // Servers with FQDN",required=True)
    parser.add_argument("-c", "--cx", dest="cx", help="Provide a CX # ",required=True)
    parser.add_argument("-e", "--email", dest="email", help="Please provide your Email Address",required=True)
    parser.add_argument("-t", "--type", choices=['server', 'bsn'], help='Please provide the object type.', required=True)
    parser.add_argument("-s", "--system", choices=['cmdb', 'asset'], help='Please provide the system name where you want to make the updates.', required=True)
    args = parser.parse_args()
    return args

def main():
    arguments = get_arguments()
    wsapi_auth = 'Basic ****************************'
    asset_api_auth = 'Basic ****************************'

    asset_token = "Bearer "+ get_asset_token(asset_api_auth)
          
    try:
        with open(arguments.file, 'r') as f_in:
            lines = list(line for line in (l.strip() for l in f_in) if line)
    except:
        print("Failed to open the file with Object Names. Please see if the file is available and the given path is valid")
        sys.exit(1)

    if arguments.system == "asset":
        for object in lines:
            object = object.strip()
            print("Fetching Object - {} - Data_Priority_ID from Asset".format(object))
            get_required_params = get_objects_asset(object,asset_token)
            if "error" in get_required_params:
                print(json.dumps(get_required_params,indent=2)+"\n")
            else:
                dp_id = get_required_params['dp_id']                            
                print("Updating DP ID - {} to Decommissioned in Asset".format(dp_id))
                print(json.dumps(decom_objects_asset(dp_id,asset_token),indent=2))
                print("####################################\n")

    elif arguments.system == "cmdb":
        for object in lines:
            object = object.strip().lower()
            print("Fetching OEM route for "+ object)
            get_required_params = get_objects_cmdb(object,wsapi_auth)
            
            if "Error" in get_required_params:
                print("Aborting the Decommission call for - " + object + "  " + str(get_required_params) + "\n")
            
            else:
                oem_route = get_required_params['oem_route']
                name = get_required_params['name']
                    
                if oem_route in ['mm', 'ctz', 'icstg', 'legacy']:
                    print("OEM Route found as "+oem_route+" Proceeding for CMDB Update call now\n")
                    print(decom_objects_cmdb(wsapi_auth,oem_route,name,arguments.type,arguments.cx,arguments.email))
                
                else:
                    print("OEM Route is other than mm/ctz/icstg/legacy. Skipping the Decommission call for this Object.")
                print("####################################\n")

if __name__ == "__main__":
  main()
