# Created for 0020_0002_stacked_forests.json

""" Summary:
The provided function, `create_stacked_forests_concept`, generates an architectural concept model inspired by the "Stacked forests" metaphor by creating a series of interlocking volumes that represent distinct layers of a forest. It uses parameters like base size, number of layers, and height variability to create an organic form. Each layer's height is randomized to mimic natural growth patterns, while voids are introduced on alternating layers to represent clearings. This design emphasizes vertical connectivity and spatial richness, reflecting the metaphor's complexity and hierarchy, resulting in a model that captures the essence of a layered forest ecosystem."""

#! python 3
function_code = """def create_stacked_forests_concept(base_size=5, num_layers=5, height_variability=2, seed=42):
    \"""
    Generates an architectural Concept Model inspired by the 'Stacked forests' metaphor. The model is composed of interlocking volumes
    that mimic a forest's diverse ecosystem, emphasizing hierarchical layering and spatial richness.

    Parameters:
    base_size (float): The base size of each forest layer in meters.
    num_layers (int): The number of vertical layers or tiers in the structure.
    height_variability (float): The variability in height for each layer to create an organic form.
    seed (int): Seed for the random number generator to ensure replicable results.

    Returns:
    list: A list of RhinoCommon Brep objects representing the 3D geometries of the concept model.
    \"""
    import Rhino.Geometry as rg
    import random

    random.seed(seed)
    geometries = []

    # Define base plane for stacking
    base_plane = rg.Plane.WorldXY

    # Loop to create each layer
    for i in range(num_layers):
        # Determine layer height and position
        layer_height = base_size + random.uniform(-height_variability, height_variability)
        translation_vector = rg.Vector3d(0, 0, i * layer_height)

        # Create a base rectangle for the layer
        rectangle = rg.Rectangle3d(base_plane, rg.Interval(-base_size / 2, base_size / 2), rg.Interval(-base_size / 2, base_size / 2))
        
        # Create a brep from the rectangle, extruding it to form a layer
        extrusion_direction = rg.Vector3d(0, 0, layer_height)
        layer_brep = rg.Brep.CreateFromSurface(rg.Surface.CreateExtrusion(rectangle.ToNurbsCurve(), extrusion_direction))

        # Apply a transformation to position the layer in the stack
        translation_transform = rg.Transform.Translation(translation_vector)
        layer_brep.Transform(translation_transform)

        # Add the layer brep to the list of geometries
        geometries.append(layer_brep)

        # Introduce voids within the layer to mimic clearings
        if i % 2 == 0:  # Create voids on every other layer
            void_size = base_size * 0.3
            void_rect = rg.Rectangle3d(base_plane, rg.Interval(-void_size / 2, void_size / 2), rg.Interval(-void_size / 2, void_size / 2))
            void_brep = rg.Brep.CreateFromSurface(rg.Surface.CreateExtrusion(void_rect.ToNurbsCurve(), extrusion_direction))
            void_brep.Transform(translation_transform)
            geometries.append(void_brep)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_stacked_forests_concept(base_size=10, num_layers=8, height_variability=3, seed=123)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_stacked_forests_concept(base_size=7, num_layers=6, height_variability=1.5, seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_stacked_forests_concept(base_size=8, num_layers=4, height_variability=2.5, seed=56)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_stacked_forests_concept(base_size=6, num_layers=10, height_variability=4, seed=77)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_stacked_forests_concept(base_size=9, num_layers=5, height_variability=2, seed=101)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
