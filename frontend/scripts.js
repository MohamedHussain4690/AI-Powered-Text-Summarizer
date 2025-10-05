const summarizeBtn = document.getElementById("summarizeBtn");
const inputText = document.getElementById("inputText");
const summaryText = document.getElementById("summaryText");

summarizeBtn.addEventListener("click", async () => {
  const text = inputText.value.trim();
  if (!text) {
    summaryText.textContent = "⚠️ Please enter some text first.";
    return;
  }

  summaryText.textContent = "⏳ Summarizing... please wait.";

  try {
    const response = await fetch("http://127.0.0.1:5000/summarize", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ text })
    });

    if (!response.ok) {
      summaryText.textContent = `❌ Error: ${response.statusText}`;
      return;
    }

    const data = await response.json();
    summaryText.textContent = data.summary || "⚠️ No summary received.";
  } catch (error) {
    summaryText.textContent = `❌ Failed to connect to backend: ${error}`;
  }
});
