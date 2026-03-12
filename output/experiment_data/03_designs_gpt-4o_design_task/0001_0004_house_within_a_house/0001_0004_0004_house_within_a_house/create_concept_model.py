# Created for 0001_0004_house_within_a_house.json

""" Summary:
The function `create_concept_model` generates an architectural concept model reflecting the "House within a house" metaphor by creating a series of concentric cylindrical layers. Each layer symbolizes the transition from an outer protective envelope to an inner sanctuary, embodying nesting and spatial hierarchy. By varying the inner and outer radii, height, and the number of layers, the model achieves dynamic layering. This design approach illustrates the interplay of exposure and seclusion, enhancing the experiential journey from public to private spaces. The result is a visually and spatially coherent representation of the metaphor's core themes of protection and intimacy."""

#! python 3
function_code = """def create_concept_model(inner_radius=5.0, outer_radius=10.0, height=10.0, layers=3):
    \"""
    Create an architectural Concept Model based on the 'House within a house' metaphor.
    
    This function generates a series of concentric cylindrical layers that represent
    the transition from an outer protective envelope to an inner sanctuary. The model 
    is designed to evoke a sense of nesting and spatial hierarchy.

    Parameters:
    inner_radius (float): The radius of the innermost cylinder representing the core.
    outer_radius (float): The radius of the outermost cylinder representing the envelope.
    height (float): The height of the entire model.
    layers (int): The number of concentric layers between the inner and outer cylinders.

    Returns:
    list: A list of Brep objects representing the concentric layers of the model.
    \"""
    import Rhino.Geometry as rg
    import random
    
    # Ensure consistent randomness for replicability
    random.seed(42)
    
    # Calculate the radial increment between layers
    radial_increment = (outer_radius - inner_radius) / layers
    
    # Create a list to hold the Brep objects
    breps = []
    
    # Create concentric layers
    for i in range(layers + 1):
        # Calculate the radius for the current layer
        current_radius = inner_radius + i * radial_increment
        
        # Add a slight variation to height for dynamic layering
        current_height = height + random.uniform(-0.5, 0.5)
        
        # Create the base circle
        base_circle = rg.Circle(rg.Plane.WorldXY, current_radius)
        
        # Create a cylindrical surface from the circle
        cylinder = rg.Cylinder(base_circle, current_height)
        
        # Convert the cylinder to a Brep
        brep_cylinder = cylinder.ToBrep(True, True)
        
        # Append the Brep to the list
        breps.append(brep_cylinder)
    
    return breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_concept_model(inner_radius=3.0, outer_radius=8.0, height=12.0, layers=4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_concept_model(inner_radius=6.0, outer_radius=12.0, height=15.0, layers=5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_concept_model(inner_radius=4.0, outer_radius=9.0, height=8.0, layers=2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_concept_model(inner_radius=2.0, outer_radius=7.0, height=10.0, layers=6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_concept_model(inner_radius=1.5, outer_radius=5.5, height=20.0, layers=7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
