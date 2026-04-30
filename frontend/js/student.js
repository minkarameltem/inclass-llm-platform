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

function niceMessage(data, successText) {
  if (data.ok) {
    return "✔ " + successText;
  }
  return "✖ " + data.message;
}

async function login() {
  const data = await postRequest("/student/login", student());

  document.getElementById("loginOut").textContent =
    niceMessage(data, "Student login successful.");

  if (data.ok) {
    const email = document.getElementById("email").value;

    document.getElementById("welcomeBox").innerHTML =
      "👋 Welcome<br><span style='font-size:14px; font-weight:700;'>" + email + "</span>";

    showToast("🚀 Dashboard unlocked!");

    const loginPanel = document.getElementById("loginPanel");
    if (loginPanel) {
      setTimeout(() => {
        loginPanel.style.display = "none";
      }, 700);
    }

    animatePanels();
  }
}

async function getActivity() {
  const data = await postRequest("/student/get-activity", {
    ...student(),
    course_id: courseId(),
    activity_no: activityNo()
  });

  if (!data.ok) {
    document.getElementById("activityOut").textContent = "✖ " + data.message;
    return;
  }

  const activity = data.data || data.activity || data;

  let text = "✔ Activity loaded successfully.\n\n";

  if (activity.activity_text) {
    text += activity.activity_text;
  } else if (activity.data && activity.data.activity_text) {
    text += activity.data.activity_text;
  } else {
    text += "Activity is available.";
  }

  text += "\n\nLearning objectives are hidden from student view.";

  document.getElementById("activityOut").textContent = renderActivityCard(activity);
  document.getElementById("activityOut").classList.add("activity-card");
  showToast("📘 Activity loaded successfully!");
}

async function logScore() {
  const data = await postRequest("/student/log-score", {
    ...student(),
    course_id: courseId(),
    activity_no: activityNo(),
    score: document.getElementById("score").value,
    meta: document.getElementById("meta").value
  });

  document.getElementById("scoreOut").textContent =
    niceMessage(data, "Score submitted successfully.");

  if (data.ok) {
    showToast("🎉 Score submitted successfully!");
  }
}
function fillDemoStudent() {
  document.getElementById("email").value = "erkisie@mef.edu.tr";
  document.getElementById("password").value = "elif123";
  document.getElementById("courseId").value = "COMP302";
  document.getElementById("activityNo").value = "4";
}


function showToast(message) {
  const oldToast = document.querySelector(".toast");
  if (oldToast) oldToast.remove();

  const toast = document.createElement("div");
  toast.className = "toast";
  toast.textContent = message;
  document.body.appendChild(toast);

  setTimeout(() => toast.remove(), 2200);
}

function animatePanels() {
  document.querySelectorAll(".panel").forEach((panel, index) => {
    setTimeout(() => panel.classList.add("fade-in"), index * 120);
  });
}

function renderActivityCard(activity) {
  return `
📘 Course: ${activity.course_id || "COMP302"}
🧩 Activity No: ${activity.activity_no || document.getElementById("activityNo").value}
🟢 Status: ${activity.status || "ACTIVE"}

📝 Activity:
${activity.activity_text || "Activity is available."}

🎯 Learning objectives are hidden from student view.
`;
}
console.log("JS LOADED 🚀");



function resetScoreForm() {
  document.getElementById("score").value = "";
  document.getElementById("meta").value = "";
  document.getElementById("scoreOut").textContent = "Score form cleared.";
}
