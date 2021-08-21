from aws_cdk import core
from aws_cdk.aws_apigateway import LambdaRestApi
from aws_cdk.aws_lambda import Runtime
from aws_cdk.aws_lambda_python import PythonFunction

APP_NAME = "CdkLambdaPowertoolsRestapi"


class CdkLambdaPowertoolsRestapiStack(core.Stack):
    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        lambda_ = PythonFunction(self, f"{APP_NAME}Lambda", entry="lambda_app", runtime=Runtime.PYTHON_3_8,)

        # RestApiでAPI Gatewayを作成する
        LambdaRestApi(self, f"{APP_NAME}Gateway", handler=lambda_)
