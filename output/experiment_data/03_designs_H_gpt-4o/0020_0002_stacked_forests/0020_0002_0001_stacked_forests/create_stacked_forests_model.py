# Created for 0020_0002_stacked_forests.json

""" Summary:
The provided function, `create_stacked_forests_model`, generates an architectural concept model inspired by the "Stacked forests" metaphor by creating a series of interlocking, organically shaped volumes. Each layer represents a distinct forest level, with a balance between density and openness achieved through variable base sizes and heights. The function incorporates random deviations to simulate natural forms and includes horizontal pathways that mimic trails, enhancing spatial exploration. The resulting model features an intricate silhouette, reflecting the complexity of a forest ecosystem, with dynamic interactions between solid and void spaces, embodying the metaphor's essence of organic growth and layered connectivity."""

#! python 3
function_code = """def create_stacked_forests_model(base_size=8.0, layer_height=3.0, num_layers=5, seed=42):
    \"""
    Generates an architectural Concept Model inspired by the 'Stacked forests' metaphor.

    This model creates a series of interlocking, organically shaped volumes that mimic 
    the layered and complex nature of a forest. The design focuses on achieving a balance 
    between density and openness, incorporating vertical and horizontal pathways that 
    simulate natural trails.

    Parameters:
    - base_size (float): The approximate size of the base of each module.
    - layer_height (float): The height of each layer in meters.
    - num_layers (int): The number of vertical layers to create.
    - seed (int): Seed for randomness to ensure replicable results.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep objects representing the 3D geometries of the concept model.
    \"""
    import Rhino.Geometry as rg
    import random
    
    random.seed(seed)
    
    # Initialize list to hold geometry
    geometries = []
    
    for i in range(num_layers):
        # Calculate the vertical position of the current layer
        z_position = i * layer_height
        
        # Create a base module with an organic shape (e.g., a distorted circle)
        deviation = random.uniform(0.1, 0.3) * base_size
        organic_shape = rg.Circle(rg.Plane.WorldXY, base_size + deviation).ToNurbsCurve()
        
        # Create a vertical extrusion of the organic shape
        extrusion = rg.Extrusion.Create(organic_shape, layer_height, True)
        if extrusion:
            extrusion_brep = extrusion.ToBrep()
            translation = rg.Transform.Translation(0, 0, z_position)
            extrusion_brep.Transform(translation)
            geometries.append(extrusion_brep)
        
        # Add horizontal pathways (simulate trails) in random directions
        if random.random() < 0.6:
            path_length = random.uniform(1.0, 3.0)
            path_direction = rg.Vector3d(random.uniform(-1, 1), random.uniform(-1, 1), 0)
            path_direction.Unitize()
            path_curve = rg.LineCurve(rg.Point3d(0, 0, z_position + layer_height / 2), 
                                      rg.Point3d(path_length * path_direction.X, path_length * path_direction.Y, z_position + layer_height / 2))
            path_brep = rg.Brep.CreatePipe(path_curve, 0.1, False, rg.PipeCapMode.Round, True, 0.01, 0.01)
            if path_brep:
                geometries.append(path_brep)
    
    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_stacked_forests_model(base_size=10.0, layer_height=4.0, num_layers=6, seed=123)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_stacked_forests_model(base_size=7.5, layer_height=2.5, num_layers=4, seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_stacked_forests_model(base_size=9.0, layer_height=3.5, num_layers=7, seed=56)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_stacked_forests_model(base_size=12.0, layer_height=5.0, num_layers=3, seed=78)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_stacked_forests_model(base_size=8.5, layer_height=3.0, num_layers=5, seed=30)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
