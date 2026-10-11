"""Patient-grouped deterministic train/validation/test split."""
import numpy as np
import pandas as pd
from .manifest import assert_patient_disjoint

def grouped_split(frame: pd.DataFrame, seed: int = 42, val: float = 0.15, test: float = 0.15) -> pd.DataFrame:
    if val < 0 or test < 0 or val + test >= 1:
        raise ValueError("Require 0 <= val,test and val+test < 1")
    if frame.patient_id.isna().any():
        raise ValueError("Patient IDs cannot be missing")
    ids = frame.patient_id.astype(str).unique().copy()
    rng = np.random.default_rng(seed)
    rng.shuffle(ids)
    n = len(ids)
    n_test, n_val = round(n * test), round(n * val)
    assignments = {patient: ("test" if i < n_test else "val" if i < n_test + n_val else "train")
                   for i, patient in enumerate(ids)}
    result = frame.copy()
    result["split"] = result.patient_id.astype(str).map(assignments)
    assert_patient_disjoint(result)
    return result
