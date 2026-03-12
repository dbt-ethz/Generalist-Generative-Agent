# Created for 0012_0005_twisted_volumes.json

""" Summary:
The function `create_twisted_volumes_model` generates an architectural concept model inspired by the metaphor "Twisted volumes." It constructs a series of entwined geometric forms by extruding a base circle into vertical strips, applying a defined twist angle to each strip. This process creates a dynamic, fluid silhouette that embodies tension and movement, enhancing spatial relationships and circulation within the structure. The model captures the transformative essence of the metaphor, allowing light and shadow to interact uniquely across surfaces. By manipulating geometric shapes, the function effectively translates the metaphor into an expressive architectural form."""

#! python 3
function_code = """def create_twisted_volumes_model(base_radius=5, height=10, twist_angle=45, num_strips=8, strip_height=1):
    \"""
    Creates an architectural Concept Model based on the 'Twisted volumes' metaphor.
    
    This function generates a series of entwined and contorted geometric forms that embody fluidity and tension,
    leading to dynamic and expressive silhouettes. The design captures the transformative essence of the twisting action 
    and explores innovative spatial experiences and circulation paths.

    Parameters:
    - base_radius: The radius of the base circle for the twisted forms (in meters).
    - height: The total height of the model (in meters).
    - twist_angle: The total twist angle in degrees applied to the strips.
    - num_strips: The number of vertical strips or sections that make up the model.
    - strip_height: The height of each strip (in meters).

    Returns:
    - A list of RhinoCommon Brep objects representing the 3D geometry of the twisted volumes.
    \"""
    import Rhino.Geometry as rg
    import math

    geometries = []
    total_twist_radians = math.radians(twist_angle)
    twist_per_strip = total_twist_radians / num_strips

    for i in range(num_strips):
        # Create a vertical strip by extruding a base circle
        base_circle = rg.Circle(rg.Plane.WorldXY, base_radius)
        strip = rg.Extrusion.Create(base_circle.ToNurbsCurve(), strip_height, True)

        # Calculate the current twist
        current_twist = twist_per_strip * (i + 1)

        # Create a rotation transform for the current strip
        rotation_transform = rg.Transform.Rotation(current_twist, rg.Vector3d.ZAxis, rg.Point3d(0, 0, strip_height * i))

        # Apply transformation to the strip
        strip.Transform(rotation_transform)

        # Translate strip to the correct height position
        translation_transform = rg.Transform.Translation(0, 0, strip_height * i)
        strip.Transform(translation_transform)

        # Add the transformed strip to the geometries list
        geometries.append(strip.ToBrep())

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_twisted_volumes_model(base_radius=6, height=12, twist_angle=90, num_strips=10, strip_height=1.2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_twisted_volumes_model(base_radius=4, height=15, twist_angle=60, num_strips=6, strip_height=2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_twisted_volumes_model(base_radius=7, height=8, twist_angle=30, num_strips=12, strip_height=0.8)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_twisted_volumes_model(base_radius=5, height=20, twist_angle=120, num_strips=14, strip_height=1.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_twisted_volumes_model(base_radius=3, height=18, twist_angle=75, num_strips=5, strip_height=3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
