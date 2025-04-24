import boto3

s3 = boto3.client('s3')

# Upload a file
s3.upload_file(
    Filename=r'C:\Users\kanis\Downloads\sql.pdf',
    Bucket='vashu-mandwal-bucket',
    Key='test.txt'  # This will be the name of the file in S3
)

# Download the same file with a new name
s3.download_file(
    Bucket='vashu-mandwal-bucket',
    Key='test.txt',
    Filename=r'C:\Users\kanis\Downloads\sql2.pdf'
)


