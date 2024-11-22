import mysql.connector

# Connect to MySQL Database
db = mysql.connector.connect(
    host="localhost",
    user="root", 
    password="root",
    database="StudentDB"
)

cursor = db.cursor()

# Function to Add a New Student
def add_student():
    name = input("Enter student's name: ")
    age = int(input("Enter student's age: "))
    grade = input("Enter student's grade: ")

    sql = "INSERT INTO Students (name, age, grade) VALUES (%s, %s, %s)"
    values = (name, age, grade)
    cursor.execute(sql, values)
    db.commit()
    print("Student added successfully!")

# Function to View All Students
def view_students():
    cursor.execute("SELECT * FROM Students")
    results = cursor.fetchall()
    if results:
        print("\n--- Student Records ---")
        for student in results:
            print(f"ID: {student[0]}, Name: {student[1]}, Age: {student[2]}, Grade: {student[3]}")
    else:
        print("No students found.")

# Function to Update a Student's Details
def update_student():
    student_id = int(input("Enter the ID of the student to update: "))
    print("1. Update Name\n2. Update Age\n3. Update Grade")
    choice = int(input("What would you like to update? "))

    if choice == 1:
        new_name = input("Enter the new name: ")
        sql = "UPDATE Students SET name = %s WHERE id = %s"
        values = (new_name, student_id)
    elif choice == 2:
        new_age = int(input("Enter the new age: "))
        sql = "UPDATE Students SET age = %s WHERE id = %s"
        values = (new_age, student_id)
    elif choice == 3:
        new_grade = input("Enter the new grade: ")
        sql = "UPDATE Students SET grade = %s WHERE id = %s"
        values = (new_grade, student_id)
    else:
        print("Invalid choice!")
        return

    cursor.execute(sql, values)
    db.commit()
    print("Student updated successfully!")

# Function to Delete a Student
def delete_student():
    student_id = int(input("Enter the ID of the student to delete: "))
    sql = "DELETE FROM Students WHERE id = %s"
    values = (student_id,)
    cursor.execute(sql, values)
    db.commit()
    print("Student deleted successfully!")

# Main Menu
def main():
    while True:
        print("\n--- Student Management System ---")
        print("1. Add Student\n2. View Students\n3. Update Student\n4. Delete Student\n5. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            add_student()
        elif choice == 2:
            view_students()
        elif choice == 3:
            update_student()
        elif choice == 4:
            delete_student()
        elif choice == 5:
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
