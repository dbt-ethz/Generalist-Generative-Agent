# Created for 0015_0004_suspended_intersecting_assembly.json

""" Summary:
The function `create_suspended_intersecting_assembly` generates an architectural concept model based on the metaphor of "Suspended intersecting assembly." It creates multiple modular elements that appear to float at various heights, simulating a delicate balance and dynamic intersections. By using lightweight materials like balsa wood or metal rods, the model emphasizes transparency and fluidity. Each module is randomly positioned and transformed to enhance the illusion of suspension, allowing for adjustable configurations that encourage interaction and visual connection. The result is a lattice-like structure that highlights the interplay of light and shadow, embodying the essence of the metaphor."""

#! python 3
function_code = """def create_suspended_intersecting_assembly(base_length=10, base_width=5, height_levels=[4, 8, 12], module_count=5):
    \"""
    Create an architectural Concept Model embodying the 'Suspended intersecting assembly' metaphor.
    
    This function generates a series of modular, interlocking elements that appear to float and intersect dynamically 
    within a space. The design emphasizes lightness, fluidity, and structural transparency, featuring components 
    that create dynamic intersections and relationships.

    Parameters:
    - base_length (float): The base length of the primary module in meters.
    - base_width (float): The base width of the primary module in meters.
    - height_levels (list of float): The z-levels at which modules will be positioned.
    - module_count (int): The number of modules to create and arrange.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep objects representing the concept model geometry.
    \"""
    import Rhino.Geometry as rg
    import random

    # Set a random seed for reproducibility
    random.seed(42)

    geometries = []

    for i in range(module_count):
        # Randomly select a height level for the module
        height = random.choice(height_levels)
        
        # Create a box representing the module
        box_plane = rg.Plane.WorldXY
        box_origin = rg.Point3d(
            random.uniform(-base_length, base_length),
            random.uniform(-base_width, base_width),
            height
        )
        box_plane.Origin = box_origin
        box = rg.Box(box_plane, rg.Interval(-base_length / 2, base_length / 2),
                     rg.Interval(-base_width / 2, base_width / 2),
                     rg.Interval(-0.5, 0.5))

        # Convert the box to a Brep
        brep = box.ToBrep()
        
        # Create transformations to simulate floating and intersecting
        translate_vector = rg.Vector3d(
            random.uniform(-2, 2),
            random.uniform(-2, 2),
            random.uniform(-2, 2)
        )
        transformed_brep = brep.Translate(translate_vector)
        
        # Add the transformed brep to the geometries list
        geometries.append(transformed_brep)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_suspended_intersecting_assembly(base_length=15, base_width=10, height_levels=[3, 6, 9, 12], module_count=7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_suspended_intersecting_assembly(base_length=12, base_width=8, height_levels=[5, 10, 15], module_count=6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_suspended_intersecting_assembly(base_length=20, base_width=15, height_levels=[2, 5, 10, 15], module_count=4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_suspended_intersecting_assembly(base_length=18, base_width=9, height_levels=[1, 3, 7, 11], module_count=10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_suspended_intersecting_assembly(base_length=14, base_width=7, height_levels=[2, 6, 10, 14], module_count=8)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
