import urllib3
import json
import pprint

def api_test():
    http = urllib3.PoolManager()
    req = http.request('GET', 'https://www.fantasyfootballnerd.com/service/players/json/5ezuys37f3bd/')
    stats = json.loads(req.data.decode('utf-8'))


    for stat in stats['Players']:
        if stat['active'] == '1':
            print(stat['playerId'])
            print(stat['displayName'])
            print(stat['team'])
            print(stat['position'])
            print(stat['jersey'])
            print()