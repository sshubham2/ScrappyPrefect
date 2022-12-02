from prefect_aws.s3 import S3Bucket
from prefect_aws import AwsCredentials
from src.config.context_vars import settings, ENV_VARS

class BLOCK_NAMES:
    S3_BUCKET = "s3bucket"
    AWS_CRED = "awscredentials"

def get_s3_bucket():
    try:
        aws_credentials_block = AwsCredentials.load(BLOCK_NAMES.AWS_CRED)
    except ValueError as err:
        print("Bucket not present. Creating..")
        AwsCredentials(
            aws_access_key_id=settings[ENV_VARS.AWS_ACCESS_KEY_ID],
            aws_secret_access_key=settings[ENV_VARS.AWS_SECRET_ACCESS_KEY]
        ).save(BLOCK_NAMES.AWS_CRED)
        aws_credentials_block = AwsCredentials.load(BLOCK_NAMES.AWS_CRED)
    try:
        S3Bucket.load(BLOCK_NAMES.S3_BUCKET)
    except ValueError as err:
        print("S3 bucket not present creating..")
        S3Bucket(
            bucket_name="prefect-baalti",  # must exist
            aws_credentials=aws_credentials_block
        ).save(name=BLOCK_NAMES.S3_BUCKET)
    return S3Bucket.load(BLOCK_NAMES.S3_BUCKET)

