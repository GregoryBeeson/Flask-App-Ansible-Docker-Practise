from flask import Flask
import random

app = Flask(__name__)

@app.route('/getRandomNumber')
def getRandomNumber():
    number_string = ''
    for i in range(5):
        random_num = random.randint(1,9)
        number_string += str(random_num)
    return f'{number_string}' 

if __name__ == "__main__":
    app.run(host = '0.0.0.0', port = 5003, debug=True)