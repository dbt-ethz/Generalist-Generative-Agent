# Created for 0009_0001_cantilevering_corners.json

""" Summary:
The function `create_cantilevering_corners` generates an architectural concept model inspired by the metaphor of "Cantilevering corners." It constructs a base structure and adds cantilevered elements at each corner, reflecting a dynamic balance between stability and movement. The parameters define the dimensions of the base and the extent of the cantilever, allowing for dramatic overhangs that challenge conventional notions of gravity. The function uses Rhinos geometry library to create and combine 3D shapes, culminating in a model that visually embodies the metaphor by projecting outward, enhancing spatial complexity and visual interest in the design."""

#! python 3
function_code = """def create_cantilevering_corners(length=10.0, width=10.0, height=10.0, overhang=3.0):
    \"""
    Creates an architectural Concept Model based on the metaphor 'Cantilevering corners'.
    This model dynamically balances stability and motion by projecting corners outward,
    creating dramatic overhangs and unexpected spaces.

    Args:
        length (float): The length of the base structure in meters.
        width (float): The width of the base structure in meters.
        height (float): The height of the base structure in meters.
        overhang (float): The extent of the cantilevered overhang in meters.

    Returns:
        List[Rhino.Geometry.Brep]: A list of breps representing the 3D geometries of the concept model.
    \"""
    import Rhino.Geometry as rg

    # Create the main base structure
    base = rg.Box(rg.Plane.WorldXY, rg.Interval(0, length), rg.Interval(0, width), rg.Interval(0, height))
    brep_base = base.ToBrep()

    # Function to create a cantilever at a specified corner
    def create_cantilever(base_point, direction):
        offset_vector = rg.Vector3d(*direction) * overhang
        offset_plane = rg.Plane(base_point, offset_vector)
        cantilever_box = rg.Box(offset_plane, rg.Interval(0, length*0.2), rg.Interval(0, width*0.2), rg.Interval(0, height*0.2))
        return cantilever_box.ToBrep()

    # Define corner points of the base structure
    corners = [
        (length, width, height),
        (length, 0, height),
        (0, width, height),
        (0, 0, height)
    ]

    # Define cantilever directions for each corner
    directions = [
        (1, 1, 0),  # Top right corner
        (-1, 1, 0), # Top left corner
        (1, -1, 0), # Bottom right corner
        (-1, -1, 0) # Bottom left corner
    ]

    # Create cantilevered corners
    cantilevers = [create_cantilever(rg.Point3d(*corners[i]), directions[i]) for i in range(4)]

    # Combine base and cantilevers
    concept_model = [brep_base] + cantilevers

    return concept_model"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_cantilevering_corners(length=15.0, width=12.0, height=8.0, overhang=4.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_cantilevering_corners(length=20.0, width=15.0, height=10.0, overhang=5.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_cantilevering_corners(length=12.0, width=10.0, height=9.0, overhang=2.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_cantilevering_corners(length=18.0, width=14.0, height=11.0, overhang=6.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_cantilevering_corners(length=25.0, width=20.0, height=15.0, overhang=7.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
