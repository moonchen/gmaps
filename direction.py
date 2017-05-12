from __future__ import print_function
from credentials import GMAPS_APIKEY
from route import Route
from model import append_eta
from datetime import datetime

import sys
from os.path import dirname, join
sys.path.append(join(dirname(__file__), 'modules'))
import googlemaps


def get_duration(from_address, to_address, when):
    gmaps = googlemaps.Client(key=GMAPS_APIKEY)
    directions_result = gmaps.directions(from_address, to_address, departure_time=when)
    return directions_result[0]['legs'][0]['duration_in_traffic']['value']


if __name__ == '__main__':
    route = Route(0)
    now = datetime.now()
    result = get_duration(route.from_address, route.to_address, now)
    print(route, 'duration in traffic:', result, 'seconds')
    append_eta(now, 0, result)
