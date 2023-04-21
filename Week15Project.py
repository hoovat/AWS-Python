import boto3

#Get the service resource
sqs = boto3.resource('sqs')

#Create the queue. This returns an SQS.Queue instance
queue = sqs.create_queue(QueueName='Week15Project', Attributes={'DelaySeconds': '5'})

#You can now access identifiers and attributes
print(queue.url)
print(queue.attributes.get('DelaySeconds'))
