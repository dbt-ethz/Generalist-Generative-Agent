# Created for 0009_0004_cantilevering_corners.json

""" Summary:
The provided function generates an architectural concept model inspired by the metaphor of "Cantilevering corners." It constructs a central core structure from which angular volumes extend dynamically, creating cantilevered corners that exemplify tension and balance. The function utilizes parameters to define the core's dimensions and the extent of cantilevering, ensuring a unique interaction between grounded and suspended elements. By randomizing the direction of the cantilevers, the model captures the essence of movement while maintaining stability. The result is a series of 3D geometries that reflect the playful balance of solid and void, enhancing spatial engagement and exploration."""

#! python 3
function_code = """def create_dynamic_cantilevered_model(core_width, core_depth, core_height, cantilever_factor, seed=42):
    \"""
    Generate an architectural Concept Model inspired by 'Cantilevering corners'.

    This function creates a central core structure from which angular volumes extend,
    forming cantilevered corners with a sense of motion and balance. The design focuses
    on the interplay between the grounded core and the dynamic projections.

    Parameters:
    - core_width (float): The width of the central core structure in meters.
    - core_depth (float): The depth of the central core structure in meters.
    - core_height (float): The height of the central core structure in meters.
    - cantilever_factor (float): A factor determining the length of cantilever extensions relative to the core dimensions.
    - seed (int): Seed for random number generator to ensure replicable results. Default is 42.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of 3D geometries (breps) representing the concept model.
    \"""
    import Rhino.Geometry as rg
    import random

    random.seed(seed)

    geometries = []

    # Create the central core structure
    core_box = rg.Box(rg.Plane.WorldXY, rg.Interval(0, core_width), rg.Interval(0, core_depth), rg.Interval(0, core_height))
    geometries.append(core_box.ToBrep())

    # Calculate the cantilever length based on the factor
    cantilever_length = max(core_width, core_depth) * cantilever_factor

    # Define potential base points for cantilevers (corners and midpoints)
    base_points = [
        rg.Point3d(0, 0, core_height),
        rg.Point3d(core_width, 0, core_height),
        rg.Point3d(0, core_depth, core_height),
        rg.Point3d(core_width, core_depth, core_height),
        rg.Point3d(core_width / 2, 0, core_height),
        rg.Point3d(0, core_depth / 2, core_height),
        rg.Point3d(core_width, core_depth / 2, core_height),
        rg.Point3d(core_width / 2, core_depth, core_height)
    ]

    # Create cantilever extensions
    for base_point in base_points:
        # Random direction for each cantilever
        direction = rg.Vector3d(random.uniform(-1, 1), random.uniform(-1, 1), 0)
        direction.Unitize()
        direction *= cantilever_length

        # Create a plane at the base point, oriented along the direction
        cantilever_plane = rg.Plane(base_point, direction, rg.Vector3d.ZAxis)

        # Create the cantilever box
        cantilever_box = rg.Box(
            cantilever_plane,
            rg.Interval(0, core_width / 3),
            rg.Interval(0, core_depth / 3),
            rg.Interval(0, core_height / 2)
        )

        # Transform the cantilever to the desired position
        cantilever_box.Transform(rg.Transform.Translation(direction))

        # Convert to Brep and add to the geometries list
        geometries.append(cantilever_box.ToBrep())

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_dynamic_cantilevered_model(5.0, 3.0, 4.0, 1.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_dynamic_cantilevered_model(6.0, 4.0, 5.0, 2.0, seed=10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_dynamic_cantilevered_model(7.0, 5.0, 6.0, 1.2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_dynamic_cantilevered_model(8.0, 6.0, 7.0, 1.0, seed=100)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_dynamic_cantilevered_model(4.0, 2.0, 3.0, 1.8, seed=21)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
