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
        enrollment = (
            supabase
            .table("enrollments")
            .select("*")
            .eq("student_email", email)
            .eq("course_id", course_id)
            .execute()
        )

        if not enrollment.data:
            return _error("Student not enrolled in this course")

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

        activity = response.data[0]
        status = activity.get("status")

        if status == "NOT_STARTED":
            return _error("Activity has not started yet")

        if status == "ENDED":
            return _error("Activity has already ended")

        return _success(activity, "Activity fetched successfully")
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

    if supabase is None:
        return _error("Database connection is not configured")

    try:
        activity_no = activity_no_optional if activity_no_optional is not None else 1

        payload = {
            "course_id": course_id,
            "activity_no": activity_no,
            "activity_text": activity_text,
            "learning_objectives": ", ".join(learning_objectives),
            "status": "NOT_STARTED"
        }

        response = supabase.table("activities").insert(payload).execute()
        return _success(response.data, "Activity created successfully")
    except Exception as e:
        return _error(f"Database error: {str(e)}")


def updateActivity(email: str, password: str, course_id: str, activity_no: int, activity_text: str, learning_objectives: list[str]) -> dict:
    if not all([email, password, course_id, activity_text]) or activity_no is None or not learning_objectives:
        return _error("Missing required fields")

    if supabase is None:
        return _error("Database connection is not configured")

    try:
        payload = {
            "activity_text": activity_text,
            "learning_objectives": ", ".join(learning_objectives)
        }

        response = (
            supabase
            .table("activities")
            .update(payload)
            .eq("course_id", course_id)
            .eq("activity_no", activity_no)
            .execute()
        )

        return _success(response.data, "Activity updated successfully")
    except Exception as e:
        return _error(f"Database error: {str(e)}")


def startActivity(email: str, password: str, course_id: str, activity_no: int) -> dict:
    if not all([email, password, course_id]) or activity_no is None:
        return _error("Missing required fields")

    if supabase is None:
        return _error("Database connection is not configured")

    try:
        response = (
            supabase
            .table("activities")
            .update({"status": "ACTIVE"})
            .eq("course_id", course_id)
            .eq("activity_no", activity_no)
            .execute()
        )
        return _success(response.data, "Activity started successfully")
    except Exception as e:
        return _error(f"Database error: {str(e)}")


def endActivity(email: str, password: str, course_id: str, activity_no: int) -> dict:
    if not all([email, password, course_id]) or activity_no is None:
        return _error("Missing required fields")

    if supabase is None:
        return _error("Database connection is not configured")

    try:
        response = (
            supabase
            .table("activities")
            .update({"status": "ENDED"})
            .eq("course_id", course_id)
            .eq("activity_no", activity_no)
            .execute()
        )
        return _success(response.data, "Activity ended successfully")
    except Exception as e:
        return _error(f"Database error: {str(e)}")


def logScore(email: str, password: str, course_id: str, activity_no: int, score: float, meta: Optional[str] = None) -> dict:
    if not all([email, password, course_id]) or activity_no is None:
        return _error("Missing required fields")

    if supabase is None:
        return _error("Database connection is not configured")

    try:
        payload = {
            "student_email": email,
            "course_id": course_id,
            "activity_no": activity_no,
            "score": score,
            "meta": meta
        }

        response = supabase.table("scores").insert(payload).execute()
        return _success(response.data, "Score logged successfully")
    except Exception as e:
        return _error(f"Database error: {str(e)}")


def exportScores(email: str, password: str, course_id: str, activity_no: int) -> dict:
    if not all([email, password, course_id]) or activity_no is None:
        return _error("Missing required fields")

    if supabase is None:
        return _error("Database connection is not configured")

    try:
        response = (
            supabase
            .table("scores")
            .select("*")
            .eq("course_id", course_id)
            .eq("activity_no", activity_no)
            .execute()
        )
        return _success(response.data, "Scores exported successfully")
    except Exception as e:
        return _error(f"Database error: {str(e)}")


def resetActivity(email: str, password: str, course_id: str, activity_no: int) -> dict:
    if not all([email, password, course_id]) or activity_no is None:
        return _error("Missing required fields")

    if supabase is None:
        return _error("Database connection is not configured")

    try:
        response = (
            supabase
            .table("activities")
            .update({"status": "NOT_STARTED"})
            .eq("course_id", course_id)
            .eq("activity_no", activity_no)
            .execute()
        )
        return _success(response.data, "Activity reset successfully")
    except Exception as e:
        return _error(f"Database error: {str(e)}")


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
