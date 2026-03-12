# Created for 0015_0004_suspended_intersecting_assembly.json

""" Summary:
The provided function generates an architectural concept model based on the metaphor "Suspended intersecting assembly." It creates a series of modular, interlocking elements that mimic the appearance of floating structures, emphasizing lightness and fluidity. By randomly positioning and rotating these elements at varying heights, the function forms a lattice-like structure that enhances visual interconnectivity and spatial relationships. The use of lightweight materials is simulated through the dimensions and transformations of each module. The result is a dynamic model that encapsulates the essence of balance and tension while allowing for adaptability and interaction within the designed space."""

#! python 3
function_code = """def create_suspended_intersecting_assembly(base_size, num_elements, height_variation, seed=None):
    \"""
    Create an architectural Concept Model embodying the 'Suspended intersecting assembly'.

    This function generates a model consisting of modular, interlocking elements that appear to float 
    and intersect at various levels, forming a lattice-like structure. The design emphasizes lightness, 
    fluidity, and dynamic spatial relationships.

    Parameters:
    - base_size (float): The size of the base module in meters.
    - num_elements (int): The number of modular elements to be created.
    - height_variation (float): The maximum variation in height for the placement of elements.
    - seed (int, optional): Seed for the random number generator to ensure replicability.

    Returns:
    - List of Brep: A list of 3D geometries representing the concept model.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    if seed is not None:
        random.seed(seed)

    elements = []
    
    for i in range(num_elements):
        # Create a base box as a module
        width = base_size
        depth = base_size / 2
        height = base_size / 4
        
        box = rg.Box(rg.Plane.WorldXY, rg.Interval(0, width), rg.Interval(0, depth), rg.Interval(0, height))
        
        # Randomly position and rotate the box
        x_offset = random.uniform(-base_size, base_size)
        y_offset = random.uniform(-base_size, base_size)
        z_offset = random.uniform(0, height_variation)
        
        translation = rg.Vector3d(x_offset, y_offset, z_offset)
        
        angle_x = random.uniform(-30, 30)  # degrees
        angle_y = random.uniform(-30, 30)  # degrees
        angle_z = random.uniform(-30, 30)  # degrees
        
        rotation_x = rg.Transform.Rotation(math.radians(angle_x), rg.Vector3d(1, 0, 0), box.Plane.Origin)
        rotation_y = rg.Transform.Rotation(math.radians(angle_y), rg.Vector3d(0, 1, 0), box.Plane.Origin)
        rotation_z = rg.Transform.Rotation(math.radians(angle_z), rg.Vector3d(0, 0, 1), box.Plane.Origin)
        
        transform = rg.Transform.Translation(translation) * rotation_x * rotation_y * rotation_z
        
        box.Transform(transform)
        
        # Add the transformed box to the elements list
        elements.append(box.ToBrep())

    return elements"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_suspended_intersecting_assembly(base_size=2.0, num_elements=10, height_variation=5.0, seed=42)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_suspended_intersecting_assembly(base_size=1.5, num_elements=15, height_variation=3.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_suspended_intersecting_assembly(base_size=3.0, num_elements=20, height_variation=6.0, seed=100)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_suspended_intersecting_assembly(base_size=2.5, num_elements=12, height_variation=4.0, seed=7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_suspended_intersecting_assembly(base_size=1.0, num_elements=8, height_variation=2.5, seed=9)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
