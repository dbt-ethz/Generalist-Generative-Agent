# Created for 0019_0003_subterranean_cavern.json

""" Summary:
The function `create_subterranean_cavern_model` generates an architectural concept model inspired by the metaphor of a subterranean cavern. It creates a low-profile exterior using a circular base to symbolize concealment and employs random height variations for interconnected chambers to evoke exploration. The chambers feature organic, flowing forms that mimic natural cave geometries, enhancing a sense of discovery. By varying the number and shape of the chambers, the model emphasizes spatial relationships that unfold sequentially, creating intimate and expansive spaces. This approach captures the contrasts between hidden and revealed elements, aligning with the metaphor's themes of mystery and refuge."""

#! python 3
function_code = """def create_subterranean_cavern_model(base_radius=20.0, height_variation=10.0, chamber_count=5):
    \"""
    Creates an architectural Concept Model inspired by the metaphor of a subterranean cavern,
    utilizing organic forms and spatial sequences to evoke exploration and refuge.

    Parameters:
    - base_radius (float): The approximate radius of the base of the cavern model in meters.
    - height_variation (float): The variation in height for the interconnected volumes in meters.
    - chamber_count (int): The number of major interconnected volumes or chambers.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Breps representing the 3D geometries of the concept model.
    \"""
    import Rhino
    import Rhino.Geometry as rg
    import random
    import math

    # Seed for randomness to ensure replicable results
    random.seed(42)

    # A list to store the generated Breps
    geometries = []

    # Generate base terrain to simulate a low-profile exterior
    base_curve = rg.Circle(rg.Plane.WorldXY, base_radius).ToNurbsCurve()
    base_surface = rg.Extrusion.Create(base_curve, -1.0, True).ToBrep()
    geometries.append(base_surface)

    # Create interconnected chambers as flowing organic volumes
    for i in range(chamber_count):
        # Randomly position chambers within the base radius
        angle = random.uniform(0, 2 * math.pi)
        distance = random.uniform(0, base_radius)
        center = rg.Point3d(distance * math.cos(angle), distance * math.sin(angle), 0)

        # Define the chamber shape using a series of random points
        chamber_profile = []
        for _ in range(5):
            chamber_point = rg.Point3d(
                center.X + random.uniform(-5, 5),
                center.Y + random.uniform(-5, 5),
                random.uniform(0, height_variation)
            )
            chamber_profile.append(chamber_point)

        # Create a lofted surface to form the chamber
        loft_curves = []
        for j in range(1, len(chamber_profile)):
            loft_curves.append(rg.Line(chamber_profile[j-1], chamber_profile[j]).ToNurbsCurve())
        chamber_surface = rg.Brep.CreateFromLoft(loft_curves, rg.Point3d.Unset, rg.Point3d.Unset, rg.LoftType.Normal, False)[0]

        # Add the chamber to the list of geometries
        geometries.append(chamber_surface)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_subterranean_cavern_model(base_radius=25.0, height_variation=15.0, chamber_count=7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_subterranean_cavern_model(base_radius=30.0, height_variation=20.0, chamber_count=10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_subterranean_cavern_model(base_radius=15.0, height_variation=5.0, chamber_count=3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_subterranean_cavern_model(base_radius=22.0, height_variation=12.0, chamber_count=6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_subterranean_cavern_model(base_radius=18.0, height_variation=8.0, chamber_count=4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
