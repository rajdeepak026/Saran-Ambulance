document.addEventListener("DOMContentLoaded", function () {
  const fareForm = document.getElementById("fareForm");
  const fareTable = document.querySelector("#fareTable tbody");

  fareForm.addEventListener("submit", function (e) {
    e.preventDefault();
    const pickup = document.getElementById("pickup").value.trim();
    const drop = document.getElementById("drop").value.trim();
    const fare = document.getElementById("fare").value.trim();

    if (pickup && drop && fare) {
      const row = document.createElement("tr");

      row.innerHTML = `
        <td>${pickup}</td>
        <td>${drop}</td>
        <td>₹${fare}</td>
        <td>
          <button class="btn btn-sm btn-primary me-2 edit-btn">✏️ Edit</button>
          <button class="btn btn-sm btn-danger delete-btn">🗑️ Delete</button>
        </td>
      `;

      fareTable.appendChild(row);
      fareForm.reset();
    }
  });

  fareTable.addEventListener("click", function (e) {
    const target = e.target;
    const row = target.closest("tr");

    if (target.classList.contains("delete-btn")) {
      row.remove();
    }

    if (target.classList.contains("edit-btn")) {
      const pickup = row.children[0].innerText;
      const drop = row.children[1].innerText;
      const fare = row.children[2].innerText.replace("₹", "");

      document.getElementById("pickup").value = pickup;
      document.getElementById("drop").value = drop;
      document.getElementById("fare").value = fare;

      row.remove();
    }
  });
});
