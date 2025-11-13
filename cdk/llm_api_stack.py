from aws_cdk import (
    Stack,
    Duration,
    aws_lambda as _lambda,
    aws_iam as iam,
    aws_apigatewayv2 as apigw,
    aws_apigatewayv2_integrations as integrations,
)
from constructs import Construct


class LlmApiStack(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)

        # Lambda function that calls Bedrock
        llm_lambda = _lambda.Function(
            self,
            "LLMLambda",
            runtime=_lambda.Runtime.PYTHON_3_10,
            handler="handler.handler",          # file.handler_function
            code=_lambda.Code.from_asset("../lambda"),
            timeout=Duration.seconds(30),
            environment={
                "AWS_REGION": "us-east-1",
                "MODEL_ID": "anthropic.claude-3-haiku-20240307",
            },
        )

        # Allow Lambda to call Bedrock
        llm_lambda.add_to_role_policy(
            iam.PolicyStatement(
                actions=["bedrock:InvokeModel"],
                resources=["*"],
            )
        )

        # HTTP API Gateway
        http_api = apigw.HttpApi(
            self,
            "LLMApiGateway",
            api_name="LLM-Bedrock-API",
            description="Serverless LLM API using AWS Bedrock",
        )

        # Route: POST /chat -> Lambda
        http_api.add_routes(
            path="/chat",
            methods=[apigw.HttpMethod.POST],
            integration=integrations.HttpLambdaIntegration(
                "LLMLambdaIntegration",
                llm_lambda,
            ),
        )

        # For convenience (you'll see this in 'cdk deploy' output)
        self.api_url = http_api.api_endpoint
