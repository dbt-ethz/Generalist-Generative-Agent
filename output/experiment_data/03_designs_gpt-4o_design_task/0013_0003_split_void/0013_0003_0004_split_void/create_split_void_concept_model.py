# Created for 0013_0003_split_void.json

""" Summary:
The provided function, `create_split_void_concept_model`, generates an architectural concept model that embodies the 'Split void' metaphor. It constructs a building form with a central void that acts as a spatial organizer, reflecting the metaphor's emphasis on separation and duality. The function takes parameters like base dimensions and void characteristics to create a solid base and a diagonal void that visually and spatially divides the structure. This void enhances light and shadow dynamics while fostering varied user interactions. By allowing for distinct zones and pathways, the model exemplifies how the void catalyzes functional and experiential transformation within the design."""

#! python 3
function_code = """def create_split_void_concept_model(base_length, base_width, height, void_angle, void_width):
    \"""
    Creates an architectural Concept Model exemplifying the 'Split void' metaphor.
    
    Parameters:
    - base_length: float, the length of the building base in meters.
    - base_width: float, the width of the building base in meters.
    - height: float, the overall height of the building in meters.
    - void_angle: float, the angle of the void in degrees from the horizontal plane.
    - void_width: float, the width of the void in meters.
    
    Returns:
    - List of RhinoCommon Brep objects representing the building form with the central void.
    \"""
    import Rhino.Geometry as rg
    import math

    # Convert angle to radians
    void_angle_rad = math.radians(void_angle)
    
    # Create base solid
    base_corners = [
        rg.Point3d(0, 0, 0),
        rg.Point3d(base_length, 0, 0),
        rg.Point3d(base_length, base_width, 0),
        rg.Point3d(0, base_width, 0)
    ]
    base_profile = rg.Polyline(base_corners + [base_corners[0]])
    base_brep = rg.Brep.CreateFromBox(rg.Box(rg.Plane.WorldXY, rg.Interval(0, base_length), rg.Interval(0, base_width), rg.Interval(0, height)))

    # Create the void volume
    void_start_point = rg.Point3d(void_width / 2, 0, 0)
    void_end_point = rg.Point3d(base_length - void_width / 2, base_width, height)
    void_line = rg.Line(void_start_point, void_end_point)

    # Create the void as a diagonal plane
    void_plane_normal = rg.Vector3d(math.cos(void_angle_rad), math.sin(void_angle_rad), 0)
    void_plane = rg.Plane(void_start_point, void_plane_normal)

    # Extend the void into a solid
    void_corners = [
        rg.Point3d(void_start_point.X + void_width / 2, 0, 0),
        rg.Point3d(void_end_point.X - void_width / 2, base_width, 0),
        rg.Point3d(void_end_point.X - void_width / 2, base_width, height),
        rg.Point3d(void_start_point.X + void_width / 2, 0, height)
    ]
    void_profile = rg.Polyline(void_corners + [void_corners[0]])
    void_brep = rg.Brep.CreateFromBox(rg.Box(rg.Plane.WorldXY, rg.Interval(void_corners[0].X, void_corners[1].X), rg.Interval(void_corners[0].Y, void_corners[1].Y), rg.Interval(void_corners[0].Z, void_corners[2].Z)))

    # Subtract the void from the base solid
    split_breps = rg.Brep.CreateBooleanDifference(base_brep, void_brep, 0.01)
    
    return split_breps if split_breps else [base_brep]"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_split_void_concept_model(10.0, 5.0, 15.0, 30.0, 2.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_split_void_concept_model(12.0, 6.0, 20.0, 45.0, 3.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_split_void_concept_model(8.0, 4.0, 10.0, 60.0, 1.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_split_void_concept_model(15.0, 7.0, 25.0, 75.0, 2.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_split_void_concept_model(14.0, 8.0, 18.0, 50.0, 4.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
