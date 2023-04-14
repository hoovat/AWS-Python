import boto3
ec2_resource=boto3.resource("ec2")
ec2_resource.create_instances(ImageId='ami-06e46074ae430fba6',
InstanceType='t2.micro',
    MaxCount=3,
    MinCount=3,)
    
print("New EC2 Instances Created")
