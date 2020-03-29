import boto3
import json
import datetime
import uuid
from boto3.dynamodb.conditions import Key

dynamodb_resource = boto3.resource('dynamodb',region_name='us-east-1')
table = dynamodb_resource.Table('Users')

response = table.query(
    KeyConditionExpression=Key('user_id').eq('1234-5678')
)

print(json.dumps(response['Items'], indent=2, sort_keys=True))