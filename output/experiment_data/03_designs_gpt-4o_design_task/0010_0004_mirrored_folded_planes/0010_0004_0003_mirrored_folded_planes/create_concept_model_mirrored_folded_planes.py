# Created for 0010_0004_mirrored_folded_planes.json

""" Summary:
The provided function, `create_concept_model_mirrored_folded_planes`, generates an architectural concept model based on the metaphor of "Mirrored folded planes." It constructs a series of angular, folded surfaces that exhibit bilateral symmetry, reflecting the metaphor's essence. The function defines parameters such as base dimensions, height, fold angle, and the number of layers to create a dynamic interplay of solid and void. Each layer features mirrored counterparts, enhancing the visual complexity and creating a cascading spatial organization. The model emphasizes depth and movement, utilizing light and shadow interactions to foster an engaging architectural experience, aligning with the design task."""

#! python 3
function_code = """def create_concept_model_mirrored_folded_planes(base_width=5.0, base_depth=10.0, height=15.0, fold_angle=30.0, num_layers=3):
    \"""
    Creates an architectural Concept Model embodying the 'Mirrored folded planes' metaphor.
    
    This function generates a set of angular, folded surfaces with bilateral symmetry, designed to reflect 
    a cascading organization of spaces that unfold in layers. The model emphasizes the interplay of light and shadow 
    and the balance between visual complexity and structural harmony.

    Parameters:
    - base_width (float): The width of the base plane in meters.
    - base_depth (float): The depth of the base plane in meters.
    - height (float): The height of the folded structure in meters.
    - fold_angle (float): The angle of folding in degrees.
    - num_layers (int): The number of mirrored folded layers.

    Returns:
    - List of RhinoCommon Brep objects representing the Concept Model.
    \"""
    import Rhino.Geometry as rg
    import math
    
    # Helper function to create a folded plane
    def create_folded_plane(center, width, depth, height, angle):
        angle_rad = math.radians(angle)
        half_width = width / 2.0
        points = [
            rg.Point3d(center.X - half_width, center.Y, center.Z),
            rg.Point3d(center.X + half_width, center.Y, center.Z),
            rg.Point3d(center.X + half_width * math.cos(angle_rad), center.Y + depth, center.Z + height),
            rg.Point3d(center.X - half_width * math.cos(angle_rad), center.Y + depth, center.Z + height)
        ]
        return rg.Brep.CreateFromCornerPoints(points[0], points[1], points[2], points[3], 0.01)
    
    geometries = []
    layer_spacing = base_depth / num_layers
    
    for i in range(num_layers):
        # Calculate the center for each layer
        center_y = i * layer_spacing
        folded_plane = create_folded_plane(rg.Point3d(0, center_y, 0), base_width, base_depth, height, fold_angle)
        geometries.append(folded_plane)
        
        # Create mirrored version
        mirrored_plane = folded_plane.Duplicate()
        mirrored_plane.Transform(rg.Transform.Mirror(rg.Plane.WorldXY))
        geometries.append(mirrored_plane)
    
    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_concept_model_mirrored_folded_planes(base_width=6.0, base_depth=12.0, height=18.0, fold_angle=45.0, num_layers=4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_concept_model_mirrored_folded_planes(base_width=7.0, base_depth=14.0, height=20.0, fold_angle=60.0, num_layers=5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_concept_model_mirrored_folded_planes(base_width=8.0, base_depth=16.0, height=22.0, fold_angle=50.0, num_layers=6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_concept_model_mirrored_folded_planes(base_width=5.0, base_depth=10.0, height=15.0, fold_angle=30.0, num_layers=3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_concept_model_mirrored_folded_planes(base_width=9.0, base_depth=18.0, height=25.0, fold_angle=70.0, num_layers=2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
