# Created for 0001_0002_house_within_a_house.json

""" Summary:
The function `create_concept_model` generates an architectural concept model inspired by the "House within a house" metaphor. It constructs a series of interlocking volumes that represent an outer protective shell and an inner sanctuary, reflecting a layered spatial hierarchy. By defining parameters such as base dimensions and curvature, the function creates a rectangular outer shell and a dynamically shaped inner sanctuary. The design emphasizes material contrasts and spatial transitions, incorporating features like courtyards that enhance light and connectivity. The resulting 3D model visually encapsulates the essence of nesting, protection, and varied spatial experiences, encouraging exploration within the architecture."""

#! python 3
function_code = """def create_concept_model(base_width=10, base_length=15, height=8, inner_offset=2, curvature=0.3):
    \"""
    Creates a conceptual architectural model based on the 'House within a house' metaphor.
    The model features a series of interlocking and nested volumes that transition from an outer protective shell to an inner sanctuary.

    Parameters:
    - base_width (float): The width of the outer shell in meters.
    - base_length (float): The length of the outer shell in meters.
    - height (float): The height of the outer shell in meters.
    - inner_offset (float): The offset distance for the inner volumes from the outer shell in meters.
    - curvature (float): The curvature factor to apply to the inner sanctuary form, between 0 and 1.

    Returns:
    - List of RhinoCommon Breps: A list of 3D geometries representing the concept model.
    \"""
    import Rhino.Geometry as rg

    # Outer shell - a simple rectangular prism
    outer_shell = rg.Box(rg.Plane.WorldXY, rg.Interval(0, base_width), rg.Interval(0, base_length), rg.Interval(0, height))
    
    # Inner sanctuary - offset and with curved or angular features
    inner_width = base_width - 2 * inner_offset
    inner_length = base_length - 2 * inner_offset
    inner_height = height - 2 * inner_offset

    # Create a basic inner sanctuary form
    inner_sanctuary_box = rg.Box(rg.Plane.WorldXY, rg.Interval(inner_offset, base_width - inner_offset), rg.Interval(inner_offset, base_length - inner_offset), rg.Interval(inner_offset, height - inner_offset))
    
    # Apply curvature to the inner sanctuary
    curvature_factor = (1 - curvature) * 0.5
    inner_sanctuary_points = [
        rg.Point3d(inner_offset, inner_offset, inner_offset),
        rg.Point3d(base_width - inner_offset, inner_offset, inner_offset),
        rg.Point3d(base_width - inner_offset, base_length - inner_offset, inner_offset),
        rg.Point3d(inner_offset, base_length - inner_offset, inner_offset),
        rg.Point3d(inner_offset, inner_offset, height - inner_offset),
        rg.Point3d(base_width - inner_offset, inner_offset, height - inner_offset),
        rg.Point3d(base_width - inner_offset, base_length - inner_offset, height - inner_offset),
        rg.Point3d(inner_offset, base_length - inner_offset, height - inner_offset)
    ]
    
    inner_sanctuary_points = [rg.Point3d(pt.X * curvature_factor + inner_offset, pt.Y * curvature_factor + inner_offset, pt.Z * curvature_factor + inner_offset) for pt in inner_sanctuary_points]

    # Create inner sanctuary lofted from adjusted points
    inner_sanctuary_loft = rg.LoftType.Normal
    inner_sanctuary_curves = [rg.Polyline(inner_sanctuary_points[:4]).ToNurbsCurve(), rg.Polyline(inner_sanctuary_points[4:]).ToNurbsCurve()]
    inner_sanctuary_brep = rg.Brep.CreateFromLoft(inner_sanctuary_curves, rg.Point3d.Unset, rg.Point3d.Unset, inner_sanctuary_loft, False)[0]
    
    # Create a void or courtyard space
    courtyard_offset = inner_offset / 2
    courtyard_width = base_width - 4 * courtyard_offset
    courtyard_length = base_length - 4 * courtyard_offset
    courtyard_height = height / 2
    
    courtyard_box = rg.Box(rg.Plane.WorldXY, rg.Interval(2 * courtyard_offset, courtyard_width + 2 * courtyard_offset), rg.Interval(2 * courtyard_offset, courtyard_length + 2 * courtyard_offset), rg.Interval(0, courtyard_height))

    # Return the list of 3D geometries: outer shell, inner sanctuary, and courtyard
    return [outer_shell.ToBrep(), inner_sanctuary_brep, courtyard_box.ToBrep()]"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_concept_model(base_width=12, base_length=18, height=10, inner_offset=3, curvature=0.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_concept_model(base_width=14, base_length=20, height=9, inner_offset=1, curvature=0.4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_concept_model(base_width=16, base_length=22, height=11, inner_offset=4, curvature=0.2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_concept_model(base_width=8, base_length=12, height=7, inner_offset=1, curvature=0.6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_concept_model(base_width=10, base_length=15, height=8, inner_offset=2, curvature=0.1)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
