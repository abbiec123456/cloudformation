import json

def lambda_handler(event, context):
    # Extract name from query string (?name=Abbie), default to "there"
    name = event.get('queryStringParameters', {}).get('name', 'there')

    message = f"Hello, {name}!"

    return {
        'statusCode': 200,
        'headers': {'Content-Type': 'application/json'},
        'body': json.dumps({'message': message})
    }

