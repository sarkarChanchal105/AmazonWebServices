import boto3
from botocore.client import Config

AWS_ACCESS_KEY_ID = 'AKIAJGI3DEMH6JKUM3NA'  # put your IAM user's access key
AWS_ACCESS_SECRET_KEY = 'Mbzwbh1xB91TdFnsF/1qS3mC7kJ0n1mR18MSE5if' # put your IAM user's sectet key
AWS_BUCKET_NAME = 'my-personal-bucket2017'  # put the name of the bucket

data = open('../local_files/Sample_upload.txt', 'rb')  # open the file from the local file system

s3 = boto3.resource(
    's3',
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_ACCESS_SECRET_KEY,
    config=Config(signature_version='s3v4')
)
s3.Bucket(AWS_BUCKET_NAME).put_object(Key='test_folder_to_create/Sample_upload.txt', Body=data)  # put the file into AWS bucket

print ("Done")