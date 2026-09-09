import json
from calculator import add, subtract, multiply

def lambda_handler(event, context):
    path = event.get("path", "")
    
    body = event.get("body")

    if isinstance(body, str):
        body = json.loads(body)

    if body is None:
        body = {}

    a = body.get("a")
    b = body.get("b")

    if not isinstance(a, int) or not isinstance(b, int):
        return {
            "statusCode": 400,
            "body": json.dumps({
                "error": "a and b must be integers"
            })
        }

    if a <= 0 or b <= 0:
        return {
            "statusCode": 400,
            "body": json.dumps({
                "error": "a and b must be positive integers"
            })
        }

    if path.endswith("/add"):
        result = add(a, b)

    elif path.endswith("/subtract"):
        result = subtract(a, b)

    elif path.endswith("/multiply"):
        result = multiply(a, b)

    else:
        return {
            "statusCode": 404,
            "body": json.dumps({
                "error": "Unknown operation"
            })
        }

    return {
        "statusCode": 200,
        "body": json.dumps({
            "result": result
        })
    }
