import requests

data = {
    "age": 10,
    "job": 50,
    "marital": 40,
    "eductaion":"primary",
    "default":"no",
    "balance":1787,
    "housing":"no",
    "loan":"no",
    "contact":"cellular",
    "day":19,
    "month":"oct",
    "duration":100,
    "campaign":4,
    "pdays":-1,
    "previous":0,
    "poutcome":"failure"

}

url = 'http://localhost:8000/predict'
response = requests.post(url, json=data)
print(response.json())
