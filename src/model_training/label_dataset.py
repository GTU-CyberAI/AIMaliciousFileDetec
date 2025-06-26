import pandas as pd

def define_malware_label(row):
    score = 0
    if row.get("SectionMaxEntropy", 0) > 7.0: score += 1
    if row.get("SectionMaxRawsize", 0) > 1000000 or row.get("SectionMinRawsize", 0) == 0: score += 1
    if row.get("ImageBase", 0) > 4294967296: score += 1
    if row.get("AddressOfEntryPoint", 0) < 2000 or row.get("AddressOfEntryPoint", 0) > 5000000: score += 1
    if row.get("SizeOfStackReserve", 0) > 2000000 or row.get("SizeOfHeapReserve", 0) > 2000000: score += 1
    if row.get("SizeOfUninitializedData", 0) > 100000: score += 1
    if row.get("SectionMaxChar", 0) > 1000000: score += 1
    if row.get("DllCharacteristics", 1) == 0: score += 1
    if row.get("SuspiciousImportFunctions", 0) > 10: score += 1
    if row.get("SuspiciousNameSection", 0) > 0: score += 1
    return 1 if score >= 4 else 0

df = pd.read_csv("dataset_malwares.csv")
df["Malware"] = df.apply(define_malware_label, axis=1)
df.to_csv("labeled_dataset.csv", index=False)
print("Malware labels created and saved to labeled_dataset.csv")
