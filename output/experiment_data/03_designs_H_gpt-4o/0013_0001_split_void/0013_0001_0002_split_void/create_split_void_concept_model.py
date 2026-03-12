# Created for 0013_0001_split_void.json

""" Summary:
The provided function, `create_split_void_concept_model`, generates an architectural concept model based on the "Split void" metaphor by creating a structure that features a prominent central void. This void divides the building into two distinct sections, with specific dimensions and a skewed alignment to enhance visual separation. The function calculates the geometry for both sides of the void, emphasizing contrasting materials and forms, and incorporates a roof element that extends over the void. By manipulating dimensions and angles, the model illustrates dynamic interactions with light and shadow, embodying the metaphor's themes of duality and spatial flow."""

#! python 3
function_code = """def create_split_void_concept_model(length=25.0, width=15.0, height=12.0, void_width=4.0, skew_angle=15.0):
    \"""
    Creates an architectural Concept Model embodying the 'Split void' metaphor. This model features a central void
    that divides the building into two distinct parts, with a skewed alignment to emphasize the separation and
    interaction with light and shadow.

    Parameters:
    - length (float): The total length of the building in meters.
    - width (float): The total width of the building in meters.
    - height (float): The height of the building in meters.
    - void_width (float): The width of the central void in meters.
    - skew_angle (float): The angle in degrees to skew the building sections relative to each other.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of 3D Brep geometries representing the architectural concept model.
    \"""
    import Rhino.Geometry as rg
    import math

    # Initialize the list to hold the geometry
    brep_list = []

    # Calculate skew translation based on skew angle
    skew_radians = math.radians(skew_angle)
    skew_distance = width / 2 * math.tan(skew_radians)

    # Create the left section solid
    left_corners = [
        rg.Point3d(0, 0, 0),
        rg.Point3d((width - void_width) / 2, 0, 0),
        rg.Point3d((width - void_width) / 2, length, 0),
        rg.Point3d(0, length, 0),
        rg.Point3d(0, 0, height),
        rg.Point3d((width - void_width) / 2, 0, height),
        rg.Point3d((width - void_width) / 2, length, height),
        rg.Point3d(0, length, height)
    ]
    left_brep = rg.Brep.CreateFromBox(left_corners)
    brep_list.append(left_brep)

    # Create the right section solid, skewed relative to the left
    right_corners = [
        rg.Point3d((width + void_width) / 2 + skew_distance, 0, 0),
        rg.Point3d(width + skew_distance, 0, 0),
        rg.Point3d(width + skew_distance, length, 0),
        rg.Point3d((width + void_width) / 2 + skew_distance, length, 0),
        rg.Point3d((width + void_width) / 2 + skew_distance, 0, height),
        rg.Point3d(width + skew_distance, 0, height),
        rg.Point3d(width + skew_distance, length, height),
        rg.Point3d((width + void_width) / 2 + skew_distance, length, height)
    ]
    right_brep = rg.Brep.CreateFromBox(right_corners)
    brep_list.append(right_brep)

    # Add a roof element over the void
    roof_corners = [
        rg.Point3d((width - void_width) / 2, 0, height),
        rg.Point3d((width + void_width) / 2 + skew_distance, 0, height),
        rg.Point3d((width + void_width) / 2 + skew_distance, length, height),
        rg.Point3d((width - void_width) / 2, length, height)
    ]
    roof_surface = rg.NurbsSurface.CreateFromCorners(*roof_corners)
    brep_list.append(roof_surface.ToBrep())

    return brep_list"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_split_void_concept_model(length=30.0, width=20.0, height=10.0, void_width=5.0, skew_angle=20.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_split_void_concept_model(length=40.0, width=25.0, height=15.0, void_width=6.0, skew_angle=10.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_split_void_concept_model(length=35.0, width=18.0, height=14.0, void_width=3.0, skew_angle=25.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_split_void_concept_model(length=28.0, width=22.0, height=16.0, void_width=4.5, skew_angle=30.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_split_void_concept_model(length=32.0, width=19.0, height=13.0, void_width=5.5, skew_angle=18.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
