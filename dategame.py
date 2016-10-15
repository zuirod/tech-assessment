from requests import post
from dateutil.parser import parse
from datetime import timedelta

token = "068a1d291aee44a97349a49bf7bef655"

data_endpoint = "http://challenge.code2040.org/api/dating"
validation_endpoint = "http://challenge.code2040.org/api/dating/validate"

request = post(data_endpoint, dict(token=token))
data = request.json()
datestamp = data["datestamp"]
interval = data["interval"]

date = parse(datestamp) + timedelta(seconds = interval)
datestring = date.isoformat().replace("+00:00", "Z")

answer = post(validation_endpoint, dict(token=token, datestamp=datestring))
