from fastapi import FastAPI
from pydantic import BaseModel
import mysql.connector

app = FastAPI()

# Define Student model
class Student(BaseModel):
    name: str
    age: int
    grade: str
    marks: int

# Database connection function
def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Mahitha!2002",  # change this
        database="school"
    )

# API to fetch students-- Rad all students.
@app.get("/students")
def get_students():
    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    cursor.execute("SELECT * FROM students")
    data = cursor.fetchall()

    connection.close()

    return data

# API to add a student-- write a student to the database.
@app.post("/students")
def add_student(student: Student):
    connection = get_connection()
    cursor = connection.cursor()

    query = "INSERT INTO students (name, age, grade, marks) VALUES (%s, %s, %s, %s)"
    values = (student.name, student.age, student.grade, student.marks)

    cursor.execute(query, values)
    connection.commit()
    connection.close()

    return {"message": "Student added successfully"}
