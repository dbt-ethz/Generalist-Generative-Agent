# Created for 0015_0003_suspended_intersecting_assembly.json

""" Summary:
The function `create_suspended_intersecting_assembly` generates an architectural concept model inspired by the metaphor of "Suspended intersecting assembly." It creates a series of curved rod elements that simulate a floating structure by randomly positioning them within a specified 3D space. Each element is represented as a NURBS curve, which is then piped to form a cylindrical shape, embodying the lightness and fluidity described in the metaphor. The randomization of directions and placements results in overlapping arcs and lines, highlighting dynamic intersections and spatial relationships, ultimately creating a visually engaging and adaptable model that reflects the metaphor's essence."""

#! python 3
function_code = """def create_suspended_intersecting_assembly(seed, num_elements, element_length, element_radius):
    \"""
    Create an architectural Concept Model that encapsulates the 'Suspended intersecting assembly' metaphor.
    
    Parameters:
    - seed: int, a seed for randomness to ensure replicable results.
    - num_elements: int, the number of curved rod elements to create.
    - element_length: float, the length of each individual curved rod element in meters.
    - element_radius: float, the radius of the curved rod elements in meters.
    
    Returns:
    - A list of RhinoCommon Brep objects representing the architectural Concept Model.
    \"""
    import Rhino.Geometry as rg
    import random

    random.seed(seed)
    
    elements = []

    # Define the space where the elements will be suspended
    bounding_box = rg.BoundingBox(rg.Point3d(0, 0, 0), rg.Point3d(20, 20, 20))  # 20x20x20 meter space

    for _ in range(num_elements):
        # Randomly choose a base plane within the bounding box for the element
        origin_x = random.uniform(bounding_box.Min.X, bounding_box.Max.X)
        origin_y = random.uniform(bounding_box.Min.Y, bounding_box.Max.Y)
        origin_z = random.uniform(bounding_box.Min.Z, bounding_box.Max.Z)

        base_point = rg.Point3d(origin_x, origin_y, origin_z)
        
        # Create a random direction for the rod
        direction_x = random.uniform(-1.0, 1.0)
        direction_y = random.uniform(-1.0, 1.0)
        direction_z = random.uniform(-1.0, 1.0)

        direction = rg.Vector3d(direction_x, direction_y, direction_z)
        direction.Unitize()
        
        # Create a curved rod using a NURBS curve
        curve_points = [
            base_point,
            base_point + direction * (element_length * 0.33),
            base_point + direction * (element_length * 0.66),
            base_point + direction * element_length
        ]
        
        rod_curve = rg.NurbsCurve.Create(False, 3, curve_points)
        
        # Pipe the curve to create a 3D cylindrical element
        rod_brep = rg.Brep.CreatePipe(rod_curve, element_radius, False, rg.PipeCapMode.Round, True, 0.01, 0.01)[0]
        
        elements.append(rod_brep)

    return elements"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_suspended_intersecting_assembly(42, 10, 5.0, 0.2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_suspended_intersecting_assembly(123, 15, 3.5, 0.1)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_suspended_intersecting_assembly(7, 20, 4.0, 0.15)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_suspended_intersecting_assembly(99, 8, 6.0, 0.3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_suspended_intersecting_assembly(2023, 12, 2.5, 0.25)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
