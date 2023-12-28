from fastapi import FastAPI, HTTPException, status
from uuid import UUID, uuid4
from models import StudentModel

app = FastAPI()

students_db = {}


@app.post("/students/", response_model=StudentModel, status_code=status.HTTP_200_OK)
def create_student(student: StudentModel):
    student_id = uuid4()
    student.id = student_id
    students_db[student_id] = student
    return student


@app.get("/students/{student_id}", response_model=StudentModel)
def read_student(student_id: UUID):
    if student_id not in students_db:
        raise HTTPException(status_code=404, detail="Студент не найден")
    return students_db[student_id]


@app.put("/students/{student_id}", response_model=StudentModel)
def update_student(student_id: UUID, updated_student: StudentModel):
    if student_id not in students_db:
        raise HTTPException(status_code=404, detail="Студент не найден")
    updated_student.id = student_id
    students_db[student_id] = updated_student
    return students_db[student_id]


@app.delete("/students/{student_id}", response_model=StudentModel)
def delete_student(student_id: UUID):
    if student_id not in students_db:
        raise HTTPException(status_code=404, detail="Студент не найден")
    deleted_student = students_db.pop(student_id)
    return deleted_student


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
