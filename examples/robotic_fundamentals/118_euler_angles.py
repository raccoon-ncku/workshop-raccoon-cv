"""Example: cg.Rotations from euler angles, rotate an object based on 3 euler angles.
"""
import compas.geometry as cg


# euler angles
alpha, beta, gamma = -0.156, -0.274, 0.785
static, axes = True, 'xyz'

# Version 1: Create Rotation from angles
R1 = cg.Rotation.from_euler_angles([alpha, beta, gamma], static, axes)

# Version 2: Concatenate 3 Rotations
xaxis, yaxis, zaxis = [1, 0, 0], [0, 1, 0], [0, 0, 1]
Rx = cg.Rotation.from_axis_and_angle(xaxis, alpha)
Ry = cg.Rotation.from_axis_and_angle(yaxis, beta)
Rz = cg.Rotation.from_axis_and_angle(zaxis, gamma)

if static:  # check difference between pre- and post-concatenation!
    R2 = Rz * Ry * Rx
else:
    R2 = Rx * Ry * Rz

# Check
print(R1 == R2)
