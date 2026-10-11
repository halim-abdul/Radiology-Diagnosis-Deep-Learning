import pytest
from radiology.reports.templates import create_draft,format_draft
from radiology.reports.grounding import validate_observation_refs

def test_draft_safety():
    report=create_draft("synthetic-1","XR",["Candidate pattern requires validation"])
    assert "NOT GENERATED" in format_draft(report)
    assert report["status"]=="DRAFT_REQUIRES_CLINICIAN_REVIEW"

def test_evidence_refs():
    with pytest.raises(ValueError):
        validate_observation_refs([{"evidence_ids":["unknown"]}],{"known"})
