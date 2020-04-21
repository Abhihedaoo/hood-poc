from flask import Flask
import requests 

app = Flask(__name__)

@app.route('/namespaces')
def hello_world():
    r  = requests.get(url = 'http://flaskapp:5000/namespaces')
    return r

if __name__ == '__main__':
    app.run()