import boto3
ec2 = boto3.resource('ec2')
ec2.Instance('i-0d170563450ef04fb').stop()
ec2.Instance('i-05c7775e7129eca36').stop()
ec2.Instance('i-0613ac33cdce1b37f').stop()

print("EC2 Instances Stopped Successfully")

