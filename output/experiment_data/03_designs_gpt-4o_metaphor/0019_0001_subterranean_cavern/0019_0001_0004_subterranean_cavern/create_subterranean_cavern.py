# Created for 0019_0001_subterranean_cavern.json

""" Summary:
The provided function `create_subterranean_cavern` generates an architectural concept model inspired by the metaphor of a "subterranean cavern." It creates a 3D representation by defining a bounding box that simulates the cavern's structure and introduces spherical voids (cavities) within this space. The random placement and sizing of these cavities evoke a sense of exploration and refuge, aligning with the metaphors traits. By incorporating organic shapes and varied lighting (through the cavities), the model creates an immersive environment reminiscent of natural, secluded spaces, thus fulfilling the design task effectively."""

#! python 3
function_code = """def create_subterranean_cavern(length, width, height, num_cavities, cavity_max_radius, seed=42):
    \"""
    Creates an architectural Concept Model representing a 'subterranean cavern' using RhinoCommon.
    
    Parameters:
    length (float): The length of the model.
    width (float): The width of the model.
    height (float): The height of the model.
    num_cavities (int): Number of cavity voids to create within the model.
    cavity_max_radius (float): Maximum radius for the spherical cavities.
    seed (int, optional): Seed for the random number generator to ensure replicability.
    
    Returns:
    list: A list of Brep objects representing the model geometry (both solid and voids).
    \"""
    import Rhino.Geometry as rg
    import random

    # Set random seed
    random.seed(seed)
    
    # Create the base bounding box for the cavern
    base_box = rg.Box(rg.Plane.WorldXY, rg.Interval(0, length), rg.Interval(0, width), rg.Interval(0, height))
    base_brep = base_box.ToBrep()
    
    # Create cavity voids within the cavern
    cavities = []
    for _ in range(num_cavities):
        # Randomly determine the center and radius of each cavity
        x = random.uniform(0, length)
        y = random.uniform(0, width)
        z = random.uniform(0, height)
        radius = random.uniform(0.1, cavity_max_radius)
        
        # Create a spherical cavity
        sphere = rg.Sphere(rg.Point3d(x, y, z), radius)
        sphere_brep = rg.Brep.CreateFromSphere(sphere)
        
        # Subtract the cavity from the base brep
        if sphere_brep and base_brep:
            result = rg.Brep.CreateBooleanDifference(base_brep, sphere_brep, 0.001)
            if result:
                base_brep = result[0]
    
    # Return the final list of Breps
    return [base_brep]"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_subterranean_cavern(100.0, 50.0, 30.0, 10, 5.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_subterranean_cavern(200.0, 100.0, 50.0, 15, 10.0, seed=123)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_subterranean_cavern(150.0, 75.0, 40.0, 20, 7.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_subterranean_cavern(80.0, 40.0, 25.0, 5, 3.0, seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_subterranean_cavern(120.0, 60.0, 35.0, 12, 6.0, seed=2023)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
