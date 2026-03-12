# Created for 0013_0003_split_void.json

""" Summary:
The function `create_split_void_concept_model` generates an architectural concept model that embodies the 'Split void' metaphor by creating a 3D structure featuring a central non-linear void. This void serves as an organizing element, facilitating spatial division and interaction between distinct functional zones. Parameters such as void angle, width, and offset allow for varied expressions of the void, enhancing visual connections and the interplay of light and shadow. The resulting model showcases asymmetry and dynamic spatial layering, effectively illustrating the transformative quality of the void in shaping the building's identity and user experience."""

#! python 3
function_code = """def create_split_void_concept_model(length, width, height, void_angle, void_width, void_offset):
    \"""
    Creates an architectural Concept Model that exemplifies the 'Split void' metaphor.

    This function generates a 3D model with a central void that acts as a spatial organizer, dividing the structure
    and creating distinct zones. The void is non-linear, enhancing the spatial dynamics and promoting interaction
    through visual connections and light play. The model explores the transformative quality of the void.

    Parameters:
    - length (float): The length of the base form in meters.
    - width (float): The width of the base form in meters.
    - height (float): The height of the building form in meters.
    - void_angle (float): The angle in degrees at which the void cuts through the structure.
    - void_width (float): The width of the void in meters.
    - void_offset (float): The offset of the void from the centerline in meters.

    Returns:
    - List of RhinoCommon.Geometry.Brep: A list of Brep geometries representing the architectural model.
    \"""
    import Rhino.Geometry as rg
    import math

    # Create the base geometry: a rectangular prism
    base_box = rg.Box(rg.Plane.WorldXY, rg.Interval(0, length), rg.Interval(0, width), rg.Interval(0, height)).ToBrep()

    # Define the void plane with an offset
    void_origin = rg.Point3d(length / 2 + void_offset, width / 2, 0)
    void_direction = rg.Vector3d(math.cos(math.radians(void_angle)), math.sin(math.radians(void_angle)), 0)
    void_plane = rg.Plane(void_origin, void_direction)

    # Create a non-linear void shape
    void_curve = rg.NurbsCurve.Create(False, 3, [
        rg.Point3d(-length, -void_width / 2, 0),
        rg.Point3d(0, void_width / 2, height / 3),
        rg.Point3d(length / 2, -void_width / 2, 2 * height / 3),
        rg.Point3d(length, void_width / 2, height)
    ])

    # Extrude the void curve to form a surface
    void_surface = rg.Brep.CreateFromSurface(rg.Surface.CreateExtrusion(void_curve, rg.Vector3d(0, 0, height)))

    # Split the base geometry with the void surface
    split_breps = rg.Brep.CreateBooleanDifference([base_box], [void_surface], 0.01)

    return split_breps if split_breps else [base_box]"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_split_void_concept_model(10.0, 5.0, 15.0, 30.0, 2.0, 1.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_split_void_concept_model(12.0, 8.0, 20.0, 45.0, 3.0, 0.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_split_void_concept_model(15.0, 10.0, 25.0, 60.0, 4.0, 2.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_split_void_concept_model(8.0, 4.0, 12.0, 75.0, 1.5, 0.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_split_void_concept_model(14.0, 6.0, 18.0, 90.0, 2.5, 1.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
