import json


def lambda_handler(event, context):
    name = 'Bot'
    city = 'World'
    time = 'day'
    day = ''
    response_code = 200
    response_body = {
        'message': 'greeting',
        'input': json.dumps(event)
    }
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
    
    print(name)
    response = {
        'statusCode': response_code,
        'headers': {
            'x-custom-header' : 'my custom header value'
        },
        'body': json.dumps(response_body)
    }
    return response
