# Created for 0010_0002_mirrored_folded_planes.json

""" Summary:
The provided function generates an architectural concept model inspired by the metaphor "Mirrored folded planes." It creates a series of angular, folded geometries that reflect across specified axes, embodying movement and visual tension. By defining base dimensions and fold heights, the function constructs folded planes with varying angles. Mirroring these planes enhances symmetry and visual complexity, aligning with the metaphor's theme. The generated geometries offer a dynamic interplay of light and shadow, while their arrangement around mirrored focal points fosters interconnected spatial experiences, ultimately achieving a balance between intricate forms and cohesive design, encouraging exploration within the architectural narrative."""

#! python 3
function_code = """def create_mirrored_folded_planes_model(base_length=20, base_width=15, fold_height=5, mirror_axis='z'):
    \"""
    Creates an architectural Concept Model inspired by the 'Mirrored folded planes' metaphor.

    This function generates a series of angular, folded elements that interact across mirrored axes,
    creating dynamic forms to embody the metaphor. The design emphasizes visual movement and tension
    through strategic folds and mirrored symmetry.

    Parameters:
    - base_length: float representing the length of each plane in meters.
    - base_width: float representing the width of each plane in meters.
    - fold_height: float representing the height of the folds in meters.
    - mirror_axis: string ('x', 'y', or 'z') representing the axis along which to apply mirroring.

    Returns:
    - A list of RhinoCommon Brep objects representing the 3D geometries of the concept model.
    \"""
    import Rhino.Geometry as rg
    import math

    def create_folded_plane(base_point, fold_angle):
        # Create a rectangle to represent the plane
        rect = rg.Rectangle3d(rg.Plane.WorldXY, base_length, base_width)
        rect.Transform(rg.Transform.Translation(base_point))
        
        # Calculate the folding vector based on the fold angle
        fold_vector = rg.Vector3d(0, 0, fold_height * math.tan(math.radians(fold_angle)))
        
        # Create folding transformation
        fold_transform = rg.Transform.Translation(fold_vector)
        rect.Transform(fold_transform)
        
        # Create a surface from the folded plane
        surface = rg.Brep.CreateFromCornerPoints(
            rect.Corner(0), rect.Corner(1), rect.Corner(2), rect.Corner(3), 0.01)
        
        return surface

    # List to store geometries
    geometries = []
    num_planes = 4
    fold_angles = [30, -30, 45, -45]  # Different angles for dynamic appearance

    # Generate folded planes
    for i in range(num_planes):
        base_pt = rg.Point3d(i * base_length, 0, 0)
        folded_plane = create_folded_plane(base_pt, fold_angles[i % len(fold_angles)])
        geometries.append(folded_plane)

    # Define the mirror plane
    mirror_plane = rg.Plane.WorldXY if mirror_axis == 'z' else rg.Plane.WorldYZ if mirror_axis == 'x' else rg.Plane.WorldZX
    
    # Mirror the folded planes
    mirrored_geometries = []
    for geom in geometries:
        mirrored_geom = geom.Duplicate()
        mirrored_geom.Transform(rg.Transform.Mirror(mirror_plane))
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
    geometry = create_mirrored_folded_planes_model(base_length=25, base_width=20, fold_height=7, mirror_axis='y')
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_mirrored_folded_planes_model(base_length=30, base_width=10, fold_height=3, mirror_axis='x')
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_mirrored_folded_planes_model(base_length=15, base_width=15, fold_height=10, mirror_axis='z')
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_mirrored_folded_planes_model(base_length=40, base_width=25, fold_height=8, mirror_axis='x')
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_mirrored_folded_planes_model(base_length=22, base_width=18, fold_height=6, mirror_axis='y')
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
