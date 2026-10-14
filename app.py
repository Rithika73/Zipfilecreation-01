import boto3
import requests
import json
from datetime import datetime
def lambda_handler(event, context):
    current_time = datetime.now()
    print(f'Hello Rithika! Current time is : {current_time}')
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
