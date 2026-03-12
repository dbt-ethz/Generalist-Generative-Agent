# Created for 0015_0003_suspended_intersecting_assembly.json

""" Summary:
The provided function generates an architectural concept model based on the metaphor "Suspended intersecting assembly" by creating a series of thin, intersecting panels that simulate a floating structure. Each panel is defined by random start and end points, with varying spans, widths, and heights, emphasizing lightness and fluidity. The function constructs a network of overlapping arcs and lines, allowing for dynamic spatial relationships and visual connections. By using adaptable connections, the design promotes interconnectivity and modularity, while the generated geometries capture the essence of suspension, creating a delicate balance that enhances the models transparency and engagement within the space."""

#! python 3
function_code = """def create_suspended_intersecting_assembly(num_panels=8, panel_width=1.5, panel_height=0.1, max_span=12, seed=42):
    \"""
    Creates an architectural Concept Model based on the 'Suspended intersecting assembly' metaphor.

    This function generates a series of thin, intersecting panels that simulate a floating assembly. 
    The panels are arranged to form a network of overlapping arcs and lines, emphasizing a sense of lightness 
    and fluidity, with adaptable connections that allow for various configurations.

    Parameters:
    - num_panels: The number of panels to generate.
    - panel_width: The width of each panel in meters.
    - panel_height: The height (thickness) of each panel in meters.
    - max_span: The maximum span (length) of each panel in meters.
    - seed: An optional seed for randomization to ensure replicable results.

    Returns:
    - A list of RhinoCommon Brep objects representing the architectural Concept Model.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    random.seed(seed)
    geometries = []

    # Define a central zone around which the panels will be suspended
    center_point = rg.Point3d(0, 0, 0)

    for _ in range(num_panels):
        # Randomly define the span length of the panel
        span = random.uniform(max_span * 0.5, max_span)

        # Define the start and end points of the panel
        start_point = rg.Point3d(
            random.uniform(-max_span, max_span),
            random.uniform(-max_span, max_span),
            random.uniform(0, max_span / 2)
        )
        end_point = rg.Point3d(
            start_point.X + span * math.cos(random.uniform(0, math.pi)),
            start_point.Y + span * math.sin(random.uniform(0, math.pi)),
            start_point.Z + random.uniform(-1, 1) * span * 0.1
        )

        # Create a line representing the panel's trajectory
        line = rg.Line(start_point, end_point)

        # Create a plane to extrude the panel along the line
        plane = rg.Plane(start_point, line.Direction)

        # Define a rectangle on this plane
        rectangle = rg.Rectangle3d(plane, panel_width, line.Length)

        # Create a planar surface from the rectangle
        panel_surface = rg.Brep.CreateFromSurface(rg.Surface.CreateExtrusion(rectangle.ToNurbsCurve(), rg.Vector3d(0, 0, panel_height)))

        # Add the panel to the list of geometries
        geometries.append(panel_surface)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_suspended_intersecting_assembly(num_panels=10, panel_width=2, panel_height=0.2, max_span=15, seed=100)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_suspended_intersecting_assembly(num_panels=5, panel_width=1.0, panel_height=0.05, max_span=10, seed=1)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_suspended_intersecting_assembly(num_panels=12, panel_width=1.8, panel_height=0.15, max_span=14, seed=50)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_suspended_intersecting_assembly(num_panels=20, panel_width=2.5, panel_height=0.3, max_span=18, seed=200)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_suspended_intersecting_assembly(num_panels=15, panel_width=1.2, panel_height=0.1, max_span=11, seed=75)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
