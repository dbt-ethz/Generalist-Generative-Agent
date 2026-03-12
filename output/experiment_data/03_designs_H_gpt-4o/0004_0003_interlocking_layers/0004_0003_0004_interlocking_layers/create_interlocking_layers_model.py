# Created for 0004_0003_interlocking_layers.json

""" Summary:
The function `create_interlocking_layers_model` generates an architectural concept model embodying the "Interlocking Layers" metaphor by creating a series of dynamically overlapping volumes. It takes parameters for base dimensions, number of layers, thickness, and height variation to define the structure's form. Each layer is created as a rectangle, extruded, and then slightly rotated and translated to emphasize interconnection and complexity. This approach captures the essence of layered design, allowing for both unity and distinct functional areas, while also enabling the creation of transitional spaces that foster interaction. The result is a visually intricate and spatially engaging model."""

#! python 3
function_code = """def create_interlocking_layers_model(base_length, base_width, num_layers, layer_thickness, height_variation):
    \"""
    Generates an architectural Concept Model based on the 'Interlocking Layers' metaphor.

    This function creates a series of interwoven volumes where each layer is slightly rotated and displaced
    to emphasize the dynamic interaction between them. Varying heights and thicknesses introduce complexity
    and depth, highlighting both unity and distinction within the design.

    Parameters:
    - base_length (float): The overall length of the base layer in meters.
    - base_width (float): The overall width of the base layer in meters.
    - num_layers (int): The number of interlocking layers to create.
    - layer_thickness (float): The base thickness of each layer in meters.
    - height_variation (float): Maximum variation in height for each layer in meters.

    Returns:
    - List of Rhino.Geometry.Brep objects representing the interlocking layers.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    # Set seed for reproducibility
    random.seed(42)

    # Store the resulting geometries
    breps = []

    # Base plane
    base_plane = rg.Plane.WorldXY

    for i in range(num_layers):
        # Calculate the position and dimensions of the current layer
        current_length = base_length * random.uniform(0.8, 1.2)
        current_width = base_width * random.uniform(0.8, 1.2)
        current_thickness = layer_thickness + random.uniform(-height_variation, height_variation)

        # Create a base rectangle for the layer
        base_rect = rg.Rectangle3d(base_plane, current_length, current_width)

        # Extrude the rectangle to create a layer volume
        extrusion_vector = rg.Vector3d(0, 0, current_thickness)
        layer_brep = rg.Brep.CreateFromBox([
            base_rect.Corner(0), base_rect.Corner(1), 
            base_rect.Corner(2), base_rect.Corner(3),
            base_rect.Corner(0) + extrusion_vector, base_rect.Corner(1) + extrusion_vector,
            base_rect.Corner(2) + extrusion_vector, base_rect.Corner(3) + extrusion_vector
        ])

        # Rotate and translate the layer to create interlocking effect
        rotation_angle = random.uniform(-10, 10)  # Rotation in degrees
        rotation_axis = rg.Vector3d(0, 0, 1)  # Rotate around Z-axis
        rotation_center = rg.Point3d(current_length / 2, current_width / 2, i * layer_thickness)

        # Apply rotation
        rotation_transform = rg.Transform.Rotation(math.radians(rotation_angle), rotation_axis, rotation_center)
        layer_brep.Transform(rotation_transform)

        # Translate to introduce layering effect
        translation_vector = rg.Vector3d(random.uniform(-1, 1), random.uniform(-1, 1), i * layer_thickness)
        translation_transform = rg.Transform.Translation(translation_vector)
        layer_brep.Transform(translation_transform)

        # Append the transformed layer to the breps list
        if layer_brep:
            breps.append(layer_brep)

    return breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_interlocking_layers_model(10.0, 5.0, 6, 0.5, 0.2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_interlocking_layers_model(15.0, 7.0, 4, 0.3, 0.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_interlocking_layers_model(12.0, 6.0, 8, 0.4, 0.3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_interlocking_layers_model(20.0, 10.0, 5, 0.6, 0.1)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_interlocking_layers_model(8.0, 4.0, 10, 0.2, 0.4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
