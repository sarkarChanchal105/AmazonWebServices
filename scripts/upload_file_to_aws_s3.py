import boto3
from botocore.client import Config
import config.aws_configs as aws_config

AWS_ACCESS_KEY_ID = aws_config.AWS_ACCESS_KEY_ID   # put your IAM user's access key
AWS_ACCESS_SECRET_KEY = aws_config.AWS_ACCESS_SECRET_KEY # put your IAM user's sectet key
AWS_BUCKET_NAME = aws_config.AWS_BUCKET_NAME # put the name of the bucket

FILE_NAME=aws_config.FILE_NAME

data = open('../local_files/'+FILE_NAME, 'rb')  # open the file from the local file system

s3 = boto3.resource(
    's3',
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_ACCESS_SECRET_KEY,
    config=Config(signature_version='s3v4')
)
s3.Bucket(AWS_BUCKET_NAME).put_object(Key=FILE_NAME, Body=data)  # put the file into AWS bucket

print ("Done")