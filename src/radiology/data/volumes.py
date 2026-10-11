"""Load volumetric MRI/CT NIfTI; keep affine for world-coordinate work."""
import numpy as np

def read_nifti(path):
    import nibabel as nib
    img = nib.load(str(path))
    volume = np.asarray(img.get_fdata(dtype=np.float32))
    if volume.ndim != 3:
        raise ValueError(f"Expected a 3-D volume, got {volume.shape}")
    return volume, img.affine.copy()

def robust_normalize(volume, lower=1, upper=99):
    v = np.asarray(volume, dtype=np.float32)
    lo, hi = np.percentile(v[np.isfinite(v)], [lower, upper])
    if hi <= lo:
        return np.zeros_like(v)
    return np.clip((v - lo) / (hi - lo), 0, 1)
