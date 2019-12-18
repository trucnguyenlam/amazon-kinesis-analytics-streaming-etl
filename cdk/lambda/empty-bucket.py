import os
import boto3
import traceback
import cfnresponse

def empty_bucket(event, context):
    bucket_name = os.environ['bucket_name']

    try:
        if event['RequestType'] == 'Delete':
            print("empty bucket: " + bucket_name)
            
            s3 = boto3.resource('s3')
            bucket = s3.Bucket(bucket_name)
            resp = bucket.object_versions.delete()

        cfnresponse.send(event, context, cfnresponse.SUCCESS, {})
    except Exception:
        traceback.print_exc()

        cfnresponse.send(event, context, cfnresponse.FAILED, {})