# Created for 0015_0004_suspended_intersecting_assembly.json

""" Summary:
The provided function generates an architectural concept model based on the metaphor of "Suspended intersecting assembly" by creating a series of modular, interlocking cylindrical elements and translucent panels. Utilizing random height variations and rotations, it mimics the appearance of floating components that intersect dynamically. The function constructs these elements with lightweight materials, emphasizing transparency and fluidity in design. By strategically arranging the modules at different heights and applying subtle translations, the model achieves a delicate balance that reflects the interplay of light and shadow. This approach encapsulates the metaphor's essence of interconnectivity and structural elegance."""

#! python 3
function_code = """def create_suspended_intersecting_assembly(modules_count=6, module_radius=2.0, height_variation=(2.0, 10.0), seed=42):
    \"""
    Creates an architectural Concept Model embodying the 'Suspended intersecting assembly' metaphor
    using modular, interlocking elements arranged in a dynamic and floating manner. The design features
    elevated, intersecting components that convey lightness, transparency, and fluidity.

    Parameters:
    - modules_count (int): Number of modular elements to create.
    - module_radius (float): Radius of the cylindrical module in meters, representing structural elements.
    - height_variation (tuple): Range (min, max) for the heights at which modules are suspended.
    - seed (int): Seed for the random number generator to ensure replicability.

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

    # Define the base plane at the origin
    base_plane = rg.Plane.WorldXY

    for i in range(modules_count):
        # Determine random height for this module
        z_height = random.uniform(*height_variation)

        # Create a cylindrical module to represent a structural element
        center = rg.Point3d(random.uniform(-5, 5), random.uniform(-5, 5), z_height)
        axis = rg.Vector3d(0, 0, random.uniform(1.5, 3.0))  # Random height for the cylinder
        cylinder = rg.Cylinder(rg.Circle(rg.Plane(center, rg.Vector3d.ZAxis), module_radius), axis.Length)
        brep_cylinder = cylinder.ToBrep(True, True)

        # Rotate the cylinder randomly for dynamic intersection
        angle = random.uniform(0, 2 * math.pi)
        rotation = rg.Transform.Rotation(angle, rg.Vector3d.ZAxis, center)
        brep_cylinder.Transform(rotation)

        # Add the cylinder to the geometries list
        geometries.append(brep_cylinder)

        # Create a translucent disc to represent a floating panel
        disc_radius = module_radius * random.uniform(1.2, 1.5)
        disc_plane = rg.Plane(center + axis, rg.Vector3d.ZAxis)
        disc = rg.Circle(disc_plane, disc_radius)
        disc_brep = rg.Brep.CreatePlanarBreps([disc.ToNurbsCurve()])[0]

        # Slightly translate the disc to enhance the floating effect
        translate = rg.Transform.Translation(rg.Vector3d(0, 0, random.uniform(0.2, 0.5)))
        disc_brep.Transform(translate)

        # Add the disc to the geometries list
        geometries.append(disc_brep)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_suspended_intersecting_assembly(modules_count=8, module_radius=1.5, height_variation=(3.0, 12.0), seed=100)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_suspended_intersecting_assembly(modules_count=5, module_radius=2.5, height_variation=(1.0, 8.0), seed=23)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_suspended_intersecting_assembly(modules_count=10, module_radius=3.0, height_variation=(4.0, 15.0), seed=56)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_suspended_intersecting_assembly(modules_count=7, module_radius=2.2, height_variation=(1.5, 9.5), seed=15)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_suspended_intersecting_assembly(modules_count=12, module_radius=2.8, height_variation=(2.5, 11.0), seed=30)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
