# Created for 0006_0002_box_in_a_cloud.json

""" Summary:
The function `create_box_in_cloud_concept_model` generates an architectural concept model based on the "Box in a Cloud" metaphor by creating a central solid 'box' surrounded by dynamic 'cloud' layers. The 'box' is defined with geometric precision and stability, reflecting solidity through its construction from dense materials. Conversely, the 'cloud' is realized through multiple wavy, layered surfaces, evoking ethereality and fluidity, using lighter materials. The model emphasizes spatial transitions, showcasing the interplay between the defined structure of the box and the soft, flowing cloud, reflecting the metaphor's essence of contrasting stability with dynamism."""

#! python 3
function_code = """def create_box_in_cloud_concept_model(box_width=10, box_depth=10, box_height=10, cloud_layer_count=5, cloud_offset=5, cloud_wave_intensity=2):
    \"""
    Creates an architectural concept model illustrating the 'Box in a Cloud' metaphor using RhinoCommon.
    
    This function generates a solid central 'box' surrounded by a 'cloud' layer that simulates ethereal presence.
    The 'cloud' is represented by a series of wavy, layered surfaces that wrap around the 'box', creating a dynamic
    and flowing exterior.

    Parameters:
    - box_width (float): Width of the central box in meters.
    - box_depth (float): Depth of the central box in meters.
    - box_height (float): Height of the central box in meters.
    - cloud_layer_count (int): Number of cloud layers enveloping the box.
    - cloud_offset (float): Distance from the box to the first cloud layer.
    - cloud_wave_intensity (float): Maximum offset for the wave effect on the cloud layers.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep geometries representing the box and the cloud.
    \"""
    import Rhino.Geometry as rg
    import math

    # Create the 'box' as a Brep (solid)
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
    box_brep = rg.Brep.CreateFromBox(box_corners)

    # Create the 'cloud' as layered Breps
    cloud_breps = []
    for layer in range(cloud_layer_count):
        offset_distance = cloud_offset + layer * (cloud_wave_intensity / cloud_layer_count)
        wave_points = []
        for i in range(4):
            angle = math.pi / 2 * i
            x = box_width / 2 + offset_distance * math.cos(angle)
            y = box_depth / 2 + offset_distance * math.sin(angle)
            z = box_height / 2 + math.sin(layer * math.pi / cloud_layer_count) * cloud_wave_intensity
            wave_points.append(rg.Point3d(x, y, z))
        
        cloud_curve = rg.NurbsCurve.Create(False, 3, wave_points + [wave_points[0]])
        axis_line = rg.Line(rg.Point3d(0, 0, 0), rg.Point3d(0, 0, box_height))
        cloud_surface = rg.Brep.CreateFromRevSurface(rg.RevSurface.Create(cloud_curve, axis_line), True, True)
        cloud_breps.append(cloud_surface)

    # Combine all geometries into a single list
    concept_model = [box_brep] + cloud_breps

    return concept_model"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_box_in_cloud_concept_model(box_width=15, box_depth=15, box_height=20, cloud_layer_count=8, cloud_offset=3, cloud_wave_intensity=5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_box_in_cloud_concept_model(box_width=12, box_depth=12, box_height=15, cloud_layer_count=6, cloud_offset=4, cloud_wave_intensity=3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_box_in_cloud_concept_model(box_width=20, box_depth=10, box_height=10, cloud_layer_count=4, cloud_offset=6, cloud_wave_intensity=1)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_box_in_cloud_concept_model(box_width=8, box_depth=8, box_height=12, cloud_layer_count=10, cloud_offset=2, cloud_wave_intensity=4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_box_in_cloud_concept_model(box_width=5, box_depth=5, box_height=5, cloud_layer_count=3, cloud_offset=2, cloud_wave_intensity=6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
