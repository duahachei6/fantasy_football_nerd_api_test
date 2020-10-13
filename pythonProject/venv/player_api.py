import urllib3
import json
import mysql.connector

def api_test():
    http = urllib3.PoolManager()
    req = http.request('GET', 'https://www.fantasyfootballnerd.com/service/players/json/5ezuys37f3bd/')
    stats = json.loads(req.data.decode('utf-8'))

    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "toor",
        database = "capstone_proj"
    )

    mycursor = mydb.cursor()

    row_inserted = 0;
    for stat in stats['Players']:
        if stat['active'] == '1':
            playerId = int(stat['playerId'])
            displayName = stat['displayName']
            team = stat['team']
            position = stat['position']
            jersey = stat['jersey']

            sql = "INSERT INTO players (playerId, displayName, team, position, jersey) " \
                  "VALUES (%s, %s, %s, %s, %s)"

            val = (playerId,displayName,team,position,jersey)
            mycursor.execute(sql, val)

            mydb.commit()

            row_inserted = row_inserted+1

            """print(stat['playerId'])
                        print(stat['displayName'])
                        print(stat['team'])
                        print(stat['position'])
                        print(stat['jersey'])
                        print()"""

    print(row_inserted, "record(s) inserted")

