import sqlite3
import csv
import io

def sql_to_csv(database, table_name):
    # Use "List of all fault lines"
    # Connect to the SQLite db
    conn = sqlite3.connect(database)
    cursor = conn.cursor()

    # Fetch data from the table
    cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
    row_count = cursor.fetchone()[0]
    print("row_count: ", row_count)
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
    csv_writer.writerows(rows)

    # Close the database connection
    conn.close()

    return output.getvalue()

def csv_to_sql(csv_content, database, table_name):
    # Connect to the SQLite db
    conn = sqlite3.connect(database)
    cursor = conn.cursor()

    # Read CSV content
    csv_reader = csv.reader(csv_content)

    # Extract column names from the first row
    columns = next(csv_reader)
    placeholders = ', '.join(['?' for _ in columns]) # Creates placholders for INSERT

    # Create the table dynamically
    column_definitions = ', '.join([f"{col} TEXT" for col in columns])
    cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} ({column_definitions})")

    # Insert rows
    for row in csv_reader:
        cursor.execute(f"INSERT INTO {table_name} VALUES {placeholders}", row)
    
    # Commit and close the connection 
    conn.commit()
    conn.close()



if __name__ == "__main__":
    database_file = "all_fault_line.db"
    table_name = "fault_lines"

    # Convert SQL to CSV and print result
    csv_result = sql_to_csv(database_file, table_name)
    print(csv_result)

    # Save the CSV result to a file
    with open("fault_lines.csv", "w") as file:
        file.write(csv_result)
