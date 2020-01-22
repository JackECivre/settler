from flask import Flask
import threading
import time
import requests

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


if __name__ == "__main__":
    threading.Thread(target=app.run).start()

response = requests.get('http://127.0.0.1:5000')
if response.status_code == 200 and response.text == "Hello World!":
    print('OK')
else:
    print('Error')