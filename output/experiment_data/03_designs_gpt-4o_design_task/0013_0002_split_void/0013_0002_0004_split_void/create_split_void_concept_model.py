# Created for 0013_0002_split_void.json

""" Summary:
The provided function, `create_split_void_concept_model`, generates an architectural concept model based on the 'Split void' metaphor. It constructs a building form with a central void serving as a dynamic separator, effectively dividing the structure into two distinct parts. By manipulating dimensions, including the void's width relative to the building's overall width, the function creates varied spatial experiences characterized by differing heights and orientations. This design fosters an interplay of light and shadow, enhancing the perception of space while promoting movement and interaction between the divided areas, thus embodying the metaphor's essence of duality and coherence."""

#! python 3
function_code = """def create_split_void_concept_model(length, width, height, void_width_ratio=0.2):
    \"""
    Creates an architectural Concept Model implementing the 'Split void' metaphor.
    
    The function generates a building form where a central void acts as a dynamic separator,
    dividing the structure into two parts. This void introduces an interplay of light and shadow,
    enhancing spatial experience and promoting interaction while maintaining architectural coherence.

    Parameters:
    - length (float): The total length of the building in meters.
    - width (float): The total width of the building in meters.
    - height (float): The height of the building in meters.
    - void_width_ratio (float, optional): The ratio of the void's width to the total width of the building. Default is 0.2.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep geometries representing the building and the void.
    \"""
    import Rhino.Geometry as rg

    # Calculate dimensions
    void_width = width * void_width_ratio
    half_building_width = (width - void_width) / 2

    # Define base rectangles for the two building halves
    left_half_base = rg.Rectangle3d(rg.Plane.WorldXY, half_building_width, length)
    right_half_base = rg.Rectangle3d(rg.Plane.WorldXY, half_building_width, length)
    
    # Move the right half base to the correct position
    right_half_base.Transform(rg.Transform.Translation(rg.Vector3d(half_building_width + void_width, 0, 0)))

    # Extrude the base rectangles to create volumes
    left_half_brep = rg.Brep.CreateFromBox((left_half_base.Corner(0), left_half_base.Corner(1), 
                                            left_half_base.Corner(3), left_half_base.Corner(2),
                                            rg.Point3d(left_half_base.Corner(0).X, left_half_base.Corner(0).Y, height),
                                            rg.Point3d(left_half_base.Corner(1).X, left_half_base.Corner(1).Y, height),
                                            rg.Point3d(left_half_base.Corner(3).X, left_half_base.Corner(3).Y, height),
                                            rg.Point3d(left_half_base.Corner(2).X, left_half_base.Corner(2).Y, height)))
                                            
    right_half_brep = rg.Brep.CreateFromBox((right_half_base.Corner(0), right_half_base.Corner(1), 
                                             right_half_base.Corner(3), right_half_base.Corner(2),
                                             rg.Point3d(right_half_base.Corner(0).X, right_half_base.Corner(0).Y, height),
                                             rg.Point3d(right_half_base.Corner(1).X, right_half_base.Corner(1).Y, height),
                                             rg.Point3d(right_half_base.Corner(3).X, right_half_base.Corner(3).Y, height),
                                             rg.Point3d(right_half_base.Corner(2).X, right_half_base.Corner(2).Y, height)))

    # Create the void as a vertical brep
    void_base = rg.Rectangle3d(rg.Plane.WorldXY, void_width, length)
    void_base.Transform(rg.Transform.Translation(rg.Vector3d(half_building_width, 0, 0)))
    
    void_brep = rg.Brep.CreateFromBox((void_base.Corner(0), void_base.Corner(1), 
                                       void_base.Corner(3), void_base.Corner(2),
                                       rg.Point3d(void_base.Corner(0).X, void_base.Corner(0).Y, height),
                                       rg.Point3d(void_base.Corner(1).X, void_base.Corner(1).Y, height),
                                       rg.Point3d(void_base.Corner(3).X, void_base.Corner(3).Y, height),
                                       rg.Point3d(void_base.Corner(2).X, void_base.Corner(2).Y, height)))

    return [left_half_brep, right_half_brep, void_brep]"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_split_void_concept_model(30, 20, 10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_split_void_concept_model(50, 25, 15, 0.3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_split_void_concept_model(40, 30, 12, 0.1)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_split_void_concept_model(60, 40, 20, 0.25)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_split_void_concept_model(45, 35, 18, 0.15)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
