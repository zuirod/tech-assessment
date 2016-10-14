import requests

reverse = "http://challenge.code2040.org/api/reverse"
validate = "http://challenge.code2040.org/api/reverse/validate"
token = "068a1d291aee44a97349a49bf7bef655"

r = requests.post(reverse, dict(token=token))
s = r.content

requests.post(validate, dict(token=token, string=s[::-1]))
