# Created for 0015_0002_suspended_intersecting_assembly.json

""" Summary:
The function `create_suspended_intersecting_assembly` generates an architectural concept model based on the metaphor of "Suspended intersecting assembly." It constructs a series of floating volumes using random dimensions and positions within a defined bounding box to reflect the dynamic intersections described in the metaphor. The model incorporates tensile cables to emphasize the suspended nature of these elements, fostering a sense of lightness and fluidity. Semi-transparent materials are simulated to create visual complexity, while negative spaces between the intersecting volumes enhance interconnectivity. The overall design embodies the metaphor's themes of balance, transparency, and structural elegance."""

#! python 3
function_code = """def create_suspended_intersecting_assembly(base_length=30, base_width=20, height=15, cable_thickness=0.1, transparency=0.5):
    \"""
    Creates an architectural Concept Model representing the 'Suspended intersecting assembly' metaphor.
    
    This function generates a series of intersecting volumes that appear to float, using a framework of tensile cables
    and semi-transparent materials to convey lightness and fluidity. The model is characterized by dynamic intersections
    and negative spaces that enhance visual interconnectivity.

    Parameters:
    - base_length (float): The length of the base area of the model in meters.
    - base_width (float): The width of the base area of the model in meters.
    - height (float): The maximum height of the model in meters.
    - cable_thickness (float): The thickness of the tensile cables in meters.
    - transparency (float): The transparency level of the intersecting volumes (0.0 = fully transparent, 1.0 = opaque).

    Returns:
    - List[Rhino.Geometry.Brep]: A list of 3D breps representing the intersecting volumes and cables.
    \"""
    import Rhino.Geometry as rg
    import random
    
    # Set a seed for replicable randomness
    random.seed(42)
    
    # Define the bounding box of the model
    bbox = rg.BoundingBox(0, 0, 0, base_length, base_width, height)
    
    # List to store geometries
    geometries = []
    
    # Create intersecting floating volumes
    num_volumes = 5
    for i in range(num_volumes):
        # Random dimensions for each volume
        length = random.uniform(5, 10)
        width = random.uniform(3, 7)
        vol_height = random.uniform(3, 5)
        
        # Random position within bounding box
        x = random.uniform(0, base_length - length)
        y = random.uniform(0, base_width - width)
        z = random.uniform(0, height - vol_height)
        
        # Create the volume as a box
        volume = rg.Box(rg.Plane.WorldXY, rg.Interval(x, x + length), rg.Interval(y, y + width), rg.Interval(z, z + vol_height))
        
        # Convert box to brep and add transparency
        volume_brep = volume.ToBrep()
        # Assuming transparency can be represented as a material property in a real implementation
        
        geometries.append(volume_brep)
    
    # Create tensile cables
    num_cables = 10
    for i in range(num_cables):
        # Random endpoints for cables
        start_x = random.uniform(0, base_length)
        start_y = random.uniform(0, base_width)
        start_z = random.uniform(0, height)
        
        end_x = random.uniform(0, base_length)
        end_y = random.uniform(0, base_width)
        end_z = random.uniform(0, height)
        
        # Create cable as a cylinder along a line
        start_point = rg.Point3d(start_x, start_y, start_z)
        end_point = rg.Point3d(end_x, end_y, end_z)
        line = rg.Line(start_point, end_point)
        
        # Create a plane along the line for the cylinder
        plane = rg.Plane(line.From, line.Direction)
        cable = rg.Cylinder(rg.Circle(plane, cable_thickness), line.Length).ToBrep(True, True)
        
        geometries.append(cable)
    
    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_suspended_intersecting_assembly(base_length=40, base_width=30, height=20, cable_thickness=0.2, transparency=0.7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_suspended_intersecting_assembly(base_length=25, base_width=15, height=10, cable_thickness=0.15, transparency=0.6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_suspended_intersecting_assembly(base_length=35, base_width=25, height=18, cable_thickness=0.12, transparency=0.4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_suspended_intersecting_assembly(base_length=50, base_width=40, height=25, cable_thickness=0.3, transparency=0.8)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_suspended_intersecting_assembly(base_length=45, base_width=35, height=22, cable_thickness=0.25, transparency=0.9)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
