function inst() {
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
  const data = await postRequest("/instructor/login", inst());
  show("loginOut", data);
}

async function listActivities() {
  const data = await postRequest("/instructor/list-activities", {
    ...inst(),
    course_id: courseId()
  });
  show("activityOut", data);
}

async function createActivity() {
  const data = await postRequest("/instructor/create-activity", {
    ...inst(),
    course_id: courseId(),
    activity_text: document.getElementById("activityText").value,
    activity_no_optional: document.getElementById("newActivityNo").value
  }, ["Message types", "Message format"]);

  show("createOut", data);
}

async function startActivity() {
  const data = await postRequest("/instructor/start-activity", {
    ...inst(),
    course_id: courseId(),
    activity_no: activityNo()
  });
  show("activityOut", data);
}

async function endActivity() {
  const data = await postRequest("/instructor/end-activity", {
    ...inst(),
    course_id: courseId(),
    activity_no: activityNo()
  });
  show("activityOut", data);
}

async function exportScores() {
  const data = await postRequest("/instructor/export-scores", {
    ...inst(),
    course_id: courseId(),
    activity_no: activityNo()
  });
  show("scoreOut", data);
}

async function leaderboard() {
  const data = await postRequest("/instructor/leaderboard", {
    ...inst(),
    course_id: courseId()
  });
  show("scoreOut", data);
}

async function stats() {
  const data = await postRequest("/instructor/activity-stats", {
    ...inst(),
    course_id: courseId(),
    activity_no: activityNo()
  });
  show("scoreOut", data);
}