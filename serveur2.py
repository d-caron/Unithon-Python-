from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/")
def index():
    return {
        "command": "talk",
        "ids":["19991606", "19990226"]
    }

if __name__=="__main__":
    app.run()    