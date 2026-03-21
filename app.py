from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap5
import smtplib
from email.message import EmailMessage
from functions.contact import send_email

app = Flask(__name__)
bootstrap = Bootstrap5(app)

# Home Page 
@app.route("/")
def homepage():
    return render_template("homepage.html")

# About Me
@app.route("/about")
def about():
    return render_template("about.html")

# Projects
@app.route("/projects")
def projects():
    return render_template("projects.html")

# Contact
@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        #gather user information from form
        user_name = request.form.get("name")
        user_email = request.form.get("user_email")
        subject = request.form.get("subject")
        message = request.form.get("message")
        print(user_name, user_email, subject, message)

        #send form information from portfolio email to personal email
        send_email(user_name, user_email, subject, message)
        return render_template("landing.html")
        
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)