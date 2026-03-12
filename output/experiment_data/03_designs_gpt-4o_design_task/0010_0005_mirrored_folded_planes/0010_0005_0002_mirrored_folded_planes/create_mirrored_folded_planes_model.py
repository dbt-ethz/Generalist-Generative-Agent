# Created for 0010_0005_mirrored_folded_planes.json

""" Summary:
The function `create_mirrored_folded_planes_model` generates an architectural concept model based on the metaphor of "Mirrored folded planes." It constructs interlocked, angular forms that reflect across specified axes, embodying dynamic equilibrium. The function takes parameters such as base dimensions, height, fold angle, and mirror axes to create a folded plane, which is then mirrored to enhance visual depth and complexity. By strategically arranging these elements, the model achieves a rhythmic interplay of light and shadow, inviting exploration of its intricate geometries. Ultimately, the resulting model effectively represents the metaphors essence of complexity and coherence."""

#! python 3
function_code = """def create_mirrored_folded_planes_model(base_length, base_width, height, fold_angle, mirror_axes):
    \"""
    Create an architectural Concept Model based on the 'Mirrored folded planes' metaphor.
    
    This function generates interlocked, angular forms that reflect across specified axes to create a dynamic equilibrium.
    
    Inputs:
    - base_length: Length of the base plane in meters.
    - base_width: Width of the base plane in meters.
    - height: Height of the folded planes in meters.
    - fold_angle: The angle in degrees at which the planes are folded.
    - mirror_axes: A list of axes ('x', 'y', 'z') across which the geometry will be mirrored.
    
    Outputs:
    - A list of Brep objects representing the 3D geometries of the concept model.
    \"""
    import Rhino
    import Rhino.Geometry as rg
    from math import radians, tan
    
    # Base plane
    base_plane = rg.Plane.WorldXY
    base_rect = rg.Rectangle3d(base_plane, base_length, base_width)
    
    # Folded plane construction
    fold_radians = radians(fold_angle)
    fold_height = height * tan(fold_radians)
    fold_vector = rg.Vector3d(0, 0, fold_height)
    
    # Create initial folded plane
    corner1 = base_rect.Corner(0)
    corner2 = base_rect.Corner(1)
    corner3 = base_rect.Corner(2) + fold_vector
    corner4 = base_rect.Corner(3) + fold_vector
    
    folded_plane = rg.Brep.CreateFromCornerPoints(corner1, corner2, corner3, corner4, 0.01)
    
    # Create mirrored copies
    breps = [folded_plane]
    for axis in mirror_axes:
        mirror_plane = None
        if axis == 'x':
            mirror_plane = rg.Plane.WorldYZ
        elif axis == 'y':
            mirror_plane = rg.Plane.WorldZX
        elif axis == 'z':
            mirror_plane = rg.Plane.WorldXY
            
        if mirror_plane:
            mirrored_brep = folded_plane.Duplicate()
            mirrored_brep.Transform(rg.Transform.Mirror(mirror_plane))
            breps.append(mirrored_brep)
    
    # Combine all breps into a cohesive model
    model_brep = rg.Brep.JoinBreps(breps, 0.01)
    
    return model_brep if model_brep else breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_mirrored_folded_planes_model(5, 3, 2, 30, ['x', 'y'])
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_mirrored_folded_planes_model(10, 5, 4, 45, ['z'])
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_mirrored_folded_planes_model(6, 4, 3, 60, ['x', 'z'])
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_mirrored_folded_planes_model(8, 2, 5, 15, ['y', 'z'])
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_mirrored_folded_planes_model(7, 3, 6, 75, ['x'])
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
