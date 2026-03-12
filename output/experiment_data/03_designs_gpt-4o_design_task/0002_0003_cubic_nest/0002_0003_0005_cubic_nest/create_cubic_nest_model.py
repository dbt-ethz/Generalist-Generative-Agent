# Created for 0002_0003_cubic_nest.json

""" Summary:
The provided function creates an architectural concept model inspired by the "Cubic nest" metaphor by generating a series of interwoven cubic forms. It defines a base cube and then creates additional layers, each slightly smaller and shifted randomly within a specified offset. This layering mimics the protective enclosure and interconnectedness of the metaphor, allowing for varied spatial experiences. The function emphasizes the balance between solid and void, enhancing exploration through dynamic arrangements. Each cubic module retains individuality while contributing to a cohesive nested structure, ultimately fostering curiosity and engagement within the designed environment."""

#! python 3
function_code = """def create_cubic_nest_model(base_length=10, num_layers=3, offset=2):
    \"""
    Create an architectural Concept Model based on the 'Cubic nest' metaphor, using a sequence of interwoven cubic forms.
    
    Parameters:
    - base_length (float): The length of the initial cube's edge in meters.
    - num_layers (int): The number of layers of interwoven cubes.
    - offset (float): The offset distance between layers to create interconnectivity.

    Returns:
    - List of Breps: A list of 3D geometries representing the nested cubic structure.
    \"""
    import Rhino.Geometry as rg
    import random

    # Set seed for reproducibility
    random.seed(42)

    # List to store the resulting Breps
    cubic_nest = []

    # Base cube
    base_cube = rg.Box(rg.Plane.WorldXY, rg.Interval(0, base_length), rg.Interval(0, base_length), rg.Interval(0, base_length))
    cubic_nest.append(base_cube.ToBrep())

    # Generate interwoven cubes
    for i in range(1, num_layers):
        # Calculate new cube dimensions and position
        new_length = base_length - i * (offset / 2)
        translation_vector = rg.Vector3d(random.uniform(-offset, offset), random.uniform(-offset, offset), random.uniform(-offset, offset))
        
        # Create a new cube
        new_cube = rg.Box(rg.Plane.WorldXY, rg.Interval(0, new_length), rg.Interval(0, new_length), rg.Interval(0, new_length))
        
        # Transform the cube by translating it
        transform = rg.Transform.Translation(translation_vector)
        new_cube.Transform(transform)

        # Add the new cube to the list
        cubic_nest.append(new_cube.ToBrep())

    # Return the list of Breps
    return cubic_nest"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_cubic_nest_model(base_length=15, num_layers=5, offset=3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_cubic_nest_model(base_length=8, num_layers=4, offset=1)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_cubic_nest_model(base_length=12, num_layers=6, offset=2.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_cubic_nest_model(base_length=20, num_layers=2, offset=4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_cubic_nest_model(base_length=5, num_layers=3, offset=1)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
