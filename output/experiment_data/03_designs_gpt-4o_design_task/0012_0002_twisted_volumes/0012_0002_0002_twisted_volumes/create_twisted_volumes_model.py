# Created for 0012_0002_twisted_volumes.json

""" Summary:
The function `create_twisted_volumes_model` generates an architectural concept model based on the metaphor of "Twisted volumes" by creating interlocking cylindrical modules that twist as they rise. Each module is constructed by segmenting the cylindrical form and applying a rotational transformation at each segment, producing a dynamic, spiraling effect. This process not only evokes movement and tension but also fosters innovative spatial relationships through overlapping and intersecting spaces. The model's design captures the fluidity and transformation associated with the metaphor, enhancing light play through varied surfaces while promoting a unique exploration of the architectural space."""

#! python 3
function_code = """def create_twisted_volumes_model(base_radius, height, num_segments, twist_angle, module_count):
    \"""
    Creates an architectural Concept Model based on the 'Twisted volumes' metaphor by constructing 
    a series of interlocking twisted modules. The function generates a dynamic form with a sense of 
    movement and tension, exploring spatial relationships through twisting and layering.

    Parameters:
    - base_radius (float): The base radius of the cylindrical modules.
    - height (float): The height of each module.
    - num_segments (int): The number of segments per module to control the smoothness of the twist.
    - twist_angle (float): The total twist angle (in degrees) applied to each module.
    - module_count (int): The number of modules to be stacked and twisted.

    Returns:
    - List of Breps: A list of 3D geometries (Breps) representing the twisted volumes.
    \"""
    import Rhino.Geometry as rg
    import math

    # Initialize the list to store the twisted geometries
    twisted_modules = []

    # Calculate the angle increment for each segment
    angle_increment = math.radians(twist_angle) / num_segments

    # Create each twisted module
    for i in range(module_count):
        # Create base circle for the module
        base_circle = rg.Circle(rg.Plane.WorldXY, base_radius)
        
        # Create a cylindrical surface from the base circle
        cylinder = rg.Cylinder(base_circle, height).ToBrep(True, True)

        # Create a twisted version of the cylinder
        twisted_brep = cylinder.DuplicateBrep()
        
        # Apply twisting by rotating each segment
        for j in range(num_segments + 1):
            # Calculate the angle for the current segment
            current_angle = j * angle_increment
            
            # Calculate the transformation from the base to the current segment
            z_translation = height / num_segments * j
            translation = rg.Transform.Translation(0, 0, z_translation)
            rotation = rg.Transform.Rotation(current_angle, rg.Vector3d.ZAxis, rg.Point3d(0, 0, z_translation))
            
            # Apply the transformations
            transform = translation * rotation
            twisted_brep.Transform(transform)
        
        # Offset each module vertically and add to the list
        module_offset = rg.Transform.Translation(0, 0, i * height)
        twisted_brep.Transform(module_offset)
        twisted_modules.append(twisted_brep)
    
    return twisted_modules"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_twisted_volumes_model(5.0, 10.0, 20, 180, 3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_twisted_volumes_model(7.5, 15.0, 30, 90, 5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_twisted_volumes_model(4.0, 8.0, 15, 360, 4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_twisted_volumes_model(6.0, 12.0, 25, 270, 6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_twisted_volumes_model(3.0, 6.0, 10, 120, 2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
