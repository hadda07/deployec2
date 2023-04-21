#!/usr/bin/env python3
import boto3
AWS_REGION = "eu-west-1"
EC2_RESOURCE = boto3.resource('ec2', region_name=AWS_REGION)
INSTANCE_ID = 'i-0db193fb2af4a35f5'
instance = EC2_RESOURCE.Instance(INSTANCE_ID)
instance.start()
print(f'Starting EC2 instance: {instance.id}')
    
instance.wait_until_running()
print(f'EC2 instance "{instance.id}" has been started')
