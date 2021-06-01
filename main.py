# ============================== Custom Website ============================== #

# Import needed modules
from flask import Flask, render_template, request, redirect, url_for
import requests
import json
import os

# Define endpoint and API key for Stock Market API
MARKETSTACK_EOD_ENDPOINT = "http://api.marketstack.com/v1/eod"
access_key = os.environ.get('MARKETSTACK_API_KEY')

# Get data from Stock Market API
def get_data(symbol):
    parameters = {
        "access_key": access_key,
        "symbols": symbol
    }
    response = requests.get(url=MARKETSTACK_EOD_ENDPOINT, params=parameters)
    response.raise_for_status()
    json_data = json.loads(response.text)
    results_list = json_data["data"]
    #for result in results_list:
        #print(result['date'][:10], result['close'], result['volume'])
    return results_list


# Start Flask Application
app = Flask(__name__)


# Display Main Page
@app.route('/')
def home():
    empty_list = []
    empty_code = ""
    return render_template("index.html", code=empty_code, values=empty_list)


@app.route('/handle_data', methods=['POST'])
def handle_data():
    my_data = request.form['mydata'].upper()
    if not my_data == "":
        data_list = get_data(my_data)
    else:
        data_list = []
    return render_template("index.html", code=my_data, values=data_list)


if __name__ == '__main__':
    app.run(debug=True)
