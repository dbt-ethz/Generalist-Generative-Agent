# Created for 0017_0001_cascading_frames.json

""" Summary:
The `cascading_frames_model` function generates an architectural concept model by creating a series of progressively tiered structures that embody the metaphor of "Cascading frames." Each layer is calculated based on parameters such as base dimensions, height increments, and offsets, resulting in staggered geometries that visually suggest movement and depth. The function utilizes Rhino's geometry capabilities to create and extrude rectangular shapes, shifting them vertically and horizontally to enhance the dynamic silhouette. This design approach emphasizes verticality and connectivity while allowing for the interplay of light and shadow, fostering a fluid transition between the model's layers."""

#! python 3
function_code = """def cascading_frames_model(base_length, base_width, height_increment, num_layers, offset_factor):
    \"""
    Creates an architectural Concept Model embodying the 'Cascading frames' metaphor.
    
    This function generates a series of progressively tiered structures or elements that suggest movement and 
    progression. Each layer is offset slightly from the previous one, creating a dynamic silhouette with 
    varying depth and visual interest.

    Parameters:
    - base_length: The length of the base layer of the structure, in meters.
    - base_width: The width of the base layer of the structure, in meters.
    - height_increment: The height increment for each successive layer, in meters.
    - num_layers: The total number of cascading layers.
    - offset_factor: The factor by which each layer is offset from the previous one, controlling the degree of 
      the cascade effect.

    Returns:
    - A list of Brep objects representing the 3D geometries of the cascading frames.
    \"""
    import Rhino.Geometry as rg
    import random

    random.seed(42)  # Ensures reproducibility

    geometries = []
    base_height = 0

    for i in range(num_layers):
        # Calculate the size and position of the current layer
        layer_length = base_length - (i * offset_factor)
        layer_width = base_width - (i * offset_factor)
        layer_height = base_height + (i * height_increment)

        # Define the base rectangle for the current layer
        base_rect = rg.Rectangle3d(
            rg.Plane.WorldXY,
            rg.Interval(-layer_length / 2, layer_length / 2),
            rg.Interval(-layer_width / 2, layer_width / 2)
        ).ToNurbsCurve()

        # Create an extrusion for the current layer
        extrude_vector = rg.Vector3d(0, 0, height_increment)
        extrude_vector.Unitize()
        extrude_vector *= height_increment

        extrusion = rg.Extrusion.Create(base_rect, height_increment, True)

        # Move the extrusion to its correct vertical position
        move_vector = rg.Vector3d(0, 0, layer_height)
        transformation = rg.Transform.Translation(move_vector)
        extrusion.Transform(transformation)

        geometries.append(extrusion.ToBrep())

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = cascading_frames_model(10, 5, 2, 5, 1)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = cascading_frames_model(15, 7, 3, 4, 2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = cascading_frames_model(8, 4, 1.5, 6, 0.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = cascading_frames_model(12, 6, 2.5, 3, 1.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = cascading_frames_model(20, 10, 4, 7, 3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
