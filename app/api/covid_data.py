import requests

endpoint = 'https://kipi.covid19.go.id/api/get-city'

files = {
  'start_id': ('BALI')
}

def covid_data():
  resp = requests.post(endpoint, files)
  return resp

