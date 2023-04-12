import boto3

client=boto3.client("ec2")

response = client.delete_vpc(
    VpcId='vpc-01bc661a445772285'
    )

print("VPC Deleted Succesfully")

