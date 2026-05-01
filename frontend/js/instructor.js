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
  return parseInt(document.getElementById("activityNo").value.trim());
}

function niceMessage(data, successText) {
  if (data.ok) return "✔ " + successText;
  return "✖ " + (data.message || "Error");
}

async function login() {
  const data = await postRequest("/instructor/login", inst());
  document.getElementById("loginOut").textContent =
    niceMessage(data, "Login successful");
}

async function listCourses() {
  const data = await postRequest("/instructor/list-my-courses", inst());
  document.getElementById("courseOut").textContent =
    JSON.stringify(data.data, null, 2);
}

async function listActivities() {
  const data = await postRequest("/instructor/list-activities", {
    ...inst(),
    course_id: courseId()
  });

  if (!data.ok) {
    document.getElementById("activityOut").textContent = "✖ " + data.message;
    return;
  }

  const activities = data.data || [];
  let text = "✔ Activities listed successfully.\n\n";

  activities.forEach(a => {
    text += `Activity ${a.activity_no} | Status: ${a.status}\n`;
    text += `${a.activity_text || ""}\n\n`;
  });

  document.getElementById("activityOut").textContent = text;
}

async function createActivity() {
  const data = await postRequest("/instructor/create-activity", {
    ...inst(),
    course_id: courseId(),
    activity_text: document.getElementById("activityText").value,
    activity_no_optional: parseInt(document.getElementById("newActivityNo").value),
    learning_objectives: ["Message types"]
  });

  document.getElementById("createOut").textContent =
    niceMessage(data, "Created");
}

async function startActivity() {
  const data = await postRequest("/instructor/start-activity", {
    ...inst(),
    course_id: courseId(),
    activity_no: activityNo()
  });

  document.getElementById("activityOut").textContent =
    niceMessage(data, "Started");
}

async function endActivity() {
  const data = await postRequest("/instructor/end-activity", {
    ...inst(),
    course_id: courseId(),
    activity_no: activityNo()
  });

  document.getElementById("activityOut").textContent =
    niceMessage(data, "Ended");
}

async function updateActivity() {
  const data = await postRequest(
    "/instructor/update-activity",
    {
      ...inst(),
      course_id: courseId(),
      activity_no: activityNo()
    },
    {
      activity_text: document.getElementById("updateText").value
    }
  );

  document.getElementById("activityOut").textContent =
    niceMessage(data, "Updated");
}

async function resetActivity() {
  const data = await postRequest("/instructor/reset-activity", {
    ...inst(),
    course_id: courseId(),
    activity_no: activityNo()
  });

  document.getElementById("activityOut").textContent =
    niceMessage(data, "Reset done");
}

async function exportScores() {
  const data = await postRequest("/instructor/export-scores", {
    ...inst(),
    course_id: courseId(),
    activity_no: activityNo()
  });

  document.getElementById("scoreOut").textContent =
    JSON.stringify(data.data, null, 2);
}

async function leaderboard() {
  const data = await postRequest("/instructor/leaderboard", {
    ...inst(),
    course_id: courseId()
  });

  document.getElementById("scoreOut").textContent =
    JSON.stringify(data.data, null, 2);
}

async function stats() {
  const data = await postRequest("/instructor/activity-stats", {
    ...inst(),
    course_id: courseId(),
    activity_no: activityNo()
  });

  document.getElementById("scoreOut").textContent =
    JSON.stringify(data.data, null, 2);
}