const form = document.querySelector("form");

form.addEventListener("submit", (e) => {
  e.preventDefault();

  const username = form.username.value;
  const password = form.password.value;
  const admin_url = "/admin";

  if (authentication(username, password)) {
    window.location.href = admin_url;
  }
});

function authentication(username, password) {
  if (username === "admin" && password === "password") {
    return true;
  } else {
    return false;
  }
}
