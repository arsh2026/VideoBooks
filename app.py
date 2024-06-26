from flask import Flask, render_template, request, jsonify
import subprocess
from NewStorage import FetchVideo
from dotenv import load_dotenv
import os

load_dotenv()
app = Flask(__name__)

email=None
password=None
title=None
textPrompt=None                                                                                     
@app.route("/")
def home():
    return render_template("signup.html")

@app.route("/login")
def login():
    return render_template("signin.html")

@app.route("/login_data",methods=["GET","POST"])
def login_data():
    data = request.json
    global email,password
    email= data.get("email")
    password = data.get("password")
    # Now you have the email, you can do whatever you want with it
    # For example, you can store it in a database or use it for other purposes
    # For demonstration purposes, let's print the email
    print("Email:", email)
    print("create_account function called")
    return email


@app.route("/landing_page")
def landing_page():
    return render_template("landing_page.html")

@app.route("/generate_page")
def generate_page():
    return render_template("prompt.html")

@app.route("/promptFunc",methods=["GET","POST"])
def promptFunc():
    data = request.json
    global title,textPrompt,email
    title= data.get("title")
    textPrompt = data.get("textPrompt")
    subprocess.run(['python', 'new.py', textPrompt])
    subprocess.run(['python','storage.py',email,title])
    print(title)
    return title

@app.route("/viewVideo")
def viewVideo():
    global video_link,email,title
    video_link=FetchVideo(email,title)
    return render_template("viewVideo.html",video_link=video_link,title=title)

@app.route("/history_page")
def history_page():
    global email
    return render_template("historypage.html",email=email)

@app.route("/browse_video")
def browse_video():
    return render_template("BrowseVideo.html")

@app.route("/help_page")
def help_page():
    return render_template("help.html")

@app.route('/config')
def config():
    firebase_config = {
        'apiKey': os.getenv('FIREBASE_API_KEY'),
        'authDomain': os.getenv('FIREBASE_AUTH_DOMAIN'),
        'databaseURL': os.getenv('FIREBASE_DATABASE_URL'),
        'projectId': os.getenv('FIREBASE_PROJECT_ID'),
        'storageBucket': os.getenv('FIREBASE_STORAGE_BUCKET'),
        'messagingSenderId': os.getenv('FIREBASE_MESSAGING_SENDER_ID'),
        'appId': os.getenv('FIREBASE_APP_ID')
    }
    return jsonify(firebase_config)







if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0")



