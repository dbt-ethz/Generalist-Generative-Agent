# Created for 0012_0001_twisted_volumes.json

""" Summary:
The function `create_twisted_volumes_model` generates an architectural concept model inspired by the metaphor of "Twisted volumes." It creates a series of interlocking geometric forms by manipulating layers that twist around a central axis, embodying a sense of dynamic movement. By varying the twist angle and the number of layers, the function explores innovative spatial relationships and circulation paths. The design emphasizes the interplay of light and shadow, with surfaces capturing and reflecting light based on their orientation. Ultimately, the model visually communicates the energy and transformation inherent in the twisting action, aligning with the metaphor's essence."""

#! python 3
function_code = """def create_twisted_volumes_model(length, width, height, twist_angle, num_layers):
    \"""
    Generates an architectural Concept Model based on the 'Twisted volumes' metaphor.

    This function creates a series of interlocking twisted forms by manipulating layers of surfaces 
    that rotate around a central axis, embodying fluidity and dynamic movement. The model emphasizes 
    innovative spatial relationships and the interplay of light and shadow.

    Parameters:
    - length (float): The length of the base layer in meters.
    - width (float): The width of the base layer in meters.
    - height (float): The total height of the twisted volume in meters.
    - twist_angle (float): The total twist angle from base to top in degrees.
    - num_layers (int): The number of horizontal layers to create.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep geometries representing the twisted volumes.
    \"""
    import Rhino.Geometry as rg
    import math

    # Calculate layer height
    layer_height = height / num_layers

    # Initialize list to hold breps
    breps = []

    # Create base profile as a rectangle
    base_plane = rg.Plane.WorldXY
    base_corners = [
        rg.Point3d(-length / 2, -width / 2, 0),
        rg.Point3d(length / 2, -width / 2, 0),
        rg.Point3d(length / 2, width / 2, 0),
        rg.Point3d(-length / 2, width / 2, 0),
        rg.Point3d(-length / 2, -width / 2, 0)
    ]
    base_curve = rg.Polyline(base_corners).ToNurbsCurve()

    # Create twisted layers
    for i in range(num_layers + 1):
        # Calculate the rotation angle for the current layer
        angle = math.radians(twist_angle * (i / num_layers))

        # Transform for twisting
        twist_transform = rg.Transform.Rotation(angle, rg.Vector3d.ZAxis, rg.Point3d(0, 0, i * layer_height))

        # Duplicate and transform the base curve to create a new layer
        layer_curve = base_curve.DuplicateCurve()
        layer_curve.Transform(twist_transform)

        # Move layer to its height level
        translation = rg.Transform.Translation(0, 0, i * layer_height)
        layer_curve.Transform(translation)

        # Add curves to loft profiles
        breps.append(layer_curve)

    # Loft all layers to create the twisted volume
    loft_type = rg.LoftType.Normal
    twisted_volume = rg.Brep.CreateFromLoft(breps, rg.Point3d.Unset, rg.Point3d.Unset, loft_type, False)

    return twisted_volume"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_twisted_volumes_model(10.0, 5.0, 15.0, 180.0, 8)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_twisted_volumes_model(12.0, 6.0, 20.0, 90.0, 6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_twisted_volumes_model(8.0, 4.0, 10.0, 360.0, 10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_twisted_volumes_model(15.0, 7.0, 25.0, 270.0, 5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_twisted_volumes_model(14.0, 7.0, 22.0, 120.0, 7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
