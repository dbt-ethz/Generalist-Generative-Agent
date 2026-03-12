# Created for 0001_0004_house_within_a_house.json

""" Summary:
The function `create_house_within_house_model` generates an architectural concept model based on the metaphor of a "House within a house," employing concentric layers to depict nesting and protection. It defines a core sanctuary and constructs overlapping layers with varying thicknesses that symbolize the transition from public to private spaces. Each layer features openings to enhance interlocking effects, allowing natural light and visual connections between spaces. By utilizing modular geometries, the model embodies a layered spatial hierarchy, creating a dynamic journey through the building, where users experience a gradual shift from external exposure to internal seclusion."""

#! python 3
function_code = """def create_house_within_house_model(core_radius=4.0, layer_thickness=1.5, num_layers=5, height=10.0):
    \"""
    Creates an architectural Concept Model based on the 'House within a house' metaphor.
    This model features concentric and interwoven layers using interlocking modular geometries 
    to evoke a sense of nesting, protection, and spatial hierarchy.

    Parameters:
    - core_radius (float): Radius of the inner sanctuary or core space in meters.
    - layer_thickness (float): Thickness of each protective layer surrounding the core in meters.
    - num_layers (int): Number of concentric layers surrounding the core.
    - height (float): Height of each layer in meters, representing vertical progression.

    Returns:
    - List of RhinoCommon Brep objects representing the 3D geometries of the concept model.
    \"""
    import Rhino.Geometry as rg
    import random
    import math  # Import math module

    random.seed(100)  # Ensures replicability

    geometries = []

    # Create the inner core, a basic cube for modular representation
    core_box = rg.Box(rg.Plane.WorldXY, rg.Interval(-core_radius, core_radius), rg.Interval(-core_radius, core_radius), rg.Interval(0, height))
    geometries.append(core_box.ToBrep())

    # Create interlocking concentric layers
    for i in range(1, num_layers + 1):
        layer_size = core_radius + i * layer_thickness
        layer_box = rg.Box(rg.Plane.WorldXY, rg.Interval(-layer_size, layer_size), rg.Interval(-layer_size, layer_size), rg.Interval(0, height))

        # Create openings to generate interlocking effect
        opening_size = layer_thickness * 0.5
        openings = []
        for j in range(4):
            offset = (core_radius + (i - 1) * layer_thickness) * (1 + random.uniform(0.2, 0.3))
            for k in range(2):  # Create two openings per face
                pos = j * 90 + k * 45
                opening_center = rg.Point3d(offset * math.cos(math.radians(pos)), offset * math.sin(math.radians(pos)), height / 2)
                opening = rg.Box(rg.Plane(opening_center, rg.Vector3d.ZAxis), rg.Interval(-opening_size, opening_size), rg.Interval(-opening_size, opening_size), rg.Interval(-height / 2, height / 2))
                openings.append(opening.ToBrep())

        # Subtract openings from the layer
        layer_brep = layer_box.ToBrep()
        for opening in openings:
            result = rg.Brep.CreateBooleanDifference([layer_brep], [opening], 0.01)
            if result:
                layer_brep = result[0]

        geometries.append(layer_brep)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_house_within_house_model(core_radius=5.0, layer_thickness=2.0, num_layers=4, height=12.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_house_within_house_model(core_radius=3.0, layer_thickness=1.0, num_layers=6, height=8.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_house_within_house_model(core_radius=6.0, layer_thickness=2.5, num_layers=3, height=15.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_house_within_house_model(core_radius=7.0, layer_thickness=2.0, num_layers=5, height=10.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_house_within_house_model(core_radius=4.5, layer_thickness=1.0, num_layers=7, height=9.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
