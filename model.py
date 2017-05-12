from __future__ import print_function
from botocore.exceptions import ClientError
import boto3
from datetime import datetime
import decimal

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
routes_table = dynamodb.Table('routes')
addresses_table = dynamodb.Table('addresses')
eta_table = dynamodb.Table('eta')


def get_addresses(route_response):
    from_id = route_response['from']
    to_id = route_response['to']
    response_from = addresses_table.get_item(Key={'id': from_id})
    response_to = addresses_table.get_item(Key={'id': to_id})
    return response_from['Item']['address'], response_to['Item']['address']

# returns (address, address)
def get_route(route_id):
    response = routes_table.get_item(Key={'id': route_id})
    return get_addresses(response['Item'])

# yields a bunch of (address, address)
def get_all_routes():
    response = routes_table.scan()
    for r in response['Items']:
        yield get_addresses(r)

def append_eta(when, route_id, seconds):
    timestamp = when.timestamp()
    decimal_timestamp = decimal.Decimal(timestamp)
    decimal_seconds = decimal.Decimal(seconds)
    eta_table.put_item(Item={'timestamp': decimal_timestamp, 'route': route_id, 'seconds': decimal_seconds})

if __name__ == '__main__':
    print ('all routes:')
    for f, t in get_all_routes():
        print (f, 'to', t)
