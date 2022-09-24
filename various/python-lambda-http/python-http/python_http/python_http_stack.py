from aws_cdk import (
    Duration,
    Stack,
    aws_dynamodb,
    aws_lambda,
    aws_apigatewayv2_alpha as apigw,
    aws_apigatewayv2_integrations_alpha as api_integrations
)
from constructs import Construct


class ImportedResources:
    def __init__(self, stack: Stack):
        arn_prefix = f'arn:aws:dynamodb:{stack.region}:{stack.account}:table/'
        self.users_table = aws_dynamodb.Table.from_table_arn(
            stack,
            'users-table',
            f'{arn_prefix}users'
        )


class UserLambdas:
    def __init__(self, stack: Stack, resources: ImportedResources):
        lambda_defaults = {
            'runtime': aws_lambda.Runtime.PYTHON_3_9,
            'code': aws_lambda.Code.from_asset('../src'),
            'architecture': aws_lambda.Architecture.ARM_64
        }
        self.get_user = aws_lambda.Function(
            stack,
            'get-user',
            function_name='get-user',
            handler='get_user.lambda_handler',
            memory_size=512,
            timeout=Duration.seconds(10),
            **lambda_defaults
        )
        resources.users_table.grant_read_data(self.get_user)


class PythonHttpStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        resources = ImportedResources(self)
        lambdas = UserLambdas(self, resources)
        self.create_user_api(lambdas)

    def create_user_api(self, lambdas: UserLambdas):
        user_api = apigw.HttpApi(
            self,
            'user-api',
            cors_preflight={
                'allow_methods': [apigw.CorsHttpMethod.ANY],
                'allow_origins': ['*'],
                'allow_headers': [
                    'Content-Type',
                    'Authorization',
                    'X-Amz-Date',
                    'X-Api-Key',
                    'X-Amz-Security-Token',
                    'X-Amz-User-Agent'
                ]
            }
        )

        user_api.add_routes(
            path='/user',
            methods=[apigw.HttpMethod.GET],
            integration=api_integrations.HttpLambdaIntegration(
                'get-user',
                lambdas.get_user
            )
        )
