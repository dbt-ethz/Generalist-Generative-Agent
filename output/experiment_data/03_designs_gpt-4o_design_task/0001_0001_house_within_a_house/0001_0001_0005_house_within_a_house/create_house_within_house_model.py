# Created for 0001_0001_house_within_a_house.json

""" Summary:
The function `create_house_within_house_model` generates an architectural concept model based on the "House within a house" metaphor by creating two nested volumes: an inner sanctuary and an outer shell. It defines the dimensions and transparency levels of both volumes using parameters. The inner volume, representing privacy and intimacy, is constructed as a more opaque box, while the outer volume, suggesting transition and openness, is a larger, semi-transparent box. This layering creates a visual and spatial hierarchy, illustrating the metaphor's implications of protection and retreat, and facilitating varied spatial experiences as one moves from the exterior to the interior."""

#! python 3
function_code = """def create_house_within_house_model(inner_dimensions, outer_dimensions, transparency_levels):
    \"""
    Creates an architectural Concept Model based on the 'House within a house' metaphor.
    
    Parameters:
    - inner_dimensions: A tuple of three floats (width, depth, height) defining the dimensions of the inner volume.
    - outer_dimensions: A tuple of three floats (width, depth, height) defining the dimensions of the outer volume.
    - transparency_levels: A tuple of two floats (0.0 to 1.0) defining the transparency of the outer and inner volumes respectively.
    
    Returns:
    - A list of RhinoCommon Breps representing the 3D geometries of the Concept Model.
    \"""
    import Rhino.Geometry as rg
    
    # Unpack dimensions
    inner_w, inner_d, inner_h = inner_dimensions
    outer_w, outer_d, outer_h = outer_dimensions
    
    # Create the inner sanctuary as a Brep box
    inner_box_corners = [
        rg.Point3d(0, 0, 0),
        rg.Point3d(inner_w, 0, 0),
        rg.Point3d(inner_w, inner_d, 0),
        rg.Point3d(0, inner_d, 0),
        rg.Point3d(0, 0, inner_h),
        rg.Point3d(inner_w, 0, inner_h),
        rg.Point3d(inner_w, inner_d, inner_h),
        rg.Point3d(0, inner_d, inner_h)
    ]
    inner_brep = rg.Brep.CreateFromBox(inner_box_corners)
    
    # Create the outer envelope as a Brep box
    outer_box_corners = [
        rg.Point3d(-0.5*(outer_w - inner_w), -0.5*(outer_d - inner_d), 0),
        rg.Point3d(0.5*(outer_w + inner_w), -0.5*(outer_d - inner_d), 0),
        rg.Point3d(0.5*(outer_w + inner_w), 0.5*(outer_d + inner_d), 0),
        rg.Point3d(-0.5*(outer_w - inner_w), 0.5*(outer_d + inner_d), 0),
        rg.Point3d(-0.5*(outer_w - inner_w), -0.5*(outer_d - inner_d), outer_h),
        rg.Point3d(0.5*(outer_w + inner_w), -0.5*(outer_d - inner_d), outer_h),
        rg.Point3d(0.5*(outer_w + inner_w), 0.5*(outer_d + inner_d), outer_h),
        rg.Point3d(-0.5*(outer_w - inner_w), 0.5*(outer_d + inner_d), outer_h)
    ]
    outer_brep = rg.Brep.CreateFromBox(outer_box_corners)
    
    # Assign transparency levels (as material property placeholders)
    # Note: Actual material assignment is managed in Rhino/Grasshopper interface, not in pure geometry
    
    # Return the list of breps
    return [outer_brep, inner_brep]"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_house_within_house_model((5.0, 10.0, 8.0), (10.0, 15.0, 12.0), (0.5, 0.8))
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_house_within_house_model((6.0, 12.0, 9.0), (12.0, 18.0, 15.0), (0.3, 0.7))
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_house_within_house_model((4.0, 8.0, 6.0), (9.0, 14.0, 10.0), (0.4, 0.6))
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_house_within_house_model((7.0, 14.0, 10.0), (13.0, 20.0, 16.0), (0.2, 0.9))
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_house_within_house_model((8.0, 16.0, 11.0), (15.0, 22.0, 18.0), (0.6, 0.5))
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
