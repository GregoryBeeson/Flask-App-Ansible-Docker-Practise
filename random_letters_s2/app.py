from flask import Flask
import random

app = Flask(__name__)

@app.route('/getRandomString')
def getRandomString():
    lowercase_alphabet = "abcdefghijklmnopqrstuvwxyz"
    upercase_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    string = ""
    for i in range(3):
        string += random.choice(lowercase_alphabet)
    for i in range(2):
        string += random.choice(upercase_alphabet)
    return f'{string}'

if __name__ == "__main__":
    app.run(host = "0.0.0.0", debug=True, port = 5002)