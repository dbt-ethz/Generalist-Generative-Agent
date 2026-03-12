# Created for 0019_0005_subterranean_cavern.json

""" Summary:
The function `create_subterranean_cavern_concept` generates an architectural concept model based on the metaphor of a subterranean cavern. It creates interlocking volumes that blend angular and organic forms, reflecting the ruggedness and fluidity of natural caves. By utilizing random dimensions and shapes, the function simulates the labyrinthine quality of cavern spaces. The construction of both organic and angular geometries fosters a dynamic interplay of solid and void, enhancing the immersive experience. Strategic openings and varied thicknesses in the materials create light and shadow effects, capturing the essence of exploration and surprise intrinsic to subterranean environments."""

#! python 3
function_code = """def create_subterranean_cavern_concept(length, width, height, num_volumes, seed=None):
    \"""
    Creates an architectural Concept Model evoking the 'subterranean cavern' metaphor. The model combines angular and organic forms to represent the rugged yet fluid nature of cavern spaces.

    Parameters:
    - length (float): The overall length of the concept model in meters.
    - width (float): The overall width of the concept model in meters.
    - height (float): The overall height of the concept model in meters.
    - num_volumes (int): Number of interlocking volumes to create.
    - seed (int, optional): Seed for random number generator to ensure replicability.

    Returns:
    - List of RhinoCommon Brep objects representing the concept model's geometry.
    \"""
    import Rhino.Geometry as rg
    import random

    if seed is not None:
        random.seed(seed)

    geometries = []
    base_point = rg.Point3d(0, 0, 0)

    # Helper function to create a random organic form
    def create_organic_form(base, max_dim):
        control_points = []
        for _ in range(5):
            x = random.uniform(base.X, base.X + max_dim)
            y = random.uniform(base.Y, base.Y + max_dim)
            z = random.uniform(base.Z, base.Z + max_dim)
            control_points.append(rg.Point3d(x, y, z))
        curve = rg.NurbsCurve.Create(False, 3, control_points)
        axis = rg.Line(base, rg.Point3d(base.X, base.Y, base.Z + 1))
        rev_surface = rg.RevSurface.Create(curve, axis)
        brep = rg.Brep.CreateFromRevSurface(rev_surface, True, True)
        return brep

    # Helper function to create a random angular form
    def create_angular_form(base, max_dim):
        corners = []
        for _ in range(4):
            x = random.uniform(base.X, base.X + max_dim)
            y = random.uniform(base.Y, base.Y + max_dim)
            z = random.uniform(base.Z, base.Z + max_dim)
            corners.append(rg.Point3d(x, y, z))
        corners.append(corners[0])  # Close the loop
        polyline = rg.Polyline(corners)
        return rg.Brep.CreateFromSurface(rg.Surface.CreateExtrusion(polyline.ToNurbsCurve(), rg.Vector3d(0, 0, random.uniform(1, height))))

    # Create interlocking volumes
    for _ in range(num_volumes):
        is_organic = random.choice([True, False])
        max_dim = random.uniform(1, min(length, width) / 4)
        offset_x = random.uniform(0, length - max_dim)
        offset_y = random.uniform(0, width - max_dim)
        offset_z = random.uniform(0, height - max_dim)
        base = rg.Point3d(offset_x, offset_y, offset_z)

        if is_organic:
            geom = create_organic_form(base, max_dim)
        else:
            geom = create_angular_form(base, max_dim)

        if geom is not None:
            geometries.append(geom)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_subterranean_cavern_concept(50.0, 30.0, 20.0, 5, seed=42)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_subterranean_cavern_concept(100.0, 50.0, 30.0, 10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_subterranean_cavern_concept(75.0, 40.0, 25.0, 8, seed=100)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_subterranean_cavern_concept(60.0, 45.0, 35.0, 7, seed=56)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_subterranean_cavern_concept(80.0, 60.0, 40.0, 6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
