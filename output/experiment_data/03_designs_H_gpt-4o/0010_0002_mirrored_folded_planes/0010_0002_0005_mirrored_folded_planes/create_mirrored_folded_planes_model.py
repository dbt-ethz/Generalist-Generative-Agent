# Created for 0010_0002_mirrored_folded_planes.json

""" Summary:
The function `create_mirrored_folded_planes_model` generates an architectural concept model based on the metaphor of "Mirrored folded planes." It creates a series of angular, folded geometries by defining a base plane and applying a specified fold angle to create dynamic forms. The function utilizes parameters like base dimensions, fold count, and mirror axis to create a coherent design that reflects the metaphor's principles. By mirroring the generated geometries across specified axes, it enhances the visual tension and complexity, resulting in a model that embodies movement and encourages exploration through interconnected spaces."""

#! python 3
function_code = """def create_mirrored_folded_planes_model(base_length, base_width, height, fold_angle, fold_count, mirror_axis):
    \"""
    Generates an architectural Concept Model inspired by the 'Mirrored folded planes' metaphor. This function creates
    angular, folded geometries that are organized around mirrored axes, forming a dynamic and cohesive design that 
    encourages spatial exploration and visual tension.

    Parameters:
    - base_length (float): The length of each folded plane in meters.
    - base_width (float): The width of each folded plane in meters.
    - height (float): The height of the folded planes in meters.
    - fold_angle (float): The angle in degrees at which the planes are folded.
    - fold_count (int): The number of folded planes to create.
    - mirror_axis (str): The axis along which the geometry will be mirrored ('x', 'y', or 'z').

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep geometries representing the concept model.
    \"""
    import Rhino.Geometry as rg
    import math

    def create_folded_plane(base_pt, length, width, height, angle):
        # Define the base plane
        plane = rg.Plane(base_pt, rg.Vector3d(0, 0, 1))

        # Create two points for the fold
        pt1 = rg.Point3d(base_pt.X, base_pt.Y, base_pt.Z)
        pt2 = rg.Point3d(base_pt.X + length, base_pt.Y, base_pt.Z)
        pt3 = rg.Point3d(base_pt.X + length, base_pt.Y + width, base_pt.Z)
        
        # Calculate the folding line
        fold_vector = rg.Vector3d(math.sin(math.radians(angle)) * width, 0, math.cos(math.radians(angle)) * height)
        pt4 = pt3 + fold_vector

        # Create the fold as a Brep
        return rg.Brep.CreateFromCornerPoints(pt1, pt2, pt3, pt4, 0.01)

    geometries = []
    for i in range(fold_count):
        # Translate each fold
        base_pt = rg.Point3d(i * (base_length + 1), 0, 0)
        folded_plane = create_folded_plane(base_pt, base_length, base_width, height, fold_angle)
        geometries.append(folded_plane)
    
    mirrored_geometries = []
    mirror_plane = None
    if mirror_axis.lower() == 'x':
        mirror_plane = rg.Plane.WorldZX
    elif mirror_axis.lower() == 'y':
        mirror_plane = rg.Plane.WorldYZ
    elif mirror_axis.lower() == 'z':
        mirror_plane = rg.Plane.WorldXY

    if mirror_plane:
        for geom in geometries:
            mirrored_geom = geom.Duplicate()
            mirrored_geom.Transform(rg.Transform.Mirror(mirror_plane))
            mirrored_geometries.append(mirrored_geom)

    geometries.extend(mirrored_geometries)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_mirrored_folded_planes_model(5.0, 2.0, 3.0, 45.0, 4, 'x')
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_mirrored_folded_planes_model(4.0, 1.5, 2.5, 30.0, 6, 'y')
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_mirrored_folded_planes_model(6.0, 3.0, 4.0, 60.0, 5, 'z')
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_mirrored_folded_planes_model(7.0, 2.5, 3.5, 90.0, 3, 'y')
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_mirrored_folded_planes_model(8.0, 4.0, 5.0, 75.0, 2, 'x')
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
