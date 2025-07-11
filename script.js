document.addEventListener("DOMContentLoaded", () => {
  const button = document.querySelector("button");
  const container = document.createElement("div");
  document.body.appendChild(container);

  button.addEventListener("click", async () => {
    try {
      const response = await fetch("http://127.0.0.1:5000/recommend");
      const data = await response.json();

      container.innerHTML = `
        <h3>오늘의 루틴</h3>
        <ul>
          ${data.routines.map(item => `<li>${item.time} - ${item.task} (${item.reason})</li>`).join("")}
        </ul>
      `;
    } catch (error) {
      container.innerHTML = `<p style="color:red;">루틴을 불러오지 못했습니다.</p>`;
      console.error("Error:", error);
    }
  });
});
