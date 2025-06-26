import pefile
import pandas as pd
import joblib

def extract_features_from_exe(file_path):
    try:
        pe = pefile.PE(file_path)
        features = {
            "e_magic": pe.DOS_HEADER.e_magic,
            "e_cblp": pe.DOS_HEADER.e_cblp,
            "e_cp": pe.DOS_HEADER.e_cp,
            "e_lfanew": pe.DOS_HEADER.e_lfanew,
            "NumberOfSections": pe.FILE_HEADER.NumberOfSections,
            "SizeOfOptionalHeader": pe.FILE_HEADER.SizeOfOptionalHeader,
            "Characteristics": pe.FILE_HEADER.Characteristics,
            "Magic": pe.OPTIONAL_HEADER.Magic,
            "MajorLinkerVersion": pe.OPTIONAL_HEADER.MajorLinkerVersion,
            "MinorLinkerVersion": pe.OPTIONAL_HEADER.MinorLinkerVersion,
            "SizeOfCode": pe.OPTIONAL_HEADER.SizeOfCode,
            "SizeOfUninitializedData": pe.OPTIONAL_HEADER.SizeOfUninitializedData,
            "AddressOfEntryPoint": pe.OPTIONAL_HEADER.AddressOfEntryPoint,
            "ImageBase": pe.OPTIONAL_HEADER.ImageBase,
            "Subsystem": pe.OPTIONAL_HEADER.Subsystem,
            "DllCharacteristics": pe.OPTIONAL_HEADER.DllCharacteristics,
            "SizeOfStackReserve": pe.OPTIONAL_HEADER.SizeOfStackReserve,
            "SizeOfHeapReserve": pe.OPTIONAL_HEADER.SizeOfHeapReserve,
            "SectionMaxEntropy": 0,
            "SectionMaxRawsize": 0,
            "SectionMinRawsize": 0,
            "SectionMaxChar": 0,
            "SuspiciousImportFunctions": 0,
            "SuspiciousNameSection": 0
        }
        if hasattr(pe, "sections"):
            entropies = [s.get_entropy() for s in pe.sections]
            raw_sizes = [s.SizeOfRawData for s in pe.sections]
            characteristics = [s.Characteristics for s in pe.sections]
            names = [s.Name.decode(errors="ignore").strip() for s in pe.sections]
            features["SectionMaxEntropy"] = max(entropies) if entropies else 0
            features["SectionMaxRawsize"] = max(raw_sizes) if raw_sizes else 0
            features["SectionMinRawsize"] = min(raw_sizes) if raw_sizes else 0
            features["SectionMaxChar"] = max(characteristics) if characteristics else 0
            features["SuspiciousNameSection"] = sum([".textbss" in n or "UPX" in n for n in names])
        return pd.DataFrame([features])
    except Exception as e:
        print(f"Feature extraction failed: {e}")
        return None

def predict(file_path):
    model = joblib.load("../models/exe_malware_model.pkl")
    feature_names = joblib.load("../models/feature_names.pkl")

    features = extract_features_from_exe(file_path)
    if features is not None:
        features = features.reindex(columns=feature_names, fill_value=0)
        prediction = model.predict(features)[0]
        confidence = model.predict_proba(features)[0][prediction]
        result = "Malicious" if prediction == 1 else "Benign"
        #print(f"Prediction: {result} (Confidence: {confidence*100:.2f}%)")
        return result, confidence*100
    else:
        #print("Could not extract features.")
        return None, None


