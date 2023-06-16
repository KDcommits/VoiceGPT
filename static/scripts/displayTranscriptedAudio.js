function displayTranscript() {
    fetch('/display', {
      method: 'POST',
      body: JSON.stringify(),
      headers: {
        'Content-Type': 'application/json'
      }
    })
    .then(response => response.json())
    .then(data => {
    document.getElementById("output-text").textContent = data;
    });
  }