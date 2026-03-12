# Created for 0015_0003_suspended_intersecting_assembly.json

""" Summary:
The function `create_suspended_intersecting_assembly` generates an architectural concept model based on the metaphor of a "Suspended intersecting assembly." It creates a series of 3D geometries representing elevated, curved elements that appear to float and intersect dynamically. By arranging these elements in a grid pattern with varying heights and orientations, the function emphasizes lightness and fluidity, reflecting the metaphor's key traits. The use of random control points for curves simulates organic movement, while modular connections allow for adaptability. This model captures the delicate balance and transparency implied in the design task, enhancing spatial relationships and engagement."""

#! python 3
function_code = """def create_suspended_intersecting_assembly(seed=42, num_elements=15, max_height=20.0, element_radius=0.15, grid_size=10) -> list:
    \"""
    Creates an architectural Concept Model that encapsulates the 'Suspended intersecting assembly' metaphor.

    The function generates a network of intersecting, suspended elements using curves and rods to emphasize lightness
    and fluidity. Elements are arranged in a grid-like pattern with varying heights and orientations to simulate 
    suspension and dynamic intersections.

    Args:
        seed (int): Seed for random number generator to ensure replicable results.
        num_elements (int): Number of curved elements to generate.
        max_height (float): Maximum height for the suspension of elements.
        element_radius (float): Radius of each element in meters.
        grid_size (int): The size of the grid to generate base points for elements.

    Returns:
        list: A list of RhinoCommon Brep objects representing the 3D geometries of the concept model.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    random.seed(seed)
    geometries = []

    # Define the grid plane and spacing
    grid_space = grid_size / math.sqrt(num_elements)

    for i in range(num_elements):
        # Calculate grid position
        row = i // int(math.sqrt(num_elements))
        column = i % int(math.sqrt(num_elements))
        
        # Define base point in grid
        base_x = column * grid_space - grid_size / 2
        base_y = row * grid_space - grid_size / 2
        base_z = random.uniform(1, max_height)

        base_point = rg.Point3d(base_x, base_y, base_z)

        # Create a dynamic curve with random control points
        control_points = [
            base_point,
            rg.Point3d(base_x + random.uniform(-1, 1), base_y + random.uniform(-1, 1), base_z + random.uniform(1, 5)),
            rg.Point3d(base_x + random.uniform(-1, 1), base_y + random.uniform(-1, 1), base_z + random.uniform(1, 5)),
            rg.Point3d(base_x + random.uniform(-1, 1), base_y + random.uniform(-1, 1), base_z)
        ]

        nurbs_curve = rg.NurbsCurve.Create(False, 3, control_points)

        # Create a pipe around the curve to represent a flexible rod
        rod_brep = rg.Brep.CreatePipe(nurbs_curve, element_radius, False, rg.PipeCapMode.Round, True, 0.01, 0.01)[0]

        # Add the rod to the list of geometries
        geometries.append(rod_brep)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_suspended_intersecting_assembly(seed=10, num_elements=20, max_height=15.0, element_radius=0.1, grid_size=12)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_suspended_intersecting_assembly(seed=5, num_elements=25, max_height=18.0, element_radius=0.2, grid_size=15)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_suspended_intersecting_assembly(seed=15, num_elements=30, max_height=25.0, element_radius=0.2, grid_size=20)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_suspended_intersecting_assembly(seed=8, num_elements=18, max_height=22.0, element_radius=0.18, grid_size=14)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_suspended_intersecting_assembly(seed=12, num_elements=10, max_height=10.0, element_radius=0.12, grid_size=8)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
