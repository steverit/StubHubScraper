import requests
import sqlite3
import time
import json
import base64
import pprint

def login():
    # Enter user's API key, secret, and Stubhub login
    app_token = 'J6QF_BD8bfKsrMaCVVCwfKGJOV0a'
    consumer_key = 'HG3A0XLMe7N67e8HSTkZFUNmzNca'
    consumer_secret = '2aZU6zhCLIRew5jmM6pAGHOoH9ka'
    stubhub_username = 'jackson.cheek@gmail.com'
    stubhub_password = 'd3p8EL4sED'

    combo = consumer_key + ':' + consumer_secret
    basic_authorization_token = base64.b64encode(combo)

    url = 'https://api.stubhub.com/login'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'Basic ' + basic_authorization_token,}
    body = {
        'grant_type': 'password',
        'username': stubhub_username,
        'password': stubhub_password,
        'scope': 'PRODUCTION'}

    r = requests.post(url, headers=headers, data=body)

    token_response = json.loads(r.content)
    access_token = token_response['access_token']
    user_GUID = r.headers['X-StubHub-User-GUID']
    headers['x-stubhub-user-guid'] = user_GUID

    return access_token, headers, body

def buildDatabase():
    conn = sqlite3.connect('tickets.db')
    cursor = conn.cursor()

    # Create table
    cursor.execute('''CREATE TABLE IF NOT EXISTS tickets
                 (event TEXT, ticket_ID TEXT, total_count_history TEXT, price_history TEXT, time_history TEXT)''')

    conn.commit()

    return conn, cursor

def handleResponse(data, cursor, conn):

    event = 'Washington Redskins vs Green Bay Packers [11/20/2016]'

    tickets = data['listing']

    ticket_IDs = [ticket['listingId'] for ticket in tickets]
    prices = [ticket['currentPrice']['amount'] for ticket in tickets]

    total = data['totalTickets']

    current_time = int(round(time.time() * 1000))

    for (i, j) in zip(ticket_IDs, prices):
        params = (i,)

        cursor.execute("SELECT * FROM tickets WHERE ticket_ID=?", params)
        result = cursor.fetchone()
        result_serialized = json.dumps(result).encode('utf-8')
        result_json = json.loads(result_serialized)

        print result

        if (result_json is not None):
            count_params = result_json[2] + ', ' + str(total)
            price_params = result_json[3] + ', ' + str(j)
            time_params = result_json[4] + ', ' + str(current_time)

            params = (count_params, price_params, time_params, str(i),)

            cursor.execute("UPDATE tickets SET total_count_history=?, price_history=?, time_history=? WHERE ticket_ID=?", params)
            conn.commit()
        else:
            params = (str(event), str(i), str(total), str(j), str(current_time))
            cursor.execute("INSERT INTO tickets VALUES (?, ?, ?, ?, ?)", params)
            conn.commit()

if __name__ == "__main__":
    conn, cursor = buildDatabase()

    while True:
        access_token, headers, body = login()
        app_token = 'J6QF_BD8bfKsrMaCVVCwfKGJOV0a'

        headers = {}
        headers['Authorization'] = 'Bearer ' + access_token
        # headers['Accept'] = 'application/json'
        # headers['Accept-Encoding'] = 'application/json'

        eventid = '9566660'
        params = {}
        params['eventId'] = eventid

        info_url = 'https://api.stubhub.com/search/inventory/v2'

        info = requests.get(info_url, headers=headers, params=params)
        handleResponse(json.loads(info.content), cursor, conn)
        time.sleep(300)

