# Created for 0015_0004_suspended_intersecting_assembly.json

""" Summary:
The function `create_suspended_intersecting_assembly` generates an architectural concept model by creating a series of modular elements that simulate the metaphor of "Suspended intersecting assembly." It randomly positions these modules in space, emphasizing lightness and fluidity by using lightweight materials. Each module is represented as a box, with additional curvilinear elements intersecting it, creating a dynamic interplay and visual connectivity. The model incorporates adjustable elements and varying heights, fostering a sense of balance and tension, while the geometry highlights the delicate nature of the design. This results in a visually engaging structure that embodies the metaphor's principles."""

#! python 3
function_code = """def create_suspended_intersecting_assembly(module_size=3.0, num_modules=5, max_height=10.0, seed=42):
    \"""
    Create an architectural Concept Model based on the 'Suspended intersecting assembly' metaphor.

    This function generates a series of modular elements that appear to float and intersect dynamically
    within a space. The design emphasizes lightness, fluidity, and structural transparency, featuring
    components that create dynamic intersections and relationships.

    Parameters:
    - module_size (float): The base size of each module in meters.
    - num_modules (int): The number of modules to create and arrange.
    - max_height (float): The maximum height for the positioning of modules.
    - seed (int, optional): Seed for the random number generator to ensure replicability.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep objects representing the concept model geometry.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    # Set the random seed for reproducibility
    random.seed(seed)

    # Initialize an empty list to store the geometries
    geometries = []

    for i in range(num_modules):
        # Randomly position each module in space
        x = random.uniform(-module_size * 2, module_size * 2)
        y = random.uniform(-module_size * 2, module_size * 2)
        z = random.uniform(0, max_height)

        # Create a base plane for the module
        base_plane = rg.Plane(rg.Point3d(x, y, z), rg.Vector3d.ZAxis)

        # Create a box representing the module
        box = rg.Box(base_plane, rg.Interval(-module_size / 2, module_size / 2),
                     rg.Interval(-module_size / 2, module_size / 2), rg.Interval(-module_size / 4, module_size / 4))

        # Convert the box to a Brep and add to the list
        brep = box.ToBrep()
        geometries.append(brep)

        # Create a curvilinear element intersecting the module
        curve_points = [rg.Point3d(x, y, z), 
                        rg.Point3d(x + random.uniform(-module_size, module_size), 
                                   y + random.uniform(-module_size, module_size), 
                                   z + random.uniform(-module_size / 4, module_size / 4)),
                        rg.Point3d(x, y, z + random.uniform(-module_size / 2, module_size / 2))]
        
        curve = rg.NurbsCurve.Create(False, 2, curve_points)
        
        # Create a pipe around the curve to emphasize the intersection
        pipe = rg.Brep.CreatePipe(curve, module_size / 10.0, False, rg.PipeCapMode.Round, True, 1e-3, 1e-3)[0]
        geometries.append(pipe)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_suspended_intersecting_assembly(module_size=4.0, num_modules=6, max_height=12.0, seed=24)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_suspended_intersecting_assembly(module_size=2.5, num_modules=10, max_height=15.0, seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_suspended_intersecting_assembly(module_size=5.0, num_modules=8, max_height=20.0, seed=10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_suspended_intersecting_assembly(module_size=3.5, num_modules=7, max_height=18.0, seed=56)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_suspended_intersecting_assembly(module_size=6.0, num_modules=4, max_height=8.0, seed=15)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
