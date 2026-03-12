# Created for 0013_0001_split_void.json

""" Summary:
The provided function generates an architectural concept model based on the "Split void" metaphor by creating a structure with a central void that divides the building into two distinct sections. It defines parameters for the building's dimensions and incorporates sloped roofs to enhance the visual separation. The function constructs left and right solid parts of the building, along with the void, using geometric points to define their shapes. This design emphasizes duality through contrasting materials or forms, facilitating dynamic interactions with light and shadow. The result is a model that visually embodies the metaphor's principles, fostering movement and spatial connections."""

#! python 3
function_code = """def create_split_void_concept_model(length=25.0, width=15.0, height=12.0, void_height=8.0, roof_slope=15.0):
    \"""
    Creates an architectural Concept Model embodying the 'Split void' metaphor. This model features a central void that 
    divides the building into two distinct parts, with sloped roofs enhancing the separation and interaction with light.

    Parameters:
    - length (float): The total length of the building in meters.
    - width (float): The total width of the building in meters.
    - height (float): The height of the building in meters.
    - void_height (float): The height of the central void in meters.
    - roof_slope (float): The angle of the roof slope in degrees.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of 3D Brep geometries representing the architectural concept model.
    \"""
    import Rhino.Geometry as rg
    import math

    # Calculate the positions for the two halves and the central void
    half_width = width / 2
    void_x = length / 2

    # Create the left and right solid parts of the building
    left_points = [
        rg.Point3d(0, 0, 0),
        rg.Point3d(void_x, 0, 0),
        rg.Point3d(void_x, half_width, 0),
        rg.Point3d(0, half_width, 0),
        rg.Point3d(0, 0, height),
        rg.Point3d(void_x, 0, height - void_height),
        rg.Point3d(void_x, half_width, height - void_height),
        rg.Point3d(0, half_width, height)
    ]
    left_brep = rg.Brep.CreateFromBox(left_points)

    right_points = [
        rg.Point3d(void_x, 0, 0),
        rg.Point3d(length, 0, 0),
        rg.Point3d(length, half_width, 0),
        rg.Point3d(void_x, half_width, 0),
        rg.Point3d(void_x, 0, height - void_height),
        rg.Point3d(length, 0, height),
        rg.Point3d(length, half_width, height),
        rg.Point3d(void_x, half_width, height - void_height)
    ]
    right_brep = rg.Brep.CreateFromBox(right_points)

    # Create the central void
    void_corners = [
        rg.Point3d(void_x, 0, 0),
        rg.Point3d(void_x + 1, 0, 0),
        rg.Point3d(void_x + 1, half_width, 0),
        rg.Point3d(void_x, half_width, 0),
        rg.Point3d(void_x, 0, void_height),
        rg.Point3d(void_x + 1, 0, void_height),
        rg.Point3d(void_x + 1, half_width, void_height),
        rg.Point3d(void_x, half_width, void_height)
    ]
    void_brep = rg.Brep.CreateFromBox(void_corners)

    # Create sloped roofs over each section
    slope_radians = math.radians(roof_slope)
    roof_left_points = [
        rg.Point3d(0, 0, height),
        rg.Point3d(void_x, 0, height - void_height),
        rg.Point3d(void_x, half_width, height - void_height),
        rg.Point3d(0, half_width, height)
    ]
    roof_left = rg.NurbsSurface.CreateFromCorners(*roof_left_points)
    
    roof_right_points = [
        rg.Point3d(void_x, 0, height - void_height),
        rg.Point3d(length, 0, height),
        rg.Point3d(length, half_width, height),
        rg.Point3d(void_x, half_width, height - void_height)
    ]
    roof_right = rg.NurbsSurface.CreateFromCorners(*roof_right_points)
    
    # Return the list of geometries
    return [left_brep, right_brep, void_brep, roof_left.ToBrep(), roof_right.ToBrep()]"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_split_void_concept_model(length=30.0, width=20.0, height=15.0, void_height=10.0, roof_slope=20.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_split_void_concept_model(length=40.0, width=25.0, height=18.0, void_height=9.0, roof_slope=25.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_split_void_concept_model(length=35.0, width=18.0, height=14.0, void_height=7.0, roof_slope=30.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_split_void_concept_model(length=28.0, width=22.0, height=16.0, void_height=11.0, roof_slope=18.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_split_void_concept_model(length=32.0, width=19.0, height=17.0, void_height=6.0, roof_slope=22.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
