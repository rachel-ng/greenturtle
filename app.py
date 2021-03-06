import os, sys
import json
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from model import predict as p


# create the flask object
app = Flask(__name__)
CORS(app)

# port = int(os.environ.get("PORT", 5000))

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
        print(prediction["prediction"])

    response = jsonify(prediction)
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Content-Type", "application/json")
    return response 

#if __name__ == "__main__":
#    app.run(host='0.0.0.0', port=port, debug=True, ssl_context='adhoc')

if __name__ == "__main__":
    # context = ('cert.pem', 'key.pem') 
    #context = 'adhoc'
    #app.run(host='0.0.0.0', port=port, debug=True, ssl_context=context)
    app.run(debug=True)

