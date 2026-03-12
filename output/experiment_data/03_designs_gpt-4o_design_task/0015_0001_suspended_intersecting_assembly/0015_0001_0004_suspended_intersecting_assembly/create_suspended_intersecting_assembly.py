# Created for 0015_0001_suspended_intersecting_assembly.json

""" Summary:
The function `create_suspended_intersecting_assembly` generates an architectural concept model based on the metaphor of a "Suspended intersecting assembly." It creates multiple elevated components that mimic the appearance of floating elements through random positioning and orientation. By defining planes at varied angles and positions within specified dimensions, the function emphasizes lightness and fluidity, reflecting the metaphor's key traits. The generated geometries are represented as a list of Breps (boundary representations), which visually articulate dynamic intersections and a sense of balance, enhancing spatial relationships and connectivity. This results in a model that embodies the essence of the provided metaphor."""

#! python 3
function_code = """def create_suspended_intersecting_assembly(base_length, base_width, height, num_elements, seed):
    \"""
    Creates an architectural Concept Model that embodies the 'Suspended intersecting assembly' metaphor.

    This function generates a model composed of multiple elevated components that appear to float and intersect within the space,
    emphasizing lightness and fluidity. The elements are represented by thin planar surfaces that intersect at various angles,
    creating a network of connections.

    Parameters:
    - base_length (float): The length of the base area for the model (in meters).
    - base_width (float): The width of the base area for the model (in meters).
    - height (float): The maximum height of the model (in meters).
    - num_elements (int): The number of intersecting elements to create.
    - seed (int): Seed for the random number generator to ensure replicable results.

    Returns:
    - List of Rhino.Geometry.Brep: A list of breps representing the 3D geometries of the concept model.
    \"""
    import Rhino.Geometry as rg
    import math
    import random

    random.seed(seed)
    geometries = []
    
    for _ in range(num_elements):
        # Randomly generate the position and orientation of each plane
        x = random.uniform(0, base_length)
        y = random.uniform(0, base_width)
        z = random.uniform(0, height)
        
        # Create a random orientation for the plane
        angle_x = random.uniform(0, 360)
        angle_y = random.uniform(0, 360)
        angle_z = random.uniform(0, 360)
        
        # Create a plane at the random position with random orientation
        origin = rg.Point3d(x, y, z)
        axis_x = rg.Vector3d(1, 0, 0)
        axis_y = rg.Vector3d(0, 1, 0)
        axis_z = rg.Vector3d(0, 0, 1)
        
        # Rotate axes
        axis_x.Rotate(math.radians(angle_x), axis_z)
        axis_y.Rotate(math.radians(angle_y), axis_x)
        axis_z.Rotate(math.radians(angle_z), axis_y)
        
        plane = rg.Plane(origin, axis_x, axis_y)
        
        # Define the size of the plane
        plane_width = random.uniform(0.1, 3.0)  # Random width between 0.1m and 3m
        plane_length = random.uniform(0.1, 3.0)  # Random length between 0.1m and 3m
        
        # Create a rectangular surface on the plane
        rectangle = rg.Rectangle3d(plane, plane_width, plane_length)
        surface = rg.Surface.CreateExtrusion(rectangle.ToNurbsCurve(), rg.Vector3d(0, 0, 0.01))
        
        # Convert surface to brep
        brep = surface.ToBrep()
        geometries.append(brep)
    
    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_suspended_intersecting_assembly(10.0, 5.0, 8.0, 20, 42)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_suspended_intersecting_assembly(15.0, 10.0, 12.0, 30, 7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_suspended_intersecting_assembly(12.0, 6.0, 10.0, 25, 99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_suspended_intersecting_assembly(8.0, 4.0, 6.0, 15, 123)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_suspended_intersecting_assembly(20.0, 15.0, 10.0, 50, 88)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
