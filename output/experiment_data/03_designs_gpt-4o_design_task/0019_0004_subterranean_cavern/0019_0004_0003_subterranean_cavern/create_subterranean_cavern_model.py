# Created for 0019_0004_subterranean_cavern.json

""" Summary:
The function `create_subterranean_cavern_model` generates an architectural concept model based on the metaphor of a subterranean cavern. It creates a series of interconnected, curvilinear shells that reflect the concept of nested spaces, emphasizing intimacy and exploration. By layering translucent materials, the model simulates depth and varying light conditions, enhancing the mysterious atmosphere akin to natural caves. Each layer is defined by a base radius and height, with translucency variations to evoke a sense of discovery. The resulting geometries embody the metaphor's essence of refuge and complexity, offering insights into spatial relationships and immersive design."""

#! python 3
function_code = """def create_subterranean_cavern_model(base_radius, height, num_layers, translucency_variation):
    \"""
    Create an architectural concept model that embodies the 'subterranean cavern' metaphor.
    
    The function generates a series of interconnected shells or volumes using curvilinear and organic shapes,
    emphasizing the transition from enclosed, intimate spaces to larger, more open areas. The model layers
    translucent materials to suggest depth and nested spaces, incorporating small openings and varied translucency
    to create a play of light that enhances the sense of mystery and discovery.
    
    Parameters:
    - base_radius (float): The radius of the base of the cavern form.
    - height (float): The total height of the layered volumes.
    - num_layers (int): The number of nested volumes or layers.
    - translucency_variation (float): The factor by which translucency varies between layers (0 to 1).
    
    Returns:
    - List of Breps: A list of 3D geometries representing the concept model.
    \"""
    import Rhino.Geometry as rg
    import random
    
    random.seed(42)  # Ensuring replicable randomness
    
    geometries = []
    layer_height = height / num_layers
    
    for i in range(num_layers):
        # Calculate parameters for each layer
        layer_radius = base_radius * (1 - (i / num_layers) * 0.5)
        layer_translucency = 1 - (i / num_layers) * translucency_variation
        
        # Create a base circle for the layer
        base_circle = rg.Circle(rg.Point3d(0, 0, i * layer_height), layer_radius)
        
        # Create an organic surface by lofting between offset circles
        offset_distance = random.uniform(0.1, 0.3) * layer_radius
        base_circle_curve = base_circle.ToNurbsCurve()
        offset_circle_curve = base_circle_curve.Offset(rg.Plane.WorldXY, offset_distance, 0.01, rg.CurveOffsetCornerStyle.Round)[0]
        
        curves = [base_circle_curve, offset_circle_curve]
        loft_type = rg.LoftType.Normal
        loft = rg.Brep.CreateFromLoft(curves, rg.Point3d.Unset, rg.Point3d.Unset, loft_type, False)[0]
        
        # Add translucency data as user attribute (for conceptual purposes)
        loft.SetUserString("Translucency", str(layer_translucency))
        
        geometries.append(loft)
    
    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_subterranean_cavern_model(10.0, 20.0, 5, 0.8)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_subterranean_cavern_model(15.0, 30.0, 7, 0.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_subterranean_cavern_model(12.0, 25.0, 6, 0.6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_subterranean_cavern_model(8.0, 15.0, 4, 0.9)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_subterranean_cavern_model(9.5, 18.0, 3, 0.7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
