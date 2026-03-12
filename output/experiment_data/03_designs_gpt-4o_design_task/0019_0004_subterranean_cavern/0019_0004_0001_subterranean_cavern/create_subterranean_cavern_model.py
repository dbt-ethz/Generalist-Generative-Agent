# Created for 0019_0004_subterranean_cavern.json

""" Summary:
The provided function, `create_subterranean_cavern_model`, generates an architectural concept model inspired by the metaphor of a subterranean cavern. It creates a series of nested, curvilinear shells that represent geological layers, enhancing depth and exploration. The model employs random height variations and base radii to mimic the organic forms of natural caverns. Small openings are introduced to allow light to filter through, creating dynamic shadows and enhancing the mysterious atmosphere. This approach captures the essence of intimacy and refuge while facilitating an immersive experience, aligning closely with the metaphor's focus on privacy and discovery within an enveloping space."""

#! python 3
function_code = """def create_subterranean_cavern_model(base_radius, height_variation, num_layers, seed=42):
    \"""
    Creates a conceptual architectural model inspired by the metaphor of a 'subterranean cavern'.
    This model uses nested curvilinear shells to suggest depth and exploration, with varied translucency
    to enhance the play of light and shadow.

    Parameters:
    - base_radius (float): The base radius of the outermost shell in meters.
    - height_variation (float): The variation in height between each nested shell in meters.
    - num_layers (int): The number of nested layers to create.
    - seed (int): Seed for random number generation to ensure replicable results.

    Returns:
    - List of RhinoCommon Brep objects representing the 3D geometries of the concept model.
    \"""

    import Rhino.Geometry as rg
    import random

    # Set the random seed
    random.seed(seed)

    geometries = []

    # Create a series of nested shells
    for i in range(num_layers):
        # Calculate the current radius and height
        current_radius = base_radius - (i * (base_radius / num_layers) * 0.8)
        current_height = height_variation * (1 + random.uniform(-0.2, 0.2))

        # Create a curvilinear shell using a lofted surface
        circle_top = rg.Circle(rg.Plane.WorldXY, current_radius).ToNurbsCurve()
        circle_bottom = rg.Circle(rg.Plane(rg.Point3d(0, 0, -current_height), rg.Vector3d.ZAxis), current_radius * 0.8).ToNurbsCurve()

        loft = rg.Brep.CreateFromLoft([circle_top, circle_bottom], rg.Point3d.Unset, rg.Point3d.Unset, rg.LoftType.Normal, False)
        
        if loft:
            geometries.append(loft[0])

    # Introduce small openings for light and shadow play
    final_geometries = []
    for geom in geometries:
        num_openings = random.randint(1, 3)
        for _ in range(num_openings):
            opening_radius = random.uniform(0.1, 0.3) * base_radius
            opening_center = rg.Point3d(random.uniform(-base_radius, base_radius), random.uniform(-base_radius, base_radius), random.uniform(-height_variation, 0))
            sphere = rg.Brep.CreateFromSphere(rg.Sphere(opening_center, opening_radius))
            if sphere:
                cutter = sphere
                trimmed_breps = geom.Trim(cutter, 0.01)
                if trimmed_breps:
                    geom = trimmed_breps[0]
        final_geometries.append(geom)

    return final_geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_subterranean_cavern_model(10.0, 5.0, 6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_subterranean_cavern_model(15.0, 3.0, 8, seed=123)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_subterranean_cavern_model(12.0, 4.0, 5, seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_subterranean_cavern_model(8.0, 6.0, 4, seed=2023)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_subterranean_cavern_model(20.0, 2.5, 10, seed=56)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
