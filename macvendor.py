#!/usr/bin/env python

import requests
import os
import sys
from requests.exceptions import HTTPError

url = 'https://api.macaddress.io/v1?output=vendor'

if (len(sys.argv) > 1):
    macaddr = sys.argv[1]
    try:
        apikey = os.environ['MACAPIKEY']
        response = requests.get(url,headers={'X-Authentication-Token':apikey},params={'search':{macaddr} })
        print("Vendor for MAC " + macaddr + " is " + response.text)
    except HTTPError as err:
        print(err.reason," : ",  err.code)
    except KeyError as err:
        print("Missing API key in the environment")
    except Exception as err:
        print('Unknown Error occurred: {err}')

else:
    print("\n{ Usage : macvendor.py <MAC address> }")
    print("\tMissing MAC address")
    sys.exit(1)
