# Created for 0010_0005_mirrored_folded_planes.json

""" Summary:
The provided function generates an architectural concept model based on the metaphor "Mirrored folded planes" by creating interlocked, angular geometries that reflect across specified axes. It begins by defining the dimensions and angles of the folded planes, using trigonometric functions to achieve the desired folding effect. The model incorporates mirroring transformations to enhance symmetry and complexity, creating a dynamic interplay of light and shadow. By generating multiple geometries with varied parameters, the function effectively illustrates the metaphors essence balancing intricate forms and cohesive spatial arrangements, inviting exploration of layered geometries that embody the design task's intent."""

#! python 3
function_code = """def create_mirrored_folded_planes_model(base_length, height, fold_angle, mirror_axis, seed):
    \"""
    Creates an architectural Concept Model based on the metaphor 'Mirrored folded planes'.
    
    This function generates a series of interlocked, angular forms that reflect across multiple axes,
    creating a cohesive yet intricate design. It uses folded planes and mirroring to achieve dynamic 
    equilibrium, emphasizing the rhythmic interplay of light and shadow.

    Parameters:
    - base_length (float): The length of the base of the folded plane.
    - height (float): The height of the folded plane.
    - fold_angle (float): The angle at which the planes are folded, in degrees.
    - mirror_axis (str): The axis across which the planes are mirrored ('x', 'y', or 'z').
    - seed (int): Seed for random number generation to ensure replicability.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep geometries representing the Concept Model.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    # Set the random seed for replicability
    random.seed(seed)

    # Convert the fold angle from degrees to radians
    fold_angle_rad = math.radians(fold_angle)

    # Create the initial folded plane
    base_plane = rg.Plane.WorldXY
    fold_vector = rg.Vector3d(math.sin(fold_angle_rad), 0, math.cos(fold_angle_rad))
    fold_vector.Unitize()
    fold_vector *= height

    # Define the points for the folded plane
    pt1 = rg.Point3d(0, 0, 0)
    pt2 = rg.Point3d(base_length, 0, 0)
    pt3 = rg.Point3d(base_length, 0, height)
    pt4 = rg.Point3d(0, 0, height)

    # Fold the plane
    fold_line = rg.Line(pt2, pt3)
    fold_transform = rg.Transform.Rotation(fold_angle_rad, fold_line.Direction, pt2)
    pt3.Transform(fold_transform)
    pt4.Transform(fold_transform)

    # Create the brep from the folded plane
    profile = rg.Polyline([pt1, pt2, pt3, pt4, pt1])
    plane_brep = rg.Brep.CreateFromCornerPoints(pt1, pt2, pt3, pt4, 0.01)

    # Mirror the plane based on the specified axis
    if mirror_axis == 'x':
        mirror_transform = rg.Transform.Mirror(rg.Plane.WorldYZ)
    elif mirror_axis == 'y':
        mirror_transform = rg.Transform.Mirror(rg.Plane.WorldZX)
    elif mirror_axis == 'z':
        mirror_transform = rg.Transform.Mirror(rg.Plane.WorldXY)
    else:
        raise ValueError("Invalid mirror axis. Choose 'x', 'y', or 'z'.")

    mirrored_plane_brep = plane_brep.DuplicateBrep()
    mirrored_plane_brep.Transform(mirror_transform)

    # Interlock the geometries
    interlocked_breps = [plane_brep, mirrored_plane_brep]

    # Return the final list of geometries
    return interlocked_breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_mirrored_folded_planes_model(10.0, 5.0, 30.0, 'z', 42)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_mirrored_folded_planes_model(15.0, 8.0, 45.0, 'x', 7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_mirrored_folded_planes_model(12.0, 6.0, 60.0, 'y', 99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_mirrored_folded_planes_model(20.0, 10.0, 75.0, 'x', 15)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_mirrored_folded_planes_model(8.0, 4.0, 90.0, 'y', 23)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
