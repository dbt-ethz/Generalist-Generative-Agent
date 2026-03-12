# Created for 0020_0003_stacked_forests.json

""" Summary:
The function `create_stacked_forests_model` generates a 3D architectural concept model that embodies the "Stacked forests" metaphor by creating a vertically tiered structure. It utilizes staggered and offset volumes to emulate the layers of a forest, with varying widths and heights reflecting the hierarchy and complexity of a natural ecosystem. The model incorporates void spaces to represent clearings, enhancing the organic feel. Vertical and diagonal circulation paths are included to facilitate movement through the layers, mirroring the experience of traversing different forest altitudes. The resulting silhouette captures the dynamic interplay of solidity and movement, akin to a swaying forest canopy."""

#! python 3
function_code = """def create_stacked_forests_model(base_size=(10, 10), layer_height=3, num_layers=6, stagger_distance=1.5, void_density=0.2):
    \"""
    Creates a 3D architectural Concept Model inspired by the 'Stacked forests' metaphor. This function designs a multi-layered 
    structure with staggered, offset volumes, capturing the organic complexity of a forest ecosystem.

    Parameters:
    - base_size (tuple): The (width, depth) dimensions of the base in meters.
    - layer_height (float): The height of each layer in meters.
    - num_layers (int): The number of vertical layers in the structure.
    - stagger_distance (float): The maximum horizontal offset between successive layers in meters.
    - void_density (float): The ratio of void space within each layer.

    Returns:
    - list: A list of RhinoCommon Brep objects representing the 3D geometries of the concept model.
    \"""
    import Rhino.Geometry as rg
    import random

    # Initialize random seed for consistency
    random.seed(42)

    geometries = []
    width, depth = base_size

    for i in range(num_layers):
        # Define the offset for each layer
        offset_x = random.uniform(-stagger_distance, stagger_distance)
        offset_y = random.uniform(-stagger_distance, stagger_distance)
        
        # Define the base point for the current layer
        base_point = rg.Point3d(offset_x, offset_y, i * layer_height)
        
        # Create the rectangular base for the current layer
        layer_box = rg.Box(rg.Plane(base_point, rg.Vector3d.ZAxis), rg.Interval(0, width), rg.Interval(0, depth), rg.Interval(0, layer_height))
        brep_layer = layer_box.ToBrep()
        
        # Add voids to the layer
        voids = []
        num_voids = int(void_density * 10)  # Determining the number of voids
        for _ in range(num_voids):
            void_width = random.uniform(0.2, void_density * width)
            void_depth = random.uniform(0.2, void_density * depth)
            void_x = random.uniform(base_point.X, base_point.X + width - void_width)
            void_y = random.uniform(base_point.Y, base_point.Y + depth - void_depth)
            
            void_box = rg.Box(rg.Plane(rg.Point3d(void_x, void_y, base_point.Z), rg.Vector3d.ZAxis), rg.Interval(0, void_width), rg.Interval(0, void_depth), rg.Interval(0, layer_height))
            voids.append(void_box.ToBrep())
        
        # Subtract the voids from the layer
        for void in voids:
            result = rg.Brep.CreateBooleanDifference(brep_layer, void, 0.01)
            if result:  # Check if the result is not empty
                brep_layer = result[0]
        
        geometries.append(brep_layer)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_stacked_forests_model(base_size=(15, 15), layer_height=4, num_layers=5, stagger_distance=2, void_density=0.25)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_stacked_forests_model(base_size=(12, 12), layer_height=5, num_layers=4, stagger_distance=1, void_density=0.15)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_stacked_forests_model(base_size=(20, 10), layer_height=3.5, num_layers=7, stagger_distance=2.0, void_density=0.3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_stacked_forests_model(base_size=(8, 10), layer_height=2, num_layers=8, stagger_distance=1, void_density=0.1)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_stacked_forests_model(base_size=(14, 14), layer_height=6, num_layers=10, stagger_distance=1.0, void_density=0.2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
