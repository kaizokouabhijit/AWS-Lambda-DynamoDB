import boto3
import json



s3 = boto3.client("s3")

def lambda_handler(event, context):
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    file_key = event['Records'][0]['s3']['object']['key']
    obj = s3.get_object(Bucket = bucket_name, Key = file_key)
    content = obj['Body'].read().decode('UTF-8')
    checkout_events = json.loads(content)
    
    for ele in checkout_events:
        print(ele)

