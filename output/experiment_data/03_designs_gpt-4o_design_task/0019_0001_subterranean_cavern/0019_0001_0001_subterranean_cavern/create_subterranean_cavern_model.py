# Created for 0019_0001_subterranean_cavern.json

""" Summary:
The provided function, `create_subterranean_cavern_model`, generates an architectural concept model inspired by the metaphor of a subterranean cavern. It utilizes parameters such as base radius, height variation, and chamber count to create interconnected, organic shapes that mimic natural formations. By incorporating random positioning and varying heights, the model achieves an undulating, immersive quality reflective of a cavern's spatial dynamics. Additionally, the function constructs tunnels between chambers to enhance exploration and mystery, while varying geometries create intimate spaces and expansive areas. The result is a complex, three-dimensional representation that embodies the essence of refuge and discovery inherent in the cavern metaphor."""

#! python 3
function_code = """def create_subterranean_cavern_model(base_radius=10, height_variation=3, chamber_count=5, randomness_seed=42):
    \"""
    Create an Architectural Concept Model based on the 'subterranean cavern' metaphor. The model emphasizes organic shapes,
    interconnected spaces, and varied spatial qualities to evoke a sense of exploration, mystery, and refuge.

    Parameters:
    - base_radius (float): The initial radius for the subterranean structure. Determines the scale of the cavern.
    - height_variation (float): Maximum variation in height for the cavern's ceiling to create a sense of undulating organic forms.
    - chamber_count (int): Number of interconnected chambers within the model, suggesting a sequence of spaces to explore.
    - randomness_seed (int): Seed for random number generation to ensure replicability of the model's random elements.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of 3D geometries representing the cavernous spaces and solid forms of the concept model.
    \"""
    import Rhino.Geometry as rg
    import random

    random.seed(randomness_seed)
    geometries = []

    # Create base cavern shape using a series of connected spheres
    for i in range(chamber_count):
        # Randomly position the center of each chamber
        x = random.uniform(-base_radius, base_radius)
        y = random.uniform(-base_radius, base_radius)
        # Vary the height of each chamber to create an organic ceiling
        z = random.uniform(-height_variation, height_variation)
        center = rg.Point3d(x, y, z)

        # Determine a radius that varies slightly to create a natural feel
        radius = base_radius * random.uniform(0.8, 1.2)

        # Create a sphere for each chamber
        sphere = rg.Sphere(center, radius)
        geometries.append(sphere.ToBrep())

    # Create tunnels connecting the chambers
    for i in range(chamber_count - 1):
        start = geometries[i].GetBoundingBox(True).Center
        end = geometries[i + 1].GetBoundingBox(True).Center

        # Create a curvilinear path between chamber centers
        points = [start, rg.Point3d((start.X + end.X) / 2, (start.Y + end.Y) / 2, (start.Z + end.Z) / 2 + height_variation * 0.5), end]
        curve = rg.NurbsCurve.Create(False, 3, points)

        # Sweep a small circle along the curve to create a tunnel
        circle = rg.Circle(start, base_radius * 0.2)
        sweep = rg.SweepOneRail()
        # Ensure the curve and circle are not None
        if curve and circle:
            tunnel_breps = sweep.PerformSweep(curve, circle.ToNurbsCurve())
            if tunnel_breps:
                geometries.append(tunnel_breps[0])

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_subterranean_cavern_model(base_radius=15, height_variation=5, chamber_count=7, randomness_seed=123)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_subterranean_cavern_model(base_radius=12, height_variation=4, chamber_count=6, randomness_seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_subterranean_cavern_model(base_radius=8, height_variation=2, chamber_count=4, randomness_seed=56)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_subterranean_cavern_model(base_radius=20, height_variation=6, chamber_count=10, randomness_seed=77)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_subterranean_cavern_model(base_radius=18, height_variation=7, chamber_count=8, randomness_seed=34)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
