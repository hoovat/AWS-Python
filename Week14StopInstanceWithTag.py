import boto3

ec2 = boto3.resource('ec2')
ec2_filter=[
    {'Name': 'tag:environment', 'Values': ['dev']}, {'Name': 'instance-state-name', 'Values': ['running']}]

ec2.instances.filter(Filters=ec2_filter).stop()

print("Tagged EC2 Instances Stopped Successfully")

