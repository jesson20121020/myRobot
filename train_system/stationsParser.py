# conding:utf-8

import re
from pprint import pprint

with open('stations.html', 'r') as f:
    text = f.read()
    text = text.decode('utf-8')
    stations = re.findall(u'([\u4e00-\u9fa5]+)\|([A-Z]+)', text)
    format_stations = {}
    for key, value in dict(stations).items():
        format_key = key.encode('utf-8')
        format_stations[format_key] = value.encode('utf-8')
    
    pprint(dict(format_stations), indent=4)
