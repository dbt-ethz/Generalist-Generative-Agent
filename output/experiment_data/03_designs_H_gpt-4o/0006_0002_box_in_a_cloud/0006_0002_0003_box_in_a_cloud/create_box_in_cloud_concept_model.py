# Created for 0006_0002_box_in_a_cloud.json

""" Summary:
The function `create_box_in_cloud_concept_model` generates an architectural concept model that embodies the "Box in a cloud" metaphor by creating a central solid geometric form (the 'box') surrounded by dynamic, ethereal surfaces (the 'cloud'). The box is defined using robust materials, while the cloud is represented by fluctuating NURBS surfaces that mimic lightness and fluidity. The function varies parameters like size, layer count, and fluctuation to explore different spatial transitions and interactions between the solid and the ephemeral, effectively visualizing the metaphor's duality and enhancing the architectural narrative of stability versus dynamism."""

#! python 3
function_code = """def create_box_in_cloud_concept_model(box_size=10, cloud_layers=5, cloud_fluctuation=2.5, cloud_density=10):
    \"""
    Creates an architectural concept model using the "Box in a cloud" metaphor. The model features a central solid
    box surrounded by layered, fluctuating cloud-like surfaces to evoke a sense of lightness and ethereality.

    Parameters:
    - box_size (float): The dimension of the box's side (in meters), assumed to be cubic.
    - cloud_layers (int): The number of fluctuating cloud layers around the box.
    - cloud_fluctuation (float): The maximum deviation in meters for the cloud's surface layers.
    - cloud_density (int): The number of divisions along each axis for creating cloud layers.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep geometries representing the box and the cloud layers.
    \"""
    import Rhino.Geometry as rg
    import random

    # Set a seed for randomness
    random.seed(42)
    
    # Create the central 'box'
    box_corners = [
        rg.Point3d(0, 0, 0),
        rg.Point3d(box_size, 0, 0),
        rg.Point3d(box_size, box_size, 0),
        rg.Point3d(0, box_size, 0),
        rg.Point3d(0, 0, box_size),
        rg.Point3d(box_size, 0, box_size),
        rg.Point3d(box_size, box_size, box_size),
        rg.Point3d(0, box_size, box_size)
    ]
    box_brep = rg.Brep.CreateFromBox(box_corners)

    # Create the 'cloud' as fluctuating NURBS surfaces
    cloud_surfaces = []
    for layer in range(cloud_layers):
        offset = layer * (cloud_fluctuation / cloud_layers)
        control_points = []
        for i in range(cloud_density):
            for j in range(cloud_density):
                x = (i / (cloud_density - 1)) * box_size
                y = (j / (cloud_density - 1)) * box_size
                z = offset + random.uniform(-cloud_fluctuation, cloud_fluctuation)
                control_points.append(rg.Point3d(x, y, z))

        # Create a NURBS surface from control points
        nurbs_surface = rg.NurbsSurface.CreateFromPoints(control_points, cloud_density, cloud_density, 3, 3)
        cloud_surfaces.append(nurbs_surface.ToBrep())

    # Combine all geometries into a single list
    concept_model = [box_brep] + cloud_surfaces

    return concept_model"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_box_in_cloud_concept_model(box_size=15, cloud_layers=7, cloud_fluctuation=3.0, cloud_density=12)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_box_in_cloud_concept_model(box_size=20, cloud_layers=4, cloud_fluctuation=1.5, cloud_density=8)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_box_in_cloud_concept_model(box_size=12, cloud_layers=6, cloud_fluctuation=2.0, cloud_density=10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_box_in_cloud_concept_model(box_size=8, cloud_layers=3, cloud_fluctuation=1.0, cloud_density=6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_box_in_cloud_concept_model(box_size=25, cloud_layers=5, cloud_fluctuation=4.0, cloud_density=15)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
