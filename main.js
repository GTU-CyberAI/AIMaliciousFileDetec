const { app, BrowserWindow, ipcMain } = require('electron');
const path = require('path');
const { spawn } = require('child_process');

function createWindow() {
  const win = new BrowserWindow({
    width: 800,
    height: 600,
    webPreferences: {
      nodeIntegration: true,
      contextIsolation: false
    }
  });

  win.loadFile('src/frontend/index.html');
}

app.whenReady().then(createWindow);

ipcMain.handle('analyze-file', async (event, filePath) => {
  return new Promise((resolve, reject) => {
    const pythonProcess = spawn('python', ['src/backend/analyze.py', filePath]);

    let result = '';
    let error = '';

    pythonProcess.stdout.on('data', (data) => {
      result += data.toString();
    });

    pythonProcess.stderr.on('data', (data) => {
      error += data.toString();
    });

    pythonProcess.on('close', () => {
      if (error) reject(error);
      else resolve(result);
    });
  });
});
