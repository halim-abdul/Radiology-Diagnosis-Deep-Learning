# Anatomical registration

For CT/MRI comparisons, determine axis orientation, pixel spacing, origin and world convention before rigid/affine transformations. Rigid motion has six degrees of freedom (in 3D), while affine registration also allows scales/shears. Nonlinear deformation requires regularization, inverse-consistency checks and anatomical plausibility. Do not compare masks or calculate physical overlap until they share a reference coordinate system.
