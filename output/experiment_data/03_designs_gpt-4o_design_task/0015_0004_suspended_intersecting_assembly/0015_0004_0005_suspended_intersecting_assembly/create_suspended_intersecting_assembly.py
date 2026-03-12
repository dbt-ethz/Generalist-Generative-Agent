# Created for 0015_0004_suspended_intersecting_assembly.json

""" Summary:
The provided function, `create_suspended_intersecting_assembly`, generates an architectural concept model based on the metaphor of "Suspended intersecting assembly." It creates a series of modular, interlocking elements that mimic the appearance of floating structures. Each module is randomly positioned at varying heights to enhance the sense of suspension and lightness. The function employs geometric transformations to create dynamic intersections, fostering interconnectivity. By manipulating the number of modules, their sizes, and height variations, the model explores different spatial configurations, embodying the fluidity and transparency described in the metaphor while allowing for adaptability in design through adjustable connections."""

#! python 3
function_code = """def create_suspended_intersecting_assembly(modules_count=5, module_size=3.0, height_variation=2.0, seed=42):
    \"""
    Creates an architectural Concept Model embodying the 'Suspended intersecting assembly' metaphor
    using modular, interlocking elements that can be rearranged. The design features elevated,
    intersecting elements that convey a sense of lightness and fluidity.

    Parameters:
    - modules_count (int): Number of modular elements to create.
    - module_size (float): Base size of each module in meters.
    - height_variation (float): Maximum variation in height for the floating appearance in meters.
    - seed (int): Seed for random number generator to ensure replicability.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep objects representing the 3D geometries.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    # Set the random seed for reproducibility
    random.seed(seed)

    # Initialize an empty list to store the geometries
    geometries = []

    # Define a base plane at the origin
    base_plane = rg.Plane.WorldXY

    for i in range(modules_count):
        # Randomly determine the height offset for each module
        height_offset = random.uniform(-height_variation, height_variation)

        # Create a base box for the module
        base_box = rg.Box(base_plane, rg.Interval(-module_size/2, module_size/2),
                          rg.Interval(-module_size/2, module_size/2),
                          rg.Interval(-module_size/2, module_size/2))

        # Offset the box to create the appearance of suspension
        transform = rg.Transform.Translation(0, 0, height_offset)
        base_box.Transform(transform)

        # Convert the box to a Brep
        brep = base_box.ToBrep()

        # Add the Brep to the list of geometries
        geometries.append(brep)

        # Introduce intersections using planes
        if i > 0:
            # Create a random plane to intersect with the previous module
            angle = random.uniform(0, 360)
            rotation = rg.Transform.Rotation(math.radians(angle), base_plane.ZAxis, base_box.Center)
            intersection_plane = rg.Plane(base_box.Center, base_plane.XAxis)
            intersection_plane.Transform(rotation)

            # Create a surface from the plane
            plane_surface = rg.PlaneSurface(intersection_plane, rg.Interval(-module_size, module_size),
                                            rg.Interval(-module_size, module_size))

            # Convert the surface to a Brep and add it to the list
            brep_plane = plane_surface.ToBrep()
            geometries.append(brep_plane)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_suspended_intersecting_assembly(modules_count=10, module_size=4.0, height_variation=3.0, seed=123)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_suspended_intersecting_assembly(modules_count=7, module_size=2.5, height_variation=1.5, seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_suspended_intersecting_assembly(modules_count=8, module_size=5.0, height_variation=4.0, seed=56)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_suspended_intersecting_assembly(modules_count=6, module_size=3.5, height_variation=2.5, seed=10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_suspended_intersecting_assembly(modules_count=12, module_size=4.5, height_variation=2.8, seed=78)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
