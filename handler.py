import json


def hello(event, context):
    body = {
        "message": "Updated"
    }

    return {"statusCode": 200, "body": json.dumps(body)}
