from direction import get_duration
from datetime import datetime
from model import append_eta, get_all_routes


def lambda_handler(event, context):
    for from_address, to_address in get_all_routes():
        now = datetime.now()
        result = get_duration(from_address, to_address, now)
        print(from_address, 'to', to_address, 'duration in traffic:', result, 'seconds')
        append_eta(now, 0, result)

if __name__ == '__main__':
    lambda_handler(None, None)
