# Created for 0004_0002_interlocking_layers.json

""" Summary:
The provided function, `create_interlocking_layers_complex`, generates an architectural concept model that embodies the "Interlocking Layers" metaphor by creating a series of overlapping and interwoven volumes. It takes parameters such as base dimensions, total height, number of layers, maximum shift, and rotation variability to define the complexity of the model. Each layer is randomly shifted and rotated, resulting in a dynamic spatial arrangement that illustrates the metaphor's implications of complexity and interaction. The generated 3D Breps represent a layered structure, showcasing varying protrusions and recesses, enhancing the visual depth and functional diversity of the architecture."""

#! python 3
function_code = """def create_interlocking_layers_complex(base_length, base_width, total_height, num_layers, max_shift, rotation_variability):
    \"""
    Creates an architectural Concept Model that embodies the 'Interlocking Layers' metaphor using complex interwoven volumes.

    This function generates a series of overlapping and interlocking volumes that emphasize spatial hierarchy and dynamic
    relationships. It aims to create a complex architectural form with varying protrusions and recesses to illustrate the
    metaphor effectively.

    Parameters:
    - base_length (float): Length of the base volume in meters.
    - base_width (float): Width of the base volume in meters.
    - total_height (float): The total height of the model in meters.
    - num_layers (int): The number of interlocking layers.
    - max_shift (float): Maximum shift in meters for the offset between layers.
    - rotation_variability (float): Maximum allowable rotation in degrees for each layer.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of 3D Brep geometries representing the interlocking layered structure.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    # Set a random seed for reproducibility
    random.seed(42)

    # Calculate the height of each layer
    layer_height = total_height / num_layers

    # List to store the resulting Breps
    breps = []

    for i in range(num_layers):
        # Define the offset and rotation for each layer
        shift_x = random.uniform(-max_shift, max_shift)
        shift_y = random.uniform(-max_shift, max_shift)
        rotation_angle = random.uniform(-rotation_variability, rotation_variability)

        # Define the base rectangle for each layer
        base_origin = rg.Point3d(shift_x, shift_y, i * layer_height)
        base_plane = rg.Plane(base_origin, rg.Vector3d.ZAxis)
        box = rg.Box(base_plane, rg.Interval(0, base_length), rg.Interval(0, base_width), rg.Interval(0, layer_height))
        
        # Construct a 3D box for the layer
        brep_box = box.ToBrep()

        # Apply rotation around the center of the box
        center = box.Center
        rotation = rg.Transform.Rotation(math.radians(rotation_angle), rg.Vector3d.ZAxis, center)
        brep_box.Transform(rotation)

        # Add the transformed Brep to the list
        breps.append(brep_box)

    return breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_interlocking_layers_complex(5.0, 3.0, 10.0, 6, 0.5, 15.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_interlocking_layers_complex(4.0, 2.0, 8.0, 8, 0.3, 10.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_interlocking_layers_complex(6.0, 4.0, 12.0, 5, 0.8, 20.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_interlocking_layers_complex(7.0, 5.0, 15.0, 4, 0.4, 25.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_interlocking_layers_complex(3.5, 2.5, 9.0, 7, 0.6, 12.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
