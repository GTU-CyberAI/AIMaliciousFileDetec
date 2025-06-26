import sys
import os
import json
from detection import predict

def analyze(file_path):
    result, confidence = predict(file_path)
    if result == "Malicious":
        result = {
            "malicious": True,
            "reason": "Malware detected",
            "confidence": confidence
        }
    elif result == "Benign":
        result = {
            "malicious": False,
            "details": "The file is benign."
        }
    else:
        result = {
            "malicious": True,
            "reason": "Unknown detection result",
            "details": f"Detection result: {result}"
        }

    
    print(json.dumps(result))

if __name__ == "__main__":
    file_path = sys.argv[1]
    analyze(file_path)
