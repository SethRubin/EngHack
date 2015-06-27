from flask import Flask, Response
app = Flask(__name__)

@app.route("/")
def hello():
    return "Starting application!"

if __name__ == "__main__":
    app.run(debug=True)
