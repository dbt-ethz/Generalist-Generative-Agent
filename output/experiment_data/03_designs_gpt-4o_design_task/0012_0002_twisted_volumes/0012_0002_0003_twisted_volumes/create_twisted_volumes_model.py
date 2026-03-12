# Created for 0012_0002_twisted_volumes.json

""" Summary:
The function `create_twisted_volumes_model` generates an architectural concept model by creating a series of twisted cylindrical modules that embody the metaphor of "Twisted volumes." Each module is defined by its base radius, height, and a specified twist angle. The function systematically applies a rotation transformation to each cylinder, resulting in a dynamic interplay of forms that reflect fluidity and movement. This twisting action fosters layered spatial relationships, encouraging exploration and enhancing light interactions through varied surfaces. The output is a collection of geometries that illustrate the transformative qualities of the metaphor, encapsulating both form and experiential depth."""

#! python 3
function_code = """def create_twisted_volumes_model(base_radius, height, num_modules, twist_angle):
    \"""
    Generates a series of twisted and interlocking volumes to form an architectural concept model 
    based on the 'Twisted volumes' metaphor. The design emphasizes dynamic forms and spatial interactions.

    Parameters:
    base_radius (float): The base radius of the cylindrical modules in meters.
    height (float): The height of each module in meters.
    num_modules (int): The total number of modules to create, each module represents a twisted volume.
    twist_angle (float): The maximum angle in degrees to twist each module.

    Returns:
    list: A list of RhinoCommon Brep geometries representing the twisted volumes.
    \"""
    import Rhino.Geometry as rg
    import random
    random.seed(42)
    
    geometries = []
    twist_increment = twist_angle / num_modules
    
    for i in range(num_modules):
        # Create base cylinder
        base_circle = rg.Circle(rg.Plane.WorldXY, base_radius)
        cylinder = rg.Cylinder(base_circle, height).ToBrep(True, True)
        
        # Determine twist for current module
        current_twist = twist_increment * (i + 1)
        
        # Create a twisting transformation
        axis_start = rg.Point3d(0, 0, i * height)
        axis_end = rg.Point3d(0, 0, (i + 1) * height)
        twist_axis = rg.Line(axis_start, axis_end)
        
        # Instead of using Twist, use Rotate to create a similar effect
        rotation_transform = rg.Transform.Rotation(current_twist * (3.14159 / 180), twist_axis.Direction, axis_start)
        
        # Apply twisting transformation to the cylinder
        twisted_cylinder = cylinder.Duplicate()
        twisted_cylinder.Transform(rotation_transform)
        
        # Add to the collection of geometries
        geometries.append(twisted_cylinder)
        
    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_twisted_volumes_model(2.0, 5.0, 10, 90)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_twisted_volumes_model(1.5, 4.0, 8, 180)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_twisted_volumes_model(3.0, 6.0, 12, 120)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_twisted_volumes_model(1.0, 3.0, 5, 60)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_twisted_volumes_model(2.5, 7.0, 15, 150)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
