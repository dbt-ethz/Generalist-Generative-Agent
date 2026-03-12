# Created for 0004_0005_interlocking_layers.json

""" Summary:
The function `create_interlocking_layers_model` generates an architectural concept model based on the "Interlocking Layers" metaphor by creating a series of overlapping and intersecting planes or volumes. It uses parameters such as base dimensions, height, number of layers, and layer thickness to define the structure's spatial complexity. Each layer is randomly oriented and positioned, reflecting the dynamic interplay of spaces characterized by both openness and privacy. The result is a collection of 3D geometries (Brep) that visually demonstrate the structural and spatial relationships, fulfilling the design task's requirements for a multifaceted architectural expression."""

#! python 3
function_code = """def create_interlocking_layers_model(base_length, base_width, height, num_layers, layer_thickness, seed=42):
    \"""
    Creates an architectural Concept Model based on the 'Interlocking Layers' metaphor.
    
    The model consists of a series of intersecting and overlapping planes or volumes to 
    express the dynamic and multifaceted form of interlocking layers. Each layer is represented 
    as a 3D geometry (Brep), with varying orientations and positions to capture the complexity 
    and spatial relationships of the design.

    Parameters:
    - base_length (float): The length of the base plane in meters.
    - base_width (float): The width of the base plane in meters.
    - height (float): The maximum height of the structure in meters.
    - num_layers (int): The number of interlocking layers to generate.
    - layer_thickness (float): The thickness of each individual layer in meters.
    - seed (int): Random seed for reproducible results. Default is 42.

    Returns:
    - List of Rhino.Geometry.Brep: A list of 3D geometries representing the layers of the structure.
    \"""
    import Rhino.Geometry as rg
    import random

    random.seed(seed)
    geometries = []
    z_position = 0

    for i in range(num_layers):
        # Randomly determine the orientation and offset of the layer
        orientation = random.choice(['horizontal', 'vertical'])
        offset_x = random.uniform(-base_length / 4, base_length / 4)
        offset_y = random.uniform(-base_width / 4, base_width / 4)

        # Create a base plane for the layer
        if orientation == 'horizontal':
            plane = rg.Plane(rg.Point3d(offset_x, offset_y, z_position), rg.Vector3d.ZAxis)
            length = base_length
            width = layer_thickness
        else:
            plane = rg.Plane(rg.Point3d(offset_x, offset_y, z_position), rg.Vector3d.YAxis)
            length = layer_thickness
            width = base_width

        # Create a surface and then convert to a Brep
        corner1 = plane.PointAt(-length / 2, -width / 2)
        corner2 = plane.PointAt(length / 2, -width / 2)
        corner3 = plane.PointAt(length / 2, width / 2)
        corner4 = plane.PointAt(-length / 2, width / 2)
        surface = rg.NurbsSurface.CreateFromCorners(corner1, corner2, corner3, corner4)

        if surface:
            brep = surface.ToBrep()
            geometries.append(brep)

        # Increment z_position for the next layer
        z_position += height / num_layers

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_interlocking_layers_model(10.0, 5.0, 15.0, 6, 0.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_interlocking_layers_model(12.0, 8.0, 20.0, 4, 0.75)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_interlocking_layers_model(15.0, 10.0, 25.0, 5, 1.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_interlocking_layers_model(8.0, 4.0, 10.0, 3, 0.3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_interlocking_layers_model(14.0, 6.0, 18.0, 7, 0.6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
