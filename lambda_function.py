import boto3
from csv_processor import extract_metadata

def lambda_handler(event, context):
    """
    Lambda function to process CSV uploaded to S3.
    """
    s3 = boto3.client("s3", endpoint_url="http://localhost:4566")
    dynamodb = boto3.resource("dynamodb", endpoint_url="http://localhost:4566")
    table = dynamodb.Table("metadata")

    # Retrieve S3 bucket and object details from the event
    bucket_name = event["Records"][0]["s3"]["bucket"]["name"]
    object_key = event["Records"][0]["s3"]["object"]["key"]

    # Download the file from S3
    file_path = f"/tmp/{object_key}"
    s3.download_file(bucket_name, object_key, file_path)

    # Extract metadata
    metadata = extract_metadata(file_path)
    metadata.update({
        "filename": object_key,
        "upload_timestamp": event["Records"][0]["eventTime"],
    })

    # Store metadata in DynamoDB
    table.put_item(Item=metadata)
    print("Metadata stored:", metadata)
