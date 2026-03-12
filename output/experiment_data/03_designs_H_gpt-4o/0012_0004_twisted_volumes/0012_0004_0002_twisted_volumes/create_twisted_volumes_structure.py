# Created for 0012_0004_twisted_volumes.json

""" Summary:
The function `create_twisted_volumes_structure` generates an architectural concept model based on the metaphor of "Twisted volumes." It creates a series of layered cylindrical shapes, each twisted incrementally to embody dynamic rotation and transformation. Parameters such as base radius, height, and twist angle dictate the model's form and massing, ensuring a multifaceted silhouette that reflects stability and motion. The function also incorporates transparency cutouts, enhancing the interplay of light and shadow, which allows for varied spatial experiences. Ultimately, this approach captures the transformative energy of the metaphor, redefining relationships between form, space, and light."""

#! python 3
function_code = """def create_twisted_volumes_structure(base_radius, height, num_layers, twist_increment, transparency_threshold):
    \"""
    Generates an architectural Concept Model based on the 'Twisted volumes' metaphor, creating layered and twisted cylindrical volumes.
    
    Parameters:
    - base_radius (float): The radius of the base of each cylindrical layer in meters.
    - height (float): The height of each cylindrical layer in meters.
    - num_layers (int): The number of cylindrical layers to generate.
    - twist_increment (float): The incremental angle in degrees to twist each subsequent layer.
    - transparency_threshold (float): The threshold to determine transparency cutouts (0 to 1).

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Breps representing the twisted cylindrical volumes of the Concept Model.
    \"""
    import Rhino
    import Rhino.Geometry as rg
    import math
    from random import seed, random

    # Set seed for reproducibility
    seed(42)
    
    # List to hold the resulting Breps
    breps = []
    
    for i in range(num_layers):
        # Create a cylindrical base
        base_circle = rg.Circle(rg.Plane.WorldXY, base_radius)
        base_cylinder = rg.Cylinder(base_circle, height)
        brep_cylinder = base_cylinder.ToBrep(True, True)

        # Calculate twist angle for the current layer
        twist_angle = math.radians(twist_increment * i)
        
        # Create a twist transformation
        twist_axis = rg.Line(base_circle.Center, rg.Point3d(base_circle.Center.X, base_circle.Center.Y, height))
        twist_transform = rg.Transform.Rotation(twist_angle, twist_axis.Direction, twist_axis.From)
        
        # Apply twist transformation
        brep_cylinder.Transform(twist_transform)

        # Determine transparency cutout
        if random() < transparency_threshold:
            # Perform a simple cutout by scaling down the cylinder
            scale_transform = rg.Transform.Scale(rg.Plane.WorldXY, 0.8, 0.8, 0.8)
            brep_cylinder.Transform(scale_transform)

        # Add the twisted brep to the result list
        breps.append(brep_cylinder)

    return breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_twisted_volumes_structure(2.0, 5.0, 10, 15, 0.3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_twisted_volumes_structure(1.5, 4.0, 8, 10, 0.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_twisted_volumes_structure(3.0, 6.0, 12, 20, 0.2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_twisted_volumes_structure(2.5, 3.0, 15, 25, 0.4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_twisted_volumes_structure(1.0, 7.0, 5, 30, 0.1)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
