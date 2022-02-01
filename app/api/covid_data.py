import requests

def get_data():
  url = 'https://corona.ntbprov.go.id/api/data'
  resp = requests.get(url).json()
  
  return resp


def total_kasus():
  data = get_data()

  total = {
    'total': data.get('total').get('konfirmasi').get('sembuh') + data.get('total').get('konfirmasi').get('meninggal') + data.get('total').get('konfirmasi').get('masih_isolasi'),
    'sembuh': data.get('total').get('konfirmasi').get('sembuh'),
    'meninggal': data.get('total').get('konfirmasi').get('meninggal'),
    'masih_isolasi': data.get('total').get('konfirmasi').get('masih_isolasi')
  }

  return total