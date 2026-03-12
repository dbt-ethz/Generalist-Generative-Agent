# Created for 0004_0002_interlocking_layers.json

""" Summary:
The provided function generates an architectural concept model based on the 'Interlocking Layers' metaphor by constructing overlapping planes or volumes. It systematically creates multiple layers, each with random offsets and rotations to enhance their interlocking nature. The parameters allow control over the base dimensions, number of layers, layer thickness, and maximum offsets, which collectively influence the model's spatial hierarchy and connectivity. By employing transparent and opaque materials, the function emphasizes depth and interaction among layers, facilitating both open vistas and secluded areas. This results in a visually complex structure that embodies the metaphor's dynamic spatial relationships."""

#! python 3
function_code = """def create_interlocking_layers_model(base_dimensions, num_layers, max_offset, layer_thickness):
    \"""
    Creates an architectural Concept Model based on the 'Interlocking Layers' metaphor.

    This function constructs a composition of overlapping and interwoven layers by arranging multiple planes
    that intersect and interlock with each other. The layers are organized to emphasize spatial hierarchy and
    varying levels of connectivity, creating a complex structure with both open and secluded spaces.

    Parameters:
    - base_dimensions: Tuple[float, float] representing the base width and depth of the model in meters.
    - num_layers: Integer indicating the number of interlocking layers to create.
    - max_offset: Float representing the maximum offset for each layer in meters to achieve interlocking.
    - layer_thickness: Float representing the thickness of each layer in meters.

    Returns:
    - List of Rhino.Geometry.Brep objects representing the interlocking layers.
    \"""
    import Rhino.Geometry as rg
    import random

    # Set a seed for reproducibility
    random.seed(42)

    width, depth = base_dimensions
    layers = []

    for i in range(num_layers):
        # Random offsets and rotations for interlocking effect
        offset_x = random.uniform(-max_offset, max_offset)
        offset_y = random.uniform(-max_offset, max_offset)
        rotation_angle = random.uniform(-15, 15)  # Degrees

        # Create a base rectangle for the layer
        rect_corners = [
            rg.Point3d(0, 0, i * layer_thickness),
            rg.Point3d(width, 0, i * layer_thickness),
            rg.Point3d(width, depth, i * layer_thickness),
            rg.Point3d(0, depth, i * layer_thickness),
            rg.Point3d(0, 0, i * layer_thickness)  # Closing the polyline
        ]

        # Create a planar surface for this layer
        polyline = rg.Polyline(rect_corners)
        curve = polyline.ToNurbsCurve()
        layer_surface = rg.Brep.CreateEdgeSurface([curve])

        if layer_surface is None:
            continue

        # Apply offset transformation
        translation = rg.Transform.Translation(offset_x, offset_y, 0)
        layer_surface.Transform(translation)

        # Apply rotation transformation
        center_point = rg.Point3d(width / 2, depth / 2, i * layer_thickness)
        rotation = rg.Transform.Rotation(rg.RhinoMath.ToRadians(rotation_angle), rg.Vector3d.ZAxis, center_point)
        layer_surface.Transform(rotation)

        # Extrude the surface to create thickness
        extrusion_vector = rg.Vector3d(0, 0, layer_thickness)
        extruded_layer = rg.Brep.CreateFromSurface(layer_surface.Surfaces[0])
        extruded_layer = rg.Brep.CreateFromOffsetFace(extruded_layer.Faces[0], extrusion_vector, 0.01, True, True)

        layers.append(extruded_layer)

    return layers"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_interlocking_layers_model((10, 5), 5, 2, 0.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_interlocking_layers_model((15, 10), 7, 3, 0.75)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_interlocking_layers_model((8, 4), 6, 1.5, 0.3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_interlocking_layers_model((12, 8), 4, 2.5, 0.6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_interlocking_layers_model((20, 15), 10, 5, 1)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
