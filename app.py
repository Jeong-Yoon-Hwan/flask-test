from flask import Flask,request,jsonify
import dbconn

app = Flask(__name__)

@app.route('/')
def home():
  return "hello,world"

@app.route("/echo_call",methods=["POST"])
def get_echo_call():
  param = request.get_json()
  return jsonify({"title": "hello"})


@app.route("/test",method=["POST"])
def test():
  
  return jsonify()

if __name__== "__main__":
  app.run(debug=True)