import boto3
import json
import datetime
import pymysql as mariadb

def date_time_converter(o):
    if isinstance(o, datetime.datetime):
        return o.__str__()

rds_identifier = 'my-rds-db'
db_name = 'mmytestdb'
user_name = 'masteruser'
user_password = 'mymasterpassword1!'
sg_group_id='sg-0a7f215612b7d1669'

#ec2_client = boto3.client('ec2', region_name='us-east-1')

rds_client = boto3.client('rds', region_name='us-east-1')

response = rds_client.delete_db_instance(
    DBInstanceIdentifier = rds_identifier,
    SkipFinalSnapshot=True)

print('RDS Instance is being terminated... This may take several minutes')

waiter = rds_client.get_waiter('db_instance_deleted')
waiter.wait(DBInstanceIdentifier=rds_identifier)

print('The Amazon RDS database has been deleted. Removing Security Groups')      
