# Created for 0015_0002_suspended_intersecting_assembly.json

""" Summary:
The provided function generates an architectural concept model that embodies the metaphor of a "Suspended intersecting assembly." It creates elevated elements using randomized positions and orientations, simulating a dynamic interplay of overlapping volumes that appear to float. By varying the heights and positions of these elements, the model captures the essence of lightness and fluidity, essential traits of the metaphor. The introduction of tensile cables conceptually represents the suspension of these components, while the use of semi-transparent materials enhances the visual complexity and transparency. This approach fosters a cohesive spatial network, emphasizing interconnectivity and negative space."""

#! python 3
function_code = """def create_suspended_intersecting_assembly(base_length=20, base_width=10, height=15, num_elements=5, seed=42):
    \"""
    Generates an architectural Concept Model based on the metaphor 'Suspended intersecting assembly'.
    The model features elevated elements that create a dynamic interplay of overlapping and crossing volumes.

    Parameters:
    - base_length (float): The length of the base area in meters.
    - base_width (float): The width of the base area in meters.
    - height (float): Maximum height of the assembly in meters.
    - num_elements (int): Number of intersecting elements to generate.
    - seed (int): Seed for randomness to ensure replicable results.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep geometries representing the concept model.
    \"""
    import Rhino.Geometry as rg
    import random

    random.seed(seed)
    breps = []

    # Create a base plane
    base_plane = rg.Plane.WorldXY

    # Generate random positions for elements
    for _ in range(num_elements):
        # Random position within the base area
        x = random.uniform(0, base_length)
        y = random.uniform(0, base_width)
        z = random.uniform(height * 0.3, height)  # Elevated start

        # Create a random orientation vector
        dir_vector = rg.Vector3d(random.uniform(-1, 1), random.uniform(-1, 1), random.uniform(-0.5, 0.5))
        dir_vector.Unitize()

        # Define the length of the element
        element_length = random.uniform(base_width * 0.5, base_length)

        # Create a box representing the element
        element_origin = rg.Point3d(x, y, z)
        element_plane = rg.Plane(element_origin, dir_vector)
        box = rg.Box(element_plane, rg.Interval(-0.5, 0.5), rg.Interval(-0.5, 0.5), rg.Interval(0, element_length))
        brep = box.ToBrep()

        # Use semi-transparent material (conceptual)
        # In Rhino, this would be applied as a material property, not directly in the geometry

        breps.append(brep)

    # Add tensile cables (conceptually represented as thin lines)
    for i in range(num_elements):
        start = breps[i].GetBoundingBox(True).Center
        end = rg.Point3d(random.uniform(0, base_length), random.uniform(0, base_width), 0)  # Grounded end
        line = rg.Line(start, end)
        line_brep = rg.Brep.CreateFromSurface(rg.NurbsSurface.CreateFromCorners(line.From, line.To, line.To))
        breps.append(line_brep)

    return breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_suspended_intersecting_assembly(base_length=25, base_width=15, height=20, num_elements=10, seed=7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_suspended_intersecting_assembly(base_length=30, base_width=20, height=25, num_elements=8, seed=100)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_suspended_intersecting_assembly(base_length=18, base_width=12, height=10, num_elements=6, seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_suspended_intersecting_assembly(base_length=22, base_width=14, height=18, num_elements=7, seed=5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_suspended_intersecting_assembly(base_length=28, base_width=18, height=22, num_elements=12, seed=3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
