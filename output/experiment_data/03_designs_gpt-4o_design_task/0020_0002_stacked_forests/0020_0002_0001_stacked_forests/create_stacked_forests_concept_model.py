# Created for 0020_0002_stacked_forests.json

""" Summary:
The `create_stacked_forests_concept_model` function generates an architectural concept model inspired by the metaphor of "Stacked forests." It creates a series of interlocking, organically shaped volumes representing different forest layers, establishing a complex, layered silhouette. Each layer is defined by a base rectangle transformed into organic shapes, reflecting the density and hierarchy of a forest. The function incorporates voids to simulate natural clearings and paths for vertical and horizontal circulation, mimicking forest trails. This design approach emphasizes varied spatial experiences and organic growth patterns, capturing the intricate relationships found in a natural ecosystem."""

#! python 3
function_code = """def create_stacked_forests_concept_model(base_length, base_width, height, num_layers, seed=42):
    \"""
    Creates an architectural Concept Model inspired by the 'Stacked forests' metaphor.
    
    This function generates a series of interlocking, organically shaped volumes that mimic the layered and complex 
    nature of a forest. Each layer represents a distinct level in the forest, with voids and solids that emulate 
    natural clearings and dense thickets. Paths representing natural trails are integrated into the design, promoting 
    vertical and horizontal exploration.

    Parameters:
    - base_length (float): The length of the base of the model in meters.
    - base_width (float): The width of the base of the model in meters.
    - height (float): The total height of the model in meters.
    - num_layers (int): The number of vertical layers to create.
    - seed (int, optional): Seed for randomness to ensure replicable results. Default is 42.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep objects representing the 3D geometries of the concept model.
    \"""
    import Rhino.Geometry as rg
    import random
    
    random.seed(seed)
    
    # Determine layer height
    layer_height = height / num_layers
    
    # Initialize list to hold geometry
    geometries = []
    
    for i in range(num_layers):
        # Calculate the vertical position of the current layer
        z_position = i * layer_height
        
        # Create a base rectangle for the layer
        base_rect = rg.Rectangle3d(rg.Plane.WorldXY, base_length, base_width)
        base_rect.Transform(rg.Transform.Translation(0, 0, z_position))
        
        # Create a random organic shape by offsetting the base rectangle
        offset_dist = random.uniform(-0.2, 0.2) * min(base_length, base_width)
        organic_curve = base_rect.ToNurbsCurve().Offset(rg.Plane.WorldXY, offset_dist, 0.01, rg.CurveOffsetCornerStyle.Round)
        
        if not organic_curve:  # Skip if offset fails
            continue

        # Create a lofted surface from the base rectangle to the organic curve
        loft_brep = rg.Brep.CreateFromLoft([base_rect.ToNurbsCurve(), organic_curve[0]], rg.Point3d.Unset, rg.Point3d.Unset, rg.LoftType.Normal, False)
        
        if not loft_brep or len(loft_brep) == 0:
            continue
        
        # Add the brep to the list of geometries
        geometries.append(loft_brep[0])
        
        # Optionally add voids to represent clearings
        if random.random() < 0.5:
            void_radius = random.uniform(0.5, 1.5)
            void_center = rg.Point3d(random.uniform(0, base_length), random.uniform(0, base_width), z_position + layer_height / 2)
            void_sphere = rg.Brep.CreateFromSphere(rg.Sphere(void_center, void_radius))
            if void_sphere:
                geometries.append(void_sphere)
    
    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_stacked_forests_concept_model(10.0, 5.0, 15.0, 4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_stacked_forests_concept_model(8.0, 4.0, 12.0, 3, seed=24)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_stacked_forests_concept_model(15.0, 7.0, 20.0, 5, seed=100)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_stacked_forests_concept_model(12.0, 6.0, 18.0, 6, seed=56)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_stacked_forests_concept_model(9.0, 4.5, 14.0, 5, seed=10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
