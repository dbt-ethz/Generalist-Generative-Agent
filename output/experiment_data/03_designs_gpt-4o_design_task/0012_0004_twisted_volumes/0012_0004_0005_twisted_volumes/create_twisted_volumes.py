# Created for 0012_0004_twisted_volumes.json

""" Summary:
The provided function, `create_twisted_volumes`, generates an architectural concept model inspired by the metaphor "Twisted volumes." It creates multiple overlapping and intersecting volumes with varying twists, simulating a dynamic interplay of stability and motion. Each volume is characterized by its height, base dimensions, and a defined twist angle, allowing for a diverse array of forms that capture light and shadow in complex ways. The function's randomization in positioning and twisting enhances the model's dynamism, promoting innovative spatial relationships and a fluid interaction between interior and exterior spaces, thereby embodying the transformative energy of the metaphor."""

#! python 3
function_code = """def create_twisted_volumes(base_length=10, base_width=10, height=30, twist_angle=45, num_volumes=5):
    \"""
    Create a series of twisted volumes to embody the 'Twisted volumes' metaphor in an Architectural Concept Model.
    
    Parameters:
    - base_length (float): The base length of each volume in meters.
    - base_width (float): The base width of each volume in meters.
    - height (float): The height of each volume in meters.
    - twist_angle (float): The maximum angle of twist in degrees for the volumes.
    - num_volumes (int): The number of volumes to create.
    
    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep objects representing the twisted volumes.
    \"""
    import Rhino
    import Rhino.Geometry as rg
    import random
    import math  # Corrected import for math module
    random.seed(42)
    
    volumes = []
    for i in range(num_volumes):
        # Define the base rectangle
        base_rect = rg.Rectangle3d(rg.Plane.WorldXY, base_length, base_width)
        
        # Define the extrusion vector
        extrusion_vector = rg.Vector3d(0, 0, height)
        
        # Create a ruled surface (loft-like) with a twist
        angle = random.uniform(-twist_angle, twist_angle)
        twist_plane = rg.Plane(base_rect.Center, rg.Vector3d(0, 0, 1))
        twisted_rect = rg.Rectangle3d(twist_plane, base_length, base_width)
        twisted_rect.Transform(rg.Transform.Rotation(math.radians(angle), rg.Vector3d(0, 0, 1), twisted_rect.Center))  # Fixed transformation using math.radians
        
        # Extrude the base to form a twisted surface
        loft = rg.Brep.CreateFromLoft([base_rect.ToNurbsCurve(), twisted_rect.ToNurbsCurve()], rg.Point3d.Unset, rg.Point3d.Unset, rg.LoftType.Straight, False)
        if loft:
            volumes.append(loft[0])  # Append the Brep object directly
        
        # Slightly move the plane for the next volume
        base_rect.Transform(rg.Transform.Translation(random.uniform(-2, 2), random.uniform(-2, 2), height * 0.2))
    
    return volumes"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_twisted_volumes(base_length=15, base_width=10, height=40, twist_angle=60, num_volumes=3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_twisted_volumes(base_length=12, base_width=8, height=25, twist_angle=30, num_volumes=4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_twisted_volumes(base_length=20, base_width=15, height=50, twist_angle=90, num_volumes=6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_twisted_volumes(base_length=10, base_width=10, height=35, twist_angle=75, num_volumes=7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_twisted_volumes(base_length=18, base_width=12, height=45, twist_angle=50, num_volumes=2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
