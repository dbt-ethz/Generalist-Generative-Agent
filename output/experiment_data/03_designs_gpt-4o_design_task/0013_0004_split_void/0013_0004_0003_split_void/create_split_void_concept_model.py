# Created for 0013_0004_split_void.json

""" Summary:
The function `create_split_void_concept_model` generates an architectural concept model that embodies the "Split void" metaphor by creating a structure with a central void that divides the building's massing. It accepts parameters for dimensions and void shape (curvilinear or faceted). Depending on the chosen shape, it constructs a void that influences the overall geometry and spatial organization, enhancing the interaction between solid and void. The model showcases dynamic spatial relationships, allowing for varied light and shadow effects. Ultimately, it manifests the metaphor's tension and duality, reflecting a vivid interplay of openness and movement within the architectural design."""

#! python 3
function_code = """def create_split_void_concept_model(width, depth, height, void_width, void_shape='curvilinear'):
    \"""
    Creates an architectural Concept Model based on the 'Split void' metaphor.

    Parameters:
    width (float): Total width of the building.
    depth (float): Total depth of the building.
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
    building_box = rg.Box(rg.Plane.WorldXY, rg.Interval(0, width), rg.Interval(0, depth), rg.Interval(0, height))

    # Determine the shape of the void
    if void_shape == 'curvilinear':
        # Create a curvilinear void shape
        void_curve = rg.NurbsCurve.Create(False, 3, [
            rg.Point3d(width / 2 - void_width / 2, 0, 0),
            rg.Point3d(width / 2, random.uniform(depth / 4, 3 * depth / 4), height / 2),
            rg.Point3d(width / 2 + void_width / 2, depth, height)
        ])
    else:
        # Create a faceted void shape
        void_curve = rg.PolylineCurve([
            rg.Point3d(width / 2 - void_width / 2, 0, 0),
            rg.Point3d(width / 2, depth / 2, height / 2),
            rg.Point3d(width / 2 + void_width / 2, depth, height)
        ])

    # Loft the void shape to create a surface
    void_surfaces = rg.Brep.CreateFromLoft(
        [void_curve], rg.Point3d.Unset, rg.Point3d.Unset, rg.LoftType.Normal, False)

    # Ensure the loft operation was successful
    if not void_surfaces or len(void_surfaces) == 0:
        return [building_box.ToBrep()]

    void_surface = void_surfaces[0]

    # Split the building with the void surface
    split_breps = building_box.ToBrep().Split(void_surface, 0.01)

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
    geometry = create_split_void_concept_model(10.0, 15.0, 20.0, 5.0, 'curvilinear')
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_split_void_concept_model(12.0, 18.0, 25.0, 4.0, 'faceted')
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_split_void_concept_model(8.0, 10.0, 12.0, 3.0, 'curvilinear')
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_split_void_concept_model(14.0, 22.0, 30.0, 6.0, 'faceted')
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_split_void_concept_model(16.0, 20.0, 28.0, 7.0, 'curvilinear')
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
