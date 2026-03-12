# Created for 0015_0001_suspended_intersecting_assembly.json

""" Summary:
The provided function, `create_suspended_intersecting_assembly`, generates an architectural concept model inspired by the metaphor of "Suspended intersecting assembly." By defining parameters like base dimensions, height, and the number of elements, it creates a series of cylindrical elements that appear to float within the specified space. The function uses randomization to determine the positions and dimensions of these elements, ensuring a dynamic arrangement that emphasizes lightness and fluidity. The resulting geometries, represented as Brep objects, embody structural transparency and interconnectivity, aligning with the metaphor's core themes of balance, gravity interplay, and spatial dialogue."""

#! python 3
function_code = """def create_suspended_intersecting_assembly(base_length, base_width, height, num_elements, randomness_seed):
    \"""
    Generates a Concept Model based on the 'Suspended intersecting assembly' metaphor.
    This model features elements that appear to float and intersect within a given space, emphasizing lightness and fluidity.

    Parameters:
    - base_length (float): The length of the base area in meters.
    - base_width (float): The width of the base area in meters.
    - height (float): The height of the space in meters.
    - num_elements (int): Number of intersecting elements to create.
    - randomness_seed (int): Seed for random number generator to ensure replicable results.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep objects representing the intersecting elements.
    \"""
    import Rhino
    import random
    from Rhino.Geometry import Brep, Point3d, Plane, Circle, Cylinder

    # Set the random seed
    random.seed(randomness_seed)

    # List to store the created geometries
    geometries = []

    # Create elements
    for _ in range(num_elements):
        # Randomly determine the position of the element
        x = random.uniform(0.2 * base_length, 0.8 * base_length)
        y = random.uniform(0.2 * base_width, 0.8 * base_width)
        z = random.uniform(0.5 * height, height)

        # Randomly determine the radius and height of the cylindrical element
        radius = random.uniform(0.2, 1.0)
        element_height = random.uniform(2.0, 5.0)

        # Create a cylinder representing the element
        base_point = Point3d(x, y, z - element_height / 2)
        axis_vector = Rhino.Geometry.Vector3d(0, 0, 1)
        base_plane = Plane(base_point, axis_vector)
        circle = Circle(base_plane, radius)
        cylinder = Cylinder(circle, element_height)

        # Convert cylinder to Brep and add to the list
        brep = cylinder.ToBrep(True, True)
        if brep is not None:
            geometries.append(brep)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_suspended_intersecting_assembly(10.0, 5.0, 8.0, 15, 42)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_suspended_intersecting_assembly(12.0, 6.0, 10.0, 20, 7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_suspended_intersecting_assembly(8.0, 4.0, 6.0, 10, 99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_suspended_intersecting_assembly(15.0, 7.0, 12.0, 25, 3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_suspended_intersecting_assembly(9.0, 4.5, 7.0, 18, 15)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
