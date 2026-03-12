# Created for 0013_0004_split_void.json

""" Summary:
The function `create_split_void_concept_model` generates an architectural concept model embodying the "Split void" metaphor by creating two solid forms separated by a central void. It accepts parameters for dimensions and the void's characteristics, enabling the design of either a faceted or curvilinear void. By using Rhino's geometry libraries, the function constructs solid volumes and a corresponding void shape that influences spatial dynamics. The resulting model showcases the interaction between solid and void, enhancing perceptions of openness and movement, while providing contrasting light conditions and spatial experiences, thereby reflecting the metaphor's inherent tension and duality."""

#! python 3
function_code = """def create_split_void_concept_model(length, width, height, void_width, void_shape='faceted'):
    \"""
    Creates an architectural Concept Model based on the 'Split void' metaphor.

    Parameters:
    length (float): Total length of the building.
    width (float): Total width of the building.
    height (float): Total height of the building.
    void_width (float): Width of the central void.
    void_shape (str): Shape of the void, either 'curvilinear' or 'faceted'.

    Returns:
    List[Rhino.Geometry.Brep]: A list of 3D Brep geometries representing the concept model.
    \"""
    import Rhino.Geometry as rg
    import random

    # Set a random seed for replicability
    random.seed(42)

    # Create the bounding box for the building
    building_box = rg.Box(rg.Plane.WorldXY, rg.Interval(0, length), rg.Interval(0, width), rg.Interval(0, height))

    # Create two solid parts separated by a void
    half_void_width = void_width / 2
    left_solid = rg.Box(rg.Plane.WorldXY, rg.Interval(0, length / 2 - half_void_width), rg.Interval(0, width), rg.Interval(0, height))
    right_solid = rg.Box(rg.Plane.WorldXY, rg.Interval(length / 2 + half_void_width, length), rg.Interval(0, width), rg.Interval(0, height))
    
    # Determine the shape of the void
    if void_shape == 'curvilinear':
        # Create a curvilinear void shape
        void_curve = rg.ArcCurve(rg.Arc(rg.Point3d(length / 2, 0, height / 2), rg.Point3d(length / 2, width / 2, height), rg.Point3d(length / 2, width, height / 2)))
    else:
        # Create a faceted void shape
        void_curve = rg.PolylineCurve([
            rg.Point3d(length / 2, 0, 0),
            rg.Point3d(length / 2, width / 2, height),
            rg.Point3d(length / 2, width, 0)
        ])
    
    # Loft the void shape to create a surface
    void_surfaces = rg.Brep.CreateFromLoft(
        [void_curve], rg.Point3d.Unset, rg.Point3d.Unset, rg.LoftType.Normal, False)
    
    # Ensure the loft operation was successful
    if not void_surfaces or len(void_surfaces) == 0:
        return [left_solid.ToBrep(), right_solid.ToBrep()]

    void_surface = void_surfaces[0]

    # Split the building with the void surface
    split_breps_left = left_solid.ToBrep().Split(void_surface, 0.01)
    split_breps_right = right_solid.ToBrep().Split(void_surface, 0.01)

    # Collect all breps
    breps = []
    if split_breps_left and len(split_breps_left) > 0:
        breps.extend(split_breps_left)
    if split_breps_right and len(split_breps_right) > 0:
        breps.extend(split_breps_right)

    # Return the breps
    return breps if breps else [left_solid.ToBrep(), right_solid.ToBrep()]"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_split_void_concept_model(20.0, 10.0, 15.0, 4.0, 'faceted')
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_split_void_concept_model(30.0, 12.0, 20.0, 6.0, 'curvilinear')
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_split_void_concept_model(25.0, 15.0, 10.0, 5.0, 'faceted')
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_split_void_concept_model(40.0, 20.0, 30.0, 8.0, 'curvilinear')
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_split_void_concept_model(35.0, 18.0, 25.0, 7.0, 'faceted')
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
