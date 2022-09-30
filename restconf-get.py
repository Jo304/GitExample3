import requests

# set up connection parameters in a dictionary
router = {"ip": "ios-xe-mgmt.cisco.com", "port": "9443",
          "user": "root", "password": "D_Vay!106"}

# set REST API headers 
headers = {"Accept": "application/yang-data+json"
           "Content-Type": "application/yang-data+json"}

url = f'https://{router['ip']
