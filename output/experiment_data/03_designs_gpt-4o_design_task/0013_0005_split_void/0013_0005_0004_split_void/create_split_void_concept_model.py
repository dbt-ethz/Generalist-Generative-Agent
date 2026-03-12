# Created for 0013_0005_split_void.json

""" Summary:
The provided function `create_split_void_concept_model` generates an architectural concept model by implementing the 'Split void' metaphor. It creates a building structure characterized by a central void that divides the architectural mass into distinct segments, either vertically or horizontally. This void influences the building's geometry, enhancing visual identity through contrasting materials and forms. The function defines parameters for the base dimensions and void width, calculates the positions of the split, and generates corresponding geometric representations. Ultimately, the model captures the dynamic interaction of spaces around the void, promoting exploration and varied experiences of light and shadow."""

#! python 3
function_code = """def create_split_void_concept_model(base_length, base_width, base_height, void_width, orientation='vertical'):
    \"""
    Creates an architectural Concept Model based on the 'Split void' metaphor.

    This function generates a building form where a central void acts as a transformative boundary,
    splitting the architectural mass into distinct segments. The void can be oriented vertically or
    horizontally, influencing the building's geometry and silhouette. The model explores spatial
    dynamics, contrasts in form and materiality, and interaction with natural light.

    Parameters:
    - base_length (float): Length of the base structure in meters.
    - base_width (float): Width of the base structure in meters.
    - base_height (float): Height of the base structure in meters.
    - void_width (float): Width of the void in meters.
    - orientation (str): Orientation of the void, either 'vertical' or 'horizontal'.

    Returns:
    - list of Rhino.Geometry.Brep: A list of Brep objects representing the 3D geometries of the model.
    \"""
    import Rhino
    import Rhino.Geometry as rg
    from random import seed, uniform

    # Set seed for randomness
    seed(42)

    # Create base structure
    base_box = rg.Box(rg.Plane.WorldXY, rg.Interval(0, base_length), rg.Interval(0, base_width), rg.Interval(0, base_height))
    base_brep = base_box.ToBrep()

    # Determine void position based on orientation
    if orientation == 'vertical':
        void_plane = rg.Plane(rg.Point3d(base_length / 2, 0, 0), rg.Vector3d(1, 0, 0))
        left_box = rg.Box(rg.Plane.WorldXY, rg.Interval(0, base_length / 2 - void_width / 2), rg.Interval(0, base_width), rg.Interval(0, base_height))
        right_box = rg.Box(rg.Plane.WorldXY, rg.Interval(base_length / 2 + void_width / 2, base_length), rg.Interval(0, base_width), rg.Interval(0, base_height))
    else:
        void_plane = rg.Plane(rg.Point3d(0, base_width / 2, 0), rg.Vector3d(0, 1, 0))
        left_box = rg.Box(rg.Plane.WorldXY, rg.Interval(0, base_length), rg.Interval(0, base_width / 2 - void_width / 2), rg.Interval(0, base_height))
        right_box = rg.Box(rg.Plane.WorldXY, rg.Interval(0, base_length), rg.Interval(base_width / 2 + void_width / 2, base_width), rg.Interval(0, base_height))

    # Convert boxes to breps
    left_brep = left_box.ToBrep()
    right_brep = right_box.ToBrep()

    # Create a void Brep
    left_corners = left_box.GetCorners()
    right_corners = right_box.GetCorners()
    if left_corners and right_corners:
        void_brep = rg.Brep.CreatePlanarBreps([rg.Polyline([rg.Point3d(left_corners[1]), rg.Point3d(right_corners[0]), rg.Point3d(right_corners[3]), rg.Point3d(left_corners[2])]).ToNurbsCurve()])
        if void_brep:
            void_brep = void_brep[0]
        else:
            void_brep = None
    else:
        void_brep = None

    # Return the list of Breps
    return [left_brep, right_brep, void_brep]

# Example Usage:
# model = create_split_void_concept_model(20, 10, 15, 2, 'vertical')"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_split_void_concept_model(25, 12, 18, 3, 'horizontal')
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_split_void_concept_model(30, 15, 20, 4, 'vertical')
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_split_void_concept_model(22, 10, 12, 1.5, 'horizontal')
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_split_void_concept_model(18, 9, 14, 2.5, 'vertical')
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_split_void_concept_model(35, 20, 25, 5, 'horizontal')
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
