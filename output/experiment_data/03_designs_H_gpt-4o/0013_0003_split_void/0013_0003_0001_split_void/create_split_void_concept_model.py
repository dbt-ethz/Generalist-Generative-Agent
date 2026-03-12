# Created for 0013_0003_split_void.json

""" Summary:
The function `create_split_void_concept_model` generates an architectural concept model based on the 'Split void' metaphor by creating a central void that divides the structure. This void influences spatial organization, facilitating distinct zones and enhancing movement and interaction. The model employs a diagonal cut, enriching spatial dynamics and user circulation while allowing light and shadow interplay. The parameters define the building's dimensions and the void's characteristics, ensuring the design reflects the duality and contrast inherent in the metaphor. Ultimately, the output is a collection of geometries that embody the transformative qualities of the central void in architectural form."""

#! python 3
function_code = """def create_split_void_concept_model(base_length, base_width, base_height, void_angle, void_width, void_depth):
    \"""
    Creates a conceptual architectural model that embodies the 'Split void' metaphor.

    This model features a central void that splits the structure, influencing spatial organization and
    creating distinct zones with varying functional or experiential purposes. The void is non-linear
    and diagonal to enhance spatial dynamics and user circulation.

    Parameters:
    - base_length (float): The length of the base form in meters.
    - base_width (float): The width of the base form in meters.
    - base_height (float): The height of the building form in meters.
    - void_angle (float): The angle in degrees at which the void cuts through the structure.
    - void_width (float): The width of the void in meters.
    - void_depth (float): The depth or thickness of the void in meters.

    Returns:
    - List of Rhino.Geometry.Brep: A list of Brep geometries representing the architectural model.
    \"""
    import Rhino.Geometry as rg
    import math

    # Create base geometry: a rectangular prism
    base_box = rg.Box(rg.Plane.WorldXY, rg.Interval(0, base_length), rg.Interval(0, base_width), rg.Interval(0, base_height)).ToBrep()

    # Define the void cut plane based on the angle
    void_plane_origin = rg.Point3d(base_length / 2, base_width / 2, 0)
    void_plane_normal = rg.Vector3d(math.cos(math.radians(void_angle)), math.sin(math.radians(void_angle)), 0)
    void_plane = rg.Plane(void_plane_origin, void_plane_normal)

    # Create the void shape (a diagonal cut)
    void_corners = [
        rg.Point3d(-void_width / 2, 0, 0),
        rg.Point3d(void_width / 2, 0, 0),
        rg.Point3d(void_width / 2, base_width, 0),
        rg.Point3d(-void_width / 2, base_width, 0),
        rg.Point3d(-void_width / 2, 0, base_height),
        rg.Point3d(void_width / 2, 0, base_height),
        rg.Point3d(void_width / 2, base_width, base_height),
        rg.Point3d(-void_width / 2, base_width, base_height)
    ]
    void_brep_lower = rg.Brep.CreateFromCornerPoints(void_corners[0], void_corners[1], void_corners[5], void_corners[4], 0.01)
    void_brep_upper = rg.Brep.CreateFromCornerPoints(void_corners[2], void_corners[3], void_corners[7], void_corners[6], 0.01)

    void_brep = rg.Brep.JoinBreps([void_brep_lower, void_brep_upper], 0.01)
    if void_brep:
        void_brep = void_brep[0]

    # Transform the void brep to the proper plane
    transformation = rg.Transform.PlaneToPlane(rg.Plane.WorldXY, void_plane)
    void_brep.Transform(transformation)

    # Cut the base geometry with the void shape
    split_breps = rg.Brep.CreateBooleanDifference([base_box], [void_brep], 0.01)

    # Return the resulting split geometries
    return split_breps if split_breps else [base_box]"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_split_void_concept_model(10, 5, 8, 45, 2, 3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_split_void_concept_model(15, 7, 10, 30, 4, 5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_split_void_concept_model(12, 6, 9, 60, 3, 4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_split_void_concept_model(20, 10, 12, 75, 5, 6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_split_void_concept_model(18, 9, 11, 50, 3, 2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
