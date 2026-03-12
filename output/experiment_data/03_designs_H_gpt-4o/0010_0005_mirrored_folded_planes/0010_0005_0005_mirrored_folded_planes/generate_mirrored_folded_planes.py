# Created for 0010_0005_mirrored_folded_planes.json

""" Summary:
The function `generate_mirrored_folded_planes` creates an architectural concept model inspired by the metaphor "Mirrored folded planes." It generates interlocked, angular forms by folding a base rectangle at specified angles, resulting in dynamic surfaces that suggest movement. The model incorporates reflective symmetry by mirroring these geometries across defined axes, enhancing visual complexity and depth. This process emphasizes the interplay of light and shadow, achieving a rhythmic design that invites exploration. The outcome is a cohesive yet intricate network of spaces, embodying the metaphor's essence of balance between complexity and coherence, while promoting a choreographed spatial experience."""

#! python 3
function_code = """def generate_mirrored_folded_planes(width, depth, height, fold_angle, mirror_axes, seed=None):
    \"""
    Generate an architectural Concept Model based on the 'Mirrored folded planes' metaphor.
    
    This function creates a series of interlocked angular forms that are folded and mirrored 
    across multiple axes. The design emphasizes dynamic equilibrium and rhythmic interplay 
    of light and shadow, embodying complexity and coherence.
    
    Parameters:
    - width (float): Width of the base plane in meters.
    - depth (float): Depth of the base plane in meters.
    - height (float): Height of the folded planes in meters.
    - fold_angle (float): Angle in degrees at which the planes are folded.
    - mirror_axes (list of str): Axes ('x', 'y', 'z') across which the geometry will be mirrored.
    - seed (int, optional): Seed for randomness to ensure replicable results.
    
    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep objects representing the 3D geometries.
    \"""
    import Rhino.Geometry as rg
    import math
    import random

    if seed is not None:
        random.seed(seed)

    def create_folded_plane(w, d, h, angle):
        # Base rectangle
        rect_corners = [
            rg.Point3d(0, 0, 0),
            rg.Point3d(w, 0, 0),
            rg.Point3d(w, d, 0),
            rg.Point3d(0, d, 0)
        ]

        base_surface = rg.Brep.CreateFromCornerPoints(rect_corners[0], rect_corners[1], rect_corners[2], rect_corners[3], 0.01)

        # Fold the plane
        fold_rad = math.radians(angle)
        fold_vector = rg.Vector3d(0, 0, h)
        axis = rg.Line(rect_corners[0], rect_corners[1])
        fold_transform = rg.Transform.Rotation(fold_rad, axis.Direction, rect_corners[0])
        base_surface.Transform(fold_transform)

        return base_surface

    folded_plane = create_folded_plane(width, depth, height, fold_angle)

    def mirror_geometry(geometry, axes):
        mirrored_geometries = [geometry]
        for axis in axes:
            if axis == 'x':
                mirror_plane = rg.Plane.WorldYZ
            elif axis == 'y':
                mirror_plane = rg.Plane.WorldZX
            elif axis == 'z':
                mirror_plane = rg.Plane.WorldXY
            else:
                continue

            mirrored_geom = geometry.Duplicate()
            mirror_transform = rg.Transform.Mirror(mirror_plane)
            mirrored_geom.Transform(mirror_transform)
            mirrored_geometries.append(mirrored_geom)

        return mirrored_geometries

    geometries = mirror_geometry(folded_plane, mirror_axes)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = generate_mirrored_folded_planes(5.0, 3.0, 2.0, 45.0, ['x', 'y'], seed=42)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = generate_mirrored_folded_planes(4.0, 2.5, 3.5, 30.0, ['z'], seed=10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = generate_mirrored_folded_planes(6.0, 4.0, 5.0, 60.0, ['x', 'z'], seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = generate_mirrored_folded_planes(7.0, 3.5, 4.0, 90.0, ['y', 'z'], seed=24)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = generate_mirrored_folded_planes(8.0, 5.0, 3.0, 75.0, ['x', 'y', 'z'], seed=15)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
