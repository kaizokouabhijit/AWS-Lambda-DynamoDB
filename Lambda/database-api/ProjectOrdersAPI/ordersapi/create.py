import json
import boto3
import os


def lambda_handler(event, context):
    print("Create lambda")
    order = json.loads(event['body'])
    dynamo_resource = boto3.resource("dynamodb")
    table_name = "Table-for-orders-lambda-project"

    table = dynamo_resource.Table(table_name)
    response = table.put_item(TableName = table_name, Item = order)

    return {
        'statusCode': 201,
        'body': json.dumps({'message': 'Order created'})
    }