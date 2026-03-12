# Created for 0020_0001_stacked_forests.json

""" Summary:
The provided function, `create_stacked_forests_model`, generates an architectural concept model inspired by the metaphor of "Stacked forests." It constructs a multi-layered structure that mimics a tiered forest by creating circular layers with decreasing radii and varying tree-like elements on each layer. Each layer is defined by a base radius and height increment, promoting vertical organization and organic growth. The random placement of cylindrical tree trunks adds spatial richness, reflecting the metaphor's emphasis on hierarchy, depth, and diverse experiences. Ultimately, the function returns a list of geometric representations that embody the intended design principles."""

#! python 3
function_code = """def create_stacked_forests_model(base_radius, height_increment, num_layers, max_tree_height, seed=42):
    \"""
    Creates an architectural Concept Model based on the 'Stacked forests' metaphor. The model features a multi-layered 
    vertical organization with varied heights and organic growth patterns, resembling a dense, tiered forest.

    Parameters:
    - base_radius (float): The radius of the base layer in meters.
    - height_increment (float): The height increase between each layer in meters.
    - num_layers (int): The number of layers in the structure.
    - max_tree_height (float): The maximum height of the tree-like elements in meters.
    - seed (int): Seed for random number generation to ensure replicable results.

    Returns:
    - List[rhino3dm.Brep]: A list of Brep geometries representing the concept model.
    \"""
    import Rhino.Geometry as rg
    import random
    import math
    
    # Seed the random generator
    random.seed(seed)
    
    geometries = []

    # Create layers
    for i in range(num_layers):
        layer_height = i * height_increment
        layer_radius = base_radius - (i * (base_radius / num_layers))
        
        # Create a circular base for each layer
        circle = rg.Circle(rg.Plane.WorldXY, layer_radius).ToNurbsCurve()
        circle.Translate(rg.Vector3d(0, 0, layer_height))
        
        # Create vertical tree-like elements on each layer
        num_trees = random.randint(5, 10)
        for _ in range(num_trees):
            angle = random.uniform(0, 2 * math.pi)
            distance = random.uniform(0, layer_radius)
            tree_base = rg.Point3d(distance * math.cos(angle), distance * math.sin(angle), layer_height)
            tree_height = random.uniform(height_increment / 2, max_tree_height)
            tree_top = rg.Point3d(tree_base.X, tree_base.Y, tree_base.Z + tree_height)
            
            # Create a tree trunk as a cylinder
            trunk_radius = random.uniform(0.1, 0.3)
            tree_trunk = rg.Cylinder(rg.Circle(tree_base, trunk_radius), tree_height).ToBrep(True, True)
            geometries.append(tree_trunk)
        
        # Create a surface for the layer
        layer_surface = rg.Brep.CreatePlanarBreps(circle)[0]
        geometries.append(layer_surface)
    
    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_stacked_forests_model(5.0, 2.0, 4, 10.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_stacked_forests_model(3.5, 1.5, 6, 8.0, seed=123)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_stacked_forests_model(4.0, 3.0, 5, 12.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_stacked_forests_model(6.0, 2.5, 3, 15.0, seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_stacked_forests_model(7.0, 1.0, 8, 5.0, seed=2023)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
