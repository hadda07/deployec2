import boto3
AWS_REGION = "us-east-2"
EC2_RESOURCE = boto3.resource('ec2', region_name=AWS_REGION)
INSTANCE_ID = 'i-020b3f1914105320d'
instance = EC2_RESOURCE.Instance(INSTANCE_ID)
instance.start()
print(f'Starting EC2 instance: {instance.id}')
    
instance.wait_until_running()
print(f'EC2 instance "{instance.id}" has been started')
