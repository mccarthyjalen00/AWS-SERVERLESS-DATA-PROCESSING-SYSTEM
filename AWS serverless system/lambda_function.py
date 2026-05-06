import json
import boto3

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    
    # Get bucket and file name from the event
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    
    print(f"File uploaded: {key} in bucket: {bucket}")
    
    # Read the file data
    response = s3.get_object(Bucket=bucket, Key=key)
    data = response['Body'].read().decode('utf-8')
    
    # Simple data processing example
    processed_data = data.upper()
    print(f"Processed Data: {processed_data}")
    
    return {
        'statusCode': 200,
        'body': json.dumps('Data ingested and processed successfully!')
    }
