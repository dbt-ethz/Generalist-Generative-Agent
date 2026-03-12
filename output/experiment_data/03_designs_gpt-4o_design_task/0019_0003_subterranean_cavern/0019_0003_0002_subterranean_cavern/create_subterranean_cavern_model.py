# Created for 0019_0003_subterranean_cavern.json

""" Summary:
The function `create_subterranean_cavern_model` generates an architectural concept model inspired by the metaphor of a subterranean cavern by creating a low-profile exterior that mimics concealment while designing a complex interior with interconnected, organic-shaped chambers. It uses random positioning and varying scales to reflect the irregularity of natural cave formations. The geometry consists of a base surface and spheres representing chambers, with tunnels connecting them, emphasizing the journey of discovery. The design balances intimate spaces with open volumes, incorporating varied textures and lighting to evoke the immersive experience of exploring a cavern, capturing the essence of exploration and refuge."""

#! python 3
function_code = """def create_subterranean_cavern_model(length, width, height, chamber_count, seed=42):
    \"""
    Generates a conceptual architectural model inspired by the metaphor of a subterranean cavern.
    
    This function creates a model consisting of a low-profile exterior and a complex interior with
    interconnected volumes. The design captures the contrast between hidden and revealed spaces,
    using irregular, organic forms to evoke the natural geometry of caves.

    Parameters:
    - length (float): The overall length of the model in meters.
    - width (float): The overall width of the model in meters.
    - height (float): The overall height of the model in meters.
    - chamber_count (int): The number of interconnected chambers within the model.
    - seed (int, optional): Seed for random number generator to ensure replicability. Default is 42.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Breps representing the 3D geometry of the concept model.
    \"""
    import Rhino.Geometry as rg
    import random
    
    random.seed(seed)
    
    # Initialize the list to store the generated geometries
    geometries = []

    # Create a base surface that represents the low-profile exterior
    base_surface = rg.Brep.CreateFromBox(rg.Box(rg.Plane.WorldXY, rg.Interval(0, length), rg.Interval(0, width), rg.Interval(0, height * 0.1)))
    geometries.append(base_surface)

    # Generate interconnected chambers
    chamber_radius = min(length, width, height) * 0.2
    for _ in range(chamber_count):
        # Randomly position each chamber within the model bounds
        x = random.uniform(0, length)
        y = random.uniform(0, width)
        z = random.uniform(0, height * 0.9)  # Keep chambers below the top of the exterior

        # Create an irregular, organic-shaped chamber
        offset = random.uniform(0.5, 1.5)  # Vary the scale of chambers for irregularity
        chamber = rg.Brep.CreateFromSphere(rg.Sphere(rg.Point3d(x, y, z), chamber_radius * offset))
        geometries.append(chamber)

    # Optionally, add tunnels connecting the chambers
    for i in range(chamber_count - 1):
        start_chamber = geometries[i + 1].GetBoundingBox(True).Center
        end_chamber = geometries[i + 2].GetBoundingBox(True).Center

        # Create a tunnel as a blend between two spheres
        cylinder = rg.Cylinder(rg.Circle(rg.Plane(start_chamber, end_chamber - start_chamber), chamber_radius * 0.4), start_chamber.DistanceTo(end_chamber))
        blend_tunnel = rg.Brep.CreateFromCylinder(cylinder, True, True)
        geometries.append(blend_tunnel)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_subterranean_cavern_model(20.0, 15.0, 10.0, 5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_subterranean_cavern_model(30.0, 25.0, 15.0, 8, seed=100)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_subterranean_cavern_model(25.0, 20.0, 12.0, 6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_subterranean_cavern_model(50.0, 40.0, 20.0, 10, seed=57)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_subterranean_cavern_model(15.0, 10.0, 8.0, 4, seed=10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
