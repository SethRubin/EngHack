from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Would you like a potato?\n\n\n\n Well no potato for you!!!!"

if __name__ == "__main__":
    app.run()
