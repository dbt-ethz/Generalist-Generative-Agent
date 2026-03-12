# Created for 0001_0001_house_within_a_house.json

""" Summary:
The function `create_conceptual_model` generates an architectural concept model based on the "House within a house" metaphor by creating a series of nested spherical volumes. Each volume represents varying levels of privacy and function, with the outer layers designed to be more transparent, symbolizing openness, while the innermost sphere serves as an opaque, intimate core sanctuary. The function emphasizes spatial progression from public to private spaces, reflecting the protective qualities of the metaphor. By manipulating parameters like radius, height, and number of layers, it allows for exploration of complex spatial relationships and varying experiences within the architectural design."""

#! python 3
function_code = """def create_conceptual_model(inner_radius=3.0, outer_radius=6.0, height=4.0, num_layers=4):
    \"""
    Creates an architectural Concept Model based on the 'House within a house' metaphor.

    This function generates a series of nested spherical volumes to represent different levels of privacy and function.
    The outermost volumes are designed to be more transparent, while the innermost volume represents a more opaque
    and intimate core sanctuary. The model emphasizes the progression from public to private spaces and the protective
    qualities of the design.

    Parameters:
    - inner_radius: The radius of the innermost sphere (core sanctuary).
    - outer_radius: The radius of the outermost sphere.
    - height: The vertical extent of the spherical layers.
    - num_layers: The number of spherical layers to create.

    Returns:
    - A list of Breps representing the nested spherical volumes.
    \"""
    import Rhino.Geometry as rg
    import random

    # Set a random seed for replicability
    random.seed(42)

    # List to store the generated Breps
    breps = []

    # Calculate the step size for each layer
    step_radius = (outer_radius - inner_radius) / num_layers
    current_radius = inner_radius

    # Create nested spherical volumes
    for i in range(num_layers):
        # Create a sphere
        center_point = rg.Point3d(0, 0, i * (height / num_layers))
        sphere = rg.Sphere(center_point, current_radius + i * step_radius)
        
        # Convert sphere to Brep
        sphere_brep = sphere.ToBrep()
        
        # Add the sphere to the list
        breps.append(sphere_brep)
    
    return breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_conceptual_model(inner_radius=2.0, outer_radius=5.0, height=10.0, num_layers=6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_conceptual_model(inner_radius=1.5, outer_radius=4.5, height=8.0, num_layers=5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_conceptual_model(inner_radius=4.0, outer_radius=8.0, height=12.0, num_layers=3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_conceptual_model(inner_radius=3.5, outer_radius=7.0, height=5.0, num_layers=8)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_conceptual_model(inner_radius=2.5, outer_radius=5.5, height=7.0, num_layers=4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
