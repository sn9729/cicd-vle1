from flask import Flask, render_template, make_response
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    response = make_response(render_template(
        "index.html",
        version="3.0",
        updated=datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    ))

    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = "0"

    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)