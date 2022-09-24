import json
import boto3

dynamodb = boto3.resource('dynamodb')


def lambda_handler(event, context):
    """ /get-user?user_id={numeric} """

    user_id = event.get("queryStringParameters", {})['user_id']

    #  load details from dynamo

    return {
        'statusCode': 200,
        'body': json.dumps({
            'id': user_id
            # add user details to response
        })
    }
