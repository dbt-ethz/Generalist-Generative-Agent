# Created for 0015_0005_suspended_intersecting_assembly.json

""" Summary:
The provided function generates an architectural concept model inspired by the metaphor "Suspended intersecting assembly." It creates a series of lightweight, translucent planes that intersect at various angles, simulating a sense of suspension and fluidity. Each plane is randomly translated upwards and rotated around different axes, enhancing the dynamic nature of the assembly. By utilizing parameters like the number of planes, size, and rotation angles, the function produces intricate geometries that emphasize transparency and connectivity. The resulting model visually embodies the metaphor's emphasis on elevation, movement, and interactivity, creating a harmonious architectural representation."""

#! python 3
function_code = """def create_suspended_intersecting_assembly(num_planes=5, plane_size=10.0, max_angle=45.0, seed=42):
    \"""
    Creates an architectural Concept Model based on the metaphor 'Suspended intersecting assembly'.
    
    This function generates a series of lightweight, intersecting planar surfaces that suggest movement
    and fluidity. The planes are represented by translucent materials and are arranged to create a 
    complex web of connections, enhancing the sense of suspension and interconnectivity.

    Parameters:
    - num_planes (int): The number of intersecting planes to create.
    - plane_size (float): The approximate size of each plane in meters.
    - max_angle (float): The maximum angle in degrees by which a plane can be randomly rotated.
    - seed (int): The seed for random number generation to ensure replicable results.

    Returns:
    - List of Rhino.Geometry.Brep: A list of Breps representing the created planar surfaces.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    random.seed(seed)
    planes = []

    for _ in range(num_planes):
        # Create a base plane at the origin
        base_plane = rg.Plane.WorldXY

        # Randomly translate the plane in the Z direction to simulate suspension
        z_translation = random.uniform(1.0, 5.0)  # Between 1 and 5 meters
        translation_vector = rg.Vector3d(0, 0, z_translation)
        base_plane.Translate(translation_vector)

        # Randomly rotate the plane around a random axis to create dynamic intersections
        angle = math.radians(random.uniform(-max_angle, max_angle))
        axis = rg.Vector3d(random.uniform(-1, 1), random.uniform(-1, 1), random.uniform(-1, 1))
        axis.Unitize()
        rotation = rg.Transform.Rotation(angle, axis, base_plane.Origin)
        base_plane.Transform(rotation)

        # Create a rectangle on the plane to represent a suspended surface
        rectangle = rg.Rectangle3d(base_plane, plane_size, plane_size)
        brep = rg.Brep.CreateFromCornerPoints(rectangle.Corner(0), rectangle.Corner(1), rectangle.Corner(2), rectangle.Corner(3), 0.001)

        if brep:
            planes.append(brep)

    return planes"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_suspended_intersecting_assembly(num_planes=7, plane_size=15.0, max_angle=30.0, seed=10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_suspended_intersecting_assembly(num_planes=10, plane_size=12.0, max_angle=60.0, seed=100)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_suspended_intersecting_assembly(num_planes=3, plane_size=8.0, max_angle=90.0, seed=21)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_suspended_intersecting_assembly(num_planes=6, plane_size=20.0, max_angle=15.0, seed=55)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_suspended_intersecting_assembly(num_planes=8, plane_size=18.0, max_angle=25.0, seed=5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
