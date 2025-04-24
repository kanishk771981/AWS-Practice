import boto3

s3 = boto3.client(
    's3',
    aws_access_key_id="AKIAVTAQN5NNXTL7UQWO",
    aws_secret_access_key="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",
    region_name='ap-south-1'
)

s3.create_bucket(
    Bucket='vashu-mandwal-bucket',
    CreateBucketConfiguration={
        'LocationConstraint': 'ap-south-1'
    }
)





# # 2. Upload a file to the bucket
# s3_client.upload_file(
#     Filename='"C:\Users\kanis\Downloads\sql.pdf"',
#     Bucket=bucket_name,
#     Key='sql.pdf'
# )
# print("File uploaded successfully.")

# # 3. Download the file from the bucket
# s3_client.download_file(
#     Bucket=bucket_name,
#     Key='sql.pdf',
#     Filename='downloaded_file.pdff'
# )
# print("File downloaded successfully.")

# # 4. List files in the bucket
# response = s3_client.list_objects_v2(Bucket=bucket_name)
# if 'Contents' in response:
#     print("Files in bucket:")
#     for obj in response['Contents']:
#         print("-", obj['Key'])
# else:
#     print("Bucket is empty.")

# # 5. Delete the uploaded file
# s3_client.delete_object(Bucket=bucket_name, Key='sql.pdf')
# print("File deleted.")
    