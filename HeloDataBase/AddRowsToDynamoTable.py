import boto3
import json
import datetime
import uuid

dynamodb_resource = boto3.resource('dynamodb',region_name='us-east-1')
table = dynamodb_resource.Table('Users')

response = table.put_item(
    Item = {
        'user_id' : '1234-5678',
        'user_email' : 'someone@where.com'
    }
)

print(json.dumps(response, indent=2, sort_keys=True))