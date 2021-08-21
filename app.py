#!/usr/bin/env python3

from aws_cdk import core

from cdk_lambda_powertools_restapi.cdk_lambda_powertools_restapi_stack import CdkLambdaPowertoolsRestapiStack


app = core.App()
CdkLambdaPowertoolsRestapiStack(app, "cdk-lambda-powertools-restapi")

app.synth()
