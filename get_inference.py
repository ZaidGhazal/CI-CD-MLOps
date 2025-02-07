"""
Get model inference from API
"""
import requests


data = {
    "age": 32,
    "workclass": "Private",
    "education": "Some-college",
    "maritalStatus": "Married-civ-spouse",
    "occupation": "Exec-managerial",
    "relationship": "Husband",
    "race": "Black",
    "sex": "Male",
    "hoursPerWeek": 60,
    "nativeCountry": "United-States"
}
r = requests.post('https://ml-ci-cd-project.herokuapp.com/', json=data)

assert r.status_code == 200

print("Response code: %s" % r.status_code)
print("Model Inference: %s" % r.json())
