import boto3

s3_resource=boto3.client("s3")

s3_resource.delete_object(Bucket='hoov-test-bucket',
Key='Hoova Taylor Resume.pages')

