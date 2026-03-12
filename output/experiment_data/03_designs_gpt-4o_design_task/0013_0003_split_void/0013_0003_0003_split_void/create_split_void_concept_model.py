# Created for 0013_0003_split_void.json

""" Summary:
The provided function generates an architectural concept model based on the 'Split void' metaphor by creating a solid base structure and introducing a central void that divides it. The parameters allow for customization of the building's dimensions and the void's characteristics, such as its angle and width. By utilizing RhinoCommon in Grasshopper, the function constructs a 3D Brep representation of the building, where the void acts as a spatial organizer, fostering distinct zones and promoting interaction through varied light and movement. This approach results in a model that reflects the metaphor's transformative qualities and enhances the architectural composition."""

#! python 3
function_code = """def create_split_void_concept_model(base_length, base_width, base_height, void_angle, void_width, seed=42):
    \"""
    Creates a 3D architectural Concept Model based on the 'Split void' metaphor using RhinoCommon in Grasshopper.
    
    Parameters:
    - base_length (float): The length of the building base in meters.
    - base_width (float): The width of the building base in meters.
    - base_height (float): The height of the building in meters.
    - void_angle (float): The angle in degrees at which the void diagonally cuts through the structure.
    - void_width (float): The width of the void in meters.
    - seed (int): An optional seed for randomness to ensure replicability. Defaults to 42.
    
    Returns:
    - List[Rhino.Geometry.Brep]: A list of 3D Brep geometries representing the building's solid and void spaces.
    \"""
    import Rhino
    import System
    from Rhino.Geometry import Point3d, Plane, Vector3d, Box, Brep, Interval
    import random

    random.seed(seed)

    # Create the base solid mass
    base_corners = [
        Point3d(0, 0, 0),
        Point3d(base_length, 0, 0),
        Point3d(base_length, base_width, 0),
        Point3d(0, base_width, 0),
        Point3d(0, 0, base_height),
        Point3d(base_length, 0, base_height),
        Point3d(base_length, base_width, base_height),
        Point3d(0, base_width, base_height)
    ]
    base_box = Box(Plane.WorldXY, Interval(0, base_length), Interval(0, base_width), Interval(0, base_height))
    base_brep = base_box.ToBrep()

    # Create the void
    void_origin = Point3d(base_length / 2, base_width / 2, 0)
    void_direction = Vector3d(
        System.Math.Cos(System.Math.PI * void_angle / 180),
        System.Math.Sin(System.Math.PI * void_angle / 180),
        0
    )
    void_plane = Plane(void_origin, void_direction)
    void_box = Box(void_plane, Interval(-void_width / 2, void_width / 2), Interval(-base_width / 2, base_width / 2), Interval(0, base_height))
    void_brep = void_box.ToBrep()

    # Split the base brep with the void brep
    split_breps = Brep.CreateBooleanDifference(base_brep, void_brep, 0.01)

    # Return the resulting geometries
    return split_breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_split_void_concept_model(10.0, 5.0, 8.0, 45.0, 2.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_split_void_concept_model(15.0, 10.0, 12.0, 30.0, 3.0, seed=100)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_split_void_concept_model(20.0, 10.0, 15.0, 60.0, 4.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_split_void_concept_model(12.0, 6.0, 10.0, 75.0, 1.5, seed=24)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_split_void_concept_model(25.0, 15.0, 20.0, 90.0, 5.0, seed=50)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
