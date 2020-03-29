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

#ec2_client = boto3.client('ec2', region_name='us-east-1')

rds_client = boto3.client('rds', region_name='us-east-1')

response = rds_client.describe_db_instances(
    DBInstanceIdentifier = rds_identifier
)

dbendpoint = json.dumps(response['DBInstances'][0]['Endpoint']['Address'])
dbendpoint = dbendpoint.replace('"','')
db_connection = mariadb.connect(host = dbendpoint, 
                                user=user_name, 
                                password = user_password, 
                                database=db_name)
cursor = db_connection.cursor()
try:
    cursor.execute("select * from Users")
    query_result = cursor.fetchall()
    print(query_result)
except mariadb.Error as e:
    print('Error while creating: {}', format(e))
finally:
    db_connection.close()