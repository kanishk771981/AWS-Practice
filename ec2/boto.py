"""
Creates an EC2 instance using Boto3.
Make sure your AMI ID, key name, and security group are correct.
"""

import boto3

# Create EC2 resource
ec2 = boto3.resource('ec2', region_name='ap-south-1')

# Launch EC2 instance
instances = ec2.create_instances(
    ImageId='ami-0f1dcc636b69a6438',  # Use your preferred AMI
    MinCount=1,
    MaxCount=1,
    InstanceType='t2.micro',
    KeyName='Kanishk-Key',  # Your key pair name
    SecurityGroupIds=['sg-02f51c5489bb315ea'],  # Your security group ID
    TagSpecifications=[
        {
            'ResourceType': 'instance',
            'Tags': [{'Key': 'Name', 'Value': 'Boto3-EC2-Instance'}]
        }
    ]
)

# Print instance IDS
for instance in instances:
    print(f"Created instance with ID: {instance.id}")
