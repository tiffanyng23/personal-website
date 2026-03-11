from flask import Flask, render_template

app = Flask(__name__)

# Home Page 
@app.route("/")
def main():
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
@app.route("/earthquake-tracker")
def earthquakes():
    return render_template("earthquakes.html")

# Spotify Artist Explore Page
@app.route("/spotify-explore")
def spotify():
    return render_template("spotify.html")

# NASA Image Repository
@app.route("nasa-images")
def nasa():
    return render_template("nasa.html")
