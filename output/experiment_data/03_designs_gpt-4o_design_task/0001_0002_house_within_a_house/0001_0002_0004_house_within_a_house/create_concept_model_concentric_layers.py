# Created for 0001_0002_house_within_a_house.json

""" Summary:
The provided function generates an architectural concept model based on the "House within a house" metaphor by creating a series of concentric layers that visually represent nesting and protection. Each layer, defined by a decreasing base length and width, symbolizes a transition from public to private space. The inclusion of voids in alternating layers fosters interaction and light penetration, reinforcing the metaphor's themes of containment and exploration. The model's varying geometries and heights reflect a layered spatial hierarchy, while contrasting materials and textures can be applied to distinguish the outer protective shell from the inner sanctuary, enhancing the overall design narrative."""

#! python 3
function_code = """def create_concept_model_concentric_layers(base_length=10.0, base_width=8.0, layer_height=3.0, num_layers=3):
    \"""
    Creates an architectural Concept Model based on the 'House within a house' metaphor. The model consists of concentric
    or overlapping layers, emphasizing spatial hierarchy and a sense of nesting. Each layer represents a transition from
    a public to a private space, with voids and openings facilitating interaction between the layers.

    Parameters:
    base_length (float): The length of the base layer in meters.
    base_width (float): The width of the base layer in meters.
    layer_height (float): The height of each layer in meters.
    num_layers (int): The number of concentric layers to create.

    Returns:
    list: A list of RhinoCommon Brep objects representing the 3D geometries of the Concept Model.
    \"""
    import Rhino.Geometry as rg
    import System
    import random

    random.seed(42)  # Ensure replicable randomness

    # Create a list to hold the 3D geometries
    geometries = []

    # Define base layer dimensions and position
    offset = 0.0
    for i in range(num_layers):
        # Calculate dimensions for the current layer
        current_length = base_length - offset * 2
        current_width = base_width - offset * 2
        current_height = layer_height

        # Create a base rectangle for the current layer
        base_rect = rg.Rectangle3d(rg.Plane.WorldXY, current_length, current_width)

        # Create a box based on the rectangle
        box = rg.Box(rg.Plane.WorldXY, rg.Interval(-current_length / 2, current_length / 2), rg.Interval(-current_width / 2, current_width / 2), rg.Interval(0, current_height))

        # Convert the box to a Brep and add to the geometries list
        brep = box.ToBrep()
        geometries.append(brep)

        # Create voids or openings by subtracting smaller volumes
        if i % 2 == 0:  # Add voids in alternate layers
            void_size = current_length * 0.3
            void_rect = rg.Rectangle3d(rg.Plane.WorldXY, void_size, void_size)
            void_box = rg.Box(rg.Plane.WorldXY, rg.Interval(-void_size / 2, void_size / 2), rg.Interval(-void_size / 2, void_size / 2), rg.Interval(0, current_height))
            void_brep = void_box.ToBrep()

            # Boolean difference to create voids
            brep_with_void = rg.Brep.CreateBooleanDifference([brep], [void_brep], 0.01)
            if brep_with_void:
                geometries[-1] = brep_with_void[0]

        # Update offset for next layer
        offset += random.uniform(0.5, 1.0)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_concept_model_concentric_layers(base_length=12.0, base_width=10.0, layer_height=4.0, num_layers=5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_concept_model_concentric_layers(base_length=15.0, base_width=12.0, layer_height=2.5, num_layers=4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_concept_model_concentric_layers(base_length=8.0, base_width=6.0, layer_height=3.5, num_layers=6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_concept_model_concentric_layers(base_length=14.0, base_width=10.0, layer_height=3.0, num_layers=2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_concept_model_concentric_layers(base_length=20.0, base_width=15.0, layer_height=5.0, num_layers=3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
