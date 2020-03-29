import boto3
import json
import datetime
sg_name='rds-sg-dev-demo'
sg_description = 'RDS Security Group for AWS Dev Study Guide'
my_ip_cidr = '0.0.0.0/0'
vpc_id='vpc-0cea463e3109d61d0'
sg_group_id='sg-0a7f215612b7d1669'

ec2_client =  boto3.client('ec2', region_name='us-east-1')
#response = ec2_client.create_security_group(Description=sg_description,GroupName=sg_name)
#print(json.dumps(response, indent=2, sort_keys=True))

response = ec2_client.authorize_security_group_ingress(
    GroupId='sg-0a7f215612b7d1669',
    IpPermissions=[
        {
            'FromPort': 3306,
            'IpProtocol': 'tcp',
            'IpRanges': [
                {
                    'CidrIp': my_ip_cidr,
                    'Description': 'SSH access from the LA office',
                },
            ],
            'ToPort': 3306,
        },
    ],
                            )
print("Security Group should be created: Verify this is in the AWS Console")                            