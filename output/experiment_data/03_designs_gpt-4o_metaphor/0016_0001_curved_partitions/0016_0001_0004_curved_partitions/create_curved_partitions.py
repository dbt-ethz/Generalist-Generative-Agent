# Created for 0016_0001_curved_partitions.json

""" Summary:
The provided function, `create_curved_partitions`, generates an architectural concept model inspired by the metaphor of "curved partitions." It creates a series of smooth, flowing partitions that embody fluidity and organic movement, enhancing spatial dynamics. By using randomly generated control points to define NURBS curves, the function ensures that each partition is unique, reflecting the metaphor's emphasis on continuity and natural progression. The resulting curved surfaces facilitate intimate spaces within an open area, promoting a calming and elegant environment. This generation process aligns with the metaphor's key traits, fostering exploration and interaction within the designed space."""

#! python 3
function_code = """def create_curved_partitions(length=10.0, width=10.0, height=3.0, num_partitions=3):
    \"""
    Creates a conceptual architectural model based on the metaphor of 'curved partitions'.
    
    This function generates a series of smooth, flowing partitions within a defined space,
    promoting fluidity and dynamic spatial organization. The partitions are represented as
    curved surfaces that offer a sense of natural progression and privacy within an open area.

    Inputs:
    - length: The length of the bounding box defining the area in which partitions are placed (meters).
    - width: The width of the bounding box defining the area in which partitions are placed (meters).
    - height: The height of the partitions (meters).
    - num_partitions: The number of curved partitions to generate.

    Outputs:
    - A list of Brep geometries representing the curved partitions.
    \"""
    import Rhino.Geometry as rg
    import random

    # Seed for randomness to ensure replicability
    random.seed(42)

    # Define the bounding area
    bounding_box = rg.BoundingBox(0, 0, 0, length, width, height)

    # List to store partition geometries
    partitions = []

    # Create partitions
    for _ in range(num_partitions):
        # Randomly generate control points for a NURBS curve within the bounding box
        control_points = [rg.Point3d(random.uniform(0, length), random.uniform(0, width), random.uniform(0, height)) for _ in range(5)]
        
        # Create a NURBS curve
        curve = rg.NurbsCurve.Create(False, 3, control_points)
        
        # Offset the curve to create a surface
        offset_distance = random.uniform(0.2, 0.5)  # Random offset for thickness
        offset_curve = curve.Offset(rg.Plane.WorldXY, offset_distance, 0.01, rg.CurveOffsetCornerStyle.Sharp)
        
        if offset_curve:
            # Loft between the original curve and the offset curve to create a surface
            loft = rg.Brep.CreateFromLoft([curve, offset_curve[0]], rg.Point3d.Unset, rg.Point3d.Unset, rg.LoftType.Normal, False)
            
            if loft:
                partitions.append(loft[0])
    
    return partitions"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_curved_partitions(length=15.0, width=10.0, height=4.0, num_partitions=5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_curved_partitions(length=20.0, width=15.0, height=5.0, num_partitions=4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_curved_partitions(length=12.0, width=8.0, height=3.5, num_partitions=6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_curved_partitions(length=25.0, width=20.0, height=6.0, num_partitions=7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_curved_partitions(length=18.0, width=12.0, height=5.0, num_partitions=2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
