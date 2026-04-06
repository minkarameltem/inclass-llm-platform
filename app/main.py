from fastapi import FastAPI
from app.services import (
    studentLogin,
    instructorLogin,
    listMyCourses,
    getActivity,
    listActivities,
    createActivity,
    startActivity,
    endActivity,
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


@app.post("/instructor/list-activities")
def instructor_list_activities(email: str, password: str, course_id: str):
    return listActivities(email, password, course_id)


@app.post("/instructor/create-activity")
def instructor_create_activity(email: str, password: str, course_id: str, activity_text: str, learning_objectives: list[str], activity_no_optional: int | None = None):
    return createActivity(email, password, course_id, activity_text, learning_objectives, activity_no_optional)


@app.post("/instructor/start-activity")
def instructor_start_activity(email: str, password: str, course_id: str, activity_no: int):
    return startActivity(email, password, course_id, activity_no)


@app.post("/instructor/end-activity")
def instructor_end_activity(email: str, password: str, course_id: str, activity_no: int):
    return endActivity(email, password, course_id, activity_no)
