# Created for 0013_0001_split_void.json

""" Summary:
The function `create_split_void_concept` generates an architectural concept model based on the 'Split void' metaphor by creating a structure divided by a central void. This void serves as a key spatial element, bifurcating the building into two distinct sections. The function calculates the geometry of each section, allowing for contrasting materials or forms to enhance the division. Additionally, it incorporates a roof element over the void, emphasizing the separation while facilitating light flow and interaction with the space. The resulting 3D Brep geometries reflect the metaphor's themes of duality, movement, and dynamic spatial experience."""

#! python 3
function_code = """def create_split_void_concept(length=30.0, width=20.0, height=10.0, void_width=5.0):
    \"""
    Creates an architectural Concept Model embodying the 'Split void' metaphor. This model features a central void that divides the building into two distinct parts.

    Parameters:
    - length (float): The total length of the building in meters.
    - width (float): The total width of the building in meters.
    - height (float): The height of the building in meters.
    - void_width (float): The width of the central void in meters.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of 3D Brep geometries representing the architectural concept model.
    \"""
    import Rhino.Geometry as rg

    # Initialize the list to hold the geometry
    brep_list = []

    # Calculate coordinates for the left and right sections
    left_section_x1 = 0
    left_section_x2 = (width - void_width) / 2
    right_section_x1 = left_section_x2 + void_width
    right_section_x2 = width

    # Create the left section solid
    left_corners = [
        rg.Point3d(left_section_x1, 0, 0),
        rg.Point3d(left_section_x2, 0, 0),
        rg.Point3d(left_section_x2, length, 0),
        rg.Point3d(left_section_x1, length, 0),
        rg.Point3d(left_section_x1, 0, height),
        rg.Point3d(left_section_x2, 0, height),
        rg.Point3d(left_section_x2, length, height),
        rg.Point3d(left_section_x1, length, height)
    ]
    left_brep = rg.Brep.CreateFromBox(left_corners)
    brep_list.append(left_brep)

    # Create the right section solid
    right_corners = [
        rg.Point3d(right_section_x1, 0, 0),
        rg.Point3d(right_section_x2, 0, 0),
        rg.Point3d(right_section_x2, length, 0),
        rg.Point3d(right_section_x1, length, 0),
        rg.Point3d(right_section_x1, 0, height),
        rg.Point3d(right_section_x2, 0, height),
        rg.Point3d(right_section_x2, length, height),
        rg.Point3d(right_section_x1, length, height)
    ]
    right_brep = rg.Brep.CreateFromBox(right_corners)
    brep_list.append(right_brep)

    # Add a roof element over the void
    roof_corners = [
        rg.Point3d(left_section_x2, 0, height),
        rg.Point3d(right_section_x1, 0, height),
        rg.Point3d(right_section_x1, length, height),
        rg.Point3d(left_section_x2, length, height)
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
    geometry = create_split_void_concept(length=40.0, width=25.0, height=15.0, void_width=6.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_split_void_concept(length=35.0, width=22.0, height=12.0, void_width=7.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_split_void_concept(length=50.0, width=30.0, height=20.0, void_width=8.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_split_void_concept(length=45.0, width=28.0, height=18.0, void_width=4.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_split_void_concept(length=32.0, width=18.0, height=14.0, void_width=5.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
