import requests

def get_data():
  url = 'https://corona.ntbprov.go.id/api/data'
  resp = requests.get(url).json()
  
  return resp