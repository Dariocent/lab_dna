import requests
from requests.auth import HTTPBasicAuth
from dnac_config import DNAC_IP, DNAC_PORT, DNAC_USER, DNAC_PASSWORD
from get_device_list import get_auth_token

def print_interface_info(interface_info):
    print("{0:42}{1:17}{2:12}{3:18}{4:17}{5:10}{6:15}".
          format("portName", "vlanId", "portMode", "portType", "duplex", "status", "lastUpdated"))
    for int in interface_info['response']:
        print("{0:42}{1:10}{2:12}{3:18}{4:17}{5:10}{6:15}".
              format(str(int['portName']),
                     str(int['vlanId']),
                     str(int['portMode']),
                     str(int['portType']),
                     str(int['duplex']),
                     str(int['status']),
                     str(int['lastUpdated'])))
        
def get_device_int(device_id):
    """
    Building out function to retrieve device interface. Using requests.get
    to make a call to the network device Endpoint
    """
    token = get_auth_token() # Get Token
    url = "https://sandboxdnac.cisco.com/api/v1/interface"
    hdr = {'x-auth-token': token, 'content-type' : 'application/json'}
    querystring = {"macAddress": device_id} 
    resp = requests.get(url, headers=hdr, params=querystring) 
    interface_info_json = resp.json()
    print_interface_info(interface_info_json)

def get_device_id(device_json):
    for device in device_json['response']: 
        print("Fetching Interfaces for Device Id ----> {}".format(device['id']))
        print('\n')
        get_device_int(device['id'])
        print('\n')

if __name__ == "__main__":
    get_device_int('5f03d9a9-33df-450e-b0c3-6bcb5f721688')