import psycopg2
conn = psycopg2.connect(
    host="localhost",
    database="mydata",
    user="postgres",
    password="kayode")