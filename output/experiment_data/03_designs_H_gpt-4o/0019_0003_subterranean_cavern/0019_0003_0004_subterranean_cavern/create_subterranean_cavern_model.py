# Created for 0019_0003_subterranean_cavern.json

""" Summary:
The function `create_subterranean_cavern_model` generates an architectural concept model by interpreting the metaphor of a subterranean cavern. It creates a low-profile exterior that blends into the landscape, suggesting concealment, while the interior comprises irregular, interconnected chambers representing the cavern's discovery and exploration. The model uses organic forms and varying textures to evoke the natural qualities of caves. It incorporates randomized chamber sizes and positions, with tunnels connecting them, simulating the experience of moving through a cavern. This design balances intimate spaces with expansive volumes, embodying a journey of revelation aligned with the metaphor's essence."""

#! python 3
function_code = """def create_subterranean_cavern_model(length=40, width=40, height=15, num_chambers=4, seed=24):
    \"""
    Create an architectural Concept Model inspired by the 'subterranean cavern' metaphor.

    This function generates a model with a low-profile exterior that blends into the landscape,
    and an interior with complex, interconnected volumes to evoke the feeling of a natural cavern.
    The design emphasizes the interplay between concealment and discovery using organic forms
    and varied textures.

    Parameters:
    - length (float): The total length of the concept model in meters.
    - width (float): The total width of the concept model in meters.
    - height (float): The maximum height of the interior spaces in meters.
    - num_chambers (int): The number of interconnected volumes or chambers to create.
    - seed (int): A seed for the random number generator for reproducibility.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep geometries representing the concept model.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    random.seed(seed)

    # Create the base low-profile exterior
    exterior = rg.Brep.CreateFromBox(rg.BoundingBox(0, 0, 0, length, width, height * 0.1))

    # Initialize a list to hold the chamber geometries
    chambers = []

    # Parameters for chamber positions and sizes
    for _ in range(num_chambers):
        # Randomize chamber dimensions
        radius = random.uniform(5, 8)
        chamber_height = random.uniform(4, 10)

        # Randomize chamber position within the base
        x = random.uniform(radius, length - radius)
        y = random.uniform(radius, width - radius)
        z = random.uniform(height * 0.1, height - chamber_height)

        # Create an organic, irregular chamber shape using a metaball-style approach
        chamber_center = rg.Point3d(x, y, z)
        sphere = rg.Sphere(chamber_center, radius)
        chamber = rg.Brep.CreateFromSphere(sphere)

        # Add chamber to the list
        chambers.append(chamber)

    # Create a boolean union of all chambers to form interconnected volumes
    interior = rg.Brep.CreateBooleanUnion(chambers, 0.01)

    # Create tunnels to connect chambers
    for i in range(len(chambers) - 1):
        start = chambers[i].GetBoundingBox(True).Center
        end = chambers[i + 1].GetBoundingBox(True).Center
        tunnel = rg.Brep.CreateFromCylinder(rg.Cylinder(rg.Circle(start, (start - end).Length * 0.1), start.DistanceTo(end)), True, True)
        if tunnel:
            chambers.append(tunnel)

    # Combine exterior and interior
    if interior:
        model = rg.Brep.CreateBooleanDifference(exterior, interior[0], 0.01)
    else:
        model = [exterior]

    return model if model else [exterior]"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_subterranean_cavern_model(length=50, width=50, height=20, num_chambers=6, seed=42)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_subterranean_cavern_model(length=30, width=30, height=12, num_chambers=5, seed=10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_subterranean_cavern_model(length=60, width=45, height=18, num_chambers=3, seed=7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_subterranean_cavern_model(length=55, width=35, height=25, num_chambers=8, seed=15)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_subterranean_cavern_model(length=45, width=45, height=22, num_chambers=7, seed=30)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
