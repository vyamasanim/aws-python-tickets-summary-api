<!--
title: AWS REST API with DynamoDB store example in Python
description: This projects allows a user to do a get and post on important fields from jira tickets
layout: Doc
-->

## Use-cases

- API for a Web Application
- API for a Mobile Application



Service Information
service: rest-api-with-dynamodb
stage: dev
region: us-west-2
api keys:
  None    
endpoints:  
  POST - https://4cmev3vrsi.execute-api.us-west-2.amazonaws.com/dev/jiraTickets  
  GET - https://4cmev3vrsi.execute-api.us-west-2.amazonaws.com/dev/jiraTickets?ticket_id={id}  
  
functions:
  arn:aws:lambda:us-west-2:577088235930:function:jiraTickets

## Usage

You can create, retrieve, jiraTickets with the following commands:

### Create a Jira Ticket Summary
```bash
curl -X POST  https://4cmev3vrsi.execute-api.us-west-2.amazonaws.com/dev/jiraTickets  --data{"description": "Admin Screen","summary": "Create Admin Screen with user roles","priority": "High","completed_dttm": "2018-01-06T15:20:07.958Z", "ticket_id": "TS-6","created_dttm": "2018-01-05T20:15:07.958Z"}
```

No output


### Get one Jira Ticket Summary

```bash
# Replace the <id>part with a real id from your todos table  (e.g. TS-1)
curl https://4cmev3vrsi.execute-api.us-west-2.amazonaws.com/dev/jiraTickets?ticket_id={id}
```

Example Result:
```bash
{"description": "Admin Screen","summary": "Create Admin Screen with user roles","priority": "High","completed_dttm": "2018-01-06T15:20:07.958Z", "ticket_id": "TS-1","created_dttm": "2018-01-05T20:15:07.958Z"}'%
```
