import json
from dataclasses import dataclass

import pytest

import lambda_app.index as app


@pytest.fixture
def lambda_context():
    @dataclass
    class LambdaContext:
        function_name: str = "test"
        memory_limit_in_mb: int = 128
        invoked_function_arn: str = "arn:aws:lambda:xx-xxxx-x:000000000:function:test"
        aws_request_id: str = "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"

    return LambdaContext()


def test_get_hello(lambda_context):
    minimal_event = {
        "path": "/hello",
        "httpMethod": "GET",
        "requestContext": {"requestId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"},
    }

    response = app.handler(minimal_event, lambda_context)

    assert response["statusCode"] == 200
    assert json.loads(response["body"]) == {"message": "hello world"}
