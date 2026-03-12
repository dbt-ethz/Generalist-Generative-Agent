# Created for 0013_0003_split_void.json

""" Summary:
The provided function, `create_split_void_concept_model`, generates an architectural concept model based on the 'Split void' metaphor by creating a central void that divides a rectangular prism form. This void, defined by its angle and width, introduces spatial dynamics and enhances the building's composition, allowing for distinct zones that facilitate varied functions and experiences. By utilizing boolean operations to subtract the void from the base geometry, the model exemplifies the interplay of light, shadow, and movement, reflecting the transformative quality of the void and its role as a catalyst for spatial organization, ultimately reinforcing the design's identity through contrast."""

#! python 3
function_code = """def create_split_void_concept_model(length, width, height, void_angle, void_width):
    \"""
    Creates a conceptual architectural model that embodies the 'Split void' metaphor.
    
    The model features a central void that divides the building form, providing spatial organization 
    and opportunities for varied interactions with light and shadow. The void is diagonal or non-linear 
    to enrich spatial dynamics and influence the building's composition and user circulation.

    Parameters:
    - length (float): The length of the base form in meters.
    - width (float): The width of the base form in meters.
    - height (float): The height of the building form in meters.
    - void_angle (float): The angle in degrees at which the void cuts through the structure.
    - void_width (float): The width of the void in meters.

    Returns:
    - List of RhinoCommon.Geometry.Brep: A list of Brep geometries representing the architectural model.
    \"""
    import Rhino.Geometry as rg
    import math

    # Base geometry: a simple rectangular prism
    base_box = rg.Box(rg.Plane.WorldXY, rg.Interval(0, length), rg.Interval(0, width), rg.Interval(0, height)).ToBrep()

    # Define the plane for the void based on the angle
    void_plane_origin = rg.Point3d(0, width / 2, 0)
    void_plane_normal = rg.Vector3d(math.cos(math.radians(void_angle)), math.sin(math.radians(void_angle)), 0)
    void_plane = rg.Plane(void_plane_origin, void_plane_normal)

    # Create a solid box representing the void
    void_box_corners = [
        rg.Point3d(-length, -void_width / 2, 0),
        rg.Point3d(length * 2, -void_width / 2, 0),
        rg.Point3d(length * 2, void_width / 2, 0),
        rg.Point3d(-length, void_width / 2, 0),
        rg.Point3d(-length, -void_width / 2, height),
        rg.Point3d(length * 2, -void_width / 2, height),
        rg.Point3d(length * 2, void_width / 2, height),
        rg.Point3d(-length, void_width / 2, height)
    ]
    void_box_lower = rg.Brep.CreateFromCornerPoints(void_box_corners[0], void_box_corners[1], void_box_corners[2], void_box_corners[3], 0.01)
    void_box_upper = rg.Brep.CreateFromCornerPoints(void_box_corners[4], void_box_corners[5], void_box_corners[6], void_box_corners[7], 0.01)
    
    # Combine upper and lower void boxes
    void_box = rg.Brep.JoinBreps([void_box_lower, void_box_upper], 0.01)
    if void_box is not None:
        void_box = void_box[0]

    # Transform void box to the correct plane
    transformation = rg.Transform.PlaneToPlane(rg.Plane.WorldXY, void_plane)
    void_box.Transform(transformation)

    # Split the base geometry with the void
    split_brep = rg.Brep.CreateBooleanDifference([base_box], [void_box], 0.01)

    return split_brep if split_brep is not None else []"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_split_void_concept_model(10, 5, 8, 45, 2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_split_void_concept_model(15, 10, 12, 30, 3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_split_void_concept_model(20, 10, 15, 60, 4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_split_void_concept_model(12, 6, 10, 75, 1.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_split_void_concept_model(18, 9, 14, 90, 2.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
