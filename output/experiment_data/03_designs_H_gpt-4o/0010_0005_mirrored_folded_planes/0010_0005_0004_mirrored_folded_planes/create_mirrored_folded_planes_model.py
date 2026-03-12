# Created for 0010_0005_mirrored_folded_planes.json

""" Summary:
The function `create_mirrored_folded_planes_model` generates an architectural concept model inspired by the metaphor "Mirrored folded planes." It constructs angular, interlocked forms that reflect across multiple axes, embodying dynamic equilibrium through strategic folding and arrangement. By defining the initial geometry with specified dimensions and a folding angle, the function creates a base structure, applies transformations to reflect and mirror it, and generates multiple mirrored versions. This process results in a cohesive design that highlights the interplay of light and shadow, thereby communicating the metaphor's complexity and coherence while inviting exploration of its rhythmic geometries."""

#! python 3
function_code = """def create_mirrored_folded_planes_model(width, depth, height, fold_angle, mirror_count):
    \"""
    Create an architectural Concept Model based on the 'Mirrored folded planes' metaphor.
    
    This function generates a series of interlocked, angular forms that reflect across multiple axes,
    creating a dynamic equilibrium with rhythmic interplay of light and shadow.

    Parameters:
    - width (float): The width of the initial plane in meters.
    - depth (float): The depth of the initial plane in meters.
    - height (float): The height of the folded planes in meters.
    - fold_angle (float): The angle in degrees at which the planes are folded.
    - mirror_count (int): The number of times the geometry is mirrored along different axes.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep objects representing the 3D geometries.
    \"""

    import Rhino.Geometry as rg
    import math

    def create_folded_geometry(w, d, h, angle):
        # Create base rectangle
        base_rect = rg.Rectangle3d(rg.Plane.WorldXY, w, d)
        base_brep = rg.Brep.CreateFromCornerPoints(base_rect.Corner(0), base_rect.Corner(1),
                                                   base_rect.Corner(2), base_rect.Corner(3), 0.01)
        # Define fold line and transform
        fold_line = rg.Line(base_rect.Corner(0), rg.Point3d(w, 0, 0))
        fold_rad = math.radians(angle)
        fold_transform = rg.Transform.Rotation(fold_rad, fold_line.Direction, base_rect.Corner(0))
        
        folded_brep = base_brep.Duplicate()
        folded_brep.Transform(fold_transform)
        
        # Move the folded brep up
        translation = rg.Transform.Translation(0, 0, h)
        folded_brep.Transform(translation)
        
        return folded_brep

    def mirror_geometry(brep, count):
        mirrored_geometries = [brep]
        for i in range(1, count):
            mirror_plane = rg.Plane.WorldXY
            rotation = rg.Transform.Rotation((math.pi * 2 / count) * i, rg.Vector3d.ZAxis, rg.Point3d(0, 0, 0))
            mirrored_brep = brep.Duplicate()
            mirrored_brep.Transform(rotation)
            mirrored_brep.Transform(rg.Transform.Mirror(mirror_plane))
            mirrored_geometries.append(mirrored_brep)
        return mirrored_geometries

    # Create initial folded geometry
    folded_geometry = create_folded_geometry(width, depth, height, fold_angle)

    # Mirror the geometry
    mirrored_geometries = mirror_geometry(folded_geometry, mirror_count)

    return mirrored_geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_mirrored_folded_planes_model(5.0, 3.0, 2.5, 45.0, 6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_mirrored_folded_planes_model(4.0, 2.0, 3.0, 60.0, 4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_mirrored_folded_planes_model(6.0, 4.0, 3.0, 30.0, 8)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_mirrored_folded_planes_model(7.0, 5.0, 4.0, 50.0, 5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_mirrored_folded_planes_model(8.0, 6.0, 3.5, 75.0, 3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
