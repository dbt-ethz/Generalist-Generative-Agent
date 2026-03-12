# Created for 0015_0002_suspended_intersecting_assembly.json

""" Summary:
The function `create_suspended_intersecting_assembly` generates an architectural concept model based on the metaphor of a "Suspended intersecting assembly." It creates a dynamic array of floating elements, represented as spheres, and connects them with a framework of tensile cables, mimicking the metaphor's emphasis on lightness and fluidity. By varying cable density, element size, and the number of elements, the function introduces spatial complexity and visual interconnectivity. The random placement of elements and cables reflects the dynamic intersections described in the metaphor, while the use of 3D geometries illustrates the delicate balance and structural elegance inherent in the design task."""

#! python 3
function_code = """def create_suspended_intersecting_assembly(cable_density=5, element_size=2, num_elements=10, seed=42):
    \"""
    Create an architectural Concept Model representing the 'Suspended intersecting assembly' metaphor.
    This function generates a series of floating elements connected by a framework of tensile cables.

    Parameters:
    - cable_density (int): The density of the cables forming the framework. Higher values increase complexity.
    - element_size (float): The approximate size of each floating element.
    - num_elements (int): The number of floating elements to create.
    - seed (int): Seed for random number generator to ensure replicable results.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of 3D brep geometries representing the concept model.
    \"""
    import Rhino
    import System
    import random
    from Rhino.Geometry import Point3d, Vector3d, Brep, Sphere, Line, Polyline

    random.seed(seed)
    elements = []
    cables = []

    # Create floating elements
    for _ in range(num_elements):
        center = Point3d(random.uniform(-10, 10), random.uniform(-10, 10), random.uniform(0, 10))
        sphere = Sphere(center, element_size * random.uniform(0.8, 1.2)).ToBrep()
        elements.append(sphere)

    # Create tensile cables (as polylines for simplicity)
    for i in range(cable_density):
        start_pt = Point3d(random.uniform(-10, 10), random.uniform(-10, 10), random.uniform(-5, 15))
        end_pt = Point3d(random.uniform(-10, 10), random.uniform(-10, 10), random.uniform(-5, 15))
        line = Line(start_pt, end_pt)
        polyline = Polyline([line.From, line.To])
        cables.append(polyline.ToNurbsCurve())

    # Combine elements and cables into a single list of breps
    concept_model = elements + cables
    
    return concept_model"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_suspended_intersecting_assembly(cable_density=10, element_size=3, num_elements=15, seed=123)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_suspended_intersecting_assembly(cable_density=7, element_size=4, num_elements=20, seed=56)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_suspended_intersecting_assembly(cable_density=8, element_size=2.5, num_elements=12, seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_suspended_intersecting_assembly(cable_density=6, element_size=1.5, num_elements=8, seed=30)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_suspended_intersecting_assembly(cable_density=12, element_size=2, num_elements=5, seed=77)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
