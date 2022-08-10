from flask import Flask, redirect, request, render_template, url_for
from flask import session as login_session
import requests
import json

firebaseConfig = {
  "apiKey": "AIzaSyBAYdzEpZ4zVCTjiLIrH3abTjYCOsenYaQ",
  "authDomain": "signnow-ea247.firebaseapp.com",
  "projectId": "signnow-ea247",
  "storageBucket": "signnow-ea247.appspot.com",
  "messagingSenderId": "448511328030",
  "appId": "1:448511328030:web:e7b6b5a8949b41ddc5130f",
  "measurementId": "G-8S05LPBBQ0"}

firebaseConfig = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
db = firebase.database()

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'

url = "https://deep-translate1.p.rapidapi.com/language/translate/v2"


headers = {
    "content-type": "application/json",
    "X-RapidAPI-Key": "2abdb173cdmsha93324285d22febp102067jsn74be32839252",
    "X-RapidAPI-Host": "deep-translate1.p.rapidapi.com"
}

demo = "Approximately 90,000,000 deaf people start their lives at a disadvantage due to the fact that the hearing majority are unfamiliar with their language - sign language."

payload = {
    "q": demo,
    "source": "en",
    "target": "ar"
}


# Your code should be below
@app.route('/join_us')
def join_us():
    return render_template("join_us.html")

@app.route('/')
def home():
        response = requests.request("POST", url, json=payload, headers=headers)
        dict1 = json.loads(response.content)
        tran = dict1 ['data']['translations']['translatedText']
    return render_template("main.html", tran = tran)

@app.route('/about_us')
def about_us():
    return render_template("aboutus.html")



# Your code should be above

if __name__ == "__main__":  # Makes sure this is the main process
    app.run(debug=True)