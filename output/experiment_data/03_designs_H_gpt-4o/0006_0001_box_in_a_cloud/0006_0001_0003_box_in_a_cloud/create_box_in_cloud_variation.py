# Created for 0006_0001_box_in_a_cloud.json

""" Summary:
The function `create_box_in_cloud_variation` generates an architectural concept model based on the "Box in a cloud" metaphor. It creates a strong, geometric "box" at the center using solid dimensions, representing structural stability. Surrounding this core is a wavy "cloud" layer, designed with translucent surfaces that evoke lightness and movement. The function employs parameters like box dimensions, cloud thickness, and wave amplitude to define the spatial characteristics, emphasizing the contrast between the solid core and the ethereal envelope. The resulting 3D geometries visually articulate the interplay between defined and fluid forms, enhancing the architectural concept."""

#! python 3
function_code = """def create_box_in_cloud_variation(box_dimensions, cloud_thickness, cloud_wave_amplitude, seed=123):
    \"""
    Creates an architectural Concept Model embodying the 'Box in a cloud' metaphor with a different approach.
    
    This function generates a central 'box' with a solid, geometric form and surrounds it with a 'cloud' layer
    characterized by wavy, translucent surfaces that suggest ethereality and movement.

    Parameters:
    - box_dimensions: Tuple of three floats representing the width, depth, and height of the box in meters.
    - cloud_thickness: Float representing the thickness of the cloud layer around the box in meters.
    - cloud_wave_amplitude: Float representing the amplitude of the wave effect in the cloud layer.
    - seed: Integer for the random seed to ensure replicable results.

    Returns:
    - A list of RhinoCommon Brep objects representing the 3D geometries of the box and cloud layer.
    \"""
    import Rhino.Geometry as rg
    import math
    import random

    # Set the random seed for reproducibility
    random.seed(seed)

    # Unpack box dimensions
    box_width, box_depth, box_height = box_dimensions

    # Create the central box
    box_corners = [
        rg.Point3d(0, 0, 0),
        rg.Point3d(box_width, 0, 0),
        rg.Point3d(box_width, box_depth, 0),
        rg.Point3d(0, box_depth, 0),
        rg.Point3d(0, 0, box_height),
        rg.Point3d(box_width, 0, box_height),
        rg.Point3d(box_width, box_depth, box_height),
        rg.Point3d(0, box_depth, box_height)
    ]
    box = rg.Brep.CreateFromBox(box_corners)

    # Create the cloud layer as a wavy surface
    cloud_breps = []
    num_wave_points = 20  # Number of points to define the wave effect

    for i in range(num_wave_points):
        angle = (math.pi * 2 / num_wave_points) * i
        wave_offset = cloud_wave_amplitude * math.sin(angle)

        cloud_corners = [
            rg.Point3d(-cloud_thickness + wave_offset, -cloud_thickness, -cloud_thickness),
            rg.Point3d(box_width + cloud_thickness + wave_offset, -cloud_thickness, -cloud_thickness),
            rg.Point3d(box_width + cloud_thickness + wave_offset, box_depth + cloud_thickness, -cloud_thickness),
            rg.Point3d(-cloud_thickness + wave_offset, box_depth + cloud_thickness, -cloud_thickness),
            rg.Point3d(-cloud_thickness + wave_offset, -cloud_thickness, box_height + cloud_thickness),
            rg.Point3d(box_width + cloud_thickness + wave_offset, -cloud_thickness, box_height + cloud_thickness),
            rg.Point3d(box_width + cloud_thickness + wave_offset, box_depth + cloud_thickness, box_height + cloud_thickness),
            rg.Point3d(-cloud_thickness + wave_offset, box_depth + cloud_thickness, box_height + cloud_thickness)
        ]

        cloud = rg.Brep.CreateFromBox(cloud_corners)
        cloud_breps.append(cloud)

    # Return the box and the wavy cloud layer
    return [box] + cloud_breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_box_in_cloud_variation((2.0, 3.0, 4.0), 0.5, 0.2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_box_in_cloud_variation((1.5, 2.5, 3.5), 0.75, 0.3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_box_in_cloud_variation((3.0, 2.0, 5.0), 1.0, 0.4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_box_in_cloud_variation((4.0, 5.0, 6.0), 0.2, 0.1)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_box_in_cloud_variation((3.5, 1.5, 2.5), 0.6, 0.25)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
