const { ipcRenderer } = require('electron');

const dropZone = document.getElementById('drop-zone');
const uploadBtn = document.getElementById('upload-btn');
const fileInput = document.getElementById('file-input');
const selectedFileText = document.getElementById('selected-file');
const checkBtn = document.getElementById('check-btn');
const resultDiv = document.getElementById('result');

let selectedFilePath = null;

// Drag & Drop
dropZone.addEventListener('dragover', (e) => {
  e.preventDefault();
  dropZone.classList.add('dragover');
});

dropZone.addEventListener('dragleave', () => {
  dropZone.classList.remove('dragover');
});

dropZone.addEventListener('drop', (e) => {
  e.preventDefault();
  dropZone.classList.remove('dragover');

  const file = e.dataTransfer.files[0];
  handleFile(file);
});

// Browse Button
uploadBtn.addEventListener('click', () => {
  fileInput.click();
});

fileInput.addEventListener('change', () => {
  const file = fileInput.files[0];
  handleFile(file);
});

// File Validation & Display
function handleFile(file) {
  if (!file) return;

  selectedFilePath = file.path;
  selectedFileText.textContent = `Selected: ${file.name}`;
  checkBtn.disabled = false;
}

// Run Python Script
checkBtn.addEventListener('click', async () => {
  if (!selectedFilePath) return;

  resultDiv.style.display = 'block';
  resultDiv.innerHTML = 'Analyzing file... Please wait.';
  checkBtn.disabled = true;

  try {
    const analysisResult = await ipcRenderer.invoke('analyze-file', selectedFilePath);
    const data = JSON.parse(analysisResult);

    if (data.malicious) {
      resultDiv.innerHTML = `
        <h3 class="error">🚨 Malicious or Invalid File</h3>
        <p><strong>Reason:</strong> ${data.reason}</p>
        <p>${data.details}</p>
      `;
    } else {
      resultDiv.innerHTML = `
        <h3 class="success">✅ File is Safe</h3>
        <p>${data.details}</p>
      `;
    }
  } catch (err) {
    resultDiv.innerHTML = `<p class="error">Error: ${err}</p>`;
  } finally {
    checkBtn.disabled = false;
  }
});
