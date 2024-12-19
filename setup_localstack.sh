#!/bin/bash
# Create S3 bucket
awslocal s3 mb s3://my-bucket

# Create DynamoDB table
awslocal dynamodb create-table \
    --table-name metadata \
    --attribute-definitions AttributeName=filename,AttributeType=S \
    --key-schema AttributeName=filename,KeyType=HASH \
    --provisioned-throughput ReadCapacityUnits=5,WriteCapacityUnits=5
