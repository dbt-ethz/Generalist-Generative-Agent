# Created for 0006_0001_box_in_a_cloud.json

""" Summary:
The provided function, `create_box_in_cloud_massing`, generates an architectural concept model based on the "Box in a cloud" metaphor by constructing a solid geometric core (the "box") and surrounding it with multiple ethereal layers (the "cloud"). The function takes parameters for the dimensions of the box, the thickness and variance of the cloud layers, and the number of layers. It creates a defined box shape using solid materials and then adds layers of perturbed, translucent shapes around it to suggest lightness and movement. This interplay emphasizes the contrast between solidity and ethereality, embodying the metaphor's essence."""

#! python 3
function_code = """def create_box_in_cloud_massing(box_dims, cloud_thickness, cloud_variance, cloud_layers, seed=42):
    \"""
    Creates an architectural Concept Model based on the 'Box in a cloud' metaphor.
    
    This function constructs a central, geometric form (the 'box') and surrounds it with layered 'cloud' forms.
    The 'box' represents the primary programmatic space with defined geometry, while the 'cloud' layers 
    represent transitional spaces, creating a sense of lightness and movement.

    Parameters:
    - box_dims (tuple): Dimensions of the box (width, depth, height) in meters.
    - cloud_thickness (float): The thickness of each cloud layer in meters.
    - cloud_variance (float): Degree of randomness applied to the cloud layers for ethereal qualities.
    - cloud_layers (int): Number of cloud layers to create around the box.
    - seed (int): Random seed for reproducibility.

    Returns:
    - list: A list of Rhino.Geometry Brep objects representing the 3D geometries of the concept model.
    \"""
    import Rhino.Geometry as rg
    import random
    
    # Set the random seed for reproducibility
    random.seed(seed)

    # Unpack box dimensions
    box_width, box_depth, box_height = box_dims
    
    # Create the central 'box'
    box_corners = [
        rg.Point3d(0, 0, 0),
        rg.Point3d(box_width, 0, 0),
        rg.Point3d(box_width, box_depth, 0),
        rg.Point3d(0, box_depth, 0),
        rg.Point3d(0, 0, box_height),
        rg.Point3d(box_width, 0, box_height),
        rg.Point3d(box_width, box_depth, box_height),
        rg.Point3d(0, box_depth, box_height)
    ]
    box_brep = rg.Brep.CreateFromBox(box_corners)

    # Create the surrounding 'cloud' layers
    cloud_breps = []
    for i in range(cloud_layers):
        layer_offset = (i + 1) * cloud_thickness
        cloud_corners = [
            rg.Point3d(-layer_offset, -layer_offset, -layer_offset),
            rg.Point3d(box_width + layer_offset, -layer_offset, -layer_offset),
            rg.Point3d(box_width + layer_offset, box_depth + layer_offset, -layer_offset),
            rg.Point3d(-layer_offset, box_depth + layer_offset, -layer_offset),
            rg.Point3d(-layer_offset, -layer_offset, box_height + layer_offset),
            rg.Point3d(box_width + layer_offset, -layer_offset, box_height + layer_offset),
            rg.Point3d(box_width + layer_offset, box_depth + layer_offset, box_height + layer_offset),
            rg.Point3d(-layer_offset, box_depth + layer_offset, box_height + layer_offset)
        ]
        
        # Introduce randomness in cloud layer
        perturbed_corners = [
            rg.Point3d(
                pt.X + random.uniform(-cloud_variance, cloud_variance),
                pt.Y + random.uniform(-cloud_variance, cloud_variance),
                pt.Z + random.uniform(-cloud_variance, cloud_variance)
            ) for pt in cloud_corners
        ]
        
        cloud_brep = rg.Brep.CreateFromBox(perturbed_corners)
        cloud_breps.append(cloud_brep)

    # Return the box and cloud layers as a list of Breps
    return [box_brep] + cloud_breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_box_in_cloud_massing((10, 5, 3), 0.5, 0.2, 4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_box_in_cloud_massing((8, 6, 4), 0.3, 0.1, 3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_box_in_cloud_massing((12, 7, 5), 0.6, 0.15, 5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_box_in_cloud_massing((15, 10, 8), 0.4, 0.25, 6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_box_in_cloud_massing((9, 4, 2), 0.7, 0.3, 2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
