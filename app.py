from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return render_template(
        "index.html",
        version="2.0",
        updated=datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)