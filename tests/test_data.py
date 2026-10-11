import pandas as pd
import pytest
from radiology.data.split import grouped_split
from radiology.data.manifest import assert_patient_disjoint

def test_split_is_patient_disjoint():
    frame=pd.DataFrame({"patient_id":[str(x//2) for x in range(40)],"study_id":[str(x) for x in range(40)]})
    output=grouped_split(frame,seed=7)
    assert_patient_disjoint(output)
    assert output.split.tolist()==grouped_split(frame,seed=7).split.tolist()

def test_leakage_guard():
    frame=pd.DataFrame({"patient_id":["same","same"],"split":["train","test"]})
    with pytest.raises(ValueError):
        assert_patient_disjoint(frame)
