

import boto3

s3 = boto3.client('s3')
#Delete the file from S3
s3.delete_object(
    Bucket='vashu-mandwal-bucket',
    Key='test.txt'
)
print("File 'test.txt' deleted from S3.")

# Delete the bucket (only if it is empty)
try:
    # Ensure the bucket is empty
    response = s3.list_objects_v2(Bucket='vashu-mandwal-bucket')
    if 'Contents' not in response:
        # If the bucket is empty, delete it
        s3.delete_bucket(Bucket='vashu-mandwal-bucket')
        print("Bucket 'vashu-mandwal-bucket' deleted successfully.")
    else:
        print("Bucket is not empty. Cannot delete.")
except Exception as e:
    print(f"Error deleting bucket: {e}")