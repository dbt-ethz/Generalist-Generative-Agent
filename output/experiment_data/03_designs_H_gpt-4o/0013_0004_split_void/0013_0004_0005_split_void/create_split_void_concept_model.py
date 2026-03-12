# Created for 0013_0004_split_void.json

""" Summary:
The function `create_split_void_concept_model` generates an architectural concept model that embodies the "Split void" metaphor by creating a structure with a central void that divides the building into contrasting entities. It takes dimensions for the building and the void, allowing for a curvilinear design that enhances spatial complexity. The void is crafted as a NURBS curve, influencing the building's geometry and facilitating dynamic interactions between solid and void spaces. By manipulating parameters like curvature, the function ensures varied light and shadow play, ultimately crafting a model that reflects the inherent tension and duality of the metaphor."""

#! python 3
function_code = """def create_split_void_concept_model(length, width, height, void_width, void_height, curvature_factor=0.5):
    \"""
    Creates an architectural Concept Model based on the 'Split void' metaphor.

    This function generates a structure with a central void that organizes the flow between two contrasting entities.
    The void is curvilinear, introducing complexity and dynamic spatial experience, influencing the perception of movement.

    Parameters:
    length (float): Total length of the building.
    width (float): Total width of the building.
    height (float): Total height of the building.
    void_width (float): Width of the central void.
    void_height (float): Height of the central void.
    curvature_factor (float): Factor to control the curvature of the void (0 to 1).

    Returns:
    list: A list of Brep geometry objects representing the architectural concept model.
    \"""
    import Rhino.Geometry as rg

    # Create the bounding box for the building
    building_box = rg.Box(rg.Plane.WorldXY, rg.Interval(0, length), rg.Interval(0, width), rg.Interval(0, height))

    # Define the curvilinear void as a NURBS curve
    void_curve = rg.NurbsCurve.Create(False, 3, [
        rg.Point3d(length / 2 - void_width / 2, 0, 0),
        rg.Point3d(length / 2, width * curvature_factor, void_height / 2),
        rg.Point3d(length / 2 + void_width / 2, width, void_height)
    ])

    # Loft the void shape to create a surface
    loft_result = rg.Brep.CreateFromLoft([void_curve], rg.Point3d.Unset, rg.Point3d.Unset, rg.LoftType.Normal, False)
    if not loft_result or len(loft_result) == 0:
        return [building_box.ToBrep()]
    void_surface = loft_result[0]

    # Extrude the void surface to create a 3D void volume
    void_volume = rg.Brep.CreateExtrusion(void_surface.Edges[0], rg.Vector3d(0, 0, height))

    # Split the building with the void volume
    split_breps = building_box.ToBrep().Split(void_volume, 0.01)

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
    geometry = create_split_void_concept_model(20, 10, 15, 5, 10, 0.7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_split_void_concept_model(30, 15, 20, 8, 12, 0.3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_split_void_concept_model(25, 12, 18, 6, 9, 0.4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_split_void_concept_model(40, 20, 25, 10, 15, 0.6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_split_void_concept_model(35, 18, 22, 7, 11, 0.8)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
