document.getElementById("uploadForm").addEventListener("submit", function(e) {
  e.preventDefault();
  const file = e.target.elements.file.files[0];
  const formData = new FormData();
  formData.append("file", file);

  fetch("http://<your-server>:5000/upload", {
    method: "POST",
    body: formData
  }).then(response => response.json()).then(data => {
    alert("Prediction: " + data.prediction);
  });
});

