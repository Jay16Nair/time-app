from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    now = datetime.now()
    return f"<h1>Current Time: {now.strftime('%Y-%m-%d %H:%M:%S')}</h1>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
