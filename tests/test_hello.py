import json

import lambda_app.index as app


def test_get_hello():
    minimal_event = {
        "path": "/hello",
        "httpMethod": "GET",
        "requestContext": {"requestId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"},
    }

    response = app.handler(minimal_event, {})

    assert response["statusCode"] == 200
    assert json.loads(response["body"]) == {"message": "hello world"}
