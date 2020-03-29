import boto3
import json
import datetime
import uuid

dynamodb_resource = boto3.resource('dynamodb',region_name='us-east-1')
table = dynamodb_resource.Table('Users')

with table.batch_writer() as user_data:
    for i in range(100):
        user_data.put_item(
            Item={
                'user_id' : str(uuid.uuid4()),
                'user_email' : 'someone'+str(i)+'@somwhere.com'
            }
        )
        print('writing record #'+str(i+1)+' to DYnamoDB Users Table')
    print('Done!')