// Highlight active navigation link based on current page
document.addEventListener("DOMContentLoaded", function () {
  const current = window.location.pathname.split("/").pop();
  const navLinks = document.querySelectorAll(".nav-link");

  navLinks.forEach(link => {
    if (link.getAttribute("href") === current) {
      link.classList.add("active", "fw-bold", "text-primary");
    }
  });
});

// Optional: Toast/alert function (e.g., success message after action)
function showAlert(message, type = "success") {
  const alertBox = document.createElement("div");
  alertBox.className = `alert alert-${type} alert-dismissible fade show position-fixed top-0 start-50 translate-middle-x mt-3`;
  alertBox.style.zIndex = 1055;
  alertBox.innerHTML = `
    ${message}
    <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
  `;
  document.body.appendChild(alertBox);

  setTimeout(() => {
    alertBox.classList.remove("show");
    alertBox.classList.add("hide");
    setTimeout(() => alertBox.remove(), 300);
  }, 3000);
}

// Example usage:
// showAlert("Blog added successfully!");

// Basic client-side validation (if needed)
function validatePhoneNumber(number) {
  return /^[0-9]{10}$/.test(number);
}

// Example usage:
// if (!validatePhoneNumber(input.value)) showAlert("Invalid phone number", "danger");

// Confirm before delete
function confirmDelete(action) {
  if (confirm("Are you sure you want to delete this item?")) {
    action();
  }
}


