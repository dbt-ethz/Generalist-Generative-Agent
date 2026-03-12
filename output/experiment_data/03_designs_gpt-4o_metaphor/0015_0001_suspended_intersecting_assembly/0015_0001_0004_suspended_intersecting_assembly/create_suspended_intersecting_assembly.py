# Created for 0015_0001_suspended_intersecting_assembly.json

""" Summary:
The provided function, `create_suspended_intersecting_assembly`, generates an architectural concept model inspired by the metaphor of a "Suspended intersecting assembly." It creates a series of elevated elements that appear to float within a defined space, emphasizing lightness and fluidity. The function randomly determines the positions of these elements within a circular base area, adjusting their height to reflect the metaphor's play with gravity. By generating multiple geometric elements with varying dimensions and positions, the function fosters dynamic intersections and connections, embodying the metaphor's essence of structural transparency and spatial dialogue. The resulting geometries can be visualized and further manipulated in architectural design software."""

#! python 3
function_code = """def create_suspended_intersecting_assembly(base_radius, height, num_elements, element_width, element_height, seed=None):
    \"""
    Creates a concept model based on the metaphor of a 'Suspended intersecting assembly'.
    
    This model consists of elements that are elevated and appear to float within the space,
    creating dynamic intersections and connections, emphasizing lightness and fluidity.

    Parameters:
    - base_radius (float): The radius of the base circular area where elements are distributed.
    - height (float): The maximum height up to which elements are suspended.
    - num_elements (int): The number of elements in the assembly.
    - element_width (float): The width of each element.
    - element_height (float): The height of each element.
    - seed (int, optional): A seed for the random number generator to ensure replicability.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep geometries representing the suspended elements.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    if seed is not None:
        random.seed(seed)

    elements = []

    for i in range(num_elements):
        # Randomly determine the angle and radius for each element's position
        angle = random.uniform(0, 2 * math.pi)
        radius = random.uniform(0.1 * base_radius, base_radius)

        # Calculate the position in the circular base area
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)

        # Random height within the specified range
        z = random.uniform(0.1 * height, height)

        # Create a box element at this position
        base_point = rg.Point3d(x, y, z)
        box_corners = [
            base_point,
            rg.Point3d(x + element_width, y, z),
            rg.Point3d(x + element_width, y + element_width, z),
            rg.Point3d(x, y + element_width, z),
            rg.Point3d(x, y, z + element_height),
            rg.Point3d(x + element_width, y, z + element_height),
            rg.Point3d(x + element_width, y + element_width, z + element_height),
            rg.Point3d(x, y + element_width, z + element_height)
        ]

        box = rg.Brep.CreateFromBox(box_corners)

        if box:
            elements.append(box)

    return elements"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_suspended_intersecting_assembly(10.0, 15.0, 5, 2.0, 3.0, seed=42)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_suspended_intersecting_assembly(8.0, 12.0, 10, 1.5, 2.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_suspended_intersecting_assembly(12.0, 20.0, 8, 3.0, 4.0, seed=100)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_suspended_intersecting_assembly(15.0, 25.0, 7, 2.5, 3.5, seed=7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_suspended_intersecting_assembly(5.0, 10.0, 6, 1.0, 2.0, seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
