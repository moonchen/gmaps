from __future__ import print_function
from model import get_route

class Route:
    def __init__(self, route_id):
        self.route_id = route_id
        route = get_route(self.route_id)
        self.from_address = route[0]['address']
        self.to_address = route[1]['address']

    def __str__(self):
        return 'From ' + self.from_address + ' to ' + self.to_address


if __name__ == '__main__':
    route = Route(0)
    print(route)
