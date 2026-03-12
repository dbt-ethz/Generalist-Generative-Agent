# Created for 0010_0003_mirrored_folded_planes.json

""" Summary:
The function `create_mirrored_folded_planes_concept` generates an architectural concept model by interpreting the metaphor of "Mirrored folded planes." It creates a series of angular, folded forms defined by specified dimensions and rotation angles. These forms are then mirrored across a chosen axis, enhancing visual symmetry and complexity. The function emphasizes harmony through the duplication of geometries, resulting in a dynamic interplay of light and shadow. By arranging spaces sequentially, the model promotes fluid movement within the structure, aligning with the metaphor's essence of continuity and depth, ultimately creating an intricate yet unified architectural design."""

#! python 3
function_code = """def create_mirrored_folded_planes_concept(width, depth, height, fold_angle, mirror_axis):
    \"""
    Creates an architectural Concept Model based on the 'Mirrored folded planes' metaphor.
    
    This function generates a series of angular, folded forms that are mirrored across a specified axis.
    The model emphasizes symmetry and balance through the use of mirrored geometries, creating a 
    dynamic and visually engaging environment.

    Parameters:
    - width (float): The width of the folded form in meters.
    - depth (float): The depth of the folded form in meters.
    - height (float): The height of the folded form in meters.
    - fold_angle (float): The angle in degrees at which the planes are folded.
    - mirror_axis (str): The axis across which the forms are mirrored ('x', 'y', or 'z').

    Returns:
    - list: A list of RhinoCommon Brep objects representing the folded and mirrored concept model.
    \"""
    import Rhino.Geometry as rg
    import math

    # Create the base folded plane
    def create_folded_plane(w, d, h, angle):
        # Create a base rectangle
        base_rect = rg.Rectangle3d(rg.Plane.WorldXY, w, d)
        base_brep = rg.Brep.CreateFromCornerPoints(base_rect.Corner(0), base_rect.Corner(1), base_rect.Corner(2), base_rect.Corner(3), 1e-6)

        # Create a fold by rotating one half of the rectangle
        mid_point = (base_rect.Corner(0) + base_rect.Corner(1)) / 2
        fold_axis = rg.Line(mid_point, mid_point + rg.Vector3d(0, 0, h))
        rotation = rg.Transform.Rotation(math.radians(angle), fold_axis.Direction, mid_point)
        base_brep.Transform(rotation)

        return base_brep

    # Create mirrored geometry
    def mirror_geometry(brep, axis):
        mirror_plane = rg.Plane.WorldXY if axis == 'x' else rg.Plane.WorldYZ if axis == 'y' else rg.Plane.WorldZX
        mirrored_brep = brep.Duplicate()
        mirrored_brep.Transform(rg.Transform.Mirror(mirror_plane))
        return mirrored_brep

    # Generate the folded plane
    folded_plane = create_folded_plane(width, depth, height, fold_angle)
    
    # Mirror the folded plane
    mirrored_plane = mirror_geometry(folded_plane, mirror_axis)

    return [folded_plane, mirrored_plane]

# Example usage:
# geometries = create_mirrored_folded_planes_concept(10, 5, 3, 45, 'y')"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_mirrored_folded_planes_concept(10, 5, 3, 45, 'y')
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_mirrored_folded_planes_concept(8, 4, 2, 30, 'z')
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_mirrored_folded_planes_concept(12, 6, 4, 60, 'x')
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_mirrored_folded_planes_concept(15, 7, 5, 90, 'x')
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_mirrored_folded_planes_concept(9, 3, 2, 75, 'y')
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
