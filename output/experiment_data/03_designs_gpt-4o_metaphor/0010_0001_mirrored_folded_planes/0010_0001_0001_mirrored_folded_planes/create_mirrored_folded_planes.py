# Created for 0010_0001_mirrored_folded_planes.json

""" Summary:
The function `create_mirrored_folded_planes` generates an architectural concept model inspired by the metaphor of "Mirrored folded planes." It creates a series of dynamic, angular surfaces that exhibit reflective symmetry and layered geometries. By specifying dimensions and fold counts, the function establishes a base plane, which is then folded and mirrored along the Y-axis. This process produces intricate forms that embody both symmetry and complexity, capturing the essence of the metaphor. The resulting geometries are designed to engage viewers through rhythmic repetition, depth, and a balance of visual elements, aligning with the specified design task."""

#! python 3
function_code = """def create_mirrored_folded_planes(width, height, depth, fold_count=3):
    \"""
    Create an architectural Concept Model based on the 'Mirrored folded planes' metaphor.
    
    This function generates a series of folded planes with reflective symmetry to explore 
    the interplay of symmetry and complexity. The design uses dynamic, angular forms and 
    mirrored symmetry to create spaces with rhythmic repetition and layered geometries.

    Parameters:
    width (float): Total width of the concept model in meters.
    height (float): Height of the concept model in meters.
    depth (float): Depth of the concept model in meters.
    fold_count (int): Number of folds in each plane. Default is 3.

    Returns:
    List[Rhino.Geometry.Brep]: A list of brep geometries representing the concept model.
    \"""
    
    import Rhino.Geometry as rg
    import random
    
    # Ensure replicability
    random.seed(42)
    
    def create_folded_plane(base_point, width, height, fold_count):
        \"""Helper function to create a single folded plane.\"""
        # Calculate segment width
        segment_width = width / fold_count
        
        points = []
        for i in range(fold_count + 1):
            x = base_point.X + i * segment_width
            z = base_point.Z + height * (random.random() - 0.5)
            points.append(rg.Point3d(x, base_point.Y, z))
        
        # Create a polyline from these points
        polyline = rg.Polyline(points)
        
        # Create a surface from the polyline by extruding it in Y direction
        curve = polyline.ToNurbsCurve()
        vector = rg.Vector3d(0, depth, 0)
        extrusion = rg.Extrusion.Create(curve, depth, True)
        surface = extrusion.ToBrep()
        
        return surface

    def mirror_geometry(geometry, axis):
        \"""Helper function to mirror geometries along a given axis.\"""
        mirror_plane = rg.Plane.WorldXY
        if axis.lower() == 'x':
            mirror_plane = rg.Plane.WorldYZ
        elif axis.lower() == 'y':
            mirror_plane = rg.Plane.WorldZX
        
        mirrored_geometry = [geometry.Duplicate()]
        for geo in mirrored_geometry:
            geo.Transform(rg.Transform.Mirror(mirror_plane))
        
        return mirrored_geometry

    # Create initial folded plane
    initial_plane = create_folded_plane(rg.Point3d(0, 0, 0), width, height, fold_count)
    
    # Mirror the plane along the Y-axis
    mirrored_planes = mirror_geometry(initial_plane, 'y')
    
    # Combine original and mirrored planes
    all_planes = [initial_plane] + mirrored_planes

    return all_planes"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_mirrored_folded_planes(10.0, 5.0, 2.0, 4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_mirrored_folded_planes(15.0, 8.0, 3.0, 2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_mirrored_folded_planes(12.0, 6.0, 4.0, 5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_mirrored_folded_planes(20.0, 10.0, 1.0, 6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_mirrored_folded_planes(8.0, 4.0, 3.0, 3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
