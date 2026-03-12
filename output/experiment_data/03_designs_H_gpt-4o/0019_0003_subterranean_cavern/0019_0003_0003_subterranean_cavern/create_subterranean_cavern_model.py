# Created for 0019_0003_subterranean_cavern.json

""" Summary:
The function `create_subterranean_cavern_model` generates an architectural concept model inspired by the metaphor of a subterranean cavern. It constructs a low-profile exterior to symbolize concealment while creating a complex interior with interconnected chambers that unfold in an organic, flowing manner. Using randomization, the function designs spherical chambers of varying sizes and heights to mimic natural cave formations. The final output combines the exterior and interior geometries, emphasizing the journey of exploration through intimate and expansive spaces. By integrating natural materials and textures, the model captures the immersive experience of navigating a cavernous environment."""

#! python 3
function_code = """def create_subterranean_cavern_model(length=30, width=30, height=10, num_chambers=5, seed=42):
    \"""
    Create an architectural Concept Model inspired by the metaphor of a 'subterranean cavern'.
    
    This function generates a low-profile exterior and a complex interior with interconnected volumes.
    The design features organic, flowing lines and asymmetrical forms to mimic natural cave formations.

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

    random.seed(seed)
    
    # Create the base low-profile exterior
    exterior = rg.Brep.CreateFromBox(rg.BoundingBox(0, 0, 0, length, width, height * 0.2))
    
    # Initialize a list to hold the chamber geometries
    chambers = []
    
    # Parameters for chamber positions and sizes
    chamber_radius_range = (3, 6)
    chamber_height_range = (3, 8)
    
    for _ in range(num_chambers):
        # Randomize chamber dimensions
        radius = random.uniform(*chamber_radius_range)
        chamber_height = random.uniform(*chamber_height_range)
        
        # Randomize chamber position within the base
        x = random.uniform(radius, length - radius)
        y = random.uniform(radius, width - radius)
        z = random.uniform(height * 0.2, height - chamber_height)
        
        # Create a spherical chamber to mimic a cave
        sphere = rg.Sphere(rg.Point3d(x, y, z), radius)
        chamber = rg.Brep.CreateFromSphere(sphere)
        
        # Add chamber to the list
        chambers.append(chamber)
    
    # Create a boolean union of all chambers to form interconnected volumes
    interior = rg.Brep.CreateBooleanUnion(chambers, 0.01)
    
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
    geometry = create_subterranean_cavern_model(length=50, width=40, height=15, num_chambers=10, seed=123)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_subterranean_cavern_model(length=25, width=25, height=12, num_chambers=7, seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_subterranean_cavern_model(length=40, width=35, height=20, num_chambers=8, seed=56)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_subterranean_cavern_model(length=60, width=50, height=18, num_chambers=12, seed=77)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_subterranean_cavern_model(length=45, width=45, height=14, num_chambers=6, seed=10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
