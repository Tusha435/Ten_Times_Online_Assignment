import psycopg2
import csv

# Connect to PostgreSQL database
connection = psycopg2.connect(
    database="newsdb",
    user="postgres",
    password="admin123",
    host="localhost",
    port="5432"
)

cursor = connection.cursor()
cursor.execute("SELECT * FROM articles")

# Write to CSV file
with open('output.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow([i[0] for i in cursor.description])  # Write header
    csvwriter.writerows(cursor.fetchall())  # Write data

cursor.close()
connection.close()
