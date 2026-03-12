# Created for 0006_0001_box_in_a_cloud.json

""" Summary:
The function `create_box_in_cloud_concept` generates an architectural concept model by embodying the "Box in a cloud" metaphor. It creates a solid geometric "box" that represents a stable core using defined dimensions, emphasizing permanence. Surrounding this core, the function adds multiple "cloud" layers constructed from lighter, translucent materials, suggesting ethereality. The layers extend beyond the box, enhancing the contrast between the solid structure and the fluid, diffused envelope. By varying translucency and introducing randomness, the design reflects the interplay of light and shadow, fostering a spatial dialogue between the robust and the ephemeral, aligning with the metaphor's essence."""

#! python 3
function_code = """def create_box_in_cloud_concept(box_length=10, box_width=6, box_height=8, cloud_layers=3, cloud_translucency=0.5):
    \"""
    Creates an architectural Concept Model based on the 'Box in a cloud' metaphor. This function constructs a central
    geometric 'box' representing a solid core and envelops it with a 'cloud' that is lighter and more diffuse.

    Parameters:
    - box_length (float): Length of the 'box' in meters.
    - box_width (float): Width of the 'box' in meters.
    - box_height (float): Height of the 'box' in meters.
    - cloud_layers (int): Number of layers representing the 'cloud' around the 'box'.
    - cloud_translucency (float): A factor between 0 and 1 representing the translucency of the 'cloud'.

    Returns:
    - list: A list of RhinoCommon Brep objects representing the 3D geometries of the concept model.
    \"""
    import Rhino.Geometry as rg
    import random

    random.seed(42)  # Ensure reproducibility

    # Create the central 'box' as a solid Brep
    box_origin = rg.Point3d(0, 0, 0)
    box_corners = [
        rg.Point3d(box_length, 0, 0),
        rg.Point3d(box_length, box_width, 0),
        rg.Point3d(0, box_width, 0),
        rg.Point3d(0, 0, box_height),
        rg.Point3d(box_length, 0, box_height),
        rg.Point3d(box_length, box_width, box_height),
        rg.Point3d(0, box_width, box_height)
    ]
    box_brep = rg.Brep.CreateFromBox(rg.Box(rg.Plane.WorldXY, box_corners))

    # Create the 'cloud' layers as lighter, diffuse Breps
    cloud_breps = []
    cloud_step = 2.0  # Distance between cloud layers
    cloud_extension = 3.0  # How much each cloud layer extends beyond the box

    for i in range(cloud_layers):
        offset = cloud_step * (i + 1)
        cloud_box_corners = [
            rg.Point3d(-cloud_extension, -cloud_extension, -cloud_extension),
            rg.Point3d(box_length + cloud_extension, -cloud_extension, -cloud_extension),
            rg.Point3d(box_length + cloud_extension, box_width + cloud_extension, -cloud_extension),
            rg.Point3d(-cloud_extension, box_width + cloud_extension, -cloud_extension),
            rg.Point3d(-cloud_extension, -cloud_extension, box_height + cloud_extension),
            rg.Point3d(box_length + cloud_extension, -cloud_extension, box_height + cloud_extension),
            rg.Point3d(box_length + cloud_extension, box_width + cloud_extension, box_height + cloud_extension),
            rg.Point3d(-cloud_extension, box_width + cloud_extension, box_height + cloud_extension)
        ]
        
        cloud_layer = rg.Brep.CreateFromBox(rg.Box(rg.Plane.WorldXY, cloud_box_corners))
        
        # Introduce some randomness to make the cloud dynamic
        for face in cloud_layer.Faces:
            if random.random() > cloud_translucency:
                cloud_breps.append(face.DuplicateFace(False))

    return [box_brep] + cloud_breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_box_in_cloud_concept(box_length=12, box_width=8, box_height=10, cloud_layers=5, cloud_translucency=0.7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_box_in_cloud_concept(box_length=15, box_width=10, box_height=5, cloud_layers=4, cloud_translucency=0.3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_box_in_cloud_concept(box_length=9, box_width=7, box_height=12, cloud_layers=6, cloud_translucency=0.6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_box_in_cloud_concept(box_length=14, box_width=9, box_height=11, cloud_layers=2, cloud_translucency=0.4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_box_in_cloud_concept(box_length=11, box_width=5, box_height=9, cloud_layers=7, cloud_translucency=0.8)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
