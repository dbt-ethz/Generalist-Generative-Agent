# Created for 0020_0005_stacked_forests.json

""" Summary:
The provided function `create_stacked_forests_concept` generates an architectural concept model inspired by the metaphor of "Stacked forests." It creates a series of cascading terraces representing various ecological layers, with each layer's dimensions and heights varying randomly to reflect natural forms. By adjusting the openness factor, the model balances enclosed and open spaces, promoting vertical integration and light interaction. The resulting geometries, structured as RhinoCommon.Brep objects, embody the dynamic, stepped silhouette of a forest hillside, enhancing spatial richness and connectivity, akin to layers in a natural forest ecosystem. This approach translates metaphorical concepts into tangible architectural forms."""

#! python 3
function_code = """def create_stacked_forests_concept(base_length, base_width, num_layers, layer_height_variation, openness_factor):
    \"""
    Creates an architectural Concept Model based on the metaphor of 'Stacked Forests'.
    This model features cascading terraces or ledges representing different ecological layers.
    
    Args:
        base_length (float): The base length of the model in meters.
        base_width (float): The base width of the model in meters.
        num_layers (int): The number of layers or terraces in the model.
        layer_height_variation (float): The maximum variation in height between layers in meters.
        openness_factor (float): A factor between 0 and 1 determining the openness of each layer (0 being completely enclosed, 1 fully open).
    
    Returns:
        list: A list of RhinoCommon.Brep objects representing the 3D geometries of the model.
    \"""
    import Rhino.Geometry as rg
    import random
    
    # Set a seed for randomness
    random.seed(42)
    
    # Initialize the list of geometries
    geometries = []
    
    # Base point for the model
    base_point = rg.Point3d(0, 0, 0)
    
    # Generate each layer
    for i in range(num_layers):
        # Calculate the position and size variation for the current layer
        offset_x = random.uniform(-0.2, 0.2) * base_length
        offset_y = random.uniform(-0.2, 0.2) * base_width
        height = sum(random.uniform(0, layer_height_variation) for _ in range(i))
        
        # Calculate openness
        openness = openness_factor * random.uniform(0.5, 1.0)
        
        # Create the base rectangle for the current layer
        layer_length = base_length * (1 - (i * openness / num_layers))
        layer_width = base_width * (1 - (i * openness / num_layers))
        
        # Create a rectangle and extrude it to form a terrace
        rectangle = rg.Rectangle3d(rg.Plane(base_point + rg.Vector3d(offset_x, offset_y, height), rg.Vector3d.ZAxis), layer_length, layer_width)
        extrusion = rg.Extrusion.Create(rectangle.ToNurbsCurve(), random.uniform(3.0, 5.0), True)
        
        # Convert extrusion to Brep
        brep = extrusion.ToBrep()
        
        # Add the brep to the geometries list
        geometries.append(brep)
    
    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_stacked_forests_concept(10.0, 5.0, 4, 2.0, 0.7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_stacked_forests_concept(15.0, 8.0, 5, 1.5, 0.9)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_stacked_forests_concept(12.0, 6.0, 3, 2.5, 0.6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_stacked_forests_concept(20.0, 10.0, 6, 3.0, 0.8)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_stacked_forests_concept(8.0, 4.0, 3, 1.0, 0.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
