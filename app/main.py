from fastapi import FastAPI
from app.services import (
    studentLogin,
    instructorLogin,
    listMyCourses,
    getActivity,
)

app = FastAPI(title="InClass LLM Platform")


@app.get("/")
def root():
    return {"ok": True, "message": "API is running"}


@app.post("/student/login")
def student_login(email: str, password: str):
    return studentLogin(email, password)


@app.post("/instructor/login")
def instructor_login(email: str, password: str):
    return instructorLogin(email, password)


@app.post("/instructor/list-my-courses")
def instructor_list_my_courses(email: str, password: str):
    return listMyCourses(email, password)


@app.post("/student/get-activity")
def student_get_activity(email: str, password: str, course_id: str, activity_no: int):
    return getActivity(email, password, course_id, activity_no)
