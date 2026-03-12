# Created for 0006_0002_box_in_a_cloud.json

""" Summary:
The provided function `create_concept_model` generates an architectural concept model based on the "Box in a cloud" metaphor by creating two distinct geometries. It constructs a solid, rectangular "box" using defined dimensions to symbolize stability and permanence. This box serves as the core structure. Surrounding it, a more fluid "cloud" form is created using random points to represent ethereality and dynamic movement. The cloud's NURBS surface allows for soft, undulating shapes that contrast with the box's rigidity. This interplay emphasizes spatial transitions and layering, effectively visualizing the metaphors duality of solidity and lightness in architectural design."""

#! python 3
function_code = """def create_concept_model(box_width, box_height, box_depth, cloud_radius, cloud_resolution):
    \"""
    Creates an architectural Concept Model symbolizing the 'Box in a cloud' metaphor.
    
    The model consists of a central geometric 'box' representing stability and structural integrity,
    encased within a 'cloud', which represents fluidity and ethereality. The box is a solid geometric form,
    while the cloud is a more amorphous, dynamic shape.

    Parameters:
    box_width (float): The width of the central box.
    box_height (float): The height of the central box.
    box_depth (float): The depth of the central box.
    cloud_radius (float): The radius of the cloud form.
    cloud_resolution (int): Number of control points for the cloud's NURBS surface.

    Returns:
    list: A list containing RhinoCommon Brep objects representing the box and the cloud.
    \"""
    import Rhino.Geometry as rg
    import random

    # Create the central 'box' as a solid form
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

    # Create the 'cloud' form using a NURBS surface
    random.seed(42)  # Ensure replicable randomness
    cloud_points = []
    for i in range(cloud_resolution):
        for j in range(cloud_resolution):
            x = (i / (cloud_resolution - 1)) * (box_width + 2 * cloud_radius) - cloud_radius
            y = (j / (cloud_resolution - 1)) * (box_depth + 2 * cloud_radius) - cloud_radius
            z = random.uniform(0, box_height) + random.uniform(-cloud_radius, cloud_radius)
            cloud_points.append(rg.Point3d(x, y, z))

    cloud_nurbs = rg.NurbsSurface.CreateFromPoints(cloud_points, cloud_resolution, cloud_resolution, 3, 3)
    cloud_brep = cloud_nurbs.ToBrep()

    return [box_brep, cloud_brep]"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_concept_model(10.0, 5.0, 3.0, 2.0, 20)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_concept_model(15.0, 7.0, 4.0, 3.0, 30)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_concept_model(12.0, 6.0, 2.0, 4.0, 25)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_concept_model(8.0, 4.0, 5.0, 1.5, 15)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_concept_model(20.0, 10.0, 8.0, 5.0, 40)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
