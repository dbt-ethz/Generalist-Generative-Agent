# Created for 0001_0001_house_within_a_house.json

""" Summary:
The function `generate_concept_model` creates an architectural concept model based on the "House within a house" metaphor. It constructs a series of nested conical volumes, representing layers of spatial hierarchy that transition from public to private areas. The outer layers are designed to be transparent, suggesting openness, while the innermost volume, more opaque, serves as a sanctuary. By varying parameters like inner and outer radii, height, and taper angle, the function generates distinct geometries that embody the metaphor's themes of protection, enclosure, and layered spatial experiences, facilitating a visual exploration of the design task."""

#! python 3
function_code = """def generate_concept_model(inner_radius=2.0, outer_radius=6.0, height=4.0, taper_angle=10.0):
    \"""
    Generates an architectural Concept Model using the 'House within a house' metaphor.

    This function creates a series of nested conical volumes, representing a spatial hierarchy
    from public to private spaces. The outermost layers are designed to be more transparent,
    suggesting permeability and gradual transition. The innermost volume is more opaque,
    representing the core sanctuary. The taper introduces a sense of enclosure and retreat.

    Parameters:
    - inner_radius: The radius of the base of the innermost cone (core sanctuary).
    - outer_radius: The radius of the base of the outermost cone.
    - height: The uniform height of all conical volumes.
    - taper_angle: The angle at which each cone tapers, affecting the sense of enclosure.

    Returns:
    - A list of Breps representing the nested conical volumes.
    \"""
    
    import Rhino.Geometry as rg
    import math
    
    # Calculate the number of layers based on the taper angle and height
    if outer_radius == inner_radius:
        num_layers = 1
    else:
        num_layers = int((outer_radius - inner_radius) / (height * math.tan(math.radians(taper_angle)))) + 1

    # Initialize list to store the generated Breps
    breps = []

    # Create nested conical volumes
    for i in range(num_layers):
        # Calculate base radius for each layer
        if num_layers > 1:
            layer_radius = inner_radius + i * ((outer_radius - inner_radius) / (num_layers - 1))
        else:
            layer_radius = inner_radius
        
        # Create a base circle for the cone
        base_circle = rg.Circle(rg.Plane.WorldXY, layer_radius)
        
        # Define the cone
        cone = rg.Cone(base_circle.Plane, height, layer_radius)
        
        # Create the conical surface
        brep = cone.ToBrep(True)
        
        # Add the cone to the list
        breps.append(brep)
    
    return breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = generate_concept_model(inner_radius=3.0, outer_radius=7.0, height=5.0, taper_angle=15.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = generate_concept_model(inner_radius=1.5, outer_radius=5.5, height=3.0, taper_angle=12.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = generate_concept_model(inner_radius=2.5, outer_radius=8.0, height=6.0, taper_angle=20.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = generate_concept_model(inner_radius=4.0, outer_radius=9.0, height=7.0, taper_angle=25.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = generate_concept_model(inner_radius=2.0, outer_radius=10.0, height=8.0, taper_angle=30.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
