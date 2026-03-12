# Created for 0001_0001_house_within_a_house.json

""" Summary:
The function `create_concept_model` generates an architectural concept model based on the "House within a house" metaphor by creating a series of nested cylindrical volumes. Each volume represents varying degrees of privacy and function, with the outer layers designed to be more transparent, suggesting permeability, while the innermost volume remains opaque, symbolizing an intimate core sanctuary. The function allows for customization of radii, height, and the number of layers, fostering exploration of spatial hierarchies. The resulting model illustrates the progression from public to private spaces, effectively embodying the metaphor's emphasis on nesting and enclosure."""

#! python 3
function_code = """def create_concept_model(inner_radius=2.0, outer_radius=5.0, height=3.0, layers=3):
    \"""
    Creates a conceptual architectural model using the 'House within a house' metaphor.
    
    This function generates a series of nested cylindrical volumes, each representing a different 
    level of privacy and function. The outermost volumes are more transparent, while the innermost 
    volume is opaque, representing an intimate core sanctuary. The geometry is inspired by the idea 
    of moving through layers, emphasizing the progression from public to private spaces.

    Parameters:
    - inner_radius: The radius of the innermost cylinder (core sanctuary).
    - outer_radius: The radius of the outermost cylinder.
    - height: The height of each cylindrical layer.
    - layers: The number of cylindrical layers to create.

    Returns:
    - A list of Breps representing the nested volumes.
    \"""

    import Rhino.Geometry as rg
    import random

    # Set a random seed for replicability
    random.seed(42)

    # List to store the generated Breps
    breps = []

    # Calculate the step size for each layer
    step_radius = (outer_radius - inner_radius) / layers
    current_radius = inner_radius

    # Create nested cylindrical volumes
    for i in range(layers):
        # Create a cylinder
        base_point = rg.Point3d(0, 0, i * height)
        circle = rg.Circle(base_point, current_radius + i * step_radius)
        cylinder = rg.Cylinder(circle, height).ToBrep(True, True)
        
        # Add the cylinder to the list
        breps.append(cylinder)
    
    return breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_concept_model(inner_radius=1.5, outer_radius=4.5, height=2.0, layers=5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_concept_model(inner_radius=3.0, outer_radius=6.0, height=4.0, layers=2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_concept_model(inner_radius=2.5, outer_radius=7.0, height=3.5, layers=4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_concept_model(inner_radius=2.0, outer_radius=8.0, height=5.0, layers=6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_concept_model(inner_radius=2.0, outer_radius=5.0, height=2.5, layers=3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
