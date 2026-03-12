# Created for 0001_0003_house_within_a_house.json

""" Summary:
The function `create_house_within_house_model` embodies the 'House within a house' metaphor by generating a dual-layered architectural concept model. It creates an outer protective volume that encapsulates a distinct inner sanctuary, reflecting the interplay between public and private spaces. The function incorporates parameters for dimensions and voids, allowing for dynamic spatial arrangements. It uses boolean operations to create voids within the inner structure, enhancing the sense of layered experiences. Vertical transitions, modeled as staircases, facilitate movement between layers, emphasizing discovery and refuge, while contrasting materials visually distinguish the outer and inner realms."""

#! python 3
function_code = """def create_house_within_house_model(outer_dimensions, inner_dimensions, void_percentage, transition_height):
    \"""
    Generates a conceptual architectural model based on the 'House within a house' metaphor.

    This function creates a dual-layered form where each layer serves a distinct function and spatial quality.
    An outer protective form encapsulates an inner sanctuary. The model emphasizes transitions and voids, 
    incorporating vertical and horizontal connections to enhance the concept of nested spaces.

    Parameters:
    - outer_dimensions: Tuple of 3 floats (length, width, height) representing the dimensions of the outer volume in meters.
    - inner_dimensions: Tuple of 3 floats (length, width, height) representing the dimensions of the inner volume in meters.
    - void_percentage: Float (0.0 to 1.0) indicating the percentage of the inner volume to be void, enhancing spatial dynamics.
    - transition_height: Float representing the height of vertical transitions like staircases or ramps.

    Returns:
    - List of RhinoCommon Brep objects representing the conceptual model's geometric entities.
    \"""
    import Rhino.Geometry as rg
    import random

    def create_box(center, dimensions):
        \"""Helper function to create a box Brep given a center point and dimensions.\"""
        length, width, height = dimensions
        corner1 = rg.Point3d(center.X - length / 2, center.Y - width / 2, center.Z - height / 2)
        corner2 = rg.Point3d(center.X + length / 2, center.Y + width / 2, center.Z + height / 2)
        box = rg.Box(rg.Plane.WorldXY, rg.Interval(corner1.X, corner2.X), rg.Interval(corner1.Y, corner2.Y), rg.Interval(corner1.Z, corner2.Z))
        return box.ToBrep()

    # Create base points for outer and inner volumes
    outer_center = rg.Point3d(0, 0, 0)
    inner_center = rg.Point3d(0, 0, 0)

    # Create outer and inner volumes
    outer_volume = create_box(outer_center, outer_dimensions)
    inner_volume = create_box(inner_center, inner_dimensions)

    # Calculate void volume dimensions based on void percentage
    void_dimensions = (
        inner_dimensions[0] * void_percentage,
        inner_dimensions[1] * void_percentage,
        inner_dimensions[2] * void_percentage
    )
    
    # Create void volume within the inner sanctuary
    void_volume = create_box(inner_center, void_dimensions)
    
    # Boolean difference to create voids in the inner volume
    inner_with_void = rg.Brep.CreateBooleanDifference([inner_volume], [void_volume], 0.01)

    # Create a staircase or ramp for vertical transition
    stair_width = inner_dimensions[0] * 0.2
    stair_length = inner_dimensions[1] * 0.3
    stair_box = rg.Box(
        rg.Plane.WorldXY,
        rg.Interval(inner_dimensions[0] / 2 - stair_width / 2, inner_dimensions[0] / 2 + stair_width / 2),
        rg.Interval(inner_dimensions[1] / 2 - stair_length / 2, inner_dimensions[1] / 2 + stair_length / 2),
        rg.Interval(0, transition_height)
    )
    stair_brep = stair_box.ToBrep()

    # Collect all geometries
    geometries = [outer_volume] + list(inner_with_void) + [stair_brep]

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_house_within_house_model((10.0, 8.0, 6.0), (6.0, 4.0, 4.0), 0.3, 2.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_house_within_house_model((12.0, 10.0, 8.0), (7.0, 5.0, 5.0), 0.25, 3.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_house_within_house_model((15.0, 12.0, 10.0), (8.0, 6.0, 6.0), 0.2, 3.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_house_within_house_model((20.0, 15.0, 10.0), (10.0, 8.0, 5.0), 0.4, 4.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_house_within_house_model((18.0, 14.0, 9.0), (9.0, 7.0, 7.0), 0.15, 3.2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
