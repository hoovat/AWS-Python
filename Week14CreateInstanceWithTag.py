import boto3

ec2=boto3.resource('ec2')

instance=ec2.create_instances(
    ImageId='ami-06e46074ae430fba6',
    MaxCount=2,
    MinCount=2,
    InstanceType='t2.micro',
    TagSpecifications=[
        {
            'ResourceType': 'instance',
            'Tags': [
                {                    
                    'Key': 'environment',
                    'Value': 'dev',
                },
            ]
        },
    ],
)

print(instance)

