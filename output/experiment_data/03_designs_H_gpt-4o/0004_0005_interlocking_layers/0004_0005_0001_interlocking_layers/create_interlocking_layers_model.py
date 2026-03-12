# Created for 0004_0005_interlocking_layers.json

""" Summary:
The provided function generates an architectural concept model based on the "Interlocking Layers" metaphor by creating a series of overlapping and intersecting planes or volumes. It accepts parameters such as layer count, size, vertical gaps, and rotation angles, which influence the model's complexity and spatial relationships. Each layer is randomly rotated and translated, enhancing the dynamic nature of the design while allowing for varied spatial experiences, such as connectivity and privacy. The result is a collection of Brep geometries that visually embody the metaphor's traits, showcasing structural complexity and a cohesive yet distinct architectural form."""

#! python 3
function_code = """def create_interlocking_layers_model(layer_count=6, base_size=12.0, vertical_gap=2.0, rotation_range=45, seed=42):
    \"""
    Creates an architectural Concept Model based on the 'Interlocking Layers' metaphor.

    This function generates a structure composed of intersecting and overlapping planes or volumes,
    illustrating diverse spatial experiences with varying degrees of openness and seclusion.

    Parameters:
    - layer_count (int): The number of interlocking layers to create.
    - base_size (float): The base size for each layer in meters.
    - vertical_gap (float): The vertical distance between layers in meters.
    - rotation_range (int): The maximum rotation angle for layers in degrees.
    - seed (int): A seed for random number generation to ensure replicability.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep geometries representing the 3D model.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    random.seed(seed)
    geometries = []

    for i in range(layer_count):
        # Random rotation and translation for each layer
        angle = random.uniform(-rotation_range, rotation_range)
        translation_x = random.uniform(-base_size / 4, base_size / 4)
        translation_y = random.uniform(-base_size / 4, base_size / 4)
        translation_z = i * vertical_gap

        # Create a base plane for each layer
        layer_plane = rg.Plane.WorldXY
        layer_plane.Translate(rg.Vector3d(translation_x, translation_y, translation_z))
        layer_plane.Rotate(math.radians(angle), rg.Vector3d.ZAxis)

        # Create a rectangle for each layer and extrude it
        layer_rect = rg.Rectangle3d(layer_plane, base_size, base_size)
        extrusion_vector = rg.Vector3d(0, 0, random.uniform(1, vertical_gap))
        layer_brep = rg.Brep.CreateFromSurface(rg.Surface.CreateExtrusion(layer_rect.ToNurbsCurve(), extrusion_vector))

        # Add the Brep to the list
        geometries.append(layer_brep)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_interlocking_layers_model(layer_count=8, base_size=10.0, vertical_gap=3.0, rotation_range=30, seed=24)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_interlocking_layers_model(layer_count=5, base_size=15.0, vertical_gap=2.5, rotation_range=60, seed=10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_interlocking_layers_model(layer_count=7, base_size=14.0, vertical_gap=1.5, rotation_range=90, seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_interlocking_layers_model(layer_count=10, base_size=20.0, vertical_gap=4.0, rotation_range=15, seed=5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_interlocking_layers_model(layer_count=6, base_size=18.0, vertical_gap=3.0, rotation_range=75, seed=1)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
