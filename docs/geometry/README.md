# Geometry for radiology researchers

Distinguish pixel coordinates (row,column), voxel indices (i,j,k), physical coordinates (millimeters), and scanner/patient frames. A 4x4 affine maps voxel positions to world positions; orientation and spacing must be checked before mask overlays, registration, surface distances, or lesion volumes. This module implements affine point transformations and Dice/IoU. Surface distance and deformable registration are research extensions, not silently assumed features.
