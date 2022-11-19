import logging

from botocore.client import BaseClient
from botocore.exceptions import ClientError


def upload_file_to_bucket(s3_client: BaseClient, file_obj, object_name: str):
    try:
        response = s3_client.upload_fileobj(file_obj, 'wardrobbers', object_name)
        return 'https://wardrobbers.s3.eu-central-1.amazonaws.com/' + object_name
    except ClientError as e:
        logging.error(e)
        return ''
