# Created for 0009_0001_cantilevering_corners.json

""" Summary:
The provided function, `create_cantilevering_corners`, generates an architectural concept model based on the metaphor of "cantilevering corners." It constructs a multi-level structure where each level projects outward, creating dramatic overhangs that embody a balance of stability and motion. The function takes parameters for base dimensions, height, and overhang depth, iteratively defining corners for each level. By alternating the direction of the cantilever for each level, it produces a dynamic visual effect. The resulting 3D geometric representations are compiled into a list, effectively translating the metaphor into a tangible architectural form while exploring gravity-defying design principles."""

#! python 3
function_code = """def create_cantilevering_corners(base_length, base_height, overhang_depth, num_levels):
    \"""
    Creates a conceptual architectural model featuring cantilevering corners, emphasizing dynamic interaction
    between stability and motion. The design consists of a base with multiple levels, each projecting outward
    to form dramatic overhangs.

    Parameters:
    - base_length (float): The length of the base structure in meters.
    - base_height (float): The height of each level in meters.
    - overhang_depth (float): The depth by which each level overhangs the one below in meters.
    - num_levels (int): The number of levels in the structure.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of 3D Breps representing the architectural concept model.
    \"""
    import Rhino.Geometry as rg

    geometries = []
    current_height = 0.0

    for i in range(num_levels):
        # Define the base corner points of each level
        if i % 2 == 0:
            # Cantilevering to the right
            corner_1 = rg.Point3d(0, 0, current_height)
            corner_2 = rg.Point3d(base_length + overhang_depth, 0, current_height)
            corner_3 = rg.Point3d(base_length + overhang_depth, base_length, current_height)
            corner_4 = rg.Point3d(0, base_length, current_height)
        else:
            # Cantilevering to the left
            corner_1 = rg.Point3d(-overhang_depth, 0, current_height)
            corner_2 = rg.Point3d(base_length, 0, current_height)
            corner_3 = rg.Point3d(base_length, base_length, current_height)
            corner_4 = rg.Point3d(-overhang_depth, base_length, current_height)

        # Create the rectangle for the current level
        base_rectangle = rg.Rectangle3d(rg.Plane.WorldXY, corner_1, corner_3)
        brep = rg.Brep.CreateFromSurface(rg.Surface.CreateExtrusion(base_rectangle.ToNurbsCurve(), rg.Vector3d(0, 0, base_height)))

        # Add the brep to the list of geometries
        geometries.append(brep)

        # Update the current height for the next level
        current_height += base_height

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_cantilevering_corners(5.0, 3.0, 1.0, 4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_cantilevering_corners(10.0, 2.5, 0.5, 6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_cantilevering_corners(7.0, 4.0, 2.0, 3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_cantilevering_corners(8.0, 3.5, 1.5, 5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_cantilevering_corners(6.0, 2.0, 1.0, 7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
