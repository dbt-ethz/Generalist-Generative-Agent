# Created for 0006_0001_box_in_a_cloud.json

""" Summary:
The function `create_box_in_cloud_alternative` generates an architectural concept model based on the 'Box in a cloud' metaphor by creating a solid geometric core (the 'box') and surrounding it with a dynamic, undulating envelope (the 'cloud'). The box is modeled as a cubic structure using defined corners, emphasizing strength and stability. The cloud is formed by lofting sinusoidal wave patterns, which introduces a sense of lightness and movement, contrasting the solidity of the box. This approach highlights the interplay between structured and ethereal elements, capturing the metaphor's essence of defined boundaries and fluid transitions in spatial design."""

#! python 3
function_code = """def create_box_in_cloud_alternative(box_size, cloud_height, cloud_waves, wave_amplitude, seed=42):
    \"""
    Creates an architectural Concept Model representing the 'Box in a cloud' metaphor with a different approach.

    This function generates a solid central 'box' and surrounds it with a 'cloud' formed by undulating surfaces 
    that suggest lightness and movement. The 'cloud' is created by lofting sinusoidal wave patterns around the box, 
    emphasizing the contrast between structured solidity and ephemeral lightness.

    Parameters:
    - box_size (float): The size of the cubic central 'box' in meters.
    - cloud_height (float): The average height of the cloud envelope in meters.
    - cloud_waves (int): The number of wave undulations forming the cloud.
    - wave_amplitude (float): The amplitude of the wave undulations.
    - seed (int): Random seed for reproducibility.

    Returns:
    - list: A list of RhinoCommon Brep objects representing the 3D geometries of the concept model.
    \"""
    import Rhino.Geometry as rg
    import math
    import random

    # Set the random seed for reproducibility
    random.seed(seed)

    # Create the central 'box' as a Brep
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

    # Create the 'cloud' using sinusoidal surfaces
    cloud_breps = []
    for i in range(cloud_waves):
        # Calculate wave parameters
        angle = 2 * math.pi * i / cloud_waves
        offset = random.uniform(-wave_amplitude, wave_amplitude)

        # Define wave control points
        control_points = [
            rg.Point3d(
                (box_size / 2) * math.cos(angle + t * 2 * math.pi / 10) * (1 + offset),
                (box_size / 2) * math.sin(angle + t * 2 * math.pi / 10) * (1 + offset),
                t / 10 * cloud_height
            ) for t in range(11)
        ]

        # Create curve and loft it
        wave_curve = rg.NurbsCurve.Create(False, 3, control_points)
        wave_curve_translated = wave_curve.Duplicate()
        wave_curve_translated.Translate(rg.Vector3d(0, 0, wave_amplitude))
        loft = rg.Brep.CreateFromLoft([wave_curve, wave_curve_translated], rg.Point3d.Unset, rg.Point3d.Unset, rg.LoftType.Normal, False)[0]
        cloud_breps.append(loft)

    # Combine the box and cloud into a single list of Brep objects
    model_breps = [box_brep] + cloud_breps

    return model_breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_box_in_cloud_alternative(5.0, 10.0, 8, 2.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_box_in_cloud_alternative(3.0, 15.0, 12, 1.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_box_in_cloud_alternative(4.0, 20.0, 10, 3.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_box_in_cloud_alternative(6.0, 12.0, 6, 2.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_box_in_cloud_alternative(2.5, 8.0, 5, 1.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
