# Created for 0005_0002_distorted_puzzle.json

""" Summary:
The provided function generates an architectural concept model based on the "Distorted puzzle" metaphor by creating a series of fragmented but interconnected modules. It takes parameters such as base size, number of modules, height variation, and overlap factor to create a dynamic arrangement. Each module is represented as a box with varying heights, simulating tension and movement. The random offsets in positioning and stacking encourage a labyrinthine quality, fostering unexpected spatial relationships and perspectives. This approach results in a model that embodies complexity and coherence, inviting exploration and engagement, aligning with the metaphor's playful yet unified essence."""

#! python 3
function_code = """def create_distorted_puzzle_model(base_size, num_modules, height_variation, overlap_factor):
    \"""
    Generate an architectural Concept Model based on the 'Distorted puzzle' metaphor.

    Parameters:
    - base_size: A float representing the base dimension of each module in meters.
    - num_modules: An integer representing the number of modules to be created.
    - height_variation: A float indicating the maximum height variation between stacked modules.
    - overlap_factor: A float between 0 and 1 indicating the degree of overlap between modules.

    Returns:
    - A list of RhinoCommon Brep objects representing the 3D geometries of the Concept Model.
    \"""
    import Rhino.Geometry as rg
    import System
    from random import seed, uniform

    # Set the randomness seed for reproducibility
    seed(42)

    # Initialize a list to store the resulting geometries
    geometries = []

    # Define the base module as a simple box
    def create_base_module(x, y, z, size, height):
        base_plane = rg.Plane(rg.Point3d(x, y, z), rg.Vector3d.ZAxis)
        box = rg.Box(base_plane, rg.Interval(0, size), rg.Interval(0, size), rg.Interval(0, height))
        return box.ToBrep()

    current_x, current_y, current_z = 0, 0, 0

    for i in range(num_modules):
        # Calculate the module's height with a variation
        module_height = base_size + uniform(-height_variation, height_variation)

        # Create a new module and add it to the list
        module = create_base_module(current_x, current_y, current_z, base_size, module_height)
        geometries.append(module)

        # Randomly decide the next module's position with overlap
        offset_x = base_size * (1 - uniform(0, overlap_factor))
        offset_y = base_size * (1 - uniform(0, overlap_factor))
        
        # Randomly select if the module should move in x or y direction
        if uniform(0, 1) > 0.5:
            current_x += offset_x
        else:
            current_y += offset_y

        # Randomly decide if the module should be stacked (add to z)
        if uniform(0, 1) > 0.3:
            current_z += module_height * (1 - overlap_factor)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_distorted_puzzle_model(2.0, 10, 0.5, 0.3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_distorted_puzzle_model(1.5, 15, 0.8, 0.4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_distorted_puzzle_model(3.0, 5, 0.2, 0.6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_distorted_puzzle_model(2.5, 8, 0.3, 0.2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_distorted_puzzle_model(1.0, 12, 0.6, 0.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
