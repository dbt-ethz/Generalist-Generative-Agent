# Created for 0015_0001_suspended_intersecting_assembly.json

""" Summary:
The function `create_suspended_intersecting_assembly` generates an architectural concept model based on the metaphor of 'Suspended intersecting assembly' by creating a network of floating elements. Utilizing lightweight materials, it constructs wire-like and acrylic sheet components that randomly intersect in three-dimensional space. Through parameters like height, width, and depth, the model emphasizes lightness and fluidity while maintaining structural transparency. The function incorporates layering techniques and random positioning to create dynamic intersections, suggesting movement and connectivity. Additionally, it allows for customization in the number of elements and their dimensions, resulting in varied and intricate architectural forms."""

#! python 3
function_code = """def create_suspended_intersecting_assembly(height, width, depth, num_elements, wire_radius, seed=42):
    \"""
    Creates an architectural Concept Model embodying the 'Suspended intersecting assembly' metaphor.
    
    This function generates a model composed of thin wire-like and acrylic sheet elements that appear to float and intersect,
    emphasizing lightness, fluidity, and transparency. The design highlights a delicate balance and network of connections.
    
    Parameters:
    - height (float): The height of the bounding space for the model in meters.
    - width (float): The width of the bounding space for the model in meters.
    - depth (float): The depth of the bounding space for the model in meters.
    - num_elements (int): The number of wire-like elements to create.
    - wire_radius (float): The radius of the wire elements.
    - seed (int, optional): Seed for the random number generator to ensure replicable results. Default is 42.
    
    Returns:
    - List of Rhino.Geometry.Brep: A list of 3D geometries representing the concept model.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    random.seed(seed)
    geometries = []

    # Create wire-like elements
    for _ in range(num_elements):
        # Randomly choose start and end points within the bounding box
        start_point = rg.Point3d(random.uniform(0, width), random.uniform(0, depth), random.uniform(0, height))
        end_point = rg.Point3d(random.uniform(0, width), random.uniform(0, depth), random.uniform(0, height))
        
        # Create a line curve
        line_curve = rg.LineCurve(start_point, end_point)
        
        # Create a pipe around the line to simulate a wire
        wire_brep = rg.Brep.CreatePipe(line_curve, wire_radius, False, rg.PipeCapMode.Round, False, 0.01, 0.01)[0]
        geometries.append(wire_brep)

    # Create acrylic sheet elements
    num_sheets = num_elements // 2
    for _ in range(num_sheets):
        # Randomly generate the position for the sheet
        sheet_center = rg.Point3d(random.uniform(0, width), random.uniform(0, depth), random.uniform(0, height))
        
        # Randomly generate normal vector for the sheet
        normal_vector = rg.Vector3d(random.uniform(-1, 1), random.uniform(-1, 1), random.uniform(-1, 1))
        normal_vector.Unitize()
        
        # Create a plane at the position with the normal vector
        plane = rg.Plane(sheet_center, normal_vector)
        
        # Define dimensions for the sheet
        sheet_width = random.uniform(0.5, 2.0)
        sheet_length = random.uniform(0.5, 2.0)
        
        # Create a rectangle on the plane
        rectangle = rg.Rectangle3d(plane, sheet_width, sheet_length)
        
        # Create a planar surface from the rectangle
        sheet_brep = rg.Brep.CreatePlanarBreps(rectangle.ToNurbsCurve())[0]
        geometries.append(sheet_brep)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_suspended_intersecting_assembly(height=3.0, width=2.0, depth=2.0, num_elements=20, wire_radius=0.05)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_suspended_intersecting_assembly(height=4.0, width=3.0, depth=5.0, num_elements=30, wire_radius=0.1, seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_suspended_intersecting_assembly(height=5.0, width=4.0, depth=3.0, num_elements=15, wire_radius=0.03)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_suspended_intersecting_assembly(height=2.5, width=1.5, depth=1.5, num_elements=25, wire_radius=0.02, seed=100)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_suspended_intersecting_assembly(height=6.0, width=5.0, depth=4.0, num_elements=50, wire_radius=0.04)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
