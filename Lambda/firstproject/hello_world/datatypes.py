import time
import os
import random



global_random_val = random.random()

def cold_start_basics(event, context):
    local_rand_val = random.random()
    print(local_rand_val)
    print(global_random_val)


def lambda_handler(event, context):   
    print("Lambda function ARN:", context.invoked_function_arn)
    print("CloudWatch log stream name:", context.log_stream_name)
    print("CloudWatch log group name:",  context.log_group_name)
    print("Lambda Request ID:", context.aws_request_id)
    time.sleep(4)
    print("Lambda function memory limits in MB:", context.memory_limit_in_mb)
    print(os.getenv('sitename'))
    for ele in os.getenv("restapiurl").split(':'):
        print(ele)
  


def simple_type(event, context):
    
    return event


def list_types(event, context):
    student_scores = {"Rakx":90, "Pooja":95, "Gyan":100}
    scores = []

    for student in event:
        scores.append(student_scores[student])

    print(scores)
    return scores

def dict_types(event, context):

    print(event)
    return event["Pooja"]

