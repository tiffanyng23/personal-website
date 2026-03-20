from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
import smtplib

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
        # user submits form, email gets sent, landing page confirms sent email
        user_email = request.form.get("user_email")
        subject = request.form.get("subject")
        message = request.form.get("message")
        return render_template("landing.html")

    else:
        return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)