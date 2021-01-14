import os, sys
import json
from flask import Flask,request,render_template
from model import predict as p
# create the flask object
app = Flask(__name__)
port = int(os.environ.get("PORT", 5000))

@app.route('/')
def index():
    return "Index Page"
@app.route('/predict',methods=['GET','POST'])
def predict():
    data = request.args.get('data') or request.form.get('data')
    if data == None:
        return 'Got None'
    else:
        prediction = p.make_prediction(data) 
    return json.dumps(str(prediction))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=port)

