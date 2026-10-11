"""Manifest utilities. Columns: patient_id, study_id, image_path, label, split (optional)."""
from pathlib import Path
import pandas as pd

REQUIRED = ("patient_id", "study_id", "image_path", "label")

def read_manifest(path: str | Path, verify_paths: bool = False) -> pd.DataFrame:
    frame = pd.read_csv(path, dtype={"patient_id": str, "study_id": str, "image_path": str})
    missing = set(REQUIRED) - set(frame.columns)
    if missing:
        raise ValueError(f"Missing manifest columns: {sorted(missing)}")
    if frame[list(REQUIRED)].isna().any().any():
        raise ValueError("Required manifest fields contain nulls")
    if frame.duplicated(subset=["study_id", "image_path"]).any():
        raise ValueError("Duplicate study/image rows")
    if verify_paths:
        absent = [p for p in frame.image_path if not Path(p).is_file()]
        if absent:
            raise FileNotFoundError(f"{len(absent)} images are unavailable; first: {absent[0]}")
    return frame

def assert_patient_disjoint(frame: pd.DataFrame, split_col: str = "split") -> None:
    if split_col not in frame:
        raise ValueError(f"Missing {split_col!r} column")
    groups = frame.groupby("patient_id")[split_col].nunique()
    if (groups > 1).any():
        raise ValueError(f"Patient leakage detected for {(groups > 1).sum()} patients")
