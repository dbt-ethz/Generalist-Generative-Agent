# Created for 0015_0002_suspended_intersecting_assembly.json

""" Summary:
The provided function generates an architectural concept model based on the metaphor "Suspended intersecting assembly." By using parameters such as base length, height, and the number of layers, it creates a series of elevated geometries that emulate a floating structure. The model incorporates fine tensile cables to illustrate the suspended nature, while semi-transparent materials, like frosted glass, depict floating elements and their intersections. This design emphasizes fluidity and lightness, creating negative spaces between intersecting components. Reflective surfaces enhance the perception of interconnectivity, allowing light to interact dynamically with the model, embodying the metaphor's essence."""

#! python 3
function_code = """def create_suspended_intersecting_assembly(seed_value, base_length, height, num_layers):
    \"""
    Create an architectural Concept Model based on the 'Suspended intersecting assembly' metaphor.
    
    This function generates a model using intersecting and elevated geometries to emulate a floating
    assembly of architectural elements. It uses a framework of fine tensile cables and semi-transparent
    materials to illustrate the dynamic interplay of spatial components.

    Parameters:
    - seed_value (int): A seed for the random number generator to ensure replicability.
    - base_length (float): The base length of the model in meters, representing the span of the assembly.
    - height (float): The vertical extent of the model in meters, depicting the elevation of elements.
    - num_layers (int): The number of layers of intersecting elements to create.

    Returns:
    - List of RhinoCommon Breps: A list of 3D geometries representing the concept model, including
      semi-transparent surfaces and reflective elements to enhance the perception of suspension.

    \"""
    import Rhino
    import random
    from Rhino.Geometry import Point3d, Line, Brep, Plane, Surface, Mesh, Vector3d, Rectangle3d

    # Ensure reproducibility with a fixed seed
    random.seed(seed_value)

    # Create base points for the assembly
    base_points = [Point3d(random.uniform(-base_length/2, base_length/2), 
                           random.uniform(-base_length/2, base_length/2), 
                           random.uniform(0, height)) for _ in range(num_layers)]

    # Generate intersecting lines to represent the tensile cables
    lines = []
    for i in range(num_layers - 1):
        line = Line(base_points[i], base_points[i + 1])
        lines.append(line)

    # Create semi-transparent surfaces between lines
    surfaces = []
    for line in lines:
        start = line.From
        end = line.To
        mid_point = Point3d((start.X + end.X) / 2, (start.Y + end.Y) / 2, (start.Z + end.Z) / 2)
        plane = Plane(mid_point, Vector3d.ZAxis)
        surface = Surface.CreateExtrusion(line.ToNurbsCurve(), Vector3d.ZAxis * random.uniform(0.3, 0.7))
        surfaces.append(surface)

    # Create reflective meshes to enhance perception
    meshes = []
    for i in range(num_layers):
        if i % 2 == 0:
            rect = Rectangle3d(Plane(base_points[i], Vector3d.ZAxis), random.uniform(0.5, 1.0), random.uniform(0.5, 1.0))
            mesh = Mesh.CreateFromBrep(Brep.CreateFromCornerPoints(rect.Corner(0), rect.Corner(1), rect.Corner(2), rect.Corner(3), 0.01))
            meshes.extend(mesh if mesh else [])

    # Combine all geometries into a single list of breps
    geometries = [Brep.CreateFromSurface(s) for s in surfaces] + [Brep.CreateFromMesh(m, True) for m in meshes]

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_suspended_intersecting_assembly(42, 10.0, 5.0, 3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_suspended_intersecting_assembly(7, 15.0, 10.0, 5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_suspended_intersecting_assembly(99, 8.0, 4.0, 6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_suspended_intersecting_assembly(15, 12.0, 8.0, 4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_suspended_intersecting_assembly(21, 20.0, 6.0, 2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
