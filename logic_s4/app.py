from flask import Flask
import requests


#every correct num or letter gives 10% of total prize

#lowercase checks for vowels
#upercase checks for conecutive letters
#numbers check if even

app = Flask(__name__)

@app.route('/logic')
def logic():
    combindedString = ""
    total_prize = 100
    user_prize = 0
    vowels = ['a', 'e', 'i', 'o', 'u']
    randomString = requests.get('http://random_letters_s2:5002/getRandomString').text
    randomNumber = requests.get('http://random_numbers_s3:5003/getRandomNumber').text
    combindedString = randomString + randomNumber
    for i in range(len(combindedString)):
        if(combindedString[i] in vowels):
            user_prize += total_prize/10
        if(i == 3):
            if(combindedString[i] == combindedString[i+1]):
                user_prize += (total_prize/10)*2
        if(i >= 5):
            list_num_val = combindedString[i]
            list_num_val = int(list_num_val)
            if((list_num_val % 2) == 0):
                user_prize += (total_prize/10)*2
    return f'{str(user_prize)}'

if __name__ == "__main__":
    app.run(host = '0.0.0.0', port = 5004, debug=True)