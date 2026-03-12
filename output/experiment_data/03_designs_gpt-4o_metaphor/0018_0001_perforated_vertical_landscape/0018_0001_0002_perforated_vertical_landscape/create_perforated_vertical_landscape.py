# Created for 0018_0001_perforated_vertical_landscape.json

""" Summary:
The function `create_perforated_vertical_landscape` generates an architectural concept model based on the metaphor of a "Perforated Vertical Landscape." It creates multiple vertical layers, each represented as a box. Within these layers, perforations are introduced according to a specified density, allowing light and air to flow through, echoing the metaphor's traits of verticality and permeability. The function uses random dimensions and positions for the perforations, resulting in a dynamic interplay between solid and void, reminiscent of a natural landscape. This method ultimately produces a series of 3D geometries that embody the conceptual design."""

#! python 3
function_code = """def create_perforated_vertical_landscape(base_width, base_depth, height, num_layers, perforation_density, seed):
    \"""
    Generates a conceptual architectural model based on the metaphor of a 'Perforated Vertical Landscape'.
    This model features a rhythmic interplay between solid and void elements, allowing light, air, and views
    to penetrate through its form, reminiscent of a natural landscape oriented vertically.

    Parameters:
    - base_width (float): The width of the model base in meters.
    - base_depth (float): The depth of the model base in meters.
    - height (float): The total height of the model in meters.
    - num_layers (int): The number of vertical layers or floors in the model.
    - perforation_density (float): A value between 0 and 1 representing the density of perforations.
    - seed (int): A seed value for random number generation for replicability.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of 3D Brep geometries representing the concept model.
    \"""
    import Rhino.Geometry as rg
    import random
    
    random.seed(seed)
    
    # Calculate layer height
    layer_height = height / num_layers
    
    # Initialize list to store breps
    model_breps = []
    
    # Iterate over each layer
    for i in range(num_layers):
        # Base plane for the current layer
        base_plane = rg.Plane.WorldXY
        base_plane.Translate(rg.Vector3d(0, 0, i * layer_height))
        
        # Create a box for the current layer
        layer_box = rg.Box(base_plane, rg.Interval(0, base_width), rg.Interval(0, base_depth), rg.Interval(0, layer_height)).ToBrep()
        
        # Generate perforations
        num_perforations = int(perforation_density * 10)  # Arbitrary scale for perforation density
        for _ in range(num_perforations):
            # Random dimensions and position for perforation
            perf_width = random.uniform(0.1, base_width * 0.5)
            perf_depth = random.uniform(0.1, base_depth * 0.5)
            perf_height = random.uniform(layer_height * 0.5, layer_height)
            
            x_offset = random.uniform(0, base_width - perf_width)
            y_offset = random.uniform(0, base_depth - perf_depth)
            z_offset = i * layer_height + random.uniform(0, layer_height - perf_height)
            
            # Create perforation box
            perf_box = rg.Box(rg.Plane.WorldXY, rg.Interval(x_offset, x_offset + perf_width),
                              rg.Interval(y_offset, y_offset + perf_depth),
                              rg.Interval(z_offset, z_offset + perf_height)).ToBrep()
            
            # Subtract the perforation from the layer box
            difference = rg.Brep.CreateBooleanDifference(layer_box, perf_box, 0.01)
            if difference:  # Check if the difference operation returned a valid result
                layer_box = difference[0]
        
        # Add modified layer box to the model
        model_breps.append(layer_box)
    
    return model_breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_perforated_vertical_landscape(10.0, 5.0, 20.0, 4, 0.6, 42)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_perforated_vertical_landscape(15.0, 7.0, 30.0, 5, 0.8, 24)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_perforated_vertical_landscape(12.0, 6.0, 25.0, 3, 0.7, 36)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_perforated_vertical_landscape(8.0, 4.0, 15.0, 6, 0.5, 18)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_perforated_vertical_landscape(20.0, 10.0, 40.0, 5, 0.9, 99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
