# AI Based Malicious File Detection

An advanced Electron application with integrated Python backend designed for comprehensive executable file analysis and malware detection using machine learning algorithms.

## Project Description

This project aims to provide a user-friendly, cross-platform desktop application that leverages machine learning techniques to analyze executable files and detect potential malware threats. The application combines the power of Electron for the frontend interface with Python's robust machine learning capabilities for backend analysis.

### Goals:
- **Real-time Malware Detection**: Instant analysis of executable files with confidence scoring
- **User-Friendly Interface**: Intuitive drag-and-drop functionality for file analysis
- **Machine Learning Integration**: Utilizing trained models for accurate threat detection
- **Cross-Platform Compatibility**: Supporting Windows, macOS, and Linux environments
- **Educational Purpose**: Demonstrating practical application of ML in cybersecurity

## Project Structure

```
├── main.js                 # Main Electron process
├── package.json            # Project dependencies and build configuration
├── src/                    # Source code directory
│   ├── frontend/          # Frontend files (Electron renderer)
│   │   ├── index.html     # Main UI
│   │   ├── renderer.js    # Renderer process logic
│   │   └── style.css      # Application styles
│   ├── backend/           # Python backend
│   │   ├── analyze.py     # Main analysis script
│   │   └── detection.py   # ML model prediction logic
│   ├── models/            # Machine learning models
│   │   ├── exe_malware_model.pkl  # Trained model
│   │   └── feature_names.pkl      # Feature names for model
│   └── model_training/    # Model training scripts
│       ├── detection.py   # Feature extraction for training
│       ├── label_dataset.py # Dataset labeling utilities
│       └── train_model.py # Model training script
├── tests/                 # Test cases
│   ├── unit/              # Unit tests
│   │   ├── test_detection.py    # Backend detection tests
│   │   ├── test_analyze.py      # Analysis workflow tests
│   │   └── test_frontend.py     # Frontend component tests
│   ├── integration/       # Integration tests
│   │   ├── test_full_workflow.py # End-to-end testing
│   │   └── test_performance.py   # Performance benchmarks
│   ├── sample_files/      # Test files for analysis
│   ├── run_tests.py       # Test runner script
│   └── test_config.json   # Test configuration
├── config/                # Configuration files
│   ├── package.json       # Original package configuration
│   └── package-lock.json  # Lock file for dependencies
└── dist/                  # Build output directory
```

## Installation Instructions

### Prerequisites
- **Node.js** (v14.0 or higher) and npm
- **Python** (3.8 or higher)
- **Git** (for cloning the repository)

### Step-by-Step Setup

1. **Clone the Repository**
```bash
git clone https://github.com/GTU-CyberAI/AIMaliciousFileDetec.git
cd malicious_file/src
```

2. **Install Node.js Dependencies**
```bash
npm install
```

3. **Install Python Dependencies**
```bash
pip install pefile pandas joblib scikit-learn numpy
```

4. **Verify Installation**
```bash
# Check Node.js version
node --version

# Check Python version
python --version

# Verify Python packages
python -c "import pefile, pandas, joblib, sklearn; print('All packages installed successfully')"
```

5. **Run the Application**
```bash
npm start
```

### Running the Application

```bash
npm start
```

### Building for Distribution

```bash
npm run build
```

## Running Tests

### Run All Tests
```bash
cd tests
python run_tests.py
```

### Run Specific Test Categories
```bash
# Unit tests only
python -m unittest discover tests/unit -v

# Integration tests only  
python -m unittest discover tests/integration -v

# Specific test file
python -m unittest tests.unit.test_detection -v
```

### Test Requirements
For running tests, install additional dependencies:
```bash
pip install psutil  # For performance monitoring
```

## Usage Examples

### Basic File Analysis

1. **Launch the Application**
   - Run `npm start` from the project directory
   - The application window will open with the main interface

2. **Analyze a File**
   - Drag and drop an executable file (.exe) onto the application window
   - Or use the "Select File" button to browse for a file
   - Wait for the analysis to complete (usually takes 2-5 seconds)

3. **Interpret Results**
   ```json
   // Example output for a benign file
   {
     "malicious": false,
     "details": "The file is benign.",
     "confidence": 95.7
   }
   
   // Example output for a malicious file
   {
     "malicious": true,
     "reason": "Malware detected",
     "confidence": 87.3
   }
   ```

### Sample Test Files
- **Benign**: Standard Windows utilities (e.g., notepad.exe, calc.exe)
- **Suspicious**: Files with unusual characteristics or packed executables

## Features

- **File Analysis**: Drag and drop executable files for analysis
- **Machine Learning Detection**: Uses trained ML model for malware detection
- **Cross-platform**: Built with Electron for Windows, macOS, and Linux
- **Real-time Results**: Instant analysis with confidence scores

## Development

- Frontend: HTML, CSS, JavaScript (Electron renderer)
- Backend: Python with machine learning capabilities
- Model: Scikit-learn based Random Forest Classifier malware detection
- Build: Electron Builder for distribution

##  Acknowledgments
=======
## Acknowledgments

### Course Information
- **Course Name**: CSE473 - Network and Information Security 
- **Institution**: Gebze Technical University
- **Semester**: Spring 2025

### Instructor
- **Professor**: Salih SARP
- **Department**: Computer Science and Engineering

### Project Team
- **Team Member 1**: Tarık CELIK
- **Team Member 2**: Ali CELIK
### Technologies & Libraries Used
- **Frontend**: Electron, HTML5, CSS3, JavaScript
- **Backend**: Python 3.x
- **Machine Learning**: Scikit-learn, Pandas, NumPy
- **File Analysis**: PEfile library
- **Build Tools**: Electron Builder, npm

### References
- PE Format Documentation
- Malware Analysis Techniques
- Machine Learning for Cybersecurity Best Practices

---

## File Organization Benefits

- **Separation of Concerns**: Frontend, backend, and models are clearly separated
- **Configuration Management**: All config files in dedicated folder
- **Model Management**: Centralized model storage prevents duplication
- **Build Optimization**: Excludes training scripts from distribution builds

---

**© 2025 CSE473 Network and Information Security Project - AI Based Malicious File Detection**
