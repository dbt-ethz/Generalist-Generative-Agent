# Created for 0006_0003_box_in_a_cloud.json

""" Summary:
The function `create_box_in_cloud_model` generates an architectural concept model representing the "Box in a Cloud" metaphor by creating a solid geometric core (the "box") and surrounding it with a dynamic, undulating outer layer (the "cloud"). The box is constructed using robust materials, while the cloud consists of multiple stratified surfaces that exhibit fluidity and lightness, achieved through variations in thickness and undulation. This interplay emphasizes the contrast between solidity and ethereality. The function outputs a list of geometric objects, effectively visualizing the metaphor's themes of stability, transition, and spatial interaction."""

#! python 3
function_code = """def create_box_in_cloud_model(box_dimensions, cloud_height, cloud_layers, seed=42):
    \"""
    Create an architectural Concept Model embodying the 'Box in a Cloud' metaphor.

    Parameters:
    box_dimensions (tuple): A tuple (length, width, height) representing the dimensions of the central box.
    cloud_height (float): The height of the cloud layer surrounding the box.
    cloud_layers (int): The number of stratified layers composing the cloud.
    seed (int, optional): The seed for random number generation to ensure replicable results. Default is 42.

    Returns:
    list: A list of RhinoCommon geometry objects (breps representing the box and surfaces representing the cloud).

    This function generates a central geometric box form and surrounds it with a stratified, amorphous cloud layer.
    The box is constructed as a solid BRep, and the cloud is represented by a series of wavy surfaces that suggest
    movement and lightness. The cloud's layers are created with varying undulations and transparency to reflect
    the metaphor of diffusion and permeability.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

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

    # Create the cloud as stratified layers
    cloud_surfaces = []
    layer_thickness = cloud_height / cloud_layers

    for i in range(cloud_layers):
        z_offset = box_height + i * layer_thickness
        wave_amplitude = random.uniform(0.1, 0.3)
        wave_frequency = random.uniform(0.5, 1.5)
        
        # Create a wavy surface for each cloud layer
        corners = [
            rg.Point3d(-box_length/2, -box_width/2, z_offset),
            rg.Point3d(box_length * 1.5, -box_width/2, z_offset),
            rg.Point3d(box_length * 1.5, box_width * 1.5, z_offset),
            rg.Point3d(-box_length/2, box_width * 1.5, z_offset)
        ]
        
        # Introduce undulation
        for corner in corners:
            corner.Z += math.sin(corner.X * wave_frequency + random.uniform(0, math.pi)) * wave_amplitude
            corner.Z += math.cos(corner.Y * wave_frequency + random.uniform(0, math.pi)) * wave_amplitude
        
        # Create surface from corners
        cloud_surface = rg.Brep.CreateFromCornerPoints(corners[0], corners[1], corners[2], corners[3], 0.1)
        if cloud_surface:
            cloud_surfaces.append(cloud_surface)

    # Return the box and the cloud surfaces as a list
    return [box_brep] + cloud_surfaces"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_box_in_cloud_model((5, 3, 2), 10, 5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_box_in_cloud_model((4, 4, 4), 15, 8)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_box_in_cloud_model((6, 2, 3), 12, 6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_box_in_cloud_model((7, 5, 1), 8, 4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_box_in_cloud_model((3, 6, 5), 20, 10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
