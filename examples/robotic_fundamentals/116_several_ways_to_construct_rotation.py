"""There are several ways to construct a `cg.Rotation`.
"""
import math
import compas.geometry as cg

R = cg.Rotation.from_axis_and_angle([1, 0, 0], math.radians(30))
R = cg.Rotation.from_axis_and_angle([1, 0, 0], math.radians(30), point=[1, 0, 0])
R = cg.Rotation.from_basis_vectors([0.68, 0.68, 0.27], [-0.67, 0.73, -0.15])
R = cg.Rotation.from_frame(cg.Frame([1, 1, 1], [0.68, 0.68, 0.27], [-0.67, 0.73, -0.15]))
R = cg.Rotation.from_axis_angle_vector([-0.043, -0.254, 0.617])
R = cg.Rotation.from_quaternion([0.945, -0.021, -0.125, 0.303])
R = cg.Rotation.from_euler_angles([1.4, 0.5, 2.3], static=True, axes='xyz')

print(R)
