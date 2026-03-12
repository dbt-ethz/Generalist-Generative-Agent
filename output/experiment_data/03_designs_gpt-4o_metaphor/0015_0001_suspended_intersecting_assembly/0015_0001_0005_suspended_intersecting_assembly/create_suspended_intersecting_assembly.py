# Created for 0015_0001_suspended_intersecting_assembly.json

""" Summary:
The provided function generates an architectural concept model inspired by the metaphor of a "Suspended intersecting assembly." It creates a series of elevated, floating elements within a defined 3D space, embodying traits like lightness and fluidity. Each element is randomly positioned and oriented, with its length and tilt varying to enhance the perception of balance and play with gravity. The intersections of these elements foster dynamic spatial relationships, reflecting the interconnectedness emphasized in the metaphor. Ultimately, the function outputs a list of 3D geometries, capturing the essence of the design task while ensuring variability through randomization."""

#! python 3
function_code = """def create_suspended_intersecting_assembly(base_length, base_width, height, num_elements, seed=42):
    \"""
    Creates an architectural Concept Model based on the metaphor of a 'Suspended intersecting assembly'.
    
    This model generates a series of elevated and floating elements that intersect dynamically within a defined space.
    The design emphasizes lightness, fluidity, and a play with gravity, creating a network of spatial relationships.

    Parameters:
    - base_length (float): The length of the base area in meters.
    - base_width (float): The width of the base area in meters.
    - height (float): The maximum height of the space in meters.
    - num_elements (int): The number of intersecting elements to generate.
    - seed (int): A seed for the random number generator to ensure replicability.

    Returns:
    - list of Rhino.Geometry.Brep: A list of 3D geometries representing the concept model.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    random.seed(seed)
    elements = []

    for _ in range(num_elements):
        # Randomly position the base of each element within the base area
        base_x = random.uniform(0, base_length)
        base_y = random.uniform(0, base_width)
        base_point = rg.Point3d(base_x, base_y, 0)

        # Randomly determine the orientation and length of each element
        length = random.uniform(0.2 * height, 0.8 * height)
        angle_xy = random.uniform(0, 2 * math.pi)
        angle_z = random.uniform(-math.pi / 6, math.pi / 6)  # Slight tilt

        # Create the direction vector for the extrusion
        direction = rg.Vector3d(length * math.cos(angle_xy), length * math.sin(angle_xy), length * math.sin(angle_z))
        
        # Create a rectangular profile for the element
        profile = rg.Rectangle3d(rg.Plane.WorldXY, random.uniform(0.1, 0.3), random.uniform(0.1, 0.3)).ToNurbsCurve()

        # Extrude the profile along the direction vector
        extrusion = rg.Extrusion.Create(profile, direction.Length, True)
        extrusion.Rotate(angle_xy, rg.Vector3d.ZAxis, base_point)
        extrusion.Translate(rg.Vector3d(base_point))

        # Convert extrusion to Brep for compatibility
        brep = extrusion.ToBrep()
        if brep:
            elements.append(brep)

    return elements"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_suspended_intersecting_assembly(10.0, 5.0, 15.0, 20)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_suspended_intersecting_assembly(8.0, 4.0, 12.0, 15, seed=123)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_suspended_intersecting_assembly(12.0, 6.0, 10.0, 25, seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_suspended_intersecting_assembly(15.0, 7.0, 20.0, 30, seed=77)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_suspended_intersecting_assembly(9.0, 3.5, 18.0, 10, seed=56)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
