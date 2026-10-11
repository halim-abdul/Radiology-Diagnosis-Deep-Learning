"""Guardrails for metadata logging; NOT a complete DICOM anonymizer."""
FORBIDDEN_KEYS={"PatientName","PatientBirthDate","PatientAddress","PatientID","AccessionNumber"}

def safe_metadata(metadata):
    return {key:value for key,value in metadata.items() if key not in FORBIDDEN_KEYS}

def reject_identifying_fields(metadata):
    found=FORBIDDEN_KEYS.intersection(metadata)
    if found:raise ValueError("Potential PHI metadata fields detected")
