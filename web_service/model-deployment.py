
import pandas as pd

import mlflow
from flask import Flask, request, jsonify

# mlflow.set_tracking_uri("sqlite:///mlflow.db")
# mlflow.set_experiment("term-deposit-exp")

RUN_ID = "a3a65c298163443a90bb0da817bc4b30"

model = f'./mlruns/1/{RUN_ID}/artifacts/dtc-pipeline'

# Load model as a PyFuncModel.
model = mlflow.pyfunc.load_model(model)


app = Flask("term-deposit")

@app.route("/predict", methods=["POST"])
def predict():

    data = request.get_json()

    pred = model.predict(data)

    result = {
        "result":int(pred)
    }
    
    return result

if __name__=="__main__":
    app.run(debug=True, host="0.0.0.0", port="8000")
