# Created for 0006_0002_box_in_a_cloud.json

""" Summary:
The provided function generates an architectural concept model based on the "Box in a cloud" metaphor by creating two distinct geometries: a central 'box' and an enveloping 'cloud'. The 'box' represents solidity, constructed from defined dimensions and materials suggesting permanence. In contrast, the 'cloud' is crafted using lofted surfaces from irregular curves, embodying fluidity and lightness. The function utilizes parameters for dimensions and resolution, allowing for varied interpretations of the metaphor. By creating a visual interplay between the stable core and dynamic envelope, the model emphasizes spatial transitions and layered experiences, capturing the essence of the metaphor effectively."""

#! python 3
function_code = """def create_architectural_concept_model(box_dimensions=(10, 10, 10), cloud_extent=(15, 15, 12), cloud_resolution=(10, 10, 5)):
    \"""
    Creates an architectural Concept Model based on the 'Box in a cloud' metaphor.

    This function generates a central geometric 'box' symbolizing solidity and permanence, enveloped by a dynamic, cloud-like form.
    The 'cloud' is represented using a lofted surface between multiple irregularly shaped curves that suggest fluidity and lightness.

    Parameters:
    - box_dimensions (tuple): A tuple of three floats representing the width, depth, and height of the central box (in meters).
    - cloud_extent (tuple): A tuple of three floats indicating the extent of the cloud form in width, depth, and height.
    - cloud_resolution (tuple): A tuple of three integers specifying the number of divisions for the cloud surface in width, depth, and height.

    Returns:
    - list: A list of RhinoCommon Brep objects representing the box and the cloud geometries.
    \"""
    import Rhino.Geometry as rg
    import random

    # Set a seed for randomness to ensure replicability
    random.seed(42)

    # Create the central 'box'
    box_width, box_depth, box_height = box_dimensions
    box_corners = [
        rg.Point3d(0, 0, 0),
        rg.Point3d(box_width, 0, 0),
        rg.Point3d(box_width, box_depth, 0),
        rg.Point3d(0, box_depth, 0),
        rg.Point3d(0, 0, box_height),
        rg.Point3d(box_width, 0, box_height),
        rg.Point3d(box_width, box_depth, box_height),
        rg.Point3d(0, box_depth, box_height),
    ]
    box_brep = rg.Brep.CreateFromBox(box_corners)

    # Create 'cloud' form as a lofted surface between curves
    cloud_width, cloud_depth, cloud_height = cloud_extent
    curves = []
    for i in range(cloud_resolution[2]):
        height = i * (cloud_height / (cloud_resolution[2] - 1))
        curve_points = []
        for j in range(cloud_resolution[0]):
            x = random.uniform(-cloud_width / 2, cloud_width / 2) + (j * box_width / (cloud_resolution[0] - 1))
            y = random.uniform(-cloud_depth / 2, cloud_depth / 2)
            curve_points.append(rg.Point3d(x, y, height))
        curve = rg.Curve.CreateInterpolatedCurve(curve_points, 3)
        curves.append(curve)

    cloud_brep = rg.Brep.CreateFromLoft(curves, rg.Point3d.Unset, rg.Point3d.Unset, rg.LoftType.Normal, False)[0]

    return [box_brep, cloud_brep]"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_architectural_concept_model(box_dimensions=(8, 8, 5), cloud_extent=(12, 12, 10), cloud_resolution=(8, 8, 6))
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_architectural_concept_model(box_dimensions=(15, 10, 7), cloud_extent=(20, 15, 14), cloud_resolution=(12, 10, 8))
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_architectural_concept_model(box_dimensions=(5, 5, 5), cloud_extent=(10, 10, 8), cloud_resolution=(6, 6, 4))
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_architectural_concept_model(box_dimensions=(12, 15, 10), cloud_extent=(18, 20, 15), cloud_resolution=(9, 12, 7))
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_architectural_concept_model(box_dimensions=(20, 15, 10), cloud_extent=(25, 20, 18), cloud_resolution=(10, 10, 6))
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
