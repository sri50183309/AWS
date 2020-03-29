import boto3
import json
import datetime
sg_name='rds-sg-dev-demo'
vpc_id='vpc-0cea463e3109d61d0'
sg_group_id='sg-009f306ab8b1cead2'

rds_identifier = 'my-rds-db'
db_name = 'mmytestdb'
user_name = 'masteruser'
user_password = 'mymasterpassword1!'
admin_email = 'sriram.mahalingam@gmail.com'
sg_id_number = ''
rds_endpoint = ''

def date_time_converter(o):
    if isinstance(o, datetime.datetime):
        return o.__str__()
        
ec2_client =  boto3.client('ec2', region_name='us-east-1')
response = ec2_client.describe_security_groups(
                GroupNames = [sg_name]
            )
sg_id_number = json.dumps(response['SecurityGroups'][0]['GroupId'])
sg_id_number = sg_id_number.replace('"','')
print(response)

rds_client = boto3.client('rds', region_name='us-east-1')

# rds_client.create_db_instance(
    # DBInstanceIdentifier=rds_identifier,
    # DBName=db_name,
    # DBInstanceClass='db.t2.micro',
    # Engine='mariadb',
    # MasterUsername=user_name,
    # MasterUserPassword=user_password,
    # VpcSecurityGroupIds=[sg_id_number],
    # AllocatedStorage=29,
    # Tags=[
        # {
            # 'Key': 'Purpose',
            # 'Value': 'AWS DEverloper study guide demo'
        # }
    # ]
# )

waiter= rds_client.get_waiter('db_instance_available')
waiter.wait(DBInstanceIdentifier=rds_identifier)
print("OKAY!! The amazon RDS Database is Up")
