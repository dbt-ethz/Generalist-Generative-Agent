# Created for 0016_0004_curved_partitions.json

""" Summary:
The function `create_curved_partitions_model` generates an architectural concept model by interpreting the metaphor of 'curved partitions'. It creates a series of interconnected, flowing forms using mathematical curves that reflect organic shapes. The model employs parameters like base radius, height, and curve amplitude to establish the partitions' dimensions and layout, promoting a dynamic spatial relationship. Each partition is crafted from interpolated curves, which are lofted into surfaces, embodying fluidity and soft transitions. This design invites exploration and interaction, enhancing the sensory experience through light and shadow interplay, while fostering a calm, elegant environment aligned with the metaphors essence."""

#! python 3
function_code = """def create_curved_partitions_model(base_radius=10.0, height=5.0, num_partitions=5, curve_amplitude=3.0, seed=42):
    \"""
    Creates a concept model using the metaphor of 'curved partitions', reflecting a dynamic and harmonious flow.
    
    Parameters:
    - base_radius: float, the base radius for the circular arrangement of partitions.
    - height: float, the height of the partitions.
    - num_partitions: int, the number of curved partitions to create.
    - curve_amplitude: float, the amplitude of the curves defining the partitions.
    - seed: int, the seed for random number generation to ensure replicability.
    
    Returns:
    - A list of RhinoCommon Brep objects representing the 3D geometries of the concept model.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    # Set the random seed for reproducibility
    random.seed(seed)

    # Container for the geometries
    geometries = []

    # Create partitions
    for i in range(num_partitions):
        angle = (2 * math.pi / num_partitions) * i
        center_point = rg.Point3d(base_radius * math.cos(angle), base_radius * math.sin(angle), 0)
        
        # Define the curve path for partition
        curve_points = []
        for j in range(5):  # 5 control points for the curve
            x_offset = curve_amplitude * math.sin(j * math.pi / 2) * (random.random() - 0.5)
            y_offset = curve_amplitude * math.cos(j * math.pi / 2) * (random.random() - 0.5)
            z = height * j / 4.0
            curve_points.append(rg.Point3d(center_point.X + x_offset, center_point.Y + y_offset, z))
        
        # Create an interpolated curve
        curve = rg.Curve.CreateInterpolatedCurve(curve_points, 3)

        # Ensure the loft operation has valid input
        if curve:
            # Create a surface by lofting the curve
            loft_surfaces = rg.Brep.CreateFromLoft([curve], rg.Point3d.Unset, rg.Point3d.Unset, rg.LoftType.Normal, False)
            if loft_surfaces and len(loft_surfaces) > 0:
                geometries.append(loft_surfaces[0])

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_curved_partitions_model(base_radius=10.0, height=5.0, num_partitions=8, curve_amplitude=4.0, seed=123)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_curved_partitions_model(base_radius=15.0, height=7.0, num_partitions=6, curve_amplitude=2.5, seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_curved_partitions_model(base_radius=12.0, height=6.0, num_partitions=4, curve_amplitude=5.0, seed=56)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_curved_partitions_model(base_radius=8.0, height=4.0, num_partitions=10, curve_amplitude=3.5, seed=77)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_curved_partitions_model(base_radius=20.0, height=10.0, num_partitions=7, curve_amplitude=6.0, seed=10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
