import boto3

#CreateS3Client
s3 = boto3.client('s3')

#S3BucketName
s3.create_bucket(Bucket='hoov-test-bucket')


