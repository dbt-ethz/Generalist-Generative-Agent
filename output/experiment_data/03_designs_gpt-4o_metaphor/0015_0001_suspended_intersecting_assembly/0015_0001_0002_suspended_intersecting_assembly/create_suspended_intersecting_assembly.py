# Created for 0015_0001_suspended_intersecting_assembly.json

""" Summary:
The function `create_suspended_intersecting_assembly` generates an architectural concept model based on the metaphor of a "Suspended intersecting assembly." It creates a series of floating 3D elements within a defined space, emphasizing lightness and fluidity. Each element's dimensions and positions are randomly generated, ensuring a diverse and dynamic assembly. The function further introduces intersections between elements, highlighting structural transparency and visual interconnectivity. By varying parameters such as base dimensions and the number of elements, the function produces multiple design iterations, allowing architects to explore different spatial relationships and configurations that align with the metaphor's qualities."""

#! python 3
function_code = """def create_suspended_intersecting_assembly(base_length=10, base_width=5, height=5, num_elements=5, random_seed=42):
    \"""
    Creates a suspended intersecting assembly concept model characterized by elevated and floating elements
    with dynamic intersections and connections, emphasizing lightness and fluidity.

    Parameters:
    - base_length (float): The length of the base plane in meters.
    - base_width (float): The width of the base plane in meters.
    - height (float): The maximum height of the assembly in meters.
    - num_elements (int): The number of floating elements to create.
    - random_seed (int): The seed for random number generation to ensure replicability.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of 3D breps representing the suspended intersecting elements.
    \"""
    import Rhino.Geometry as rg
    import random
    
    random.seed(random_seed)
    
    elements = []
    
    # Create a base plane
    base_plane = rg.Plane.WorldXY
    
    # Create a bounding box for the space
    bbox = rg.BoundingBox(base_plane.Origin, base_plane.Origin + rg.Vector3d(base_length, base_width, height))
    
    # Generate random suspended elements
    for _ in range(num_elements):
        # Random dimensions for the element
        element_length = random.uniform(1, base_length / 3)
        element_width = random.uniform(0.5, base_width / 3)
        element_height = random.uniform(0.5, height / 3)
        
        # Random position within the bounding box
        x_pos = random.uniform(bbox.Min.X, bbox.Max.X - element_length)
        y_pos = random.uniform(bbox.Min.Y, bbox.Max.Y - element_width)
        z_pos = random.uniform(bbox.Min.Z + element_height, bbox.Max.Z - element_height)
        
        # Create a box (as brep) for the element
        element_box = rg.Box(
            rg.Plane(rg.Point3d(x_pos, y_pos, z_pos), base_plane.XAxis, base_plane.YAxis),
            rg.Interval(0, element_length),
            rg.Interval(0, element_width),
            rg.Interval(0, element_height)
        ).ToBrep()
        
        elements.append(element_box)
    
    # Introduce intersections by combining some elements
    for i in range(len(elements) - 1):
        current_element = elements[i]
        next_element = elements[i + 1]
        
        # Create an intersection brep
        intersection = rg.Brep.CreateBooleanIntersection(current_element, next_element, 0.001)
        if intersection:
            elements.append(intersection[0])
    
    return elements"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_suspended_intersecting_assembly(base_length=15, base_width=8, height=10, num_elements=7, random_seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_suspended_intersecting_assembly(base_length=20, base_width=10, height=7, num_elements=10, random_seed=123)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_suspended_intersecting_assembly(base_length=12, base_width=6, height=4, num_elements=6, random_seed=56)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_suspended_intersecting_assembly(base_length=18, base_width=9, height=12, num_elements=8, random_seed=77)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_suspended_intersecting_assembly(base_length=25, base_width=15, height=15, num_elements=12, random_seed=30)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
