from flask import Flask
import random

app = Flask(__name__)

def getRandomNumber():
    number_string = ''
    for i in range(6):
        random_num = random.randint(1,9)
        number_string += random_num
    return getRandomString 

if __name__ == "__main__":
    app.run(host = '0.0.0.0', port = 5003, debug=True)