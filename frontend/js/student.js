function student() {
  return {
    email: document.getElementById("email").value.trim(),
    password: document.getElementById("password").value.trim()
  };
}

function courseId() {
  return document.getElementById("courseId").value.trim();
}

function activityNo() {
  return document.getElementById("activityNo").value.trim();
}

async function login() {
  const data = await postRequest("/student/login", student());
  show("loginOut", data);
}

async function getActivity() {
  const data = await postRequest("/student/get-activity", {
    ...student(),
    course_id: courseId(),
    activity_no: activityNo()
  });
  show("activityOut", data);
}

async function logScore() {
  const data = await postRequest("/student/log-score", {
    ...student(),
    course_id: courseId(),
    activity_no: activityNo(),
    score: document.getElementById("score").value,
    meta: document.getElementById("meta").value
  });
  show("scoreOut", data);
}