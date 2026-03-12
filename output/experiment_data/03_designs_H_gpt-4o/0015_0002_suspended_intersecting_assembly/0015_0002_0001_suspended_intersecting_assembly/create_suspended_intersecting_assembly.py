# Created for 0015_0002_suspended_intersecting_assembly.json

""" Summary:
The provided function generates an architectural concept model based on the metaphor of a "Suspended intersecting assembly." It creates a visual representation of elevated, floating structures through multiple layers of intersecting geometries. Each layer is randomly rotated and extruded to mimic dynamic intersections, while fine tensile cables are added to connect these layers, enhancing the feeling of suspension. The use of varying heights and spatial complexity emphasizes lightness and fluidity, reflecting the metaphor. This approach allows for an intricate interplay of forms, showcasing structural elegance and the dynamic nature of the assembly through negative spaces and reflections."""

#! python 3
function_code = """def create_suspended_intersecting_assembly(base_area=30, height=20, num_layers=6, layer_height=4, seed=42):
    \"""
    Generates an architectural Concept Model based on the metaphor 'Suspended intersecting assembly'.
    The model features layers of intersecting volumes and tensile cables to simulate a dynamic floating structure.

    Parameters:
    - base_area (float): The size of the base area in meters (assumed square base).
    - height (float): Overall height of the assembly in meters.
    - num_layers (int): Number of horizontal layers to create.
    - layer_height (float): Height difference between layers.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep geometries representing the concept model.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    random.seed(seed)
    breps = []

    # Calculate the height step per layer
    vertical_step = height / num_layers

    # Create layers of intersecting planes
    for i in range(num_layers):
        z = i * vertical_step
        # Create a random rotation for each layer to simulate dynamic intersections
        angle = random.uniform(0, 180)
        rotation = rg.Transform.Rotation(math.radians(angle), rg.Vector3d.ZAxis, rg.Point3d(0, 0, z))

        # Create a plane that extends across the base area
        plane = rg.Plane(rg.Point3d(0, 0, z), rg.Vector3d.ZAxis)
        plane.Transform(rotation)
        rect = rg.Rectangle3d(plane, base_area, base_area)
        surface = rg.NurbsSurface.CreateFromCorners(rect.Corner(0), rect.Corner(1), rect.Corner(2), rect.Corner(3))
        
        # Extrude surface to create a volume
        extrusion_vector = rg.Vector3d(0, 0, layer_height * random.uniform(0.5, 1.5))
        extrusion_curve = rg.LineCurve(rect.Corner(0), rect.Corner(0) + extrusion_vector)
        volume = rg.Brep.CreateFromSurface(surface).Faces[0].CreateExtrusion(extrusion_curve, True)
        breps.append(volume)

    # Create tensile cables to connect layers
    num_cables = num_layers - 1
    for i in range(num_cables):
        start_z = i * vertical_step
        end_z = (i + 1) * vertical_step

        # Randomly place cables within the base area
        x = random.uniform(-base_area / 2, base_area / 2)
        y = random.uniform(-base_area / 2, base_area / 2)

        # Create a line representing the cable
        start_point = rg.Point3d(x, y, start_z)
        end_point = rg.Point3d(x, y, end_z)
        cable_line = rg.Line(start_point, end_point)

        # Create a thin cylinder around the line to represent the cable
        cable_radius = 0.1
        cable = rg.Cylinder(rg.Circle(rg.Plane(cable_line.From, cable_line.Direction), cable_radius), cable_line.Length).ToBrep(True, True)
        breps.append(cable)

    return breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_suspended_intersecting_assembly(base_area=40, height=25, num_layers=8, layer_height=3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_suspended_intersecting_assembly(base_area=50, height=30, num_layers=5, layer_height=5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_suspended_intersecting_assembly(base_area=35, height=22, num_layers=7, layer_height=4.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_suspended_intersecting_assembly(base_area=45, height=27, num_layers=10, layer_height=6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_suspended_intersecting_assembly(base_area=60, height=40, num_layers=9, layer_height=2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
