import requests

token = "068a1d291aee44a97349a49bf7bef655"

data_endpoint = "http://challenge.code2040.org/api/prefix"
validation_endpoint = "http://challenge.code2040.org/api/prefix/validate"

request = requests.post(data_endpoint, dict(token=token))
data = request.json()
prefix = data["prefix"]
array = data["array"]

strings = [s for s in array if not s.startswith(prefix)]

answer = requests.post(validation_endpoint, json=dict(token=token, array=strings))
assert answer.status_code == 200
