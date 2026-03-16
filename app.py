from flask import Flask, render_template
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
bootstrap = Bootstrap5(app)

# Home Page 
@app.route("/")
def main():
    #insert slideshow of images
    return render_template("homepage.html")

# About Me
@app.route("/about")
def about():
    return render_template("about.html")

# Contact
@app.route("/contact")
def contact():
    return render_template("contact.html")

# Projects
# Earthquake Tracker Dashboard
@app.route("/projects")
def earthquakes():
    return render_template("projects.html")

if __name__ == "__main__":
    app.run(debug=True)