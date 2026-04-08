from typing import Optional
from app.db import supabase


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

    if supabase is None:
        return _error("Database connection is not configured")

    try:
        response = supabase.table("courses").select("*").execute()
        return _success(response.data, "Courses listed successfully")
    except Exception as e:
        return _error(f"Database error: {str(e)}")


def getActivity(email: str, password: str, course_id: str, activity_no: int) -> dict:
    if not all([email, password, course_id]) or activity_no is None:
        return _error("Missing required fields")

    if supabase is None:
        return _error("Database connection is not configured")

    try:
        response = (
            supabase
            .table("activities")
            .select("*")
            .eq("course_id", course_id)
            .eq("activity_no", activity_no)
            .execute()
        )

        if not response.data:
            return _error("Activity not found")

        return _success(response.data[0], "Activity fetched successfully")
    except Exception as e:
        return _error(f"Database error: {str(e)}")


def listActivities(email: str, password: str, course_id: str) -> dict:
    if not all([email, password, course_id]):
        return _error("Missing required fields")

    if supabase is None:
        return _error("Database connection is not configured")

    try:
        response = (
            supabase
            .table("activities")
            .select("*")
            .eq("course_id", course_id)
            .execute()
        )
        return _success(response.data, "Activities listed successfully")
    except Exception as e:
        return _error(f"Database error: {str(e)}")


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


def updateActivity(email: str, password: str, course_id: str, activity_no: int, activity_text: str, learning_objectives: list[str]) -> dict:
    if not all([email, password, course_id, activity_text]) or activity_no is None or not learning_objectives:
        return _error("Missing required fields")

    updated_activity = {
        "course_id": course_id,
        "activity_no": activity_no,
        "activity_text": activity_text,
        "learning_objectives": learning_objectives,
        "status": "NOT_STARTED"
    }
    return _success(updated_activity, "Activity updated successfully")


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


def changeStudentPassword(email: str, old_password: str, new_password: str) -> dict:
    if not all([email, old_password, new_password]):
        return _error("Missing required fields")

    return _success(message="Student password changed successfully")


def setStudentPassword(email: str, new_password: str) -> dict:
    if not all([email, new_password]):
        return _error("Missing required fields")

    return _success(message="Student password set successfully")


def changeInstructorPassword(email: str, old_password: str, new_password: str) -> dict:
    if not all([email, old_password, new_password]):
        return _error("Missing required fields")

    return _success(message="Instructor password changed successfully")


def setInstructorPassword(email: str, new_password: str) -> dict:
    if not all([email, new_password]):
        return _error("Missing required fields")

    return _success(message="Instructor password set successfully")
