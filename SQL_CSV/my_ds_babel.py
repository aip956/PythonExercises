import sqlite3
import csv
import io

def sql_to_csv(database, table_name):

    # Connect to the SQLite db
    conn = sqlite3.connect(database)
    cursor = conn.cursor()

    # Fetch data from the table
    cursor.execute(f"SELECT * FROM {table_name}")
    rows = cursor.fetchall()

    # Fetch column names
    cursor.execute(f"PRAGMA table_info({table_name})")
    columns = [col[1] for col in cursor.fetchall()]

    # Write to CSV format
    output = io.StringIO()
    csv_writer = csv.writer(output)

    # Write header
    csv_writer.writerow(columns)
    # Write data rows
    csv_writer.writerow(rows)

    # Close the database connection
    conn.close()

    return output.getvalue()

