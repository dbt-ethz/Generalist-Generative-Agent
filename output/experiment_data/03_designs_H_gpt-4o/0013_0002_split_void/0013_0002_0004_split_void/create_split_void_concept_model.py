# Created for 0013_0002_split_void.json

""" Summary:
The function `create_split_void_concept_model` generates an architectural concept model that embodies the "Split void" metaphor by creating a building with a central void that separates yet connects two distinct halves. It defines the structure's dimensions, including varying heights, to enhance visual contrast and spatial dynamics. By calculating the void's position and width, it generates two separate volumes that embody duality in form and function. The void facilitates natural light penetration, creating shifting patterns of light and shadow, thereby enriching the user experience. The resulting 3D geometry reflects the interplay of divided spaces as a cohesive architectural identity."""

#! python 3
function_code = """def create_split_void_concept_model(length, width, max_height, min_height, void_position_ratio=0.5, void_width_ratio=0.2):
    \"""
    Generates an architectural Concept Model based on the 'Split void' metaphor, featuring a central void that not only
    separates but also connects the two halves of the structure through dynamic spatial relations and light interplay.

    Parameters:
    - length (float): The total length of the building in meters.
    - width (float): The total width of the building in meters.
    - max_height (float): The maximum height of the building in meters.
    - min_height (float): The minimum height of the building in meters.
    - void_position_ratio (float, optional): The ratio determining the central void's position along the width (0 < ratio < 1).
    - void_width_ratio (float, optional): The ratio of the void's width to the total width of the building (0 < ratio < 1).

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep objects representing the 3D geometry of the concept model.
    \"""
    import Rhino.Geometry as rg

    # Define void dimensions
    void_width = width * void_width_ratio
    void_position = width * void_position_ratio

    # Calculate the widths of the two halves
    left_width = void_position - (void_width / 2)
    right_width = width - void_position - (void_width / 2)

    # Create base rectangles for the two halves
    left_half = rg.Rectangle3d(rg.Plane.WorldXY, left_width, length)
    right_half = rg.Rectangle3d(rg.Plane.WorldXY, right_width, length)

    # Adjust the right half's position
    right_half.Transform(rg.Transform.Translation(rg.Vector3d(void_position + (void_width / 2), 0, 0)))

    # Extrude the base rectangles to create volumes with varying heights
    left_half_brep = rg.Brep.CreateFromBox((left_half.Corner(0), left_half.Corner(1),
                                            left_half.Corner(3), left_half.Corner(2),
                                            rg.Point3d(left_half.Corner(0).X, left_half.Corner(0).Y, max_height),
                                            rg.Point3d(left_half.Corner(1).X, left_half.Corner(1).Y, max_height),
                                            rg.Point3d(left_half.Corner(3).X, left_half.Corner(3).Y, min_height),
                                            rg.Point3d(left_half.Corner(2).X, left_half.Corner(2).Y, min_height)))

    right_half_brep = rg.Brep.CreateFromBox((right_half.Corner(0), right_half.Corner(1),
                                             right_half.Corner(3), right_half.Corner(2),
                                             rg.Point3d(right_half.Corner(0).X, right_half.Corner(0).Y, min_height),
                                             rg.Point3d(right_half.Corner(1).X, right_half.Corner(1).Y, min_height),
                                             rg.Point3d(right_half.Corner(3).X, right_half.Corner(3).Y, max_height),
                                             rg.Point3d(right_half.Corner(2).X, right_half.Corner(2).Y, max_height)))

    # Create the void as a vertical brep
    void_base = rg.Rectangle3d(rg.Plane.WorldXY, void_width, length)
    void_base.Transform(rg.Transform.Translation(rg.Vector3d(void_position - (void_width / 2), 0, 0)))

    void_brep = rg.Brep.CreateFromBox((void_base.Corner(0), void_base.Corner(1),
                                       void_base.Corner(3), void_base.Corner(2),
                                       rg.Point3d(void_base.Corner(0).X, void_base.Corner(0).Y, max_height),
                                       rg.Point3d(void_base.Corner(1).X, void_base.Corner(1).Y, max_height),
                                       rg.Point3d(void_base.Corner(3).X, void_base.Corner(3).Y, max_height),
                                       rg.Point3d(void_base.Corner(2).X, void_base.Corner(2).Y, max_height)))

    return [left_half_brep, right_half_brep, void_brep]"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_split_void_concept_model(30, 20, 10, 5, 0.5, 0.2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_split_void_concept_model(40, 25, 12, 6, 0.4, 0.15)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_split_void_concept_model(50, 30, 15, 7, 0.6, 0.25)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_split_void_concept_model(35, 22, 14, 8, 0.3, 0.1)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_split_void_concept_model(45, 28, 20, 10, 0.55, 0.3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
