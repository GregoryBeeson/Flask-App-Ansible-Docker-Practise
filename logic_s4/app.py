from flask import Flask
import requests


app = Flask(__name__)

@app.route('/logic')
def logic():
    randomString = requests.get('http://random_letters_s2:5002/getRandomString').text
    randomNumber = requests.get('http://random_numbers_s3:5003/getRandomNumber').text
    return f'{randomString} {randomNumber}'

if __name__ == "__main__":
    app.run(host = '0.0.0.0', port = 5004, debug=True)