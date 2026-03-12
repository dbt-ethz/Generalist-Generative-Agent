# Created for 0015_0004_suspended_intersecting_assembly.json

""" Summary:
The provided function generates an architectural concept model based on the metaphor of "Suspended intersecting assembly." It creates a series of modular elements designed to appear suspended at various heights, emphasizing lightness and fluidity. By using truncated cones that can rotate and translate in X, Y, and Z dimensions, the modules dynamically intersect to form a lattice-like structure. This design fosters visual interplay and interaction among elements, aligning with the metaphor's focus on transparency and balance. The function incorporates adjustable parameters, allowing for exploration of different configurations while maintaining the essence of the metaphor."""

#! python 3
function_code = """def create_suspended_intersecting_assembly(modules_count=6, module_size=2.5, height_levels=(2, 4, 6, 8), seed=11):
    \"""
    Creates an architectural Concept Model embodying the 'Suspended intersecting assembly' metaphor.
    
    This function generates a series of modular, interlocking elements that appear suspended at various heights,
    forming dynamic intersections. The design emphasizes lightness, fluidity, and interaction through transparency
    and strategic spatial dialogues.

    Parameters:
    - modules_count (int): Number of modular elements to be created.
    - module_size (float): The size of each module in meters.
    - height_levels (tuple of float): Discrete z-levels for module placement.
    - seed (int): Seed for the random number generator to ensure replicability.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep objects representing the 3D geometries of the concept model.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    # Set the random seed for reproducibility
    random.seed(seed)

    # Initialize a list to store geometry
    geometries = []

    # Define a base plane for module creation
    base_plane = rg.Plane.WorldXY

    # Define base and top radii for the truncated cone
    base_radius = module_size
    top_radius = module_size / 2

    for i in range(modules_count):
        # Randomly choose a height level for each module
        height = random.choice(height_levels)

        # Create a base module as a truncated cone to emphasize suspension
        cone = rg.Cone(base_plane, height, base_radius)
        truncated_cone_surface = cone.ToNurbsSurface()
        truncated_cone = rg.Brep.CreateFromSurface(truncated_cone_surface) if truncated_cone_surface else None

        if truncated_cone:
            # Rotate the module to create dynamic intersections
            rotation_angle = random.uniform(0, math.pi / 2)
            rotation_axis = rg.Vector3d(random.uniform(-1, 1), random.uniform(-1, 1), 0)
            rotation_transform = rg.Transform.Rotation(rotation_angle, rotation_axis, rg.Point3d.Origin)
            truncated_cone.Transform(rotation_transform)

            # Translate the module randomly in the X and Y to create a floating effect
            translation_vector = rg.Vector3d(random.uniform(-5, 5), random.uniform(-5, 5), 0)
            truncated_cone.Translate(translation_vector)

            # Add to geometries list
            geometries.append(truncated_cone)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_suspended_intersecting_assembly(modules_count=8, module_size=3.0, height_levels=(1, 3, 5, 7), seed=42)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_suspended_intersecting_assembly(modules_count=10, module_size=2.0, height_levels=(1, 2, 3, 4), seed=7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_suspended_intersecting_assembly(modules_count=5, module_size=2.0, height_levels=(3, 6, 9), seed=25)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_suspended_intersecting_assembly(modules_count=7, module_size=2.5, height_levels=(2, 5, 8), seed=15)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_suspended_intersecting_assembly(modules_count=12, module_size=1.5, height_levels=(4, 6, 10), seed=30)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
