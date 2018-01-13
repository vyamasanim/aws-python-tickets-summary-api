from __future__ import print_function
from datetime import datetime

import boto3
import json

print('Loading function')
dynamo = boto3.client('dynamodb')
dynamodb = boto3.resource('dynamodb', region_name='us-west-2')
table = dynamodb.Table('ticket_summary')


def respond(err, res=None):
    return {
        'statusCode': '400' if err else '200',
        'body': err.message if err else json.dumps(res),
        'headers': {
            'Content-Type': 'application/json',
        },
    }

#Method to calculate the difference between two dates
def days_between(d1, d2):
    d1 = datetime.strptime(d1, "%Y-%m-%dT%H:%M:%S.%fZ")
    d2 = datetime.strptime(d2,  "%Y-%m-%dT%H:%M:%S.%fZ")
    return abs((d2 - d1).days)
    
    
def lambda_handler(event, context):
    #print("Received event: " + json.dumps(event, indent=2))

    #Get HTTP Method that has been invoked
    operation = event['httpMethod']
    
    #POST Method
    if operation == 'POST':
        #Get the data from json body
        data = json.loads(event['body'])
        ticket_duration = days_between(data['created_dttm'],  data['completed_dttm'])
        #create the record
        item = {
                'ticket_id' : data['ticket_id'],
                'description': data['description'],
                'priority': data['priority'],
                'created_dttm' : data['created_dttm'],
                'completed_dttm' : data['completed_dttm'],
                'ticket_duration' : ticket_duration
                }
        #insert the record        
        table.put_item(Item=item)
        return respond(None, item)
    
    #GET method    
    elif operation == 'GET':
        result = table.get_item(
            Key={
            'ticket_id': event['queryStringParameters']['ticket_id']
            }
        )
        return respond(None, result['Item'])
    
    else:
        return respond(ValueError('Unsupported method "{}"'.format(operation))) 
             
   
        
        