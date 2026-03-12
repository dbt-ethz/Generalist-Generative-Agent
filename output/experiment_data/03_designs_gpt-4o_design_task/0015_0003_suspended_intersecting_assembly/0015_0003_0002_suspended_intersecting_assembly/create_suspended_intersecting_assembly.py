# Created for 0015_0003_suspended_intersecting_assembly.json

""" Summary:
The function `create_suspended_intersecting_assembly` generates an architectural concept model inspired by the metaphor "Suspended intersecting assembly." By employing a random seed for replicability, it creates a series of curved rods that mimic elevated, floating elements. Each rod is constructed between randomly determined start and end points, forming dynamic curves that represent fluid spatial connections. The rods' arrangement emphasizes lightness and transparency, echoing the metaphor's essence through their intersecting arcs. The resulting geometries highlight adaptability and movement, creating a visually engaging model that captures the interplay of architectural components while embodying structural elegance."""

#! python 3
function_code = """def create_suspended_intersecting_assembly(seed: int = 42, num_rods: int = 10, rod_length: float = 5.0, rod_radius: float = 0.1) -> list:
    \"""
    Creates an architectural Concept Model based on the metaphor 'Suspended intersecting assembly'.
    
    The model consists of curved rods representing floating and intersecting elements, arranged to create a network of overlapping arcs and lines.
    The design emphasizes lightness, fluidity, and a dynamic interplay between components.

    Args:
        seed (int): Seed for random number generator to ensure replicable results.
        num_rods (int): Number of rods to generate.
        rod_length (float): Length of each rod in meters.
        rod_radius (float): Radius of each rod in meters.

    Returns:
        list: A list of RhinoCommon Brep objects representing the 3D geometries of the concept model.
    \"""
    import Rhino.Geometry as rg
    import random

    random.seed(seed)
    geometries = []

    # Define a central point around which the rods will be suspended
    center_point = rg.Point3d(0, 0, 0)

    for _ in range(num_rods):
        # Randomly define the start and end points for each rod
        start_point = rg.Point3d(
            random.uniform(-rod_length, rod_length),
            random.uniform(-rod_length, rod_length),
            random.uniform(-rod_length, rod_length)
        )
        end_point = rg.Point3d(
            random.uniform(-rod_length, rod_length),
            random.uniform(-rod_length, rod_length),
            random.uniform(-rod_length, rod_length)
        )

        # Create a curve between the start and end points
        curve = rg.Curve.CreateInterpolatedCurve([start_point, center_point, end_point], 3)

        # Generate a cylindrical rod around the curve
        rod = rg.Brep.CreatePipe(curve, rod_radius, True, rg.PipeCapMode.Flat, True, 0.01, 0.01)[0]

        # Add the rod to the list of geometries
        geometries.append(rod)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_suspended_intersecting_assembly(seed=123, num_rods=15, rod_length=6.0, rod_radius=0.2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_suspended_intersecting_assembly(seed=10, num_rods=5, rod_length=4.0, rod_radius=0.15)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_suspended_intersecting_assembly(seed=99, num_rods=8, rod_length=7.0, rod_radius=0.05)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_suspended_intersecting_assembly(seed=200, num_rods=12, rod_length=8.0, rod_radius=0.1)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_suspended_intersecting_assembly(seed=50, num_rods=20, rod_length=10.0, rod_radius=0.3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
