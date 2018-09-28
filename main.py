from flask import Flask, request, render_template, redirect
import cgi
app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('login.html',user_error="",password_error="",verify_error="",email_error="")

@app.route("/",methods=['POST'])
def success():
    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']
    username_error = ""
    password_error = ""
    verify_error = ""
    email_error = ""
    userFlag = False
    passFlag = False
    atFlag = False
    periodFlag = False
    emailFlag = False
    for letter in email:
        if letter == " ":
            emailFlag = True
    for letter in username:
        if letter == " ":
            userFlag = True
    for letter in password:
        if letter == " ":
            passFlag = True
    for letter in email:
        if letter == "@":
            atFlag = True
        if letter == ".":
            periodFlag = True         
    if userFlag == True:
        username_error = "Your username can't contain spaces."  
    if len(username) < 3:
        username_error = "Your username must be at least 3 characters in length."   
    if username == "":
        username_error = "Your username field can't be blank."
    if password != verify or verify == "":
        verify_error = "Your passwords must match."
        password_error = "Your passwords must match."     
    if passFlag == True:
        password_error = "Your password can't contain spaces."
    if len(password) < 3:
        password_error = "Your password must be at least 3 characters in length"
    if password == "":
        password_error = "Your password can't be blank."                      
    if (len(email) < 3 and len(email) > 0) or len(email) > 20:
        email_error = "Your email must be between 3 and 20 characters"
    if atFlag == False or periodFlag == False or emailFlag == True:
        email_error = "Please enter a valid email."
    if email == "":
        email_error = ""
    if username_error == "" and password_error == "" and verify_error == "" and email_error == "": 
        return render_template("success.html",username = username)
    else: 
        return render_template('login.html',user_error=username_error,password_error=password_error,
            verify_error=verify_error,email_error=email_error,user_place=username,email_place=email)    
               


app.run()