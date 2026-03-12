# Created for 0020_0002_stacked_forests.json

""" Summary:
The function `create_stacked_forests_concept` generates an architectural concept model inspired by the "Stacked forests" metaphor. It creates multiple vertically stacked layers, each representing distinct forest levels, using random parameters for height and base radius to ensure organic variability. The function incorporates voids, simulating clearings, by probabilistically subtracting smaller volumes from the solid layers. This approach reflects the metaphor's emphasis on density and hierarchy, offering spatial richness through interlocking forms. The resulting model embodies vertical connectivity and varied experiences, mirroring the complexity and diversity found in a natural forest ecosystem."""

#! python 3
function_code = """def create_stacked_forests_concept(seed:int, num_layers:int, base_radius:float, height_intervals:tuple, void_probability:float):
    \"""
    Generates an architectural Concept Model based on the 'Stacked forests' metaphor using parametric inputs.
    
    Parameters:
    seed (int): Seed for random number generator to ensure replicability.
    num_layers (int): The number of vertical layers representing the forest's tiers.
    base_radius (float): The base radius for the organic forms representing the forest modules.
    height_intervals (tuple): A tuple containing the minimum and maximum heights for each layer.
    void_probability (float): The probability of creating a void in a certain space, simulating clearings.

    Returns:
    list: A list of RhinoCommon Brep geometries representing the Concept Model.
    \"""
    import Rhino.Geometry as rg
    import random
    
    random.seed(seed)
    
    # Initialize an empty list to store the resulting geometries
    geometries = []
    
    for i in range(num_layers):
        # Determine layer height
        layer_height = random.uniform(*height_intervals)
        
        # Create a base circle for the layer
        base_circle = rg.Circle(rg.Plane.WorldXY, base_radius)
        
        # Generate a random number of segments for the current layer
        num_segments = random.randint(3, 8)
        
        # Create the base polygon for the layer by converting the circle to a polyline
        base_polygon = rg.Polyline.CreateInscribedPolygon(base_circle, num_segments)
        
        # Create vertical extrusion to form a layer volume
        layer_solid = rg.Extrusion.Create(base_polygon.ToNurbsCurve(), layer_height, True).ToBrep()
        
        # Randomly decide to carve out a void
        if random.random() < void_probability:
            # Create a void by subtracting a smaller volume from the solid
            void_radius = base_radius * random.uniform(0.3, 0.6)
            void_circle = rg.Circle(rg.Plane.WorldXY, void_radius)
            void_polygon = rg.Polyline.CreateInscribedPolygon(void_circle, num_segments)
            void_solid = rg.Extrusion.Create(void_polygon.ToNurbsCurve(), layer_height, True).ToBrep()
            layer_solid = rg.Brep.CreateBooleanDifference(layer_solid, void_solid, 0.01)[0]
        
        # Move the layer to its respective height
        translation = rg.Transform.Translation(0, 0, i * (height_intervals[1] + 1))
        layer_solid.Transform(translation)
        
        # Add the layer to the list of geometries
        geometries.append(layer_solid)
    
    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_stacked_forests_concept(seed=42, num_layers=5, base_radius=3.0, height_intervals=(2.0, 5.0), void_probability=0.3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_stacked_forests_concept(seed=101, num_layers=4, base_radius=2.5, height_intervals=(1.5, 4.5), void_probability=0.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_stacked_forests_concept(seed=7, num_layers=6, base_radius=4.0, height_intervals=(3.0, 6.0), void_probability=0.2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_stacked_forests_concept(seed=15, num_layers=3, base_radius=2.0, height_intervals=(1.0, 3.0), void_probability=0.4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_stacked_forests_concept(seed=30, num_layers=7, base_radius=5.0, height_intervals=(2.5, 7.0), void_probability=0.1)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
