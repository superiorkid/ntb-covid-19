import requests

BASE_URL = 'http://apicovid19indonesia-v2.vercel.app/api'


def total_cases():
  url = BASE_URL + '/indonesia'
  response = requests.get(url)
  data = response.json()
  return data
