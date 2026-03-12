# Created for 0020_0005_stacked_forests.json

""" Summary:
The provided function generates an architectural concept model inspired by the "Stacked forests" metaphor, which emphasizes cascading terraces reflecting ecological layers. By defining parameters such as base dimensions, layer count, height variation, and openness, the function constructs a series of stepped geometries. Each layer is created with varying dimensions and heights to simulate the vertical stratification of a forest, incorporating both solid and void elements for light and shadow interplay. The resulting model embodies organic growth patterns and spatial connectivity, mirroring a natural forest ecosystem while allowing for diverse experiences across its layered structure."""

#! python 3
function_code = """def generate_stacked_forests_structure(base_length, base_width, num_layers, height_variation, openness_ratio):
    \"""
    Generates an architectural Concept Model based on the 'Stacked forests' metaphor.
    
    This model features a cascading series of terraces or ledges that represent different
    ecological layers, with an emphasis on vertical integration and a balance between open
    and enclosed spaces.

    Parameters:
    - base_length (float): The base length of the structure in meters.
    - base_width (float): The base width of the structure in meters.
    - num_layers (int): The number of cascading layers to create.
    - height_variation (float): Maximum variation in height for each layer in meters.
    - openness_ratio (float): A value between 0 and 1 indicating the degree of openness (0 fully enclosed, 1 fully open).

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep objects representing the 3D geometries of the concept model.
    \"""
    import Rhino.Geometry as rg
    import random

    # Set the random seed for consistency
    random.seed(42)

    # Initialize the list to store the generated geometries
    geometries = []

    # Base starting point
    base_point = rg.Point3d(0, 0, 0)
    current_height = 0

    for layer in range(num_layers):
        # Define layer height with variation
        layer_height = random.uniform(height_variation * 0.5, height_variation)

        # Calculate reduced dimensions for the current layer
        layer_length = base_length * (1 - openness_ratio * (layer / num_layers))
        layer_width = base_width * (1 - openness_ratio * (layer / num_layers))

        # Create a rectangle that acts as the base for the current layer
        plane = rg.Plane(base_point + rg.Vector3d(0, 0, current_height), rg.Vector3d.ZAxis)
        rectangle = rg.Rectangle3d(plane, layer_length, layer_width)

        # Extrude the rectangle upwards to form a terrace
        extrusion = rg.Extrusion.Create(rectangle.ToNurbsCurve(), layer_height, True)
        brep = extrusion.ToBrep()

        # Add the current layer to the geometries list
        geometries.append(brep)

        # Create voids for openness
        if openness_ratio > 0:
            void_length = layer_length * openness_ratio * random.uniform(0.2, 0.5)
            void_width = layer_width * openness_ratio * random.uniform(0.2, 0.5)
            void_rectangle = rg.Rectangle3d(plane, void_length, void_width)
            void_extrusion = rg.Extrusion.Create(void_rectangle.ToNurbsCurve(), layer_height, True)
            void_brep = void_extrusion.ToBrep()
            geometries.append(void_brep)

        # Update the height for the next layer
        current_height += layer_height * 0.8

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = generate_stacked_forests_structure(10.0, 5.0, 3, 2.0, 0.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = generate_stacked_forests_structure(15.0, 7.5, 4, 3.0, 0.3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = generate_stacked_forests_structure(12.0, 6.0, 5, 1.5, 0.7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = generate_stacked_forests_structure(8.0, 4.0, 6, 2.5, 0.2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = generate_stacked_forests_structure(20.0, 10.0, 2, 4.0, 0.6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
