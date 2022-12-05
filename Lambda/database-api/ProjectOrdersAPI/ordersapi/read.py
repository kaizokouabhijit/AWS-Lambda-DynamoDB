import simplejson as json
import boto3
import os
from boto3.dynamodb.conditions import Key



def lambda_handler(event, context):
    print("read lambda")
    dynamo_resource = boto3.resource("dynamodb")
    table_name = "Table-for-orders-lambda-project"
    table = dynamo_resource.Table(table_name)
    order_id = int(event['pathParameters']['id'])
    response = table.query(KeyConditionExpression=Key('id').eq(order_id))
    


    return {
        'statusCode': 200,
        'body': json.dumps(response['Items'])
    }