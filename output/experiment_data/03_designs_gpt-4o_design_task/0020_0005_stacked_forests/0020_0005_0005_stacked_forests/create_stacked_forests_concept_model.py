# Created for 0020_0005_stacked_forests.json

""" Summary:
The provided function, `create_stacked_forests_concept_model`, generates an architectural concept model inspired by the "Stacked forests" metaphor. It creates a series of cascading terraces that represent different ecological layers, mimicking the stratification found in a forest. By adjusting the dimensions of each layer and introducing randomness to their corners, the function reflects organic growth patterns. It emphasizes vertical connectivity, allowing light and shadows to interact dynamically across the layers. The resulting geometries embody the metaphor's essence, capturing the stepped silhouette and spatial richness of a forest landscape, thus fulfilling the design task effectively."""

#! python 3
function_code = """def create_stacked_forests_concept_model(base_length, base_width, num_layers, layer_height, randomness_seed=42):
    \"""
    Creates an architectural Concept Model based on the 'Stacked forests' metaphor.
    
    This function generates a cascading series of terraces or ledges, each representing
    a different ecological layer. It integrates vertical spaces to allow light penetration 
    and creates a play of shadows. The design uses a combination of linear and organic 
    shapes to reflect the natural stratification and growth patterns of a forest.

    Parameters:
    - base_length (float): The overall length of the building base in meters.
    - base_width (float): The overall width of the building base in meters.
    - num_layers (int): The number of cascading layers or terraces.
    - layer_height (float): The average height of each layer in meters.
    - randomness_seed (int): Random seed for replicable results when introducing randomness.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep objects representing the 3D geometries 
      of the concept model.
    \"""
    import Rhino.Geometry as rg
    import random
    
    random.seed(randomness_seed)
    
    geometries = []
    current_z = 0
    
    for i in range(num_layers):
        # Determine dimensions for this layer
        length = base_length * (1 - i * 0.1)  # Decrease length progressively
        width = base_width * (1 - i * 0.1)    # Decrease width progressively
        
        # Create a base rectangle for the current layer
        base_plane = rg.Plane(rg.Point3d(0, 0, current_z), rg.Vector3d.ZAxis)
        rectangle = rg.Rectangle3d(base_plane, length, width)
        
        # Add randomness to the corner points to simulate organic growth
        corners = [rectangle.Corner(i) for i in range(4)]
        for j, corner in enumerate(corners):
            offset_x = random.uniform(-1, 1)
            offset_y = random.uniform(-1, 1)
            corners[j] = rg.Point3d(corner.X + offset_x, corner.Y + offset_y, corner.Z)
        
        # Create a lofted surface from the perturbed rectangle
        loft_curve = rg.PolylineCurve(corners + [corners[0]])
        loft_surface = rg.Brep.CreateFromLoft([loft_curve], base_plane.Origin, base_plane.Origin, rg.LoftType.Normal, False)
        
        if loft_surface is not None and len(loft_surface) > 0:
            loft_surface = loft_surface[0]
        
            # Create vertical connectors between layers
            if geometries:
                previous_top = geometries[-1]
                connector_surfaces = rg.Brep.CreateFromLoft([previous_top.Edges[0].ToNurbsCurve(), loft_curve], 
                                                            rg.Point3d.Unset, rg.Point3d.Unset, rg.LoftType.Straight, False)
                if connector_surfaces:
                    geometries.extend(connector_surfaces)
            
            # Add the current layer's surface to the geometries
            geometries.append(loft_surface)
        
        # Update current Z position
        current_z += layer_height
    
    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_stacked_forests_concept_model(10.0, 8.0, 5, 2.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_stacked_forests_concept_model(15.0, 10.0, 4, 3.0, randomness_seed=7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_stacked_forests_concept_model(12.0, 9.0, 6, 1.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_stacked_forests_concept_model(20.0, 15.0, 3, 2.5, randomness_seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_stacked_forests_concept_model(8.0, 6.0, 7, 1.0, randomness_seed=21)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
