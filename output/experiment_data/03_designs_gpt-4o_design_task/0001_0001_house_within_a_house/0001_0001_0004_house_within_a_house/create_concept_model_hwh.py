# Created for 0001_0001_house_within_a_house.json

""" Summary:
The provided function, `create_concept_model_hwh`, generates an architectural concept model based on the "House within a house" metaphor by creating nested cylindrical volumes. Each volume represents varying levels of privacy and function, with the innermost cylinder designed as an intimate sanctuary. The function calculates radii for three layers, creating a series of cylinders that transition from a public outer shell to a private inner core. By applying transparency to the outer layers, it emphasizes the metaphor's layered spatial hierarchy and the journey from exterior to interior, fostering a sense of protection and varied spatial experiences."""

#! python 3
function_code = """def create_concept_model_hwh(inner_radius, outer_radius, height, seed=42):
    \"""
    Creates an architectural Concept Model based on the 'House within a house' metaphor.
    
    This function generates a series of nested cylindrical volumes that represent varying levels of privacy and function.
    The model embodies the idea of moving through layers, transitioning from public to private spaces with the inner core
    being the most intimate sanctuary.
    
    Parameters:
    - inner_radius: The radius of the innermost core volume (float).
    - outer_radius: The radius of the outermost shell volume (float).
    - height: The uniform height of all volumes (float).
    - seed: Seed for randomness to ensure consistent results (int, default is 42).
    
    Returns:
    - A list of RhinoCommon Brep objects representing the nested cylindrical volumes.
    \"""
    import Rhino.Geometry as rg
    import random
    
    random.seed(seed)
    
    # Define the number of layers
    num_layers = 3
    
    # Calculate radii for each layer
    radii = [
        inner_radius + i * ((outer_radius - inner_radius) / (num_layers - 1))
        for i in range(num_layers)
    ]
    
    # Create cylindrical volumes for each layer
    breps = []
    for i, radius in enumerate(radii):
        # Create a circle base
        circle = rg.Circle(rg.Plane.WorldXY, radius)
        
        # Create a cylinder
        cylinder = rg.Cylinder(circle, height)
        
        # Convert cylinder to brep
        brep = cylinder.ToBrep(True, True)
        
        # Apply transparency to the outer layers (conceptual)
        if i < num_layers - 1:
            transparency = 0.5 + (0.5 * i / (num_layers - 2))
            # Here you would apply material properties if needed, but it's conceptual in this context
        
        breps.append(brep)
    
    return breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_concept_model_hwh(5.0, 10.0, 15.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_concept_model_hwh(3.0, 8.0, 12.0, seed=100)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_concept_model_hwh(2.5, 7.5, 10.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_concept_model_hwh(4.0, 9.0, 20.0, seed=77)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_concept_model_hwh(6.0, 12.0, 18.0, seed=50)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
