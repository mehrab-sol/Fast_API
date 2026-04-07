from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from database import SessionLocal, engine
from models import Student
from schemas import StudentCreate, StudentResponse
from database import Base

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency for DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Home route
@app.get("/")
def home():
    return {"message": "Student CRUD API"}

# CREATE student
@app.post("/students/", response_model=StudentResponse)
def create_student(student: StudentCreate, db: Session = Depends(get_db)):
    new_student = Student(
        name=student.name,
        age=student.age,
        department=student.department
    )
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return new_student

# READ all students
@app.get("/students/")
def get_students(db: Session = Depends(get_db)):
    return db.query(Student).all()

# READ one student
@app.get("/students/{student_id}")
def get_student(student_id: int, db: Session = Depends(get_db)):
    student = db.query(Student).filter(Student.id == student_id).first()

    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    return student

# UPDATE student
@app.put("/students/{student_id}")
def update_student(student_id: int, updated_data: StudentCreate, db: Session = Depends(get_db)):
    student = db.query(Student).filter(Student.id == student_id).first()

    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    student.name = updated_data.name
    student.age = updated_data.age
    student.department = updated_data.department

    db.commit()
    db.refresh(student)

    return {"message": "Updated successfully", "data": student}

# DELETE student
@app.delete("/students/{student_id}")
def delete_student(student_id: int, db: Session = Depends(get_db)):
    student = db.query(Student).filter(Student.id == student_id).first()

    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    db.delete(student)
    db.commit()

    return {"message": "Deleted successfully"}