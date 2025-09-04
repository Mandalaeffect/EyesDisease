import sqlite3
import os

# Path to the database
db_path = 'EyeDiseaseDetection/instance/users.db'

if os.path.exists(db_path):
    print(f"Database file exists at: {db_path}")
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Get table names
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    print(f"Tables in database: {tables}")

    for table in tables:
        table_name = table[0]
        print(f"\nTable: {table_name}")
        cursor.execute(f"PRAGMA table_info({table_name});")
        columns = cursor.fetchall()
        print("Columns:")
        for col in columns:
            print(f"  {col[1]} ({col[2]})")

        cursor.execute(f"SELECT COUNT(*) FROM {table_name};")
        count = cursor.fetchone()[0]
        print(f"Number of rows: {count}")

        if count > 0:
            cursor.execute(f"SELECT * FROM {table_name} LIMIT 5;")
            rows = cursor.fetchall()
            print("Sample rows:")
            for row in rows:
                print(f"  {row}")

    conn.close()
else:
    print(f"Database file does not exist at: {db_path}")