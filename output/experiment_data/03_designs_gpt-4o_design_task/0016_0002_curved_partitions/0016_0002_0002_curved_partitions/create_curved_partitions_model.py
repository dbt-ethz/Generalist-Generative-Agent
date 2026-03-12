# Created for 0016_0002_curved_partitions.json

""" Summary:
The provided function generates an architectural concept model embodying the "curved partitions" metaphor by creating a series of layered, undulating surfaces that mimic natural landscapes. It defines parameters like the number of layers, base dimensions, and height variations, allowing for fluid, organic forms. Using Rhino.Geometry, it constructs curves from randomly varied control points, then lofts these curves into Brep geometries that represent the partitions. This approach emphasizes spatial transitions, light interplay, and exploration, aligning with the metaphor's themes of fluidity and dynamic movement, ultimately crafting a cohesive and elegant architectural model."""

#! python 3
function_code = """def create_curved_partitions_model(num_layers: int, base_width: float, base_depth: float, height_variation: float) -> list:
    \"""
    Creates an architectural Concept Model embodying the 'curved partitions' metaphor.
    
    The model consists of a series of undulating layers that mimic natural landscapes,
    creating spaces that emerge from and recede into the forms. The design emphasizes
    fluidity, natural progression, and the dynamic interplay of light and shadow.

    Parameters:
    - num_layers (int): Number of curved layers to create.
    - base_width (float): The width of the base of the model in meters.
    - base_depth (float): The depth of the base of the model in meters.
    - height_variation (float): Maximum variation in height for the curves in meters.

    Returns:
    - list: A list of Brep geometries representing the curved partitions.
    \"""
    import Rhino.Geometry as rg
    import random

    # Seed for randomness to ensure replicable results
    random.seed(42)
    
    # Prepare base points for the curves
    base_points = [rg.Point3d(x, y, 0) for x in range(0, int(base_width), int(base_width/num_layers))
                   for y in range(0, int(base_depth), int(base_depth/num_layers))]

    layers = []
    
    for i in range(num_layers):
        # Create a curve for each layer with random height variations
        control_points = [
            rg.Point3d(pt.X, pt.Y, random.uniform(0, height_variation))
            for pt in base_points
        ]

        # Create an interpolated curve through these control points
        curve = rg.Curve.CreateInterpolatedCurve(control_points, 3)

        # Loft the curve to create a surface and then convert to a Brep
        translated_curve = curve.Duplicate()  # Duplicate the curve before translating
        translated_curve.Translate(0, 0, height_variation)
        loft_curves = [curve, translated_curve]
        brep = rg.Brep.CreateFromLoft(loft_curves, rg.Point3d.Unset, rg.Point3d.Unset, rg.LoftType.Loose, False)[0]
        
        # Add the brep to the list of layers
        layers.append(brep)
    
    return layers"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_curved_partitions_model(5, 10.0, 8.0, 2.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_curved_partitions_model(7, 12.0, 10.0, 3.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_curved_partitions_model(4, 15.0, 12.0, 1.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_curved_partitions_model(6, 20.0, 15.0, 4.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_curved_partitions_model(3, 25.0, 20.0, 5.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
