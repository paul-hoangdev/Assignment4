import psycopg2
from psycopg2 import sql

# Database connection parameters
db_params = {
    "dbname": "school",
    "user": "postgres",
    "password": "admin123456",
    "host": "localhost",
    "port": 5432
}

# Connect to the PostgreSQL database
def connect_db():
    """
    Establishes and returns a connection to the PostgreSQL database.
    Replace 'your_db_name', 'your_username', 'your_password', 'your_host', and 'your_port' 
    with your actual database credentials.
    """
    try:
        conn = psycopg2.connect(**db_params)
        return conn
    except Exception as e:
        print(f"Error connecting to the database: {e}")
        return None

# CRUD Operations
def getAllStudents():
    """
    Retrieves all records from the 'students' table and prints them.
    Handles any exceptions that occur during database operations.
    """
    try:
        conn = connect_db()
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM students")
            for record in cur.fetchall():
                print(record)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if conn:
            conn.close()

def addStudent(first_name, last_name, email, enrollment_date):
    """
    Inserts a new student record into the 'students' table.
    Parameters:
    first_name (str): Student's first name
    last_name (str): Student's last name
    email (str): Student's email address
    enrollment_date (str): Date of enrollment (format: YYYY-MM-DD)
    """
    try:
        conn = connect_db()
        with conn.cursor() as cur:
            cur.execute(sql.SQL("INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s)"),
                        (first_name, last_name, email, enrollment_date))
            conn.commit()
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if conn:
            conn.close()

def updateStudentEmail(student_id, new_email):
    """
    Updates the email address for a student in the 'students' table.
    Parameters:
    student_id (int): The ID of the student to update
    new_email (str): The new email address to set
    """
    try:
        conn = connect_db()
        with conn.cursor() as cur:
            cur.execute(sql.SQL("UPDATE students SET email = %s WHERE student_id = %s"),
                        (new_email, student_id))
            conn.commit()
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if conn:
            conn.close()

def deleteStudent(student_id):
    """
    Deletes a student record from the 'students' table based on the student_id.
    Parameters:
    student_id (int): The ID of the student to delete
    """
    try:
        conn = connect_db()
        with conn.cursor() as cur:
            cur.execute(sql.SQL("DELETE FROM students WHERE student_id = %s"),
                        (student_id,))
            conn.commit()
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if conn:
            conn.close()

# Main function to test operations
def main():
    choice = -1
    while (choice != 0):
        print("0. Exit")
        print("1. Get all students' records")
        print("2. Add a new student record")
        print("3. Update the email address for a student")
        print("4. Delete the student record")
        choice = input()
        if (choice == "0"):
            break
        elif (choice == "1"):
            getAllStudents()
        elif (choice == "2"):
            fname = input("Please enter student's first name: ")
            lname = input("Please enter student's last name: ")
            email = input("Please enter student's email: ")
            enr_date = input("Please enter student's enrollment date: ")
            addStudent(fname, lname, email, enr_date)
        elif (choice == "3"):
            id = input("Please enter student's ID: ")
            new_email = input("Please enter student's new email: ")
            updateStudentEmail(id, new_email)
        else:
            id = input("Please enter student's ID: ")
            deleteStudent(id)
            
if __name__ == "__main__":
    main()
