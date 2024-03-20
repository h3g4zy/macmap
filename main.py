import requests
import uuid
import json
from flask import Flask, jsonify, request

app = Flask(__name__)

def fetch_ntm_measures(reporter='392', partner='156', product='382764010'):
    # Generate a random ASP.NET_SessionId
    session_id = uuid.uuid4()

    # Define the URL
    url = 'https://www.macmap.org/api/results/ntm-measures'

    # Define the query parameters with function arguments
    params = {
        'reporter': reporter,
        'partner': partner,
        'product': product
    }

    # Define the headers
    headers = {
        'Content-Length': '0',
        'Cookie': f'ASP.NET_SessionId={session_id}; path=/; secure; HttpOnly; SameSite=None; SameSite=None; Secure',
        'Sec-Ch-Ua': '"Not(A:Brand";v="24", "Chromium";v="122"',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Content-Type': 'application/json; charset=utf-8',
        'X-Requested-With': 'XMLHttpRequest',
        'Sec-Ch-Ua-Mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.112 Safari/537.36',
        'Sec-Ch-Ua-Platform': '"Windows"',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://www.macmap.org/en/query/results?reporter=392&partner=156&product=382764&level=6',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9',
        'Priority': 'u=1, i',
        'Connection': 'close',
    }

    # Make the request with query parameters
    response = requests.get(url, headers=headers, params=params)

    # Check if the request was successful
    if response.status_code == 200:
        # Return the JSON response
        return response.json()
    else:
        # Return the HTTP status code and reason if the request failed
        return {'status_code': response.status_code, 'reason': response.reason}

def fetch_ntm_measures_detail(reporter='392', partner='156', product='382764010'):
    # Generate a random ASP.NET_SessionId
    session_id = uuid.uuid4()

    # Define the URL
    url = 'https://www.macmap.org/api/results/ntm-measures-detail'

    # Define the query parameters with function arguments
    params = {
        'reporter': reporter,
        'partner': partner,
        'product': product
    }

    # Define the headers
    headers = {
        'Cookie': f'ASP.NET_SessionId={session_id}; path=/; secure; HttpOnly; SameSite=None; SameSite=None; Secure',
        'Sec-Ch-Ua': '"Not(A:Brand";v="24", "Chromium";v="122"',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Content-Type': 'application/json; charset=utf-8',
        'X-Requested-With': 'XMLHttpRequest',
        'Sec-Ch-Ua-Mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.112 Safari/537.36',
        'Sec-Ch-Ua-Platform': '"Windows"',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://www.macmap.org/en/query/results?reporter=392&partner=156&product=382764&level=6',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9',
        'Priority': 'u=1, i',
        'Connection': 'close',
    }

    # Make the request with query parameters
    response = requests.get(url, headers=headers, params=params)

    # Check if the request was successful
    if response.status_code == 200:
        # Return the JSON response
        return response.json()
    else:
        # Return the HTTP status code and reason if the request failed
        return {'status_code': response.status_code, 'reason': response.reason}

def fetch_ntlc_products(countryCode='392', level='8', code='382764'):
    # Generate a random ASP.NET_SessionId
    session_id = uuid.uuid4()

    # Define the URL
    url = 'https://www.macmap.org/api/v2/ntlc-products'

    # Define the query parameters with function arguments
    params = {
        'countryCode': countryCode,
        'level': level,
        'code': code
    }

    # Define the headers
    headers = {
        'Cookie': f'ASP.NET_SessionId={session_id}; path=/; secure; HttpOnly; SameSite=None; SameSite=None; Secure',
        'Sec-Ch-Ua': '"Not(A:Brand";v="24", "Chromium";v="122"',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Content-Type': 'application/json; charset=utf-8',
        'X-Requested-With': 'XMLHttpRequest',
        'Sec-Ch-Ua-Mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.112 Safari/537.36',
        'Sec-Ch-Ua-Platform': '"Windows"',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://www.macmap.org/en/query/results?reporter=392&partner=156&product=382764&level=6',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9',
        'Priority': 'u=1, i',
        'Connection': 'close',
    }

    # Make the request with query parameters
    response = requests.get(url, headers=headers, params=params)

    # Check if the request was successful
    if response.status_code == 200:
        # Return the JSON response
        return response.json()
    else:
        # Return the HTTP status code and reason if the request failed
        return {'status_code': response.status_code, 'reason': response.reason}



@app.route('/api/results/ntm-measures', methods=['GET'])
def api_ntm_measures():
    reporter = request.args.get('reporter', default='392')
    partner = request.args.get('partner', default='156')
    product = request.args.get('product', default='382764010')
    response = fetch_ntm_measures(reporter, partner, product)
    return jsonify(response), 200 if 'status_code' not in response else response['status_code']

@app.route('/api/results/ntm-measures-detail', methods=['GET'])
def api_ntm_measures_detail():
    reporter = request.args.get('reporter', default='392')
    partner = request.args.get('partner', default='156')
    product = request.args.get('product', default='382764010')
    response = fetch_ntm_measures_detail(reporter, partner, product)
    return jsonify(response), 200 if 'status_code' not in response else response['status_code']

@app.route('/api/v2/ntlc-products', methods=['GET'])
def api_ntlc_products():
    countryCode = request.args.get('countryCode', default='392')
    level = request.args.get('level', default='8')
    code = request.args.get('code', default='382764')
    response = fetch_ntlc_products(countryCode, level, code)
    return jsonify(response), 200 if 'status_code' not in response else response['status_code']

if __name__ == '__main__':
    app.run(debug=True)
