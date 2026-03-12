# Created for 0010_0003_mirrored_folded_planes.json

""" Summary:
The provided function generates an architectural concept model inspired by the metaphor of "Mirrored folded planes" by creating a series of angular, folded geometries. It takes parameters such as dimensions and the number of planes, and for each plane, it constructs a polyline and lofts it into a surface. Each surface is then mirrored across a specified axis, achieving a symmetrical design that reflects the metaphor's essence. This process results in a collection of interconnected geometries that embody complexity and unity, promoting a dynamic interplay of light and shadow, while facilitating fluid transitions between spaces in the model."""

#! python 3
function_code = """def create_mirrored_folded_planes_model(base_length, base_width, height, num_planes, mirror_axis):
    \"""
    Creates an architectural Concept Model based on the metaphor of "Mirrored folded planes".
    
    Parameters:
    - base_length: The base length of the folded plane structure.
    - base_width: The base width of the folded plane structure.
    - height: The height of each folded plane.
    - num_planes: The number of folded planes to generate.
    - mirror_axis: The axis along which the planes will be mirrored ('X', 'Y', or 'Z').

    Returns:
    - A list of mirrored Brep geometries representing the folded planes.
    \"""
    import Rhino.Geometry as rg
    import random
    
    random.seed(42)  # Ensure replicable randomness

    # Create a list to store the Breps
    breps = []

    # Create the initial folded plane
    base_plane = rg.Plane.WorldXY
    for i in range(num_planes):
        # Calculate the offset for the current plane
        offset = i * base_width
        
        # Create the initial points for the fold
        pt1 = rg.Point3d(offset, 0, 0)
        pt2 = rg.Point3d(offset + base_length / 2, base_width / 2, height)
        pt3 = rg.Point3d(offset + base_length, 0, 0)
        
        # Create the fold as a polyline
        polyline = rg.Polyline([pt1, pt2, pt3])
        
        # Loft the polyline to create a surface
        curve = polyline.ToNurbsCurve()
        lofted_surfaces = rg.Brep.CreateFromLoft([curve], rg.Point3d.Unset, rg.Point3d.Unset, rg.LoftType.Straight, False)
        
        if not lofted_surfaces:
            continue
        
        lofted_surface = lofted_surfaces[0]
        
        # Reflect the lofted surface across the specified axis
        if mirror_axis.upper() == 'X':
            mirror_plane = rg.Plane.WorldYZ
        elif mirror_axis.upper() == 'Y':
            mirror_plane = rg.Plane.WorldXZ
        else:
            mirror_plane = rg.Plane.WorldXY
        
        mirrored_surface = lofted_surface.DuplicateBrep()
        mirrored_surface.Transform(rg.Transform.Mirror(mirror_plane))
        
        # Add both original and mirrored surfaces to the list of breps
        breps.extend([lofted_surface, mirrored_surface])
    
    return breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_mirrored_folded_planes_model(10, 5, 3, 4, 'X')
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_mirrored_folded_planes_model(15, 7, 5, 6, 'Y')
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_mirrored_folded_planes_model(12, 6, 4, 5, 'Z')
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_mirrored_folded_planes_model(20, 10, 8, 3, 'Y')
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_mirrored_folded_planes_model(18, 9, 4, 7, 'X')
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
