import boto3

s3_resource=boto3.client("s3")

import os
import glob

objects=s3_resource.list_objects(Bucket="hoov-test-bucket")["Contents"]

len(objects)

for object in objects:
    s3_resource.delete_object(Bucket='hoov-test-bucket',
    Key=object["Key"])
    
print("All Objects Were Deleted Successfully")    