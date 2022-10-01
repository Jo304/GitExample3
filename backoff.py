import requests
from time import sleep

base_url = 'https://api.discogs.com/'

backoffs = {
    "factor" : 1.3,
    "wait" : 1,
    "max_tries" : 5
}

def get_releases(release_id):
    endpoint = f'/releases/{release_id}'

    print(f'Getting release #{release_id}')

    resp = requests.get(base_url+endpoint)
    resp_code = resp.status_code

    return resp_code


for i in range(0,30):
    tries = 0
    resp_code = 0
    while resp_code 