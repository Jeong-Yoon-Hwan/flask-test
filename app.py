from flask import Flask,request,jsonify
import dbconn
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

@app.route('/')
def home():
  return "hello,world"

@app.route("/echo_call",methods=["POST"])
def get_echo_call():
  param = request.get_json()
  print("ok")
  return jsonify({"title": "hello"})

if __name__== "__main__":
  app.run(debug=True)