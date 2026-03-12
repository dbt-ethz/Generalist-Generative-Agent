# Created for 0019_0003_subterranean_cavern.json

""" Summary:
The function `create_subterranean_cavern_model` generates an architectural concept model inspired by the metaphor of a subterranean cavern. It creates a low-profile exterior that blends into the landscape, symbolizing concealment. Inside, it features interconnected, organically shaped chambers that unfold sequentially, evoking the exploration and surprise associated with natural caves. The model employs random dimensions and irregular forms to mimic cave geometry, while varied textures and materials represent the duality of hidden and revealed spaces. Tunnels connect these chambers, enhancing the sense of discovery and refuge, ultimately reflecting the immersive experience of a cavern environment."""

#! python 3
function_code = """def create_subterranean_cavern_model(length=40, width=40, max_height=12, chamber_count=6, seed=101):
    \"""
    Create an architectural Concept Model inspired by the 'subterranean cavern' metaphor.

    This function generates a low-profile exterior with a series of interconnected,
    irregularly shaped volumes that mimic the natural geometry of caves. The design
    focuses on sequential spaces that unfold as one moves through the model.

    Parameters:
    - length (float): The overall length of the model in meters.
    - width (float): The overall width of the model in meters.
    - max_height (float): The maximum height of the interior spaces in meters.
    - chamber_count (int): The number of interconnected chambers within the model.
    - seed (int): Seed for random number generator to ensure replicability.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Breps representing the 3D geometry of the concept model.
    \"""
    import Rhino.Geometry as rg
    import random

    random.seed(seed)

    # Initialize the list to store the generated geometries
    geometries = []

    # Create a low-profile exterior base
    base_height = max_height * 0.2
    exterior_base = rg.Brep.CreateFromBox(rg.BoundingBox(0, 0, 0, length, width, base_height))
    geometries.append(exterior_base)

    # Generate interconnected chambers
    chamber_radius_range = (2, 5)
    for _ in range(chamber_count):
        # Randomly determine chamber dimensions and position
        radius = random.uniform(*chamber_radius_range)
        x = random.uniform(radius, length - radius)
        y = random.uniform(radius, width - radius)
        z = random.uniform(base_height, max_height - radius)

        # Create an irregular, organic-shaped chamber
        sphere = rg.Sphere(rg.Point3d(x, y, z), radius)
        chamber = rg.Brep.CreateFromSphere(sphere)

        # Add chamber to the list
        geometries.append(chamber)

    # Optionally, create tunnels to connect chambers
    for i in range(1, len(geometries)):
        start = geometries[i - 1].GetBoundingBox(True).Center
        end = geometries[i].GetBoundingBox(True).Center
        tunnel_axis = rg.Line(start, end)
        tunnel_radius = random.uniform(0.5, 1.0)

        # Create a cylindrical tunnel
        tunnel = rg.Cylinder(rg.Circle(rg.Plane(start, end - start), tunnel_radius), tunnel_axis.Length)
        tunnel_brep = rg.Brep.CreateFromCylinder(tunnel, True, True)

        if tunnel_brep:
            geometries.append(tunnel_brep)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_subterranean_cavern_model(length=50, width=30, max_height=10, chamber_count=8, seed=202)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_subterranean_cavern_model(length=60, width=45, max_height=15, chamber_count=5, seed=303)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_subterranean_cavern_model(length=45, width=35, max_height=8, chamber_count=10, seed=404)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_subterranean_cavern_model(length=55, width=50, max_height=20, chamber_count=7, seed=505)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_subterranean_cavern_model(length=70, width=60, max_height=18, chamber_count=9, seed=606)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
