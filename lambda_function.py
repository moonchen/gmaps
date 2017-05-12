from route import Route
from direction import get_duration
from datetime import datetime
from model import append_eta


def lambda_handler(event, context):
    route = Route(0)
    now = datetime.now()
    result = get_duration(route.from_address, route.to_address, now)
    print(route, 'duration in traffic:', result, 'seconds')
    append_eta(now, 0, result)

if __name__ == '__main__':
    lambda_handler(None, None)
