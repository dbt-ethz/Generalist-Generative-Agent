# Created for 0015_0004_suspended_intersecting_assembly.json

""" Summary:
The function `create_suspended_intersecting_assembly` generates an architectural concept model inspired by the metaphor "Suspended intersecting assembly." It creates a series of modular elements that appear to float and intersect dynamically, reflecting lightness and fluidity. By utilizing random transformations, such as height variations and rotations, the function arranges these modules in a way that emphasizes their interconnectivity and creates a visually engaging lattice-like structure. The use of lightweight materials, like the simulated balsa wood and translucent panels, enhances the perception of suspension, while adjustable joints allow for reconfiguration, fostering adaptability within the design."""

#! python 3
function_code = """def create_suspended_intersecting_assembly(mod_count=7, mod_size=2.5, height_range=(2, 8), seed=42):
    \"""
    Creates an architectural Concept Model embodying the 'Suspended intersecting assembly' metaphor.
    
    This function generates a series of modular, interlocking elements that are arranged to appear as if they are 
    suspended and intersecting dynamically within space. The design emphasizes lightness, transparency, and fluidity.

    Parameters:
    - mod_count (int): Number of modular elements to create.
    - mod_size (float): The base size of each module in meters.
    - height_range (tuple): A range (min, max) in meters for the heights at which intersections occur.
    - seed (int): Seed for the random number generator to ensure replicability.

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

    # Define a base plane at the origin
    base_plane = rg.Plane.WorldXY

    for i in range(mod_count):
        # Randomly determine the height offset for each module
        height_offset = random.uniform(*height_range)

        # Create a base cylinder to represent the module
        radius = mod_size * 0.2
        height = mod_size * 0.5
        base_circle = rg.Circle(base_plane, radius)
        cylinder = rg.Cylinder(base_circle, height).ToBrep(True, True)

        # Randomly position and rotate the cylinder to enhance dynamic appearance
        x_offset = random.uniform(-mod_size, mod_size)
        y_offset = random.uniform(-mod_size, mod_size)
        translation = rg.Transform.Translation(x_offset, y_offset, height_offset)

        # Apply a random rotation around a vertical axis
        rotation_angle = random.uniform(0, 2 * math.pi)
        rotation = rg.Transform.Rotation(rotation_angle, base_plane.ZAxis, rg.Point3d(0, 0, height_offset))

        # Combine transformations
        transform = translation * rotation
        cylinder.Transform(transform)

        # Add the transformed cylinder to the list of geometries
        geometries.append(cylinder)

        # Create a translucent panel as a surface
        panel_radius = mod_size * 0.5
        panel_plane = rg.Plane(rg.Point3d(0, 0, height_offset + height), rg.Vector3d.ZAxis)
        panel_circle = rg.Circle(panel_plane, panel_radius)
        panel_surface = rg.Brep.CreatePlanarBreps(panel_circle.ToNurbsCurve())[0]

        # Apply the same transformation to the panel
        panel_surface.Transform(transform)

        # Add the panel surface to the list of geometries
        geometries.append(panel_surface)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_suspended_intersecting_assembly(mod_count=10, mod_size=3.0, height_range=(3, 10), seed=123)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_suspended_intersecting_assembly(mod_count=5, mod_size=1.5, height_range=(1, 5), seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_suspended_intersecting_assembly(mod_count=12, mod_size=2.0, height_range=(1, 6), seed=2023)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_suspended_intersecting_assembly(mod_count=8, mod_size=2.0, height_range=(4, 12), seed=50)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_suspended_intersecting_assembly(mod_count=15, mod_size=4.0, height_range=(2, 9), seed=77)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
