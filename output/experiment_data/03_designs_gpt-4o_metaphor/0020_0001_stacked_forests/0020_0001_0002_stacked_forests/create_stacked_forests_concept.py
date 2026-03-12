# Created for 0020_0001_stacked_forests.json

""" Summary:
The provided function, `create_stacked_forests_concept`, generates a 3D architectural concept model based on the metaphor of "Stacked Forests." It creates multiple vertical layers, each represented by a circular surface that diminishes in radius, simulating a tiered forest. The function introduces randomness in the placement of cylindrical "trees," reflecting organic growth and spatial richness. Each layer's height increases incrementally, fostering vertical connectivity akin to a natural ecosystem. By varying parameters like layers, base radius, and randomness, the function produces diverse models that embody the metaphor's key traits, emphasizing hierarchy and interaction within the architectural design."""

#! python 3
function_code = """def create_stacked_forests_concept(layers=5, base_radius=10.0, height_increment=3.0, randomness_factor=0.2):
    \"""
    Creates a 3D architectural Concept Model based on the metaphor of "Stacked Forests".
    This metaphor emphasizes a multi-layered, vertical organization that resembles a dense, tiered forest.

    Parameters:
    - layers (int): The number of vertical layers or "floors" in the structure.
    - base_radius (float): The radius of the base layer, which determines the starting point for the structure's footprint.
    - height_increment (float): The height difference between consecutive layers.
    - randomness_factor (float): A factor that introduces slight randomness to the placement of elements, simulating organic growth.

    Returns:
    - list: A list of 3D Brep objects representing the concept model.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    random.seed(42)  # Ensures replicable randomness

    breps = []

    for i in range(layers):
        height = i * height_increment
        layer_radius = base_radius * (1 - (i / layers) * randomness_factor)
        
        # Create a circle for the current layer
        circle = rg.Circle(rg.Plane.WorldXY, layer_radius)
        
        # Create a surface for the current layer
        surface = rg.Brep.CreatePlanarBreps(circle.ToNurbsCurve())[0]
        
        # Move the surface to the correct height
        translation = rg.Transform.Translation(0, 0, height)
        surface.Transform(translation)
        
        # Add some vertical elements to simulate trees
        num_trees = random.randint(3, 6)
        for _ in range(num_trees):
            tree_radius = random.uniform(0.2, 0.5)
            tree_height = random.uniform(2.0, 4.0)
            angle = random.uniform(0, 2 * math.pi)
            distance_from_center = random.uniform(1.0, layer_radius - 1.0)
            
            x_pos = distance_from_center * math.cos(angle)
            y_pos = distance_from_center * math.sin(angle)
            
            cylinder_base = rg.Point3d(x_pos, y_pos, height)
            cylinder = rg.Cylinder(rg.Circle(rg.Plane.WorldXY, tree_radius), tree_height).ToBrep(True, True)
            
            # Move the cylinder to the correct location
            translation = rg.Transform.Translation(x_pos, y_pos, height)
            cylinder.Transform(translation)
            
            breps.append(cylinder)

        breps.append(surface)

    return breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_stacked_forests_concept(layers=7, base_radius=12.0, height_increment=4.0, randomness_factor=0.3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_stacked_forests_concept(layers=10, base_radius=15.0, height_increment=2.5, randomness_factor=0.1)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_stacked_forests_concept(layers=4, base_radius=8.0, height_increment=5.0, randomness_factor=0.15)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_stacked_forests_concept(layers=6, base_radius=11.0, height_increment=3.5, randomness_factor=0.25)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_stacked_forests_concept(layers=5, base_radius=9.0, height_increment=2.0, randomness_factor=0.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
