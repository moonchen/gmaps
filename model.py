from __future__ import print_function
from botocore.exceptions import ClientError
import boto3
from datetime import datetime
import decimal

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
routes_table = dynamodb.Table('routes')
addresses_table = dynamodb.Table('addresses')
eta_table = dynamodb.Table('eta')


def get_route(route_id):
    try:
        response = routes_table.get_item(Key={'id': route_id})
        from_id = response['Item']['from']
        to_id = response['Item']['to']

        response_from = addresses_table.get_item(Key={'id': from_id})
        response_to = addresses_table.get_item(Key={'id': to_id})
        return (response_from['Item'], response_to['Item'])

    except ClientError as e:
        print(e.response['Error']['Message'])


def append_eta(when, route_id, seconds):
    timestamp = when.timestamp()
    decimal_timestamp = decimal.Decimal(timestamp)
    decimal_seconds = decimal.Decimal(seconds)
    eta_table.put_item(Item={'timestamp': decimal_timestamp, 'route': route_id, 'seconds': decimal_seconds})

