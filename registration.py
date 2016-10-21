import requests

endpoint = "http://challenge.code2040.org/api/register"
token = "068a1d291aee44a97349a49bf7bef655"
github = "https://github.com/zuirod/tech-assessment"

request = requests.post(endpoint, data = dict(token=token, github=github))
assert request.status_code == 200
