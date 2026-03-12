# Created for 0004_0004_interlocking_layers.json

""" Summary:
The function `create_interlocking_layers_model` generates an architectural concept model based on the metaphor of "Interlocking Layers." It constructs a series of overlapping planes or volumes that illustrate connectivity and interaction. By utilizing random offsets, angles, and defined properties like length, width, and thickness, the model embodies the complexity of interwoven elements. Each layer is created as a distinct yet integrated entity, enhancing the spatial dynamics of the design. The final output comprises 3D geometries that visually represent the balance between openness and separation, aligning with the metaphor's emphasis on cohesive spatial experiences."""

#! python 3
function_code = """def create_interlocking_layers_model(length=20, width=10, height=5, num_layers=5, layer_thickness=0.5, random_seed=42):
    \"""
    Creates an architectural Concept Model based on the 'Interlocking Layers' metaphor. The model consists of a series
    of overlapping and integrated planes that illustrate the concept of interaction and connectivity.

    Parameters:
    - length (float): The length of the model in meters.
    - width (float): The width of the model in meters.
    - height (float): The maximum height of the model in meters.
    - num_layers (int): The number of interlocking layers to create.
    - layer_thickness (float): The thickness of each layer.
    - random_seed (int): The seed for random number generation to ensure replicability.

    Returns:
    - list of Rhino.Geometry.Brep: A list of 3D geometries representing the interlocking layers.
    \"""
    import Rhino.Geometry as rg
    import random

    random.seed(random_seed)

    layers = []
    base_height = 0

    for i in range(num_layers):
        # Randomly determine the offset and angle for each layer
        offset_x = random.uniform(-length * 0.1, length * 0.1)
        offset_y = random.uniform(-width * 0.1, width * 0.1)
        angle = random.uniform(-15, 15)

        # Create a base plane for the layer
        base_plane = rg.Plane(rg.Point3d(offset_x, offset_y, base_height), rg.Vector3d.ZAxis)

        # Create a rectangular surface for the layer
        rectangle = rg.Rectangle3d(base_plane, rg.Interval(-length / 2, length / 2), rg.Interval(-width / 2, width / 2))
        surface = rg.Surface.CreateExtrusion(rectangle.ToNurbsCurve(), rg.Vector3d(0, 0, layer_thickness))

        # Rotate the layer around its center
        center_point = rg.Point3d(offset_x, offset_y, base_height + layer_thickness / 2)
        rotated_surface = surface.Rotate(angle, rg.Vector3d.ZAxis, center_point)

        # Add the rotated surface to the layers list
        layers.append(rotated_surface)

        # Update the base height for the next layer
        base_height += layer_thickness

    return layers"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_interlocking_layers_model(length=30, width=15, height=7, num_layers=8, layer_thickness=0.4, random_seed=123)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_interlocking_layers_model(length=25, width=12, height=6, num_layers=10, layer_thickness=0.3, random_seed=56)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_interlocking_layers_model(length=40, width=20, height=10, num_layers=6, layer_thickness=0.6, random_seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_interlocking_layers_model(length=35, width=18, height=9, num_layers=7, layer_thickness=0.7, random_seed=78)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_interlocking_layers_model(length=28, width=14, height=8, num_layers=5, layer_thickness=0.2, random_seed=11)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
