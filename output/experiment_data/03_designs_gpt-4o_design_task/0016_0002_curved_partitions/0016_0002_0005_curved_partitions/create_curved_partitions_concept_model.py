# Created for 0016_0002_curved_partitions.json

""" Summary:
The function `create_curved_partitions_concept_model` generates an architectural concept model based on the metaphor of "curved partitions." It creates layered, sweeping curves that emulate natural landscapes, reflecting fluidity and organic movement. By defining control points with random vertical displacements and extruding them into surfaces, the model forms a visually dynamic structure that encourages exploration. The varying heights and curve displacements embody the metaphor's implications of intimacy and openness, allowing light to filter through and creating engaging spatial relationships. The function ultimately produces a series of geometrically intricate Breps that resonate with the architectural vision."""

#! python 3
function_code = """def create_curved_partitions_concept_model(num_layers=5, layer_height=2.0, max_curve_displacement=3.0, seed=42):
    \"""
    Creates an architectural Concept Model based on the 'curved partitions' metaphor, using layered sweeping curves
    to mimic natural landscapes. The model emphasizes the fluidity and organic movement of spaces, guiding circulation
    and creating zones of varying intimacy.

    Parameters:
    - num_layers (int): The number of curved partitions to generate.
    - layer_height (float): The vertical distance between each layer.
    - max_curve_displacement (float): The maximum displacement of the curves from a straight line.
    - seed (int): The seed for random number generation to ensure replicability.

    Returns:
    - List of Rhino.Geometry.Brep: A list of breps representing the curved partitions.
    \"""
    import Rhino
    import random
    from Rhino.Geometry import Point3d, NurbsCurve, Brep

    random.seed(seed)
    partitions = []

    for i in range(num_layers):
        # Define control points for a sweeping curve
        points = []
        for j in range(5):
            x = j * 5.0  # Spacing between control points
            y = random.uniform(-max_curve_displacement, max_curve_displacement)
            z = i * layer_height
            points.append(Point3d(x, y, z))

        # Create a NURBS curve from the control points
        curve = NurbsCurve.Create(False, 3, points)

        # Create a surface by extruding the curve along the Y-axis
        start_point = curve.PointAtStart
        end_point = Point3d(start_point.X, start_point.Y + 1.0, start_point.Z)
        line = Rhino.Geometry.Line(start_point, end_point)
        surface = Rhino.Geometry.Surface.CreateExtrusion(curve, line.Direction)

        # Convert the surface to a Brep
        brep = surface.ToBrep()
        partitions.append(brep)

    return partitions"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_curved_partitions_concept_model(num_layers=10, layer_height=3.0, max_curve_displacement=5.0, seed=123)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_curved_partitions_concept_model(num_layers=7, layer_height=1.5, max_curve_displacement=2.5, seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_curved_partitions_concept_model(num_layers=8, layer_height=2.5, max_curve_displacement=4.0, seed=58)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_curved_partitions_concept_model(num_layers=6, layer_height=4.0, max_curve_displacement=2.0, seed=77)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_curved_partitions_concept_model(num_layers=12, layer_height=2.0, max_curve_displacement=3.5, seed=30)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
