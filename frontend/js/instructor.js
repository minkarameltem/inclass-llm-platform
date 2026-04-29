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

function niceMessage(data, successText) {
  if (data.ok) {
    return "✔ " + successText;
  }
  return "✖ " + data.message;
}

async function login() {
  const data = await postRequest("/instructor/login", inst());
  document.getElementById("loginOut").textContent =
    niceMessage(data, "Instructor login successful.");
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
    text += `${a.activity_text}\n\n`;
  });

  document.getElementById("activityOut").textContent = text;
}

async function createActivity() {
  const data = await postRequest("/instructor/create-activity", {
    ...inst(),
    course_id: courseId(),
    activity_text: document.getElementById("activityText").value,
    activity_no_optional: document.getElementById("newActivityNo").value
  }, ["Message types", "Message format"]);

  document.getElementById("createOut").textContent =
    niceMessage(data, "Activity created successfully.");
}

async function startActivity() {
  const data = await postRequest("/instructor/start-activity", {
    ...inst(),
    course_id: courseId(),
    activity_no: activityNo()
  });

  document.getElementById("activityOut").textContent =
    niceMessage(data, "Activity started successfully.");
}

async function endActivity() {
  const data = await postRequest("/instructor/end-activity", {
    ...inst(),
    course_id: courseId(),
    activity_no: activityNo()
  });

  document.getElementById("activityOut").textContent =
    niceMessage(data, "Activity ended successfully.");
}

async function exportScores() {
  const data = await postRequest("/instructor/export-scores", {
    ...inst(),
    course_id: courseId(),
    activity_no: activityNo()
  });

  if (!data.ok) {
    document.getElementById("scoreOut").textContent = "✖ " + data.message;
    return;
  }

  const rows = data.data || [];
  let text = "✔ Scores exported successfully.\n\n";

  if (rows.length === 0) {
    text += "No score records found for this activity.";
  } else {
    rows.forEach(r => {
      text += `${r.student_email} | Score: ${r.score} | Meta: ${r.meta}\n`;
    });
  }

  document.getElementById("scoreOut").textContent = text;
}

async function leaderboard() {
  const data = await postRequest("/instructor/leaderboard", {
    ...inst(),
    course_id: courseId()
  });

  if (!data.ok) {
    document.getElementById("scoreOut").textContent = "✖ " + data.message;
    return;
  }

  document.getElementById("scoreOut").textContent =
    "✔ Leaderboard loaded successfully.\n\n" +
    JSON.stringify(data.data, null, 2);
}

async function stats() {
  const data = await postRequest("/instructor/activity-stats", {
    ...inst(),
    course_id: courseId(),
    activity_no: activityNo()
  });

  if (!data.ok) {
    document.getElementById("scoreOut").textContent = "✖ " + data.message;
    return;
  }

  document.getElementById("scoreOut").textContent =
    "✔ Activity statistics loaded successfully.\n\n" +
    JSON.stringify(data.data, null, 2);
}