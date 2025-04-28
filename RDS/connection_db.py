import psycopg2
from psycopg2 import OperationalError


endpoint = "database-1.cdaym4aucjdp.ap-south-1.rds.amazonaws.com"
port = 5432
database = "postgres"       
username = "Kanishk"         
password = "KanishkMandwal"      

try:
    conn = psycopg2.connect(
        host=endpoint,
        port=port,
        user=username,
        password=password,
        dbname=database
    )
    print("Successfully connected to the RDS PostgreSQL database.")
    conn.close()

except OperationalError as e:
    print(f"An error occurred while connecting to the RDS: {e}")
