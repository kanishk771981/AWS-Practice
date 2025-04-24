"""
Terminates a specified EC2 instance using Boto3.
"""

import boto3

# Create EC2 resource
ec2 = boto3.resource('ec2', region_name='ap-south-1')

# Replace this with your instance ID
instance_id = 'i-0f5e775711714efe5'

# Terminate the instance
instance = ec2.Instance(instance_id)
response = instance.terminate()

print(f"Terminating instance: {instance_id}")
print(f"Current state: {response['TerminatingInstances'][0]['CurrentState']['Name']}")
