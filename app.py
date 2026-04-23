from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello! This is my simple web app for the final test."

@app.route("/about")
def about():
    return "This page is for the web app created using Python Flask."

if __name__ == "__main__":
    app.run(debug=True)
