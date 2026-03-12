# Created for 0015_0001_suspended_intersecting_assembly.json

""" Summary:
The provided function generates an architectural concept model based on the metaphor of a "Suspended Intersecting Assembly." It creates a series of suspended elements that appear to float, embodying lightness and fluidity through random placements and orientations. The function uses parameters such as base dimensions and element count to control the model's scale and complexity. Each element, represented as a box, is positioned at varying heights and angles, emphasizing the dynamic intersections and relationships described in the metaphor. This approach results in a visually interconnected and transparent structure that plays with gravity, aligning with the design task's intent."""

#! python 3
function_code = """def create_suspended_assembly(base_length=10, base_width=10, height=5, num_elements=5):
    \"""
    Generate a 'Suspended Intersecting Assembly' Concept Model.
    
    This function creates an architectural model with elements that appear suspended and intersecting,
    emphasizing lightness and fluidity. The design features hovering elements that intersect dynamically.
    
    Parameters:
    - base_length (float): The length of the base area in meters.
    - base_width (float): The width of the base area in meters.
    - height (float): The maximum height of the assembly in meters.
    - num_elements (int): The number of suspended elements to create.
    
    Returns:
    - List of Breps: A list of Brep geometries representing the suspended intersecting elements.
    \"""
    import Rhino
    import Rhino.Geometry as rg
    import random

    # Set seed for randomness to ensure replicability
    random.seed(42)

    # List to store the resulting geometries
    geometries = []

    # Define a base plane for reference
    base_plane = rg.Plane.WorldXY

    # Create suspended elements
    for i in range(num_elements):
        # Define random position within the base area
        x = random.uniform(-base_length / 2, base_length / 2)
        y = random.uniform(-base_width / 2, base_width / 2)
        
        # Define height position for suspension
        z = random.uniform(0, height)

        # Create a random direction vector for dynamic orientation
        direction = rg.Vector3d(random.uniform(-1, 1), random.uniform(-1, 1), random.uniform(-0.5, 0.5))
        direction.Unitize()

        # Create a simple elongated box to represent the suspended element
        box_length = random.uniform(1, 3)
        box_width = random.uniform(0.2, 0.5)
        box_height = random.uniform(0.2, 0.5)
        
        # Define the center point of the box
        center_point = rg.Point3d(x, y, z)

        # Create a base plane for the box oriented by the direction vector
        box_plane = rg.Plane(center_point, direction)

        # Create the box
        box = rg.Box(box_plane, rg.Interval(-box_length / 2, box_length / 2),
                     rg.Interval(-box_width / 2, box_width / 2),
                     rg.Interval(-box_height / 2, box_height / 2))

        # Convert the box to a Brep and add to the list
        brep = box.ToBrep()
        geometries.append(brep)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_suspended_assembly(base_length=15, base_width=10, height=8, num_elements=7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_suspended_assembly(base_length=12, base_width=12, height=6, num_elements=10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_suspended_assembly(base_length=20, base_width=15, height=10, num_elements=6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_suspended_assembly(base_length=18, base_width=9, height=7, num_elements=4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_suspended_assembly(base_length=14, base_width=11, height=9, num_elements=8)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
