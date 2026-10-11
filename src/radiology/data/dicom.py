"""DICOM pixel preprocessing (research only). No identifiers are logged."""
import numpy as np

def dicom_to_array(path, center=None, width=None):
    import pydicom
    ds = pydicom.dcmread(str(path))
    if not hasattr(ds, "PixelData"):
        raise ValueError("DICOM missing PixelData")
    data = ds.pixel_array.astype(np.float32)
    slope = float(getattr(ds, "RescaleSlope", 1.))
    intercept = float(getattr(ds, "RescaleIntercept", 0.))
    data = data * slope + intercept
    if center is not None and width is not None:
        if width <= 0:
            raise ValueError("Window width must be positive")
        low, high = center - width / 2, center + width / 2
        data = np.clip(data, low, high)
    elif str(getattr(ds, "PhotometricInterpretation", "")) == "MONOCHROME1":
        data = np.max(data) + np.min(data) - data
    low, high = float(data.min()), float(data.max())
    return ((data - low) / (high - low + 1e-8)).astype(np.float32)
