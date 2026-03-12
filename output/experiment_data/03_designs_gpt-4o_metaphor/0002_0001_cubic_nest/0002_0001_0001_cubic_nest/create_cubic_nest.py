# Created for 0002_0001_cubic_nest.json

""" Summary:
The function `create_cubic_nest` generates an architectural concept model inspired by the metaphor "Cubic nest." It creates a series of interlocking cubic volumes that reflect the metaphor's key traits of shelter, complexity, and interconnectedness. Each cube is positioned based on a specified overlap factor, resulting in a layered structure that encourages exploration. The function reduces the size of each subsequent cube to enhance the nesting effect, while random directional movements create dynamic spatial experiences. The output is a collection of 3D Brep geometries, visually embodying the metaphor and fulfilling the design task of creating a cohesive yet distinct architectural form."""

#! python 3
function_code = """def create_cubic_nest(base_size, num_cubes, overlap_factor):
    \"""
    Generates a 'Cubic Nest' architectural concept model consisting of interlocking or overlapping cubic volumes.

    Parameters:
    - base_size (float): The base size for the initial cube in meters.
    - num_cubes (int): The number of cubes to generate in the nest.
    - overlap_factor (float): A factor determining the extent of overlap between cubes (0 to 1).

    Returns:
    - List of Rhino.Geometry.Brep: A list of Brep objects representing the 3D geometry of the cubic nest.
    \"""
    import Rhino.Geometry as rg
    import random

    # Set a seed for randomness to ensure replicability
    random.seed(42)

    # List to store the resulting Brep cubes
    breps = []

    # Start position for the first cube
    current_position = rg.Point3d(0, 0, 0)

    for i in range(num_cubes):
        # Create a cube (box) centered at the current position
        cube = rg.Box(rg.Plane.WorldXY, rg.Interval(-base_size/2, base_size/2), rg.Interval(-base_size/2, base_size/2), rg.Interval(-base_size/2, base_size/2))
        breps.append(cube.ToBrep())

        # Calculate new position for the next cube with an overlap
        overlap_distance = base_size * overlap_factor
        direction = random.choice([(1, 0, 0), (0, 1, 0), (0, 0, 1), (-1, 0, 0), (0, -1, 0), (0, 0, -1)])
        move_vector = rg.Vector3d(direction[0] * overlap_distance, direction[1] * overlap_distance, direction[2] * overlap_distance)
        current_position += move_vector

        # Update the position for the next cube
        base_size *= 0.9  # Slightly reduce the size for the next cube to create a nesting effect

    return breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_cubic_nest(2.0, 5, 0.3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_cubic_nest(1.5, 10, 0.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_cubic_nest(3.0, 8, 0.2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_cubic_nest(2.5, 6, 0.4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_cubic_nest(1.0, 12, 0.1)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
