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


def kasus_per_kabupaten():
  data = get_data()

  temp_nama_kabupaten = list()
  temp_data_kabupaten = list()

  for k, v in data.get('data_per_kabupaten').items():
    temp_nama_kabupaten.append(k.replace('_', ' ').capitalize())
    temp_data_kabupaten.append(list(v.get('konfirmasi').values()))

  kombinasi_data = dict(zip(temp_nama_kabupaten, temp_data_kabupaten))

  return kombinasi_data
