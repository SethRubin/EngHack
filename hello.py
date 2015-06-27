from flask import Flask
import json
app = Flask(__name__)

@app.route('/')
def hello_world():
    obj = {
        'key': 3,
        'key2': 5,
        'key3': 6 
    }
    return json.dumps(obj)

@app.route('/word')
def hello_world():
    obj = {
        'key': 3,
        'key2': 5,
        'key3': 6 
    }
    return json.dumps(obj)




if __name__ == '__main__':
    app.run(debug=True)