from flask import Flask, render_template, request
import requests

API_KEY = "BTuxA4iTj2hEcEcq77RHBr_0XTi3cyrn2XgvQN_3t8RU"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey":
 API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

app = Flask(__name__)

@app.route("/")
@app.route("/index")
@app.route("/home")
def index():
    return render_template("index.html")

@app.route("/predict")
def predicts():
    return render_template("predict.html")

@app.route('/submit', methods =['GET', 'POST']) 
def predict():
    fips_1 =float(request.form['FIPS'])
    age =  float(request.form['Age-Adjusted Incidence Rate(Ê) - cases per 100,000']) 
    lowerconf = float(request.form['Lower 95% Confidence Interval']) 
    upperconf=float(request.form[ 'Upper 95% Confidence Interval']) 
    average = float(request.form['Average Annual Count'])
    rates = float(request.form['Recent 5-Year Trend (ˆ) in Incidence Rates'])
    lowerconf_1= float(request.form['Lower 95% Confidence Interval.1']) 
    upperconf_1 = float(request.form['Upper 95% Confidence Interval.1'])
    payload_scoring = {"input_data": [{"fields": ['FIPS','Age-Adjusted Incidence Rate(Ê) - cases per 100,000','Lower 95% Confidence Interval','Upper 95% Confidence Interval','Average Annual Count','Recent 5-Year Trend (ˆ) in Incidence Rates','Lower 95% Confidence Interval.1','Upper 95% Confidence Interval.1'], "values": [[fips_1, age, lowerconf, upperconf, average, rates, lowerconf_1, upperconf_1]]}]}
    print("Scoring response")
    url='https://us-south.ml.cloud.ibm.com/ml/v4/deployments/da9d100a-259e-4aa5-82e2-8901b63066a1/predictions?version=2023-05-19'
    headers = {'Authorization': 'Bearer ' + mltoken}
    response_scoring = requests.post(url, json=payload_scoring, headers=headers)
    print("Response structure:")
    predictions = response_scoring.json()
    print(predictions.keys())
    print(response_scoring.json())
    predictions = response_scoring.json()
    predicts = predictions['predictions'][0]['values'][0][0]
    if predicts==0:
        return render_template('submit.html', predict="Falling")
    elif predicts==1:
        return render_template('submit.html', predict="Stable")
    elif predicts==2:
        return render_template('submit.html', predict="Rising")
    else:
        return render_template('submit.html', predict="None")
    
if __name__ == "__main__":
    app.run(debug=True)