# Created for 0006_0003_box_in_a_cloud.json

""" Summary:
The function `create_box_in_cloud_model` generates an architectural concept model based on the "Box in a Cloud" metaphor. It creates a solid geometric core (the "box") using defined dimensions and robust materials, representing stability. This core is surrounded by layered, amorphous cloud surfaces that embody lightness and fluidity, achieved through randomized, translucent shapes. The function incorporates parameters for cloud characteristics, allowing for variation in form and density, thus enhancing the visual contrast between the solid core and the ethereal outer layer. The interplay of light and shadow further emphasizes the metaphor's themes of solidity and ethereality."""

#! python 3
function_code = """def create_box_in_cloud_model(box_dimensions, cloud_radius, cloud_layers, seed=42):
    \"""
    Create an architectural Concept Model embodying the 'Box in a Cloud' metaphor.

    Parameters:
    box_dimensions (tuple): A tuple (length, width, height) representing the dimensions of the central box.
    cloud_radius (float): The radius of the amorphous cloud layer surrounding the box.
    cloud_layers (int): The number of translucent layers to create for the cloud.
    seed (int, optional): The seed for random number generation to ensure replicable results. Default is 42.

    Returns:
    list: A list of RhinoCommon geometry objects (breps representing the box and surfaces representing the cloud).

    This function generates a central geometric box form and surrounds it with dynamic, layered cloud surfaces.
    The box is constructed as a BRep, and the cloud consists of a series of concentric, semi-transparent layers
    that create a nebulous envelope around the box.
    \"""
    import Rhino.Geometry as rg
    import random
    import math  # Corrected the import for the math module

    # Set the random seed for reproducibility
    random.seed(seed)

    # Create the central box as a BRep
    box_length, box_width, box_height = box_dimensions
    box_corners = [
        rg.Point3d(0, 0, 0),
        rg.Point3d(box_length, 0, 0),
        rg.Point3d(box_length, box_width, 0),
        rg.Point3d(0, box_width, 0),
        rg.Point3d(0, 0, box_height),
        rg.Point3d(box_length, 0, box_height),
        rg.Point3d(box_length, box_width, box_height),
        rg.Point3d(0, box_width, box_height)
    ]
    box_brep = rg.Brep.CreateFromBox(box_corners)

    # Create the cloud layer surfaces
    cloud_surfaces = []
    for i in range(cloud_layers):
        layer_radius = cloud_radius * ((i + 1) / cloud_layers)
        points = []
        for j in range(6):  # Create 6 points per layer for a rough circular shape
            angle = j * (2 * math.pi / 6)  # Replaced 3.14159 with math.pi
            x = layer_radius * random.uniform(0.8, 1.2) * math.cos(angle)  # Replaced rg.Math.Cos with math.cos
            y = layer_radius * random.uniform(0.8, 1.2) * math.sin(angle)  # Replaced rg.Math.Sin with math.sin
            z = random.uniform(0.2 * box_height, 0.8 * box_height)
            points.append(rg.Point3d(x + box_length / 2, y + box_width / 2, z))
        cloud_curve = rg.Curve.CreateInterpolatedCurve(points, 3)
        cloud_surface = rg.Surface.CreateExtrusion(cloud_curve, rg.Vector3d(0, 0, 1))
        cloud_surfaces.append(cloud_surface)

    return [box_brep] + cloud_surfaces"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_box_in_cloud_model((10, 5, 3), 15.0, 5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_box_in_cloud_model((8, 4, 2), 10.0, 3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_box_in_cloud_model((12, 6, 4), 20.0, 4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_box_in_cloud_model((15, 7, 5), 12.0, 6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_box_in_cloud_model((5, 3, 2), 8.0, 2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
