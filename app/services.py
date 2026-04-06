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
