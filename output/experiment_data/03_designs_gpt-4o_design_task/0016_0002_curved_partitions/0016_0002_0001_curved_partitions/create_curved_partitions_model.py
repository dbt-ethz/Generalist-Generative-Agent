# Created for 0016_0002_curved_partitions.json

""" Summary:
The provided function generates an architectural concept model based on the metaphor of "curved partitions." It creates a series of layered, sweeping curves that mimic natural landscapes, embodying fluidity and organic movement. Using parameters like layer count and curve amplitude, the function constructs 3D geometries that form terrain-like shapes, enhancing spatial dynamics and light interplay. The resulting model allows for varied spatial relationships, encouraging exploration while maintaining a cohesive aesthetic. This approach aligns with the metaphor's essence, crafting private yet open areas that invite interaction and create a calming atmosphere through their undulating forms."""

#! python 3
function_code = """def create_curved_partitions_model(layer_count=5, layer_height=2.0, max_curve_amplitude=3.0, seed=42):
    \"""
    Create an architectural Concept Model characterized by 'curved partitions' using RhinoCommon.
    
    This function generates a series of layered, sweeping curves that form a terrain-like structure, embodying the metaphor of 'curved partitions'.
    The design incorporates undulating layers that create dynamic spatial relationships and interplay of light and shadow.
    
    Parameters:
    - layer_count (int): Number of curved layers to generate.
    - layer_height (float): Vertical distance between each layer.
    - max_curve_amplitude (float): Maximum amplitude of the curves.
    - seed (int): Random seed for replicable results.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep objects representing the 3D geometries of the model.
    \"""
    import Rhino.Geometry as rg
    import random
    
    random.seed(seed)
    
    geometries = []

    length = 20.0  # Length of the model in meters
    width = 10.0   # Width of the model in meters
    
    for i in range(layer_count):
        height = i * layer_height
        control_points = []
        for j in range(6):  # Creating a curve with 6 control points
            x = j * (length / 5)
            y = random.uniform(-max_curve_amplitude, max_curve_amplitude)
            control_points.append(rg.Point3d(x, y, height))
        
        # Create a curve through the control points
        curve = rg.Curve.CreateInterpolatedCurve(control_points, 3)
        
        # Create a planar surface from the curve
        surface = rg.Brep.CreateFromCornerPoints(
            rg.Point3d(0, -width / 2, height),
            rg.Point3d(length, -width / 2, height),
            rg.Point3d(length, width / 2, height),
            rg.Point3d(0, width / 2, height),
            0.01
        )
        
        # Add the surface to the geometries list
        geometries.append(surface)
    
    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_curved_partitions_model(layer_count=8, layer_height=1.5, max_curve_amplitude=4.0, seed=123)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_curved_partitions_model(layer_count=6, layer_height=3.0, max_curve_amplitude=2.5, seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_curved_partitions_model(layer_count=10, layer_height=2.5, max_curve_amplitude=5.0, seed=7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_curved_partitions_model(layer_count=4, layer_height=2.0, max_curve_amplitude=3.5, seed=56)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_curved_partitions_model(layer_count=7, layer_height=1.0, max_curve_amplitude=2.0, seed=30)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
