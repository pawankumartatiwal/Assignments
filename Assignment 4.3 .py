import sqlite3

# Connect to database 
conn = sqlite3.connect('school.db')

# Create table 
conn.execute('''
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER
)
''')

# Clear existing records 
conn.execute("DELETE FROM students")

# Insert new student records
conn.execute("""
INSERT INTO students (name, age)
VALUES 
    ('Amit', 19),
    ('Neha', 21),
    ('Rohit', 20),
    ('Simran', 22)
""")

# Show all students
print("All students:")
cursor = conn.execute("SELECT * FROM students")
for row in cursor:
    print(row)

# Update Rohit's age
conn.execute("UPDATE students SET age = 23 WHERE name = 'Rohit'")

# Delete Neha
conn.execute("DELETE FROM students WHERE name = 'Neha'")

# Show updated list
print("\nAfter changes:")
cursor = conn.execute("SELECT * FROM students")
for row in cursor:
    print(row)

# Save changes and close the connection
conn.commit()
conn.close()
