# Created for 0010_0001_mirrored_folded_planes.json

""" Summary:
The function `create_concept_model_mirrored_folded_planes` generates an architectural concept model inspired by the metaphor of "Mirrored folded planes." It takes parameters such as base dimensions, plane height, fold angle, and fold count to create a series of folded planes. The function first constructs folded planes on one side, employing a systematic rotation to introduce dynamic, angular forms. Then, it mirrors these planes across a defined axis to achieve reflective symmetry, enhancing visual impact and coherence. The resulting 3D geometries embody the interplay of symmetry and complexity, inviting exploration of intricate layered structures."""

#! python 3
function_code = """def create_concept_model_mirrored_folded_planes(base_length, base_width, plane_height, fold_angle, fold_count):
    \"""
    Creates an architectural Concept Model based on the metaphor of 'Mirrored folded planes'.
    
    Parameters:
    - base_length (float): The length of the base plane in meters.
    - base_width (float): The width of the base plane in meters.
    - plane_height (float): The height of each folded plane in meters.
    - fold_angle (float): The angle in degrees by which the planes are folded.
    - fold_count (int): The number of folds on each side of the symmetry axis.

    Returns:
    - List of RhinoCommon Brep: A list of 3D geometries representing the concept model.
    \"""
    import Rhino
    import Rhino.Geometry as rg
    import math

    # Helper function to create a folded plane
    def create_folded_plane(base_pt, length, width, height, angle, folds):
        planes = []
        current_pt = base_pt
        angle_rad = math.radians(angle)
        for i in range(folds):
            # Create a base rectangle
            rect = rg.Rectangle3d(rg.Plane.WorldXY, rg.Interval(0, length), rg.Interval(0, width)).ToNurbsCurve()
            
            # Create a plane
            plane = rg.Plane(current_pt, rg.Vector3d.ZAxis)
            plane.Rotate(angle_rad * (i % 2 == 0 and 1 or -1), plane.YAxis)
            
            # Extrude the rectangle along the plane's normal
            extrude_vector = plane.Normal * height
            extrusion = rg.Extrusion.Create(rect, height, True)
            extrusion.Rotate(angle_rad * (i % 2 == 0 and 1 or -1), plane.Origin, plane.YAxis)
            
            # Move the current point for the next fold
            translation_vector = rg.Vector3d(length, 0, 0)
            current_pt = rg.Point3d.Add(current_pt, translation_vector)
            
            planes.append(extrusion.ToBrep())
        return planes

    # Create folded planes on one side
    base_point = rg.Point3d(0, 0, 0)
    folded_planes_one_side = create_folded_plane(base_point, base_length, base_width, plane_height, fold_angle, fold_count)

    # Mirror the folded planes to the other side
    mirror_plane = rg.Plane(rg.Point3d(0, base_width / 2, 0), rg.Vector3d.YAxis)
    mirrored_planes = [brep.Transform(rg.Transform.Mirror(mirror_plane)) or brep for brep in folded_planes_one_side]

    # Combine all geometries
    concept_model = folded_planes_one_side + mirrored_planes

    return concept_model"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_concept_model_mirrored_folded_planes(10.0, 5.0, 3.0, 45.0, 4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_concept_model_mirrored_folded_planes(8.0, 4.0, 2.5, 30.0, 3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_concept_model_mirrored_folded_planes(12.0, 6.0, 4.0, 60.0, 5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_concept_model_mirrored_folded_planes(15.0, 7.0, 5.0, 50.0, 6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_concept_model_mirrored_folded_planes(9.0, 4.5, 3.5, 40.0, 2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
