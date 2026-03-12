# Created for 0001_0004_house_within_a_house.json

""" Summary:
The provided function generates an architectural concept model based on the "House within a house" metaphor by creating a series of nested cubic volumes. Each layer represents a protective and intimate space, transitioning from an outer public area to a secluded inner sanctuary. Parameters like core radius, layer width, and height define the dimensions and characteristics of these layers. The function uses geometric calculations to form overlapping boxes, enhancing the interplay of light and shadow through openings. This approach reflects the metaphor's emphasis on nesting, protection, and varied spatial experiences, facilitating a journey from public to private realms."""

#! python 3
function_code = """def generate_concept_model_house_within_house(core_radius=4.0, layer_width=2.0, num_layers=5, height=10.0):
    \"""
    Generate an architectural Concept Model based on the 'House within a house' metaphor.
    
    This function creates a series of nested cubic volumes, representing layers of protection and 
    intimacy, transitioning from a public exterior to a private interior sanctuary. The layers are 
    interwoven with openings to enhance the spatial interplay of light and shadow.
    
    Parameters:
    - core_radius (float): The half-length of the innermost cube's edge, representing the sanctuary.
    - layer_width (float): The additional width added to each successive layer, symbolizing protective layers.
    - num_layers (int): The number of nested cubic layers to create.
    - height (float): The height of each cubic layer, defining the vertical extent of the model.
    
    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep geometries representing the nested cubic layers of the Concept Model.
    \"""
    import Rhino.Geometry as rg
    
    # Initialize a list to store the resulting geometries
    breps = []
    
    # Define a point for the base of the cubes
    base_point = rg.Point3d(0, 0, 0)
    
    # Generate nested cubes
    for i in range(num_layers):
        # Calculate the half-length of the cube's edge for this layer
        half_length = core_radius + i * layer_width
        
        # Create a box (cube) geometry for this layer
        box_corners = [
            rg.Point3d(-half_length, -half_length, 0),
            rg.Point3d(half_length, -half_length, 0),
            rg.Point3d(half_length, half_length, 0),
            rg.Point3d(-half_length, half_length, 0),
            rg.Point3d(-half_length, -half_length, height),
            rg.Point3d(half_length, -half_length, height),
            rg.Point3d(half_length, half_length, height),
            rg.Point3d(-half_length, half_length, height)
        ]
        box = rg.Box(rg.Plane.WorldXY, box_corners)
        brep = box.ToBrep()
        
        # Add the Brep to the list
        breps.append(brep)
    
    # Return the list of Breps representing the concept model
    return breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = generate_concept_model_house_within_house(core_radius=5.0, layer_width=3.0, num_layers=4, height=12.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = generate_concept_model_house_within_house(core_radius=6.0, layer_width=1.5, num_layers=6, height=8.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = generate_concept_model_house_within_house(core_radius=3.0, layer_width=2.5, num_layers=3, height=15.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = generate_concept_model_house_within_house(core_radius=4.5, layer_width=2.0, num_layers=7, height=9.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = generate_concept_model_house_within_house(core_radius=7.0, layer_width=2.5, num_layers=5, height=11.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
