# Created for 0016_0003_curved_partitions.json

""" Summary:
The function `generate_curved_partitions_model` creates an architectural concept model by generating a series of interconnected curvilinear partitions that embody the metaphor of 'curved partitions.' It utilizes controlled randomness to form smooth, undulating curves, simulating the organic movement and fluidity described in the design task. Each partition is created by generating a NURBS curve, offsetting it, and lofting surfaces to define spatial areas. This approach allows for a dynamic interplay between openness and enclosure, enhancing light and shadow effects while inviting exploration. The resulting model captures the essence of tranquility and curiosity as intended by the design metaphor."""

#! python 3
function_code = """def generate_curved_partitions_model(partition_count=6, partition_width=2.0, partition_height=4.0, seed=42):
    \"""
    Generates an architectural Concept Model based on the 'curved partitions' metaphor.

    This function creates a series of curvilinear partitions that define space through fluid and dynamic forms.
    The partitions are designed to suggest division while maintaining continuity and interaction between spaces.
    The design incorporates gentle curves and undulations to evoke a sense of tranquility and curiosity.

    Parameters:
    - partition_count (int): The number of curved partition elements to create.
    - partition_width (float): The width of each partition in meters.
    - partition_height (float): The height of each partition in meters.
    - seed (int): Seed for random number generation to ensure replicability.

    Returns:
    - list: A list of RhinoCommon Brep geometries representing the curved partitions.
    \"""
    import Rhino.Geometry as rg
    import random

    # Set the random seed for replicability
    random.seed(seed)

    # List to store the resulting Breps
    partitions = []

    # Create base curves with controlled randomness for shape variation
    for i in range(partition_count):
        # Generate control points for a smooth, undulating curve
        control_points = []
        for j in range(7):  # 7 control points for more complex curves
            x = j * partition_width / 6.0  # Evenly spaced along the width
            y = random.uniform(-0.5, 0.5) * partition_width  # Random y displacement
            z = random.uniform(0, 0.5) * partition_height  # Random z displacement
            control_points.append(rg.Point3d(x, y, z))
        
        # Create a nurbs curve from the control points
        nurbs_curve = rg.NurbsCurve.Create(False, 3, control_points)
        
        # Offset the curve to create a partition volume
        offset_curve = nurbs_curve.Offset(rg.Plane.WorldZX, partition_width, 0.01, rg.CurveOffsetCornerStyle.Sharp)[0]
        
        # Create a lofted surface between the original and offset curves
        loft_surfaces = rg.Brep.CreateFromLoft([nurbs_curve, offset_curve], rg.Point3d.Unset, rg.Point3d.Unset, rg.LoftType.Normal, False)
        
        if loft_surfaces:
            # Cap the lofted surface to form a closed Brep
            brep = loft_surfaces[0].CapPlanarHoles(0.01)
            if brep:
                # Move each partition slightly along the y-axis for spatial arrangement
                translation_vector = rg.Vector3d(0, i * (partition_width * 1.5), 0)
                brep.Transform(rg.Transform.Translation(translation_vector))
                partitions.append(brep)

    return partitions"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = generate_curved_partitions_model(partition_count=8, partition_width=3.0, partition_height=5.0, seed=123)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = generate_curved_partitions_model(partition_count=10, partition_width=1.5, partition_height=3.0, seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = generate_curved_partitions_model(partition_count=5, partition_width=2.5, partition_height=6.0, seed=56)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = generate_curved_partitions_model(partition_count=7, partition_width=4.0, partition_height=2.5, seed=77)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = generate_curved_partitions_model(partition_count=12, partition_width=2.5, partition_height=4.5, seed=34)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
