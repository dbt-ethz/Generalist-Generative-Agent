# Created for 0002_0002_cubic_nest.json

""" Summary:
The function `create_cubic_nest_concept_model` generates an architectural concept model by creating a series of nested, overlapping cubic volumes based on the "Cubic nest" metaphor. It defines a base cube and systematically adds layers of larger cubes, varying their positions randomly to foster dynamic intersections and spatial complexity. This overlapping arrangement reflects the metaphor's notion of interconnectedness and protection, evoking a sense of shelter. Furthermore, by adjusting the cube sizes and their layering, the function enhances the perception of solid and void, inviting exploration and interaction within the intricate architectural composition."""

#! python 3
function_code = """def create_cubic_nest_concept_model(base_size, num_layers, overlap_factor, randomness_seed):
    \"""
    Generate an architectural Concept Model based on the 'Cubic Nest' metaphor using nested and overlapping cubes.

    Parameters:
    base_size (float): The base size of the smallest cube in meters.
    num_layers (int): The number of nested layers of cubes.
    overlap_factor (float): A factor that determines how much cubes overlap each other.
    randomness_seed (int): Seed for the random number generator to ensure reproducible results.

    Returns:
    list: A list of RhinoCommon Breps representing the nested cubic volumes.
    \"""
    import Rhino.Geometry as rg
    import random

    # Set the random seed for reproducibility
    random.seed(randomness_seed)

    # Initialize a list to store the Breps
    breps = []

    # Define the base cube
    base_cube = rg.Box(rg.Plane.WorldXY, rg.Interval(-base_size/2, base_size/2), 
                       rg.Interval(-base_size/2, base_size/2), rg.Interval(-base_size/2, base_size/2))
    
    # Add the base cube to the breps list
    breps.append(base_cube.ToBrep())

    # Create nested and overlapping cubes
    for i in range(1, num_layers + 1):
        # Calculate size increment for each layer
        size_increment = base_size * overlap_factor * i
        
        # Randomize position to create dynamic alignments and intersections
        dx = random.uniform(-size_increment, size_increment)
        dy = random.uniform(-size_increment, size_increment)
        dz = random.uniform(-size_increment, size_increment)
        
        translation = rg.Vector3d(dx, dy, dz)

        # Create a new cube with the increased size
        cube_size = base_size + size_increment
        cube_box = rg.Box(rg.Plane.WorldXY, rg.Interval(-cube_size/2, cube_size/2), 
                          rg.Interval(-cube_size/2, cube_size/2), rg.Interval(-cube_size/2, cube_size/2))
        
        # Translate the cube to create overlap and dynamic intersections
        cube_box.Transform(rg.Transform.Translation(translation))
        
        # Add the new cube to the breps list
        breps.append(cube_box.ToBrep())

    return breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_cubic_nest_concept_model(2.0, 5, 0.5, 42)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_cubic_nest_concept_model(1.5, 3, 0.3, 10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_cubic_nest_concept_model(3.0, 4, 0.7, 99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_cubic_nest_concept_model(2.5, 6, 0.4, 21)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_cubic_nest_concept_model(4.0, 2, 0.2, 77)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
