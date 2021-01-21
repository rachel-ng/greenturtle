import os, sys
import json
from flask import Flask, request, jsonify, send_from_directory
from model import predict as p

# create the flask object
app = Flask(__name__)
port = int(os.environ.get("PORT", 5000))

@app.route('/')
def index():
    return "welcome to greenturtle"

@app.route('/favicon.ico') 
def favicon(): 
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico')

@app.route('/predict',methods=['GET','POST'])
def predict():
    data = request.args.get('data') or request.form.get('data')
    if data == None:
        return 'no data'
    else:
        prediction = p.make_prediction(data) 

    response = jsonify(prediction)
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("content-type", "application/json")
    return response 

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=port, ssl_context='adhoc', debug=True)

