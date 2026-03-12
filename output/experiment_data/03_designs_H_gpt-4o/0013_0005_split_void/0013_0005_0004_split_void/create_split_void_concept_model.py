# Created for 0013_0005_split_void.json

""" Summary:
The function `create_split_void_concept_model` generates architectural concept models reflecting the 'Split void' metaphor by creating a building structure divided by a central void. The parameters specify the dimensions and orientation of the building and void. Using geometric operations, it constructs the main volume and subtracts the void to create distinct segments, reflecting a stark contrast in form. The function also incorporates pathways within the void, emphasizing circulation and interaction. This design captures the essence of duality and dynamic tension, enhancing the building's engagement with light and shadow, thus fulfilling the design task effectively."""

#! python 3
function_code = """def create_split_void_concept_model(length, width, height, void_width, orientation='vertical'):
    \"""
    Creates an architectural Concept Model embodying the 'Split void' metaphor, with a central void dividing the structure.

    Parameters:
    - length (float): Total length of the building in meters.
    - width (float): Total width of the building in meters.
    - height (float): Height of the building in meters.
    - void_width (float): Width of the central void in meters.
    - orientation (str): Orientation of the void, either 'vertical' or 'horizontal'.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep objects representing the 3D geometry of the concept model.
    \"""
    import Rhino.Geometry as rg
    
    geometries = []

    # Main building volume
    building_volume = rg.Box(rg.Plane.WorldXY, rg.Interval(0, length), rg.Interval(0, width), rg.Interval(0, height))
    building_brep = building_volume.ToBrep()

    # Create void brep depending on orientation
    if orientation == 'vertical':
        void_box = rg.Box(rg.Plane.WorldXY, rg.Interval(length / 2 - void_width / 2, length / 2 + void_width / 2),
                          rg.Interval(0, width), rg.Interval(0, height))
    else:
        void_box = rg.Box(rg.Plane.WorldXY, rg.Interval(0, length),
                          rg.Interval(width / 2 - void_width / 2, width / 2 + void_width / 2), rg.Interval(0, height))

    void_brep = void_box.ToBrep()

    # Split the building volume with the void
    split_breps = rg.Brep.CreateBooleanDifference([building_brep], [void_brep], 0.001)

    # Add resulting breps to geometries list
    if split_breps:
        geometries.extend(split_breps)

    # Create pathways within the void
    path_width = void_width * 0.3
    if orientation == 'vertical':
        path_box = rg.Box(rg.Plane.WorldXY, rg.Interval(length / 2 - path_width / 2, length / 2 + path_width / 2),
                          rg.Interval(0, width), rg.Interval(0, height))
    else:
        path_box = rg.Box(rg.Plane.WorldXY, rg.Interval(0, length),
                          rg.Interval(width / 2 - path_width / 2, width / 2 + path_width / 2), rg.Interval(0, height))

    path_brep = path_box.ToBrep()
    geometries.append(path_brep)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_split_void_concept_model(20, 10, 5, 2, orientation='vertical')
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_split_void_concept_model(15, 8, 3, 1.5, orientation='horizontal')
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_split_void_concept_model(30, 12, 7, 3, orientation='vertical')
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_split_void_concept_model(25, 15, 6, 2.5, orientation='horizontal')
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_split_void_concept_model(40, 20, 10, 4, orientation='vertical')
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
