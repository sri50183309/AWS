import boto3
import json
import datetime

def date_time_converter(o):
    if isinstance(o, datetime.datetime):
        return o.__str__()


        
ec2_client = boto3.client('ec2', region_name='us-east-1')

sg_name = 'rds-sg-dev-demo'

print('Fetching the Security Group endpoint .......')
response =  ec2_client.describe_security_groups(
        GroupNames=[sg_name]
    )
print(response)    

sg_id_number = json.dumps(response['SecurityGroups'][0]['GroupId'])
sg_id_number = sg_id_number.replace('"','')

ec2_client.delete_security_group(
                GroupId = sg_id_number
            )

print('Clean up is complete')            
            
            