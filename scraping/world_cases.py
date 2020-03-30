import urllib.request, json
from pprint import pprint

def  get_world_data():
    url = "https://pomber.github.io/covid19/timeseries.json"

    with urllib.request.urlopen(url) as u:
        data = json.loads(u.read().decode())

    return data
