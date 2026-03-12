# Created for 0015_0001_suspended_intersecting_assembly.json

""" Summary:
The function `create_suspended_intersecting_assembly` generates an architectural concept model that embodies the metaphor of "Suspended intersecting assembly." It creates a dynamic arrangement of elevated elements using lightweight materials, specifically thin wires and transparent sheets. The function randomly determines the positions and orientations of these components within a specified volume, ensuring they appear to float and intersect, thus reflecting the metaphor's emphasis on lightness and fluidity. By varying the number of elements and their sizes, the model achieves a complex network that promotes visual interconnectivity and a delicate balance, ultimately suggesting movement and connectivity in space."""

#! python 3
function_code = """def create_suspended_intersecting_assembly(volume_size, num_elements, wire_radius, transparency_factor, seed=42):
    \"""
    Generates an architectural Concept Model embodying the 'Suspended intersecting assembly' metaphor 
    using thin wires and transparent sheets. The design focuses on floating and intersecting elements 
    to create a complex network of connections, emphasizing lightness and fluidity.

    Parameters:
    - volume_size (float): The size of the cubic bounding volume for the entire assembly (in meters).
    - num_elements (int): The number of intersecting wire elements to create.
    - wire_radius (float): The radius of the wire elements (in meters) to represent the floating components.
    - transparency_factor (float): A factor to adjust the transparency of the sheet elements, range from 0 to 1.
    - seed (int, optional): Seed for the random number generator to ensure replicable results. Default is 42.

    Returns:
    - List of Rhino.Geometry.Brep: A list of Brep geometries representing the 3D concept model.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    # Initialize random seed
    random.seed(seed)

    # List to hold the resulting geometries
    geometries = []

    # Create wires (represented as thin cylindrical breps)
    for _ in range(num_elements):
        # Randomly determine the start and end points of the wire within the volume
        start_point = rg.Point3d(
            random.uniform(0, volume_size),
            random.uniform(0, volume_size),
            random.uniform(0, volume_size)
        )
        end_point = rg.Point3d(
            random.uniform(0, volume_size),
            random.uniform(0, volume_size),
            random.uniform(0, volume_size)
        )

        # Create a line and then a cylindrical brep to represent the wire
        line = rg.Line(start_point, end_point)
        cylinder = rg.Cylinder(rg.Circle(rg.Plane(line.From, line.Direction), wire_radius), line.Length)
        wire_brep = cylinder.ToBrep(True, True)

        geometries.append(wire_brep)

    # Create intersecting transparent sheets
    num_sheets = num_elements // 2
    for _ in range(num_sheets):
        # Randomly determine the position and size of the sheet within the volume
        corner1 = rg.Point3d(
            random.uniform(0, volume_size),
            random.uniform(0, volume_size),
            random.uniform(0, volume_size)
        )
        corner2 = rg.Point3d(
            corner1.X + random.uniform(1, volume_size / 2),
            corner1.Y + random.uniform(1, volume_size / 2),
            corner1.Z
        )

        # Create a planar surface as a sheet
        rect = rg.Rectangle3d(rg.Plane.WorldXY, corner1, corner2)
        sheet_surface = rg.Brep.CreatePlanarBreps(rect.ToNurbsCurve())[0]

        # Apply transparency logic (here placeholder as RhinoCommon does not directly support transparency)
        # This would typically be handled in the rendering/material properties in the application environment

        geometries.append(sheet_surface)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_suspended_intersecting_assembly(10.0, 20, 0.05, 0.7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_suspended_intersecting_assembly(15.0, 30, 0.03, 0.5, seed=123)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_suspended_intersecting_assembly(12.0, 25, 0.04, 0.6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_suspended_intersecting_assembly(8.0, 15, 0.02, 0.8, seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_suspended_intersecting_assembly(20.0, 50, 0.1, 0.9, seed=100)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
