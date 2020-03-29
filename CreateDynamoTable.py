import boto3
import json
import datetime

dynamodb_resource = boto3.resource('dynamodb', region_name='us-east-1')

dynamoSchemaJson = [
    {
        'AttributeName' : 'user_id',
        'KeyType' : 'HASH'
    },
    {
        'AttributeName' : 'user_email',
        'KeyType' : 'RANGE'
    }
]

dynamoAttributeDefnJson = [
    {
        'AttributeName' : 'user_id',
        'AttributeType' : 'S'
    },
    {
        'AttributeName' : 'user_email',
        'AttributeType' : 'S'
    }
]

table = dynamodb_resource.create_table(
        TableName = "Users",
        KeySchema = dynamoSchemaJson,
        AttributeDefinitions = dynamoAttributeDefnJson,
        ProvisionedThroughput = {
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5
        }
)

print("The dynamo table is being created, this may take a minutes.....")
table.meta.client.get_waiter('table_exists').wait(TableName='users')
print("Table is ready!!")