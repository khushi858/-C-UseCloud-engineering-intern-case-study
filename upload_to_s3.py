import boto3

def upload_file_to_s3(file_path, bucket_name, object_name=None):
    """
    Upload a file to an S3 bucket.
    """
    s3 = boto3.client("s3", endpoint_url="http://localhost:4566")
    if object_name is None:
        object_name = file_path.split("/")[-1]

    s3.upload_file(file_path, bucket_name, object_name)
    print(f"File {file_path} uploaded to bucket {bucket_name} as {object_name}.")
