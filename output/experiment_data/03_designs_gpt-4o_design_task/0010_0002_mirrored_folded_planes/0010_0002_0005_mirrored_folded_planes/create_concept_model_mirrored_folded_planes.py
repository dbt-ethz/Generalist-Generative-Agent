# Created for 0010_0002_mirrored_folded_planes.json

""" Summary:
The function `create_concept_model_mirrored_folded_planes` generates an architectural concept model by creating angular, folded geometries inspired by the metaphor "Mirrored folded planes." It achieves this through a series of transformations, including creating a base plane and applying fold angles to generate dynamic forms. The model incorporates multiple mirrored axes, enhancing symmetry and visual tension. By strategically placing folds and voids, it emphasizes light interaction with materials, creating a visually engaging spatial experience. The resulting 3D geometries reflect the interconnected environments envisioned in the design task, promoting exploration and movement within the architectural space."""

#! python 3
function_code = """def create_concept_model_mirrored_folded_planes(base_length, base_width, height, fold_angle, mirror_axis_count):
    \"""
    Generates an architectural Concept Model inspired by the 'Mirrored folded planes' metaphor. The function creates angular, folded geometries
    that are mirrored across multiple axes to form a visually dynamic and cohesive design. The model highlights interplay of form and void 
    through the strategic placement of folds and mirrors, encouraging spatial exploration.

    Parameters:
    - base_length (float): The length of the base plane in meters.
    - base_width (float): The width of the base plane in meters.
    - height (float): The height of the folded elements in meters.
    - fold_angle (float): The angle in degrees at which the planes are folded.
    - mirror_axis_count (int): The number of axes across which the model is mirrored.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of 3D Brep geometries representing the concept model.
    \"""
    import Rhino.Geometry as rg
    import math

    # Initialize the list to hold the final geometries
    geometries = []

    # Create the base plane
    base_plane = rg.Plane.WorldXY
    base_rectangle = rg.Rectangle3d(base_plane, base_length, base_width)
    base_surface = rg.Brep.CreateFromCornerPoints(
        base_rectangle.Corner(0), base_rectangle.Corner(1), base_rectangle.Corner(2), base_rectangle.Corner(3), 0.01)

    # Calculate fold vector
    angle_rad = math.radians(fold_angle)
    fold_vector = rg.Vector3d(0, 0, height * math.sin(angle_rad))

    # Create folded planes
    for i in range(mirror_axis_count):
        # Calculate the offset for mirroring
        offset = (i + 1) * base_width / (mirror_axis_count + 1)

        # Create the left fold
        left_fold = base_surface.Duplicate()
        left_fold.Translate(rg.Vector3d(-offset, 0, 0))
        left_fold.Rotate(math.radians(45), rg.Vector3d.XAxis, rg.Point3d(0, 0, 0))
        geometries.append(left_fold)

        # Create the right fold mirrored across YZ plane
        right_fold = left_fold.Duplicate()
        right_fold.Transform(rg.Transform.Mirror(rg.Plane.WorldYZ))
        geometries.append(right_fold)

    # Create the mirrored folds across XY plane
    mirrored_geometries = []
    for geom in geometries:
        mirrored_geom = geom.Duplicate()
        mirrored_geom.Transform(rg.Transform.Mirror(rg.Plane.WorldXY))
        mirrored_geometries.append(mirrored_geom)

    # Combine original and mirrored geometries
    geometries.extend(mirrored_geometries)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_concept_model_mirrored_folded_planes(10.0, 5.0, 3.0, 30.0, 4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_concept_model_mirrored_folded_planes(15.0, 7.5, 2.5, 60.0, 3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_concept_model_mirrored_folded_planes(12.0, 6.0, 4.0, 45.0, 5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_concept_model_mirrored_folded_planes(8.0, 4.0, 2.0, 90.0, 2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_concept_model_mirrored_folded_planes(20.0, 10.0, 5.0, 15.0, 6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
