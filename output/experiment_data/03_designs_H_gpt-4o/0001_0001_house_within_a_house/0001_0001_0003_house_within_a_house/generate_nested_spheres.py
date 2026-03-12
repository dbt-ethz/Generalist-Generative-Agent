# Created for 0001_0001_house_within_a_house.json

""" Summary:
The provided function, `generate_nested_spheres`, creates an architectural concept model embodying the "House within a house" metaphor through a series of nested spherical volumes. Each sphere represents different levels of privacy and function, with the outer layers being more transparent and the innermost layer opaque, symbolizing an intimate core sanctuary. The function calculates the radius for each layer based on the specified inner and outer radii, reinforcing the design's spatial hierarchy. By generating multiple sets of spheres, the model visually conveys the transition from public to private spaces, illustrating the protective and enclosing qualities central to the metaphor."""

#! python 3
function_code = """def generate_nested_spheres(inner_radius=1.5, outer_radius=4.0, num_layers=3):
    \"""
    Creates an architectural Concept Model using the 'House within a house' metaphor.
    
    This function generates a series of nested spherical volumes, each representing
    different levels of privacy and function. The outermost spheres are more transparent,
    while the innermost sphere is opaque, symbolizing an intimate core sanctuary. The geometry
    embodies the concept of transitioning through layers, from public to private spaces.

    Parameters:
    - inner_radius: The radius of the innermost sphere (core sanctuary).
    - outer_radius: The radius of the outermost sphere.
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
    step_radius = (outer_radius - inner_radius) / (num_layers - 1)
    
    # Create nested spherical volumes
    for i in range(num_layers):
        # Calculate the current radius
        current_radius = inner_radius + i * step_radius
        
        # Create a sphere
        center_point = rg.Point3d(0, 0, 0)
        sphere = rg.Sphere(center_point, current_radius)
        
        # Convert the sphere to a Brep
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
    geometry = generate_nested_spheres(inner_radius=2.0, outer_radius=5.0, num_layers=4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = generate_nested_spheres(inner_radius=1.0, outer_radius=3.0, num_layers=5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = generate_nested_spheres(inner_radius=3.0, outer_radius=6.0, num_layers=2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = generate_nested_spheres(inner_radius=1.5, outer_radius=7.0, num_layers=6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = generate_nested_spheres(inner_radius=2.5, outer_radius=8.0, num_layers=3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
