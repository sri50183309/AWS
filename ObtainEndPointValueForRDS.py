import boto3
import json
import datetime


def date_time_converter(o):
    if isinstance(o, datetime.datetime):
        return o.__str__()

rds_identifier = 'my-rds-db'
db_name = 'mmytestdb'
user_name = 'masteruser'
user_password = 'mymasterpassword1!'
admin_email = 'sriram.mahalingam@gmail.com'
sg_name='rds-sg-dev-demo'
vpc_id='vpc-0cea463e3109d61d0'
sg_group_id='sg-009f306ab8b1cead2'
sg_id_number = ''
rds_endpoint = ''

        
rds_client = boto3.client('rds', region_name='us-east-1')

print('Fetching the RDS endpoint .......')
response =  rds_client.describe_db_instances(
        DBInstanceIdentifier=rds_identifier
    )
print(response)    
rds_endpoint = json.dumps(response['DBInstances'][0]['Endpoint'])
rds_endpoint = rds_endpoint.replace('"','')
print('RDS Endpoint:' + rds_endpoint)