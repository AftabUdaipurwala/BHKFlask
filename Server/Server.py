from flask import Flask,request,jsonify
import Util
app = Flask(__name__)

@app.route("/get_location_names")
def get_location_names():
    response = jsonify({
    'locations':Util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route("/predict_home_prices", methods=['POST'])
def predict_home_prices():
    bath=int(request.form['bath'])
    bhk=int(request.form['bhk'])
    location= request.form(['location'])
    TotalSqftAct=float(request.form['TotalSqftAct'])

    response = jsonify({
      'estimated_price':Util.get_estimated_price(location,bath,bhk,TotalSqftAct)
    })


if __name__ == "__main__":
  app.run()