from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    # If the request method is POST, it means the user has submitted the form
    if request.method == 'POST':
        # Get the selected values from the form
        origin = request.form['origin']
        destination = request.form['destination']
        cabin = request.form['cabin']

        # Set the API request headers
        headers = {
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'en-US,en;q=0.9,hi;q=0.8',
            'cache-control': 'no-cache',
            'content-type': 'application/json',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
        }

        # Set the API request JSON data
        json_data = {
            'origin': origin,
            'destination': destination,
            'partnerPrograms': [
                'Air Canada',
                'United Airlines',
                'KLM',
                'Qantas',
                'American Airlines',
                'Etihad Airways',
                'Alaska Airlines',
                'Qatar Airways',
                'LifeMiles',
            ],
            'stops': 2,
            'departureTimeFrom': '2024-07-09T00:00:00Z',
            'departureTimeTo': '2024-10-07T00:00:00Z',
            'isOldData': False,
            'limit': 302,
            'offset': 0,
            'cabinSelection': [
                cabin,
            ],
            'date': '2024-07-09T12:00:17.796Z',
        }

        # Send the API request
        response = requests.post('https://cardgpt.in/apitest', headers=headers, json=json_data)

        # Get the API response JSON data
        response_json = response.json()

        # Render the template with the API response data
        return render_template('index.html', data=response_json['data'], origin=origin, destination=destination, cabin=cabin)

    # If the request method is GET, it means the user has loaded the page for the first time
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)