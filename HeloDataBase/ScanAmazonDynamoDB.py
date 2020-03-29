import boto3
import json
import datetime
import uuid

dynamodb_resource = boto3.resource('dynamodb',region_name='us-east-1')
table = dynamodb_resource.Table('Users')

response = table.scan()

print('The total count is: '+json.dumps(response['Count']))
print(json.dumps(response['Items'], indent = 2, sort_keys=True))