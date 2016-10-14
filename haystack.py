import requests

token = "068a1d291aee44a97349a49bf7bef655"

data_endpoint = "http://challenge.code2040.org/api/haystack"
validation_endpoint = "http://challenge.code2040.org/api/haystack/validate"

r = requests.post(data_endpoint, dict(token=token))
data = r.json()
needle = data["needle"]
haystack = data["haystack"]

i = haystack.index(needle)
requests.post(validation_endpoint, dict(token=token, needle=i))
