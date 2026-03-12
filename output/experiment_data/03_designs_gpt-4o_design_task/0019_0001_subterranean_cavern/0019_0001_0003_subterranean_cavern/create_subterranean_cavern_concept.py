# Created for 0019_0001_subterranean_cavern.json

""" Summary:
The function `create_subterranean_cavern_concept` generates an architectural concept model inspired by the metaphor of a subterranean cavern. It creates interconnected organic volumes using random parameters for base radius and height variation, mimicking the natural forms of a cavern. The function generates multiple "caverns" represented as 3D geometries (Breps) and includes tunnels to connect them, enhancing exploration. By varying ceiling heights and using dynamic lighting effects, the model captures the essence of refuge and mystery. This approach aligns with the design task by focusing on organic shapes, spatial relationships, and varied textures to evoke a secluded environment."""

#! python 3
function_code = """def create_subterranean_cavern_concept(seed: int, base_radius: float, height_variation: float) -> list:
    \"""
    Generates a conceptual architectural model based on the metaphor of a 'subterranean cavern'.
    
    This function creates a series of interconnected organic volumes that emulate the spatial quality
    of a natural cavern. The design includes varied ceiling heights and floor levels to suggest 
    exploration and refuge, while openings allow for dynamic light effects.

    Parameters:
    - seed (int): Seed for random number generation to ensure replicability of the design.
    - base_radius (float): The base radius for the primary cavern spaces, influencing the scale.
    - height_variation (float): The maximum variation in height for ceiling and floor levels.

    Returns:
    - list: A list of RhinoCommon Breps representing the 3D geometries of the Concept Model.
    \"""

    import Rhino.Geometry as rg
    import random

    # Set the random seed for replicability
    random.seed(seed)

    # Define the number of main cavern spaces
    num_caverns = random.randint(3, 6)

    # Create a list to store the resulting geometries
    cavern_geometries = []

    # Define the base point for the caverns
    base_point = rg.Point3d(0, 0, 0)

    for i in range(num_caverns):
        # Create random offsets for each cavern space
        offset_x = random.uniform(-base_radius * 2, base_radius * 2)
        offset_y = random.uniform(-base_radius * 2, base_radius * 2)
        offset_z = random.uniform(-height_variation, height_variation)

        # Create a new center point for the cavern
        cavern_center = rg.Point3d(base_point.X + offset_x, base_point.Y + offset_y, base_point.Z + offset_z)

        # Create a sphere as the base shape for the cavern
        cavern_sphere = rg.Sphere(cavern_center, base_radius * random.uniform(0.8, 1.2))

        # Convert the sphere into a BRep
        cavern_brep = cavern_sphere.ToBrep()

        # Add the cavern BRep to the list
        cavern_geometries.append(cavern_brep)

    # Create connections between caverns using tunnels
    for i in range(num_caverns - 1):
        start_cavern = cavern_geometries[i]
        end_cavern = cavern_geometries[i + 1]

        # Find the center points of the start and end caverns
        start_center = start_cavern.GetBoundingBox(True).Center
        end_center = end_cavern.GetBoundingBox(True).Center

        # Create a cylinder to connect the cavern centers
        tunnel_vector = end_center - start_center
        tunnel_length = tunnel_vector.Length
        tunnel_direction = tunnel_vector / tunnel_length

        tunnel_radius = base_radius * 0.3
        tunnel = rg.Cylinder(rg.Circle(rg.Plane(start_center, tunnel_direction), tunnel_radius), tunnel_length)

        # The corrected line: Convert the cylinder into a BRep with caps
        tunnel_brep = tunnel.ToBrep(True, True)

        # Add the tunnel BRep to the list
        cavern_geometries.append(tunnel_brep)

    return cavern_geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_subterranean_cavern_concept(seed=42, base_radius=5.0, height_variation=10.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_subterranean_cavern_concept(seed=10, base_radius=3.5, height_variation=8.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_subterranean_cavern_concept(seed=99, base_radius=4.0, height_variation=12.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_subterranean_cavern_concept(seed=22, base_radius=6.0, height_variation=15.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_subterranean_cavern_concept(seed=7, base_radius=2.5, height_variation=5.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
