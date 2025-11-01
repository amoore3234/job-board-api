import os
import psycopg2
from psycopg2 import pool

def get_db_connection():
  postgresql_connection_pool = None
  try:
    postgresql_connection_pool = pool.SimpleConnectionPool(
          1,
          10,
          user=os.getenv("POSTGRES_USER_TEST"),
          password=os.getenv("POSTGRES_PASSWORD_TEST"),
          host=os.getenv("POSTGRES_HOST_TEST"),
          port=os.getenv("POSTGRES_PORT_TEST"),
          database=os.getenv("POSTGRES_DB_TEST")
        )
    print("Connection pool created successfully")
    return postgresql_connection_pool
  except (Exception, psycopg2.DatabaseError) as error:
      print("Error while connecting to PostgreSQL:", error)