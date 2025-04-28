import boto3

rds = boto3.client('rds')

response = rds.create_db_instance(
    DBInstanceIdentifier='Database-1',
    DBInstanceClass='db.t3.micro',
    Engine='postgres',
    MasterUsername='Kanishk',
    MasterUserPassword='KanishkMandwal',
    AllocatedStorage=20,
    BackupRetentionPeriod=7,
    VpcSecurityGroupIds=['sg-02f51c5489bb315ea'],
    AvailabilityZone='ap-south-1a',
    PubliclyAccessible=True
)

print(response)