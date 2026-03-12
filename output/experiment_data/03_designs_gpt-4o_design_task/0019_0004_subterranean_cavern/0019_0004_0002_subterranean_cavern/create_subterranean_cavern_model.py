# Created for 0019_0004_subterranean_cavern.json

""" Summary:
The provided function generates an architectural concept model inspired by the metaphor of a subterranean cavern by creating a series of nested, curvilinear layers that mimic geological formations. It employs a randomized scaling factor to introduce organic variations, enhancing the immersive quality of the model. Each layer is formed using ellipses that are lofted together, reflecting the idea of depth and complexity through varying heights and thicknesses. The result is a structure that embodies hidden spaces and transitions, emphasizing light and shadow dynamics while utilizing natural materials to evoke a connection to the earth, aligning with the metaphor's themes of exploration and refuge."""

#! python 3
function_code = """def create_subterranean_cavern_model(radius=10.0, height=5.0, num_layers=3, layer_thickness=0.5, seed=42):
    \"""
    Creates an architectural Concept Model based on the metaphor of a subterranean cavern.
    
    Parameters:
    - radius (float): The base radius of the cavern model in meters.
    - height (float): The height of the cavern model in meters.
    - num_layers (int): The number of nested layers or shells to create.
    - layer_thickness (float): The thickness of each layer or shell in meters.
    - seed (int): Seed for randomness to ensure replicable results.
    
    Returns:
    - List of RhinoCommon Breps representing the nested, curvilinear layers of the cavern model.
    \"""

    import Rhino.Geometry as rg
    import random

    random.seed(seed)
    layers = []

    for i in range(num_layers):
        # Create a base ellipse shape for the cavern that will be transformed
        base_radius = radius * (1 - (i * layer_thickness / height))
        base_height = height * (1 - (i / num_layers))
        ellipse = rg.Ellipse(rg.Plane.WorldXY, base_radius, base_radius * 0.6)
        
        # Introduce randomness to create a more organic, cave-like structure
        scale_factor = 1 + (random.uniform(-0.1, 0.1))
        curve = ellipse.ToNurbsCurve()
        curve.Transform(rg.Transform.Scale(rg.Point3d(0, 0, 0), scale_factor))
        
        # Loft the curve with a copy of itself shifted upwards to make a shell
        loft_curves = [curve]
        for j in range(1, int(base_height / layer_thickness)):
            moved_curve = curve.Duplicate()
            move_transform = rg.Transform.Translation(0, 0, j * layer_thickness)
            moved_curve.Transform(move_transform)
            loft_curves.append(moved_curve)
            
        loft = rg.Brep.CreateFromLoft(loft_curves, rg.Point3d.Unset, rg.Point3d.Unset, rg.LoftType.Normal, False)
        if loft:
            layers.append(loft[0])

    return layers"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_subterranean_cavern_model(radius=15.0, height=10.0, num_layers=5, layer_thickness=1.0, seed=123)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_subterranean_cavern_model(radius=8.0, height=6.0, num_layers=4, layer_thickness=0.75, seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_subterranean_cavern_model(radius=12.0, height=7.0, num_layers=6, layer_thickness=0.3, seed=2023)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_subterranean_cavern_model(radius=20.0, height=15.0, num_layers=2, layer_thickness=2.0, seed=56)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_subterranean_cavern_model(radius=18.0, height=12.0, num_layers=8, layer_thickness=0.4, seed=77)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
