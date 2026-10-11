"""Evidence-grounding checks for observations in structured report drafts."""
def validate_observation_refs(observations,allowed_evidence):
    allowed=set(allowed_evidence)
    invalid=[obs for obs in observations if not set(obs.get("evidence_ids",[])).issubset(allowed)]
    if invalid: raise ValueError("Unknown evidence reference(s) in observation")
    return True
