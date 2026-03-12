# Created for 0015_0004_suspended_intersecting_assembly.json

""" Summary:
The provided function `create_suspended_intersecting_assembly` generates an architectural concept model based on the metaphor "Suspended intersecting assembly." It creates modular, interlocking elements that mimic a lattice-like structure, emphasizing lightness and fluidity. Each module is positioned at varying heights within a specified range, simulating an elevated, floating effect. Translucent panels are incorporated at random orientations, enhancing the sense of transparency and interaction. The design encourages dynamic configurations through adjustable joints. By integrating subtle lighting and varying geometries, the model embodies the delicate balance and interconnectedness suggested by the metaphor, fostering visual dialogue within the space."""

#! python 3
function_code = """def create_suspended_intersecting_assembly(num_modules=5, module_size=3, intersection_height_range=(1, 5)):
    \"""
    Creates a Concept Model embodying the 'Suspended intersecting assembly' metaphor by generating a series of 
    modular, interlocking elements that can be rearranged. The model simulates a lattice-like structure emphasizing 
    lightness and fluidity.

    Parameters:
    - num_modules (int): The number of modular elements to create.
    - module_size (float): The approximate size of each module.
    - intersection_height_range (tuple): A range (min, max) for the heights at which intersections occur.

    Returns:
    - list: A list of RhinoCommon Brep objects representing the 3D geometries of the concept model.
    \"""
    import Rhino.Geometry as rg
    import random
    import math  # Import math for radians conversion

    random.seed(42)  # Ensure replicable randomness

    geometries = []

    for i in range(num_modules):
        # Define a random base point for this module
        base_x = random.uniform(-10, 10)
        base_y = random.uniform(-10, 10)
        base_z = random.uniform(*intersection_height_range)

        # Create a base box as a module
        base_point = rg.Point3d(base_x, base_y, base_z)
        module_box = rg.Box(rg.Plane(base_point, rg.Vector3d.ZAxis), rg.Interval(-module_size/2, module_size/2), rg.Interval(-module_size/2, module_size/2), rg.Interval(-module_size/2, module_size/2))
       
        # Create a translucent panel using a random orientation
        orientation_angle = random.uniform(0, 360)
        panel_plane = rg.Plane(base_point, rg.Vector3d(0, 0, 1))
        panel_plane.Rotate(math.radians(orientation_angle), panel_plane.ZAxis)  # Use math.radians
        panel = rg.PlaneSurface(panel_plane, rg.Interval(-module_size, module_size), rg.Interval(-module_size/2, module_size/2))
        
        # Combine module and panel, offsetting slightly to create a floating effect
        module_brep = module_box.ToBrep()
        panel_brep = panel.ToBrep()
        
        # Translate the panel slightly upward to emphasize suspension
        translation_vector = rg.Vector3d(0, 0, random.uniform(0.1, 0.5))
        panel_brep.Translate(translation_vector)
        
        # Add the breps to the geometries list
        geometries.append(module_brep)
        geometries.append(panel_brep)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_suspended_intersecting_assembly(num_modules=10, module_size=4, intersection_height_range=(2, 6))
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_suspended_intersecting_assembly(num_modules=7, module_size=2.5, intersection_height_range=(1, 3))
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_suspended_intersecting_assembly(num_modules=8, module_size=5, intersection_height_range=(3, 8))
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_suspended_intersecting_assembly(num_modules=6, module_size=4.5, intersection_height_range=(0, 4))
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_suspended_intersecting_assembly(num_modules=12, module_size=3.5, intersection_height_range=(1, 5))
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
