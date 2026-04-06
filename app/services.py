from typing import Optional


def _success(data=None, message="Success"):
    return {
        "ok": True,
        "message": message,
        "data": data
    }


def _error(message="Error"):
    return {
        "ok": False,
        "message": message
    }


def studentLogin(email: str, password: str) -> dict:
    if not email or not password:
        return _error("Email and password are required")
    return _success({"email": email, "role": "student"}, "Student login successful")


def instructorLogin(email: str, password: str) -> dict:
    if not email or not password:
        return _error("Email and password are required")
    return _success({"email": email, "role": "instructor"}, "Instructor login successful")


def listMyCourses(email: str, password: str) -> dict:
    if not email or not password:
        return _error("Email and password are required")

    courses = [
        {"course_id": "SE101", "course_name": "Software Engineering"},
        {"course_id": "CS102", "course_name": "Intro to Programming"}
    ]
    return _success(courses, "Courses listed successfully")


def getActivity(email: str, password: str, course_id: str, activity_no: int) -> dict:
    if not all([email, password, course_id]) or activity_no is None:
        return _error("Missing required fields")

    sample_activity = {
        "course_id": course_id,
        "activity_no": activity_no,
        "activity_text": "Explain the difference between AI and Machine Learning.",
        "status": "ACTIVE"
    }
    return _success(sample_activity, "Activity fetched successfully")


def listActivities(email: str, password: str, course_id: str) -> dict:
    if not all([email, password, course_id]):
        return _error("Missing required fields")

    activities = [
        {"activity_no": 1, "status": "NOT_STARTED"},
        {"activity_no": 2, "status": "ACTIVE"}
    ]
    return _success(activities, "Activities listed successfully")


def createActivity(email: str, password: str, course_id: str, activity_text: str, learning_objectives: list[str], activity_no_optional: int | None = None) -> dict:
    if not all([email, password, course_id, activity_text]) or not learning_objectives:
        return _error("Missing required fields")

    activity = {
        "course_id": course_id,
        "activity_no": activity_no_optional if activity_no_optional is not None else 1,
        "activity_text": activity_text,
        "learning_objectives": learning_objectives,
        "status": "NOT_STARTED"
    }
    return _success(activity, "Activity created successfully")


def startActivity(email: str, password: str, course_id: str, activity_no: int) -> dict:
    if not all([email, password, course_id]) or activity_no is None:
        return _error("Missing required fields")

    return _success({
        "course_id": course_id,
        "activity_no": activity_no,
        "status": "ACTIVE"
    }, "Activity started successfully")


def endActivity(email: str, password: str, course_id: str, activity_no: int) -> dict:
    if not all([email, password, course_id]) or activity_no is None:
        return _error("Missing required fields")

    return _success({
        "course_id": course_id,
        "activity_no": activity_no,
        "status": "ENDED"
    }, "Activity ended successfully")


def logScore(email: str, password: str, course_id: str, activity_no: int, score: float, meta: Optional[str] = None) -> dict:
    if not all([email, password, course_id]) or activity_no is None:
        return _error("Missing required fields")

    return _success({
        "course_id": course_id,
        "activity_no": activity_no,
        "score": score,
        "meta": meta
    }, "Score logged successfully")


def exportScores(email: str, password: str, course_id: str, activity_no: int) -> dict:
    if not all([email, password, course_id]) or activity_no is None:
        return _error("Missing required fields")

    return _success({
        "csv_content": "student_email,score\nstudent1@example.com,2\nstudent2@example.com,3"
    }, "Scores exported successfully")


def resetActivity(email: str, password: str, course_id: str, activity_no: int) -> dict:
    if not all([email, password, course_id]) or activity_no is None:
        return _error("Missing required fields")

    return _success({
        "course_id": course_id,
        "activity_no": activity_no,
        "status": "ENDED"
    }, "Activity reset successfully")


def resetStudentPassword(email: str, password: str, course_id: str, student_email: str, new_password: str) -> dict:
    if not all([email, password, course_id, student_email, new_password]):
        return _error("Missing required fields")

    return _success(message="Student password reset successfully")
