#Author puneetsd
from aws_cdk import (
    Stack,
    CfnOutput,
    Aws, 
    RemovalPolicy, 
    Duration,
    aws_s3 as s3,
    aws_dynamodb as dynamodb,
    aws_ec2 as ec2,
    aws_iam as iam,
    aws_lambda as lambda_,
    aws_mwaa as mwaa, 
    aws_transfer as transfer
)

from constructs import Construct

class CdkDemosStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # # Create a S3 bucket
        # bucket = s3.Bucket(self, 
        #     "create-bucket", 
        #     bucket_name="cdk-demo-bucket-"+Aws.ACCOUNT_ID, 
        #     versioned=False,
        #     removal_policy=RemovalPolicy.DESTROY,
        #     enforce_ssl=True,
        #     block_public_access=s3.BlockPublicAccess.BLOCK_ALL,
        #     encryption=s3.BucketEncryption.S3_MANAGED)
        
        # CfnOutput(self, "BucketName", value=bucket.bucket_name)

        # # CDK for creating a dynamoDB table with name puneetsd and columns sessionid
        # table = dynamodb.Table(self, "puneetsd",
        #     table_name="puneetsd",
        #     partition_key=dynamodb.Attribute(
        #         name="sessionid",
        #         type=dynamodb.AttributeType.STRING
        #     ),
        #     removal_policy=RemovalPolicy.DESTROY
        # )
        # CfnOutput(self, "TableName", value=table.table_name)

        # # Create a Lambda function
        # pdf_to_image_function = lambda_.Function(
        #     self, "cdk-demo-lambda",
        #     runtime=lambda_.Runtime.PYTHON_3_8,
        #     handler="test_lambda.handler",
        #     function_name="cdk-demo-lambda-function-"+Aws.ACCOUNT_ID,
        #     code=lambda_.Code.from_asset("cdk_demos/cdk_demo_lambdas"),
        #     timeout=Duration.minutes(5),
        #     memory_size=4096,
        #     environment={
        #         # "IMAGE_FOLDER": "images",
        #         # "IMAGE_FORMAT": "png",
        #         "LOG_LEVEL": "INFO",
        #         # "PDF_FOLDER": "pdf-input"
        #     }
        # )
        
        # self.function = pdf_to_image_function
        # CfnOutput(self, "DemoLambda", value=pdf_to_image_function.function_name)

        # table.grant_read_data(pdf_to_image_function)
        # bucket.grant_read(pdf_to_image_function)
