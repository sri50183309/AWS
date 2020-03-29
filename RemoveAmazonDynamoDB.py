import boto3
import json
import datetime
import uuid

dynamodb_client = boto3.client('dynamodb', region_name='us-east-1')

response = dynamodb_client.delete_table(TableName='Users')
print(json.dumps(response , indent = 2, sort_keys=True))