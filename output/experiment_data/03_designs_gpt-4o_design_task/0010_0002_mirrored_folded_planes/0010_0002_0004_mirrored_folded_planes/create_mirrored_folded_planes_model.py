# Created for 0010_0002_mirrored_folded_planes.json

""" Summary:
The function `create_mirrored_folded_planes_model` generates an architectural concept model inspired by the metaphor of "Mirrored folded planes." It creates a series of angular, folded surfaces that interact with mirrored geometries across specified axes (X or Y). The function calculates fold angles and employs randomization to introduce dynamic visual tension and movement. Each folded plane is mirrored to enhance symmetry, while the arrangement of these elements fosters interconnected spaces that encourage exploration. By utilizing materials that reflect and refract light, the model embodies the metaphor's essence, balancing complexity with harmonious repetition in its design."""

#! python 3
function_code = """def create_mirrored_folded_planes_model(base_length, height, num_folds, mirror_axis):
    \"""
    Creates an architectural Concept Model inspired by the 'Mirrored folded planes' metaphor.
    
    Parameters:
    - base_length (float): The length of the base plane in meters.
    - height (float): The height of the folded planes in meters.
    - num_folds (int): Number of folds to generate.
    - mirror_axis (str): Axis along which the model is mirrored ('X' or 'Y').
    
    Returns:
    - List of Brep: A list of RhinoCommon Brep geometries representing the concept model.
    \"""
    import Rhino.Geometry as rg
    from System import Random
    
    # Set seed for randomness
    rand = Random(42)
    
    # List to store geometries
    geometries = []
    
    # Function to create a single folded plane
    def create_folded_plane(base_pt, length, height, fold_angle):
        # Create a base rectangle
        rect = rg.Rectangle3d(rg.Plane.WorldXY, length, height)
        rect.Transform(rg.Transform.Translation(base_pt))
        
        # Create a folding line
        mid_pt = rg.Point3d(base_pt.X + length / 2, base_pt.Y, base_pt.Z)
        folding_line = rg.Line(mid_pt, rg.Point3d(mid_pt.X, mid_pt.Y, mid_pt.Z + height))
        
        # Rotate the plane around the folding line
        rotate_transform = rg.Transform.Rotation(fold_angle, folding_line.Direction, folding_line.PointAt(0.5))
        rect.Transform(rotate_transform)
        
        # Create a surface from the folded plane
        surface = rg.Brep.CreateFromSurface(rg.NurbsSurface.CreateFromCorners(rect.Corner(0), rect.Corner(1), rect.Corner(2), rect.Corner(3)))
        
        return surface
    
    # Calculate fold angle increment
    base_fold_angle = rand.NextDouble() * 0.5  # Random base angle for dynamic appearance
    fold_angle_increment = base_fold_angle / num_folds
    
    # Generate folded planes
    for i in range(num_folds):
        fold_angle = base_fold_angle + i * fold_angle_increment
        base_pt = rg.Point3d(i * base_length, 0, 0)
        folded_plane = create_folded_plane(base_pt, base_length, height, fold_angle)
        geometries.append(folded_plane)
        
        # Mirror the folded plane
        if mirror_axis.upper() == 'X':
            mirror_transform = rg.Transform.Mirror(rg.Plane.WorldZX)
        elif mirror_axis.upper() == 'Y':
            mirror_transform = rg.Transform.Mirror(rg.Plane.WorldYZ)
        else:
            raise ValueError("Invalid mirror axis. Use 'X' or 'Y'.")
        
        mirrored_plane = folded_plane.DuplicateBrep()
        mirrored_plane.Transform(mirror_transform)
        geometries.append(mirrored_plane)
    
    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_mirrored_folded_planes_model(5.0, 3.0, 10, 'X')
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_mirrored_folded_planes_model(4.0, 2.5, 8, 'Y')
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_mirrored_folded_planes_model(6.0, 4.0, 12, 'X')
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_mirrored_folded_planes_model(3.5, 2.0, 5, 'Y')
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_mirrored_folded_planes_model(7.0, 5.0, 15, 'Y')
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
