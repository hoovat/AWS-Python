import boto3

ec2=boto3.resource('ec2')

instance=ec2.create_instances(
    ImageId='ami-06e46074ae430fba6',
    MaxCount=3,
    MinCount=3,
    InstanceType='t2.micro',
    )
print(instance)