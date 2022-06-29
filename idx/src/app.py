from dataAdaptor.input_adaptor import Input
import config
import boto3
# import requests


def lambda_handler(event, context):
    input_file = Input()
    session = boto3.Session(
            aws_access_key_id=config.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=config.AWS_SECRET_ACCESS_KEY,
        )         
    s3 = session.resource('s3')
    input_file.fileAdaptor(s3)

# def upload_to_aws():

    # uploaded = upload_to_aws('db.pdf', 'input-adaptor', 'Temp/db.pdf')
