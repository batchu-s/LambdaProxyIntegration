import json
import base64

def lambda_handler(event, context):
    name = 'Bot'
    city = 'World'
    time = 'day'
    day = ''
    response_code = 200
    print('request: ' + json.dumps(event))
    

    if event['queryStringParameters'] and event['queryStringParameters']['name']:
        print('Received name: ' + str(event['queryStringParameters']['name']))
        name = str(event['queryStringParameters']['name'])

    if event['queryStringParameters'] and event['queryStringParameters']['city']:
        print('Received city: ' + str(event['queryStringParameters']['city']))
        city = str(event['queryStringParameters']['city'])
    
    if event['headers'] and event['headers']['day']:
        print('Received day: ' + str(event['headers']['day']))
        day = str(event['headers']['day'])
    
    if event['body']:
        base64_bytes = event['body'].encode('ascii')
        body_bytes = base64.b64decode(base64_bytes)
        body_str = body_bytes.decode('ascii')
        body_json = json.loads(body_str)
        if body_json['time']:
            time = body_json['time']

    greeting = 'Good {0}, {1} of {2}.'.format(time, name, city) 
    if day:
        greeting += ' Happy {0}'.format(day)

    response_body = {
        'message': greeting,
        'input': json.dumps(event)
    }
    
    response = {
        'statusCode': response_code,
        'headers': {
            'x-custom-header' : 'my custom header value'
        },
        'body': json.dumps(response_body)
    }
    print('response: ' + json.dumps(response))
    return response
