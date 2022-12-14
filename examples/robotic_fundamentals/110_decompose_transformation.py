"""Example: Decompose transformations
"""
import compas.geometry as cg

scale_factors = [0.1, 0.3, 0.4]
A = cg.Scale.from_factors(scale_factors)  # create Scale
axis, angle = [-0.8, 0.35, 0.5], 2.2
B = cg.Rotation.from_axis_and_angle(axis, angle)  # create Rotation
translation = [1, 2, 3]
C = cg.Translation.from_vector(translation)  # create Translation

# Concatenate transformations
M = C * B * A

# A matrix can also be decomposed into its components of Scale,
# Shear, Rotation, Translation and Perspective
Sc, Sh, R, T, P = M.decomposed()
# Check, must be all `True`
print(A == Sc)
print(B == R)
print(C == T)
print(P * T * R * Sh * Sc == M)
