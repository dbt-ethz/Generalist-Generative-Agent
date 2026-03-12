# Created for 0006_0001_box_in_a_cloud.json

""" Summary:
The provided function generates an architectural concept model based on the "Box in a cloud" metaphor by creating a solid, geometric core (the 'box') and surrounding it with a lighter, more fluid 'cloud' layer. The function constructs the 'box' as a rectangular prism using defined dimensions to convey stability. It then generates the 'cloud' using curved surfaces, which extend beyond the box and suggest ethereality, employing randomization for organic shape variations. This interplay between the solid box and the flowing cloud highlights the contrast between structure and lightness, facilitating a spatial dialogue that embodies the metaphor effectively."""

#! python 3
function_code = """def create_box_in_cloud_model(box_x, box_y, box_z, cloud_offset, cloud_curvature, seed=123):
    \"""
    Creates an architectural Concept Model based on the 'Box in a cloud' metaphor.

    This function generates a central geometric form (the 'box') and surrounds it with a secondary layer 
    (the 'cloud') that is lighter and more diffuse. The 'box' is represented by a solid rectangular prism 
    while the 'cloud' is represented by a series of curved surfaces that suggest movement and ethereality.

    Parameters:
    - box_x (float): Width of the central box in meters.
    - box_y (float): Depth of the central box in meters.
    - box_z (float): Height of the central box in meters.
    - cloud_offset (float): The distance the cloud extends beyond the box.
    - cloud_curvature (float): The degree of curvature applied to the cloud surfaces.
    - seed (int, optional): Seed for random number generator for reproducibility.

    Returns:
    - List of RhinoCommon Brep objects representing the 3D geometries of the concept model.
    \"""
    import Rhino.Geometry as rg
    import random
    
    # Set random seed for reproducibility
    random.seed(seed)

    # Create the central 'box' as a Brep
    box_corners = [
        rg.Point3d(0, 0, 0),
        rg.Point3d(box_x, 0, 0),
        rg.Point3d(box_x, box_y, 0),
        rg.Point3d(0, box_y, 0),
        rg.Point3d(0, 0, box_z),
        rg.Point3d(box_x, 0, box_z),
        rg.Point3d(box_x, box_y, box_z),
        rg.Point3d(0, box_y, box_z)
    ]
    box = rg.Brep.CreateFromBox(box_corners)

    # Create the 'cloud' surfaces
    cloud_breps = []
    for i in range(4):
        # Define the cloud's control points
        pt1 = rg.Point3d(-cloud_offset, -cloud_offset, box_z/2) if i in [0, 3] else rg.Point3d(box_x + cloud_offset, -cloud_offset, box_z/2)
        pt2 = rg.Point3d(-cloud_offset, box_y + cloud_offset, box_z/2) if i in [0, 1] else rg.Point3d(box_x + cloud_offset, box_y + cloud_offset, box_z/2)
        
        curve1 = rg.NurbsCurve.Create(False, 3, [
            pt1,
            rg.Point3d(pt1.X, pt1.Y + box_y/2 + random.uniform(-cloud_curvature, cloud_curvature), random.uniform(0, box_z)),
            rg.Point3d(pt1.X, pt1.Y + box_y + cloud_offset, random.uniform(0, box_z))
        ])
        
        curve2 = rg.NurbsCurve.Create(False, 3, [
            pt2,
            rg.Point3d(pt2.X, pt2.Y - box_y/2 + random.uniform(-cloud_curvature, cloud_curvature), random.uniform(0, box_z)),
            rg.Point3d(pt2.X, pt2.Y - box_y - cloud_offset, random.uniform(0, box_z))
        ])
        
        loft = rg.Brep.CreateFromLoft([curve1, curve2], rg.Point3d.Unset, rg.Point3d.Unset, rg.LoftType.Normal, False)
        if loft:
            cloud_breps.append(loft[0])

    return [box] + cloud_breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_box_in_cloud_model(5.0, 3.0, 4.0, 2.0, 1.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_box_in_cloud_model(10.0, 8.0, 6.0, 3.0, 2.0, seed=456)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_box_in_cloud_model(7.0, 5.0, 3.0, 1.0, 2.5, seed=789)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_box_in_cloud_model(12.0, 9.0, 5.0, 4.0, 3.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_box_in_cloud_model(8.0, 6.0, 7.0, 2.5, 2.0, seed=321)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
