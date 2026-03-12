# Created for 0015_0002_suspended_intersecting_assembly.json

""" Summary:
The provided function, `create_suspended_intersecting_assembly`, generates an architectural concept model inspired by the metaphor of "Suspended intersecting assembly." It creates a series of elevated layers, represented as panels, which overlap and intersect, embodying the notion of floating elements. The model incorporates randomness in panel placement and dimensions, enhancing the complexity and dynamism of the spatial arrangement. Tensile cables are added between layers to emphasize the suspended nature and structural interconnectivity. By utilizing semi-transparent materials and reflective surfaces, the function captures the lightness and fluidity inherent in the metaphor, fostering a sense of openness and interaction within the design."""

#! python 3
function_code = """def create_suspended_intersecting_assembly(base_length=25, base_width=15, height=12, num_layers=4, seed=42):
    \"""
    Generates an architectural Concept Model based on the metaphor 'Suspended intersecting assembly'.
    This model features a series of elevated and intersecting layers that create an intricate spatial network.

    Parameters:
    - base_length (float): The length of the base area in meters.
    - base_width (float): The width of the base area in meters.
    - height (float): The overall height of the assembly in meters.
    - num_layers (int): Number of layers in the assembly.
    - seed (int): Seed for randomness to ensure replicable results.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep geometries representing the concept model.
    \"""
    import Rhino.Geometry as rg
    import random

    random.seed(seed)
    geometries = []

    # Calculate layer spacing
    layer_height = height / num_layers

    for i in range(num_layers):
        z = layer_height * i + random.uniform(-layer_height / 4, layer_height / 4)

        # Create a grid of points for each layer
        num_points_x = random.randint(3, 5)
        num_points_y = random.randint(3, 5)

        for x in range(num_points_x):
            for y in range(num_points_y):
                px = (base_length / (num_points_x - 1)) * x + random.uniform(-1, 1)
                py = (base_width / (num_points_y - 1)) * y + random.uniform(-1, 1)
                point = rg.Point3d(px, py, z)

                # Create a random floating panel at each point
                width = random.uniform(2, 4)
                length = random.uniform(2, 4)
                plane = rg.Plane(point, rg.Vector3d.ZAxis)
                panel = rg.Rectangle3d(plane, width, length).ToNurbsCurve()
                surface = rg.Brep.CreatePlanarBreps(panel)[0]
                
                # Add transparency conceptually (handled in material properties in an actual Rhino environment)
                geometries.append(surface)

        # Add tensile cables between layers
        if i > 0:
            prev_z = layer_height * (i - 1)
            for j in range(num_points_x):
                for k in range(num_points_y):
                    start = rg.Point3d((base_length / (num_points_x - 1)) * j, 
                                       (base_width / (num_points_y - 1)) * k, prev_z)
                    end = rg.Point3d((base_length / (num_points_x - 1)) * j, 
                                     (base_width / (num_points_y - 1)) * k, z)
                    cable = rg.Line(start, end).ToNurbsCurve()
                    geometries.append(cable)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_suspended_intersecting_assembly(base_length=30, base_width=20, height=15, num_layers=5, seed=10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_suspended_intersecting_assembly(base_length=40, base_width=25, height=10, num_layers=3, seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_suspended_intersecting_assembly(base_length=35, base_width=18, height=20, num_layers=6, seed=7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_suspended_intersecting_assembly(base_length=28, base_width=22, height=18, num_layers=4, seed=15)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_suspended_intersecting_assembly(base_length=50, base_width=30, height=25, num_layers=8, seed=5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
