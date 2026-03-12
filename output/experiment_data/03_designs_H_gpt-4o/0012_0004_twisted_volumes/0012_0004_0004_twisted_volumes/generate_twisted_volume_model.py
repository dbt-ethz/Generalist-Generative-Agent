# Created for 0012_0004_twisted_volumes.json

""" Summary:
The provided function generates an architectural concept model that embodies the "Twisted volumes" metaphor by creating a series of layered, intersecting volumes. The function utilizes parameters such as length, width, height, number of layers, twist factor, and cutout ratio to define the geometry. Each layer is twisted using a rotation transformation, resulting in dynamic forms that convey a sense of motion and balance. Cutouts are incorporated to enhance transparency and facilitate light interaction, allowing for varied light patterns and spatial experiences. This process ultimately transforms the relationship between form, space, and light within the architectural model."""

#! python 3
function_code = """def generate_twisted_volume_model(length, width, height, num_layers, twist_factor, cutout_ratio):
    \"""
    Generates an architectural Concept Model using the 'Twisted volumes' metaphor.
    This function constructs a composition of layered and intersecting volumes with twists,
    emphasizing dynamic balance and interaction of light and shadow.

    Parameters:
    - length (float): The length of each volume in meters.
    - width (float): The width of each volume in meters.
    - height (float): The height of each volume in meters.
    - num_layers (int): The number of layered volumes to create.
    - twist_factor (float): The factor determining the degree of twist for each layer.
    - cutout_ratio (float): The ratio of cutout areas to add transparency (0 to 1).

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Breps representing the twisted volumes.
    \"""
    import Rhino
    import Rhino.Geometry as rg
    import random
    import math

    # Seed the random number generator for reproducibility
    random.seed(42)

    breps = []

    # Define base plane
    base_plane = rg.Plane.WorldXY

    # Loop to create each twisted volume layer
    for i in range(num_layers):
        # Define base rectangle
        base_rect = rg.Rectangle3d(base_plane, length, width)

        # Define twist transformation
        angle_rad = twist_factor * math.pi / 180
        twist_transform = rg.Transform.Rotation(angle_rad * i, rg.Vector3d.ZAxis, base_rect.Center)

        # Create and transform the volume
        extrude_vector = rg.Vector3d(0, 0, height)
        brep = rg.Brep.CreateFromSurface(rg.Surface.CreateExtrusion(base_rect.ToNurbsCurve(), extrude_vector))
        brep.Transform(twist_transform)

        # Apply cutouts if specified
        if cutout_ratio > 0:
            cutout_length = length * cutout_ratio
            cutout_width = width * cutout_ratio
            cutout_rect = rg.Rectangle3d(base_plane, cutout_length, cutout_width)
            cutout_brep = rg.Brep.CreateFromSurface(rg.Surface.CreateExtrusion(cutout_rect.ToNurbsCurve(), extrude_vector))
            boolean_diff = rg.Brep.CreateBooleanDifference(brep, cutout_brep, 0.01)
            if boolean_diff:
                brep = boolean_diff[0]

        # Append the resulting brep
        breps.append(brep)

        # Move the base plane for the next layer
        base_plane.OriginZ += height * 0.8

    return breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = generate_twisted_volume_model(10, 5, 3, 8, 15, 0.2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = generate_twisted_volume_model(12, 6, 4, 10, 30, 0.3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = generate_twisted_volume_model(8, 4, 2, 6, 20, 0.1)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = generate_twisted_volume_model(15, 7, 5, 12, 25, 0.15)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = generate_twisted_volume_model(14, 7, 6, 5, 10, 0.25)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
