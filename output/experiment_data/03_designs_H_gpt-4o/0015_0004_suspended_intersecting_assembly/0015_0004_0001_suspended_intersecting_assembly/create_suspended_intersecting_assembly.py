# Created for 0015_0004_suspended_intersecting_assembly.json

""" Summary:
The provided function, `create_suspended_intersecting_assembly`, generates an architectural concept model that embodies the metaphor of a "Suspended intersecting assembly." It creates a series of modular, interlocking elements designed to appear weightless and dynamically intersecting. By randomly determining the heights and orientations of circular modules and their extrusions, the function emphasizes fluidity and transparency, creating a visually engaging lattice structure. The use of lightweight materials simulated through geometry enhances the notion of suspension and balance, while adjustable configurations allow for adaptability. Ultimately, the model reflects the metaphor's emphasis on spatial dialogue and interconnectivity."""

#! python 3
function_code = """def create_suspended_intersecting_assembly(module_radius=3.0, num_modules=8, height_range=(3, 15), seed=24):
    \"""
    Create an architectural Concept Model embodying the 'Suspended intersecting assembly' metaphor.

    This function generates a series of modular, interlocking elements that appear to float and intersect
    dynamically within a space. The design emphasizes lightness, fluidity, and structural transparency,
    featuring components that create dynamic intersections and relationships.

    Parameters:
    - module_radius (float): The radius of the circular modules.
    - num_modules (int): The number of modules to create.
    - height_range (tuple of float): The range (min, max) for the height at which modules are placed.
    - seed (int): Seed for the random number generator to ensure replicability.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep objects representing the concept model geometry.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    # Set a random seed for reproducibility
    random.seed(seed)

    geometries = []

    for i in range(num_modules):
        # Randomly select a height for each module
        height = random.uniform(*height_range)
        
        # Create a circular module
        center_point = rg.Point3d(
            random.uniform(-10, 10),
            random.uniform(-10, 10),
            height
        )
        circle = rg.Circle(center_point, module_radius)
        circle_brep = rg.Brep.CreatePlanarBreps(circle.ToNurbsCurve())[0]

        # Create a vertical extrusion to simulate structural elements
        extrusion_height = random.uniform(1, 3)
        extrusion_vector = rg.Vector3d(0, 0, extrusion_height)
        extrusion_surface = rg.Surface.CreateExtrusion(circle.ToNurbsCurve(), extrusion_vector)
        extrusion_brep = extrusion_surface.ToBrep()

        # Rotate the extrusion to create dynamic intersections
        angle = random.uniform(-math.pi/4, math.pi/4)
        rotation_axis = rg.Line(center_point, rg.Point3d(center_point.X, center_point.Y, center_point.Z + 1)).ToNurbsCurve()
        rotation = rg.Transform.Rotation(angle, rotation_axis.PointAtStart, rotation_axis.PointAtEnd)
        extrusion_brep.Transform(rotation)

        # Add the circular module and the extrusion to the geometries list
        geometries.append(circle_brep)
        geometries.append(extrusion_brep)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_suspended_intersecting_assembly(module_radius=4.0, num_modules=10, height_range=(5, 12), seed=42)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_suspended_intersecting_assembly(module_radius=2.5, num_modules=5, height_range=(4, 10), seed=30)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_suspended_intersecting_assembly(module_radius=3.5, num_modules=12, height_range=(6, 18), seed=50)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_suspended_intersecting_assembly(module_radius=3.0, num_modules=15, height_range=(2, 20), seed=15)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_suspended_intersecting_assembly(module_radius=3.0, num_modules=20, height_range=(1, 25), seed=10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
