# Created for 0020_0001_stacked_forests.json

""" Summary:
The function `create_stacked_forests_model` generates an architectural concept model inspired by the metaphor of "Stacked forests" by creating vertically layered platforms. Each layer is distinct in size and orientation, reflecting the diverse strata of a forest. The function incorporates randomness in height and rotation to evoke organic forms, simulating a natural growth pattern. Vertical circulation elements, such as ramps and stairs, enhance connectivity between layers, mimicking the movement through a forest. This approach emphasizes hierarchy and spatial richness, creating a dynamic structure that offers varied experiences akin to traversing through different forest layers."""

#! python 3
function_code = """def create_stacked_forests_model(base_size, num_layers, height_variation, rotation_variation, seed=42):
    \"""
    Creates an architectural Concept Model embodying the 'Stacked forests' metaphor. The model consists of 
    a series of layered platforms or blocks that rise vertically. Each layer is distinct in form and orientation, 
    interconnected by vertical circulation elements like ramps or staircases. The design emphasizes organic shapes 
    and irregular forms to represent the diverse forest strata.

    Inputs:
    - base_size: Tuple of two floats representing the base platform size in meters (width, length).
    - num_layers: Integer representing the number of vertical layers to create.
    - height_variation: Float representing the maximum variation in height between layers in meters.
    - rotation_variation: Float representing the maximum rotation in degrees for the orientation of each layer.
    - seed: Integer for random seed to ensure replicability of the design.

    Outputs:
    - List of RhinoCommon Breps representing the 3D geometries of the concept model.
    \"""

    import Rhino.Geometry as rg
    import random
    import math
    random.seed(seed)

    width, length = base_size
    current_height = 0
    layer_height = 3.0  # Average height for each layer in meters
    geometries = []

    for i in range(num_layers):
        # Create base plane for the current layer
        base_plane = rg.Plane.WorldXY
        base_plane.Translate(rg.Vector3d(0, 0, current_height))
        
        # Create a rectangle for the layer
        rect = rg.Rectangle3d(base_plane, width, length)
        
        # Apply random rotation to simulate organic form
        rotation_angle = random.uniform(-rotation_variation, rotation_variation)
        rotation = rg.Transform.Rotation(math.radians(rotation_angle), base_plane.ZAxis, rect.Center)
        rect.Transform(rotation)
        
        # Create a surface from the rectangle
        surface = rg.Brep.CreateFromCornerPoints(rect.Corner(0), rect.Corner(1), rect.Corner(2), rect.Corner(3), 0.01)
        
        # Vary the height of each layer for organic stacking
        current_height += layer_height + random.uniform(-height_variation, height_variation)
        
        # Add the generated surface to the list of geometries
        geometries.append(surface)
        
        # Optionally, create vertical circulation elements (ramps, stairs)
        if i < num_layers - 1:
            ramp_start = rect.Center + rg.Vector3d(0, 0, layer_height / 2)
            ramp_end = ramp_start + rg.Vector3d(0, 0, layer_height)
            ramp_curve = rg.LineCurve(ramp_start, ramp_end)
            ramp = rg.Brep.CreatePipe(ramp_curve, 0.5, True, rg.PipeCapMode.Flat, True, 0.01, 0.01)[0]
            geometries.append(ramp)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_stacked_forests_model((10.0, 15.0), 5, 2.0, 30.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_stacked_forests_model((8.0, 12.0), 4, 1.5, 45.0, seed=123)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_stacked_forests_model((6.0, 10.0), 3, 1.0, 15.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_stacked_forests_model((12.0, 18.0), 6, 3.0, 60.0, seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_stacked_forests_model((5.0, 8.0), 7, 2.5, 20.0, seed=2023)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
