"""Structured non-diagnostic draft; never auto-sign or infer unsupported findings."""
from datetime import datetime, timezone

def create_draft(study_id,modality,observations,uncertainty=None):
    if modality not in {"XR","CT","MR"}: raise ValueError("Unsupported modality")
    if not isinstance(observations,list): raise ValueError("Observations must be a list")
    safe=[str(x).strip() for x in observations if str(x).strip()]
    return {"study_id":str(study_id),"modality":modality,"status":"DRAFT_REQUIRES_CLINICIAN_REVIEW",
            "generated_utc":datetime.now(timezone.utc).isoformat(),
            "observations":safe,"limitations":uncertainty or "Research prototype; not clinically validated.",
            "impression":"NOT GENERATED — clinician must assess source imaging."}

def format_draft(draft):
    return ("RESEARCH DRAFT — NOT A RADIOLOGY REPORT\n"
            f"Study: {draft['study_id']} | Modality: {draft['modality']}\n"
            "Observations (unverified):\n"
            +("\n".join("- "+x for x in draft["observations"]) or "- None supplied")
            +f"\nLimitations: {draft['limitations']}\n{draft['impression']}\n")
