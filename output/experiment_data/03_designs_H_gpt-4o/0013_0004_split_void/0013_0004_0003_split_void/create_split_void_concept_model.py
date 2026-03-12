# Created for 0013_0004_split_void.json

""" Summary:
The function `create_split_void_concept_model` generates an architectural concept model that embodies the 'Split void' metaphor by defining a building space divided by a central void. It takes parameters for the building's dimensions and the void's characteristics, allowing for either a curvilinear or faceted void. The function constructs a bounding box for the building and then creates the void shape accordingly. By splitting the building mass with the void, it establishes contrasting spaces that enhance light, movement, and interaction. This approach ensures a dynamic interplay between solid and void, reflecting the metaphors inherent tension and duality in spatial organization."""

#! python 3
function_code = """def create_split_void_concept_model(width, depth, height, void_width, void_depth, void_type='curvilinear'):
    \"""
    Creates an architectural Concept Model based on the 'Split void' metaphor.

    Parameters:
    width (float): Total width of the building.
    depth (float): Total depth of the building.
    height (float): Total height of the building.
    void_width (float): Width of the central void.
    void_depth (float): Depth of the central void.
    void_type (str): Type of the void, either 'curvilinear' or 'faceted'.

    Returns:
    List[Rhino.Geometry.Brep]: A list of 3D Brep geometries representing the concept model.
    \"""
    import Rhino.Geometry as rg
    import random

    # Set a random seed for replicability
    random.seed(42)

    # Create the bounding box for the building
    building_box = rg.Box(rg.Plane.WorldXY, rg.Interval(0, width), rg.Interval(0, depth), rg.Interval(0, height))

    # Determine the shape of the void
    if void_type == 'curvilinear':
        # Create a curvilinear void shape using a cylinder
        base_circle = rg.Circle(rg.Plane.WorldXY, void_width / 2)
        void_cylinder = rg.Cylinder(base_circle, height).ToBrep(True, True)
    else:
        # Create a faceted void shape using a box
        void_cylinder = rg.Box(rg.Plane.WorldXY, rg.Interval(-void_width / 2, void_width / 2),
                               rg.Interval(-void_depth / 2, void_depth / 2), rg.Interval(0, height)).ToBrep()

    # Position the void in the center of the building
    void_translation = rg.Transform.Translation(width / 2, depth / 2, 0)
    void_cylinder.Transform(void_translation)

    # Split the building with the void
    split_breps = building_box.ToBrep().Split(void_cylinder, 0.01)

    # Check if the split was successful and return the components
    if split_breps and len(split_breps) > 1:
        return split_breps
    else:
        return [building_box.ToBrep()]"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_split_void_concept_model(10, 20, 30, 5, 10, 'curvilinear')
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_split_void_concept_model(15, 25, 35, 7, 12, 'faceted')
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_split_void_concept_model(12, 18, 24, 6, 8, 'curvilinear')
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_split_void_concept_model(20, 30, 40, 10, 15, 'faceted')
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_split_void_concept_model(8, 16, 24, 4, 6, 'curvilinear')
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
