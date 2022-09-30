import requests
base_url = 'https//apidiscogs.com/'

def get_releases(release_id):
    endpoint = f'/releases/{release_id}'

    print(f'Getting release #{release_id}')

    resp = requests.get(base_url+endpoint)
    print(resp)



get_releases(249505)
