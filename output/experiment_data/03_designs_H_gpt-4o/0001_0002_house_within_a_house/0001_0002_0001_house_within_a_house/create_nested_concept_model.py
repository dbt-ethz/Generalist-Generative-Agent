# Created for 0001_0002_house_within_a_house.json

""" Summary:
The provided function generates an architectural concept model based on the "House within a house" metaphor by creating nested forms that embody a sense of protection and layering. The function constructs an outer shell as a box and defines an inner sanctuary using ratios to determine its size relative to the outer structure. Curved geometries are applied to the inner form to enhance the interplay between containment and openness. By incorporating parameters for curvature and height, the model visually represents the metaphor's themes of nesting and spatial hierarchy, facilitating a dynamic relationship between public and private spaces."""

#! python 3
function_code = """def create_nested_concept_model(outer_length, outer_width, outer_height, inner_length_ratio, inner_width_ratio, height_ratio, curvature_ratio):
    \"""
    Creates an architectural Concept Model based on the 'House within a house' metaphor, using interlocking
    and nested forms to convey a sense of nesting and protection. This model uses angular and curved geometries
    to suggest the interplay between containment and openness.

    Parameters:
    - outer_length (float): The length of the outer shell.
    - outer_width (float): The width of the outer shell.
    - outer_height (float): The height of the outer shell.
    - inner_length_ratio (float): The ratio of the inner sanctuary's length to the outer length.
    - inner_width_ratio (float): The ratio of the inner sanctuary's width to the outer width.
    - height_ratio (float): The ratio of the inner sanctuary's height to the outer height.
    - curvature_ratio (float): The amount of curvature applied to the inner sanctuary, between 0 and 1.

    Returns:
    - List of Breps: A list of 3D geometries representing the concept model.
    \"""
    import Rhino.Geometry as rg

    # Create the outer shell as a box
    outer_shell = rg.Box(rg.Plane.WorldXY, rg.Interval(0, outer_length), rg.Interval(0, outer_width), rg.Interval(0, outer_height)).ToBrep()

    # Calculate dimensions for the inner sanctuary
    inner_length = outer_length * inner_length_ratio
    inner_width = outer_width * inner_width_ratio
    inner_height = outer_height * height_ratio

    # Create the inner sanctuary as a curved lofted form
    inner_sanctuary_base_points = [
        rg.Point3d(outer_length * (1 - inner_length_ratio) / 2, outer_width * (1 - inner_width_ratio) / 2, 0),
        rg.Point3d(outer_length * (1 + inner_length_ratio) / 2, outer_width * (1 - inner_width_ratio) / 2, 0),
        rg.Point3d(outer_length * (1 + inner_length_ratio) / 2, outer_width * (1 + inner_width_ratio) / 2, 0),
        rg.Point3d(outer_length * (1 - inner_length_ratio) / 2, outer_width * (1 + inner_width_ratio) / 2, 0)
    ]

    inner_sanctuary_top_points = [
        rg.Point3d(p.X, p.Y, inner_height * curvature_ratio) for p in inner_sanctuary_base_points
    ]

    # Create the inner sanctuary using loft
    inner_curves = [
        rg.Polyline(inner_sanctuary_base_points + [inner_sanctuary_base_points[0]]).ToNurbsCurve(),
        rg.Polyline(inner_sanctuary_top_points + [inner_sanctuary_top_points[0]]).ToNurbsCurve()
    ]
    inner_sanctuary = rg.Brep.CreateFromLoft(inner_curves, rg.Point3d.Unset, rg.Point3d.Unset, rg.LoftType.Tight, False)[0]

    # Return list of geometry
    return [outer_shell, inner_sanctuary]"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_nested_concept_model(10, 8, 12, 0.6, 0.4, 0.5, 0.3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_nested_concept_model(15, 10, 20, 0.5, 0.5, 0.6, 0.2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_nested_concept_model(12, 9, 15, 0.7, 0.5, 0.4, 0.1)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_nested_concept_model(20, 15, 25, 0.4, 0.6, 0.7, 0.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_nested_concept_model(18, 12, 22, 0.55, 0.45, 0.65, 0.4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
