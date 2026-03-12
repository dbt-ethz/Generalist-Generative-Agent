# Created for 0016_0003_curved_partitions.json

""" Summary:
The function `create_curved_partitions_concept_model` generates an architectural concept model based on the metaphor of "curved partitions" by creating a series of undulating, interconnected curvilinear elements. It employs random control points to define smooth, organic curves that reflect the fluidity of natural forms. Each curve is offset to create dynamic partitions, enhancing spatial transitions and light interplay. By varying parameters like curve count, height, and thickness, the model fosters a sense of openness while maintaining intimate zones, ultimately producing an inviting and tranquil environment that encourages exploration, aligning with the design task and metaphor provided."""

#! python 3
function_code = """def create_curved_partitions_concept_model(curve_count=5, partition_height=3.0, partition_thickness=0.1, seed=42):
    \"""
    Creates a Concept Model embodying the metaphor of 'curved partitions' using interconnected curvilinear elements.
    
    Parameters:
    - curve_count (int): The number of curved partitions to generate.
    - partition_height (float): The height of each partition in meters.
    - partition_thickness (float): The thickness of each partition in meters.
    - seed (int): Seed for random number generation to ensure replicability.
    
    Returns:
    - List of Breps: A list of 3D Brep geometries representing the curved partitions.
    \"""
    import Rhino.Geometry as rg
    import random

    # Set the random seed for replicability
    random.seed(seed)

    # List to store the resulting Breps
    breps = []

    # Define a base plane for the partitions
    base_plane = rg.Plane.WorldXY

    # Create curves with random undulations to serve as the base for the partitions
    for i in range(curve_count):
        # Randomly generate control points
        control_points = []
        for j in range(5):  # Use 5 control points for simplicity
            x = random.uniform(-5, 5)  # Random x position within a 10m range
            y = j * 2.0  # Evenly spaced along the y-axis
            z = random.uniform(-1, 1)  # Small z variation for undulation
            control_points.append(rg.Point3d(x, y, z))

        # Create a nurbs curve from the control points
        nurbs_curve = rg.NurbsCurve.Create(False, 3, control_points)

        # Offset the curve to create a partition surface
        offset_curve = nurbs_curve.Offset(base_plane, partition_thickness, 0.01, rg.CurveOffsetCornerStyle.Sharp)[0]

        # Create a surface between the original and offset curves
        loft_surfaces = rg.Brep.CreateFromLoft([nurbs_curve, offset_curve], base_plane.Origin, base_plane.Origin, rg.LoftType.Normal, False)

        if loft_surfaces:
            # Cap the lofted surface to create a Brep
            brep = loft_surfaces[0].CapPlanarHoles(0.01)
            if brep:
                # Move the brep to the correct height
                translation_vector = rg.Vector3d(0, 0, i * (partition_height + 0.1))
                brep.Transform(rg.Transform.Translation(translation_vector))
                breps.append(brep)

    return breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_curved_partitions_concept_model(curve_count=7, partition_height=4.0, partition_thickness=0.2, seed=123)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_curved_partitions_concept_model(curve_count=10, partition_height=2.5, partition_thickness=0.15, seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_curved_partitions_concept_model(curve_count=6, partition_height=3.5, partition_thickness=0.2, seed=56)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_curved_partitions_concept_model(curve_count=8, partition_height=5.0, partition_thickness=0.1, seed=2023)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_curved_partitions_concept_model(curve_count=4, partition_height=3.0, partition_thickness=0.05, seed=30)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
