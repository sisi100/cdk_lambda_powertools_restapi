from aws_lambda_powertools.event_handler.api_gateway import ApiGatewayResolver, ProxyEventType
from aws_lambda_powertools.utilities.data_classes import APIGatewayProxyEvent
from aws_lambda_powertools.utilities.typing import LambdaContext

app = ApiGatewayResolver(proxy_type=ProxyEventType.APIGatewayProxyEvent)


@app.get("/hello")
def get_hello_world():
    return {"message": "hello world"}


def handler(event: APIGatewayProxyEvent, context: LambdaContext):
    return app.resolve(event, context)
