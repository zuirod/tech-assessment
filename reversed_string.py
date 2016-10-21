import requests

token = "068a1d291aee44a97349a49bf7bef655"

data_endpoint = "http://challenge.code2040.org/api/reverse"
validation_endpoint = "http://challenge.code2040.org/api/reverse/validate"

request = requests.post(data_endpoint, dict(token=token))
string_to_reverse = request.content

string = string_to_reverse[::-1]

answer = requests.post(validation_endpoint, dict(token=token, string=string))
assert answer.status_code == 200
