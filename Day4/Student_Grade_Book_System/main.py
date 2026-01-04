from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import Dict, List

app = FastAPI()

class StudentCreate(BaseModel):
    id: int
    name: str
    marks: Dict[str, int]

class UpdateMarks(BaseModel):
    marks: Dict[str, int]

class StudentGradeBook:
    def __init__(self):
        self.students: List[Dict] = []

    def add_student(self, student: StudentCreate):
        for s in self.students:
            if s['id'] == student.id:
                raise HTTPException(status_code = status.HTTP_400_BAD_REQUEST, detail="Student with this ID already exists")
        self.students.append({
            "id":student.id,
            "name":student.name,    
            "marks":student.marks
        })
    
    def get_student_by_name(self, name: str):
        for s in self.students:
            if s['name'].lower() == name.lower():
                return s
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = "Student not found")
    
    def update_student_marks(self, id: int, new_marks: Dict[str, int]):
        for s in self.students:
            if s['id'] == id:
                s['marks'].update(new_marks)
                return s
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = "Student not found")  
    
    def delete_student(self, id: int):
        for i, s in enumerate(self.students):
            if s['id'] == id:
                del self.students[i]
                return {"detail": "Student deleted successfully"}
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = "Student not found")
    
    def class_average(self):
        total_marks = 0
        total_subjects = 0

        if not self.students:
            raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = "No students available to calculate average")
        
        for s in self.students:
            for mark in s['marks'].values():
                total_marks += mark
                total_subjects += 1
        
        return total_marks / total_subjects
    
    def top_students(self):
        if not self.students:
            raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = "No students available to determine top students")
        
        max_average = -1
        top_students = []

        for s in self.students:
            avg = sum(s['marks'].values()) / len(s['marks'])
            if avg > max_average:
                max_average = avg
                top_students = [s]
            elif avg == max_average:
                top_students.append(s)
        
        return top_students
    
grade_book = StudentGradeBook()

# add student
@app.post("/students", status_code=201)
def add_student(student: StudentCreate):
    grade_book.add_student(student)
    return {"message": "Student added successfully"}

# get student by name
@app.get("/students/{name}")
def get_student_by_name(name: str):
    return grade_book.get_student_by_name(name)   

# update student marks
@app.put("/students/{student_id}")
def update_student_marks(student_id: int, data: UpdateMarks):
    return grade_book.update_student_marks(student_id, data.marks)

# delete student
@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    return grade_book.delete_student(student_id)

# class average
@app.get("/class/average")
def get_class_average():
    return {"average": grade_book.class_average()}

# top students
@app.get("/class/toppers")
def get_top_students():
    return {"top_students": grade_book.top_students()}