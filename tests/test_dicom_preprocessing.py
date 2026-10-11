import numpy as np
from radiology.data.volumes import robust_normalize

def test_normalize_constant():
    assert np.allclose(robust_normalize(np.ones((3,3,3))),0)

def test_normalize_range():
    x=robust_normalize(np.arange(100))
    assert x.min()>=0 and x.max()<=1
