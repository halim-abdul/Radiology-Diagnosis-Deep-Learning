# Data ingestion and leakage controls

Use a UTF-8 CSV with columns `patient_id,study_id,image_path,label`. Assign entire patients to exactly one of train, validation, or test using `radiology.data.split.grouped_split`; verify with `assert_patient_disjoint`. Only use de-identified, licensed medical data under appropriate study oversight.

- PNG/JPEG: `radiology.data.xray.XrayDataset` loads 2D RGB tensors.
- DICOM: `dicom_to_array` demonstrates basic rescaling/windowing but does **not** de-identify records and is not a complete clinical normalization pipeline.
- NIfTI: `read_nifti` returns the 3D voxel grid and affine. Verify orientation, spacing and modality-specific normalization.

Synthetic toy examples are created directly in the Jupyter plotting cells. No medical images are bundled or downloadable through this repository.
