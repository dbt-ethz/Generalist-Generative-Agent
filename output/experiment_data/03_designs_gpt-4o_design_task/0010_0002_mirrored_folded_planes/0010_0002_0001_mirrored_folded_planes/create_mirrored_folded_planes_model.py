# Created for 0010_0002_mirrored_folded_planes.json

""" Summary:
The function `create_mirrored_folded_planes_model` generates an architectural concept model inspired by the metaphor "Mirrored folded planes" by creating a series of angular, folded surfaces that reflect across specified axes. It defines parameters for base dimensions, fold angles, and the number of planes to construct. Each plane is created with alternating fold angles to enhance visual tension and movement. The function mirrors these planes to create symmetrical reflections, which reinforces unity in the design. The resulting model comprises complex yet harmonious geometries, effectively embodying the metaphor's themes of dynamic exploration and layered spatial organization."""

#! python 3
function_code = """def create_mirrored_folded_planes_model(base_size, fold_angle, num_planes, mirror_axis='x'):
    \"""
    Create an architectural Concept Model inspired by the 'Mirrored folded planes' metaphor.
    
    This function generates a composition of angular, folded elements that interact across several mirrored axes,
    creating a dynamic interplay of form and void. The model emphasizes visual movement and tension through strategic
    positioning of folds and voids, with mirrored symmetry enhancing order and unity.

    Parameters:
    - base_size: tuple of three floats (length, width, height) representing the base size of the model in meters.
    - fold_angle: float representing the angle in degrees to fold each plane.
    - num_planes: integer representing the number of planes to be generated.
    - mirror_axis: string ('x', 'y', or 'z') representing the axis along which to apply mirroring.

    Returns:
    - A list of RhinoCommon Brep objects representing the 3D geometries of the concept model.
    \"""
    import Rhino.Geometry as rg
    import math

    length, width, height = base_size
    planes = []
    mirrored_planes = []

    # Create planes with folds
    for i in range(num_planes):
        # Determine the angle for the current plane
        angle = math.radians(fold_angle * (i % 2) * (-1)**i)  # Alternate fold direction

        # Create the base plane
        base_plane = rg.Plane.WorldXY
        base_plane.Origin = rg.Point3d(i * length / num_planes, 0, 0)

        # Create the fold
        fold_vector = rg.Vector3d(0, math.tan(angle) * width, height)
        fold_plane = rg.Plane(base_plane)
        fold_plane.Translate(fold_vector)

        # Create the surface for the folded plane
        surface = rg.Brep.CreateFromCornerPoints(base_plane.Origin, 
                                                 base_plane.Origin + rg.Vector3d(length, 0, 0), 
                                                 fold_plane.Origin + rg.Vector3d(length, 0, 0), 
                                                 fold_plane.Origin, 
                                                 0.01)
        planes.append(surface)

    # Mirror the planes
    mirror_plane = rg.Plane.WorldZX if mirror_axis == 'x' else rg.Plane.WorldYZ if mirror_axis == 'y' else rg.Plane.WorldXY
    for plane in planes:
        mirrored = plane.Duplicate()
        mirrored.Transform(rg.Transform.Mirror(mirror_plane))
        mirrored_planes.append(mirrored)

    # Combine original and mirrored planes
    concept_model = planes + mirrored_planes

    return concept_model"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_mirrored_folded_planes_model((10.0, 5.0, 3.0), 30.0, 6, 'y')
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_mirrored_folded_planes_model((15.0, 8.0, 2.0), 45.0, 4, 'z')
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_mirrored_folded_planes_model((12.0, 6.0, 4.0), 60.0, 5, 'x')
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_mirrored_folded_planes_model((20.0, 10.0, 5.0), 15.0, 3, 'x')
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_mirrored_folded_planes_model((8.0, 4.0, 2.5), 75.0, 8, 'y')
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
