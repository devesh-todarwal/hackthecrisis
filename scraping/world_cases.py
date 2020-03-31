import urllib.request, json
from pprint import pprint

def get_world_data():
    url = "https://pomber.github.io/covid19/timeseries.json"

    with urllib.request.urlopen(url) as u:
        data = json.loads(u.read().decode())
    return data

def get_list(data, country, show=['date','confirmed']):
    country_data = dict()

    for key in data[country][0].keys():
        if key in show:
            country_data[key] = []

    for d in data[country]:
        for k,v in d.items():
            if k in show:
                country_data[k].append(v)

    return country_data

if __name__ == '__main__':
    data = get_world_data()
    pprint(get_list(data,'India'))  
