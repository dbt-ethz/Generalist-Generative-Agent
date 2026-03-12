# Created for 0019_0004_subterranean_cavern.json

""" Summary:
The provided function generates an architectural concept model inspired by the metaphor of a "subterranean cavern" by creating a series of interconnected, curvilinear volumes. It employs parameters such as volume radius, height, number of shells, and curvature intensity to design nested structures that evoke depth and transition from intimate to open spaces. The use of randomized curvature in the base profiles enhances organic forms, mimicking natural cave structures. The function emphasizes light and shadow play through varying translucency, encapsulating the metaphor's essence of exploration, refuge, and the unveiling of hidden environments within the architectural design."""

#! python 3
function_code = """def create_subterranean_cavern_model(volume_radius, volume_height, num_shells, curvature_intensity, seed=42):
    \"""
    Generates an architectural Concept Model inspired by the 'subterranean cavern' metaphor.
    The function creates a series of interconnected, curvilinear volumes that suggest depth and
    transitions from intimate, enclosed spaces to more open areas. The design emphasizes organic 
    forms with a play of light and shadow.

    Parameters:
    - volume_radius (float): The base radius of the outermost cavern volume in meters.
    - volume_height (float): The total height of the cavern model in meters.
    - num_shells (int): The number of nested shells or volumes to create.
    - curvature_intensity (float): Intensity of curvature to create more organic forms (0 to 1).
    - seed (int): Seed for random number generation to ensure replicable results.

    Returns:
    - List of RhinoCommon Brep objects representing the 3D geometries of the concept model.
    \"""
    import Rhino.Geometry as rg
    import random

    # Set the random seed
    random.seed(seed)

    geometries = []

    # Calculate the height and radius decrement per shell
    height_decrement = volume_height / num_shells
    radius_decrement = volume_radius / num_shells

    # Create a series of nested shells
    for i in range(num_shells):
        current_radius = volume_radius - (i * radius_decrement)
        current_height = volume_height - (i * height_decrement)

        # Create a base profile curve with added curvature
        base_curve = rg.Circle(rg.Plane.WorldXY, current_radius).ToNurbsCurve()
        control_points = base_curve.Points
        for j in range(1, control_points.Count - 1):
            # Introduce curvature using random offsets
            offset = curvature_intensity * current_radius * random.uniform(-0.1, 0.1)
            control_point = control_points[j]
            control_point.Location += rg.Vector3d(offset, offset, 0)
            control_points[j] = control_point

        # Create a lofted volume from the modified base curve
        top_curve = base_curve.Duplicate()
        top_curve.Translate(rg.Vector3d(0, 0, current_height))

        loft = rg.Brep.CreateFromLoft([base_curve, top_curve], rg.Point3d.Unset, rg.Point3d.Unset, rg.LoftType.Normal, False)
        if loft:
            geometries.append(loft[0])

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_subterranean_cavern_model(10.0, 20.0, 5, 0.8)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_subterranean_cavern_model(15.0, 30.0, 7, 0.6, seed=100)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_subterranean_cavern_model(12.0, 25.0, 6, 0.5, seed=50)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_subterranean_cavern_model(8.0, 15.0, 4, 0.7, seed=23)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_subterranean_cavern_model(20.0, 40.0, 10, 0.9, seed=10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
