# Created for 0015_0001_suspended_intersecting_assembly.json

""" Summary:
The provided function `create_suspended_intersecting_assembly` generates an architectural concept model based on the metaphor of "Suspended intersecting assembly." It constructs a dynamic 3D model comprising lightweight panels suspended by cables, emphasizing fluidity and transparency. The function randomly positions and orients panels within specified dimensions, simulating intersections at various angles to reflect the metaphor's essence. By creating a network of cables that connect these panels, the model visually represents balance and tension, capturing the idea of elements that appear to float. The outcome is a complex, interconnected structure that embodies the principles of lightness and spatial dialogue."""

#! python 3
function_code = """def create_suspended_intersecting_assembly(base_length, base_width, height, num_cables, num_panels, seed):
    \"""
    Creates an architectural Concept Model embodying the 'Suspended intersecting assembly' metaphor.
    
    This function generates a model composed of intersecting panels suspended by cables, emphasizing lightness
    and fluidity. The cables create a network of connections, while the panels intersect at various angles
    to enhance structural transparency and balance.
    
    Parameters:
    - base_length (float): The length of the base area for the model (in meters).
    - base_width (float): The width of the base area for the model (in meters).
    - height (float): The maximum height of the model (in meters).
    - num_cables (int): The number of cables to create for suspending panels.
    - num_panels (int): The number of intersecting panels to create.
    - seed (int): Seed for the random number generator to ensure replicable results.
    
    Returns:
    - List of Rhino.Geometry.Brep: A list of breps representing the 3D geometries of the concept model.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    random.seed(seed)
    geometries = []

    # Create cables
    for _ in range(num_cables):
        start_point = rg.Point3d(random.uniform(0, base_length), random.uniform(0, base_width), height)
        end_point = rg.Point3d(random.uniform(0, base_length), random.uniform(0, base_width), 0)
        cable = rg.Line(start_point, end_point)
        cable_curve = cable.ToNurbsCurve()
        geometries.append(rg.Brep.CreatePipe(cable_curve, 0.02, True, rg.PipeCapMode.Flat, True, 0.01, 0.01)[0])

    # Create panels
    for _ in range(num_panels):
        # Randomly generate the position within the bounding box
        x = random.uniform(0, base_length)
        y = random.uniform(0, base_width)
        z = random.uniform(0, height)

        # Create a random orientation for the panel
        angle_x = random.uniform(0, 360)
        angle_y = random.uniform(0, 360)
        angle_z = random.uniform(0, 360)

        # Create a plane at the random position with random orientation
        origin = rg.Point3d(x, y, z)
        plane = rg.Plane.WorldXY
        plane.Origin = origin
        plane.Rotate(math.radians(angle_x), plane.XAxis)
        plane.Rotate(math.radians(angle_y), plane.YAxis)
        plane.Rotate(math.radians(angle_z), plane.ZAxis)

        # Define the size of the panel
        panel_width = random.uniform(0.5, 2.0)  # Random width between 0.5m and 2m
        panel_length = random.uniform(0.5, 2.0)  # Random length between 0.5m and 2m

        # Create a rectangular panel on the plane
        rectangle = rg.Rectangle3d(plane, panel_width, panel_length)
        panel_surface = rg.Brep.CreatePlanarBreps(rectangle.ToNurbsCurve())[0]
        
        # Add to the list of geometries
        geometries.append(panel_surface)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_suspended_intersecting_assembly(10.0, 5.0, 15.0, 20, 10, 42)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_suspended_intersecting_assembly(8.0, 4.0, 12.0, 15, 8, 7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_suspended_intersecting_assembly(12.0, 6.0, 20.0, 25, 12, 99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_suspended_intersecting_assembly(15.0, 7.0, 18.0, 30, 15, 56)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_suspended_intersecting_assembly(9.0, 3.0, 10.0, 18, 9, 15)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
