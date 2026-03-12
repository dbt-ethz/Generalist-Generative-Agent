# Created for 0012_0005_twisted_volumes.json

""" Summary:
The function `create_twisted_volumes_model` generates an architectural concept model inspired by the metaphor of "Twisted volumes." By creating interwoven and contorted geometric shapes, the function embodies fluidity and tension, resulting in dynamic silhouettes that evoke motion. It constructs multiple layers of twisted forms, manipulating height and twist angles to redefine spatial relationships and circulation paths. The resulting models emphasize light and shadow interactions, enhancing visual connections between interior and exterior spaces. This approach ensures that the architectural design aligns with the metaphor, creating unique spatial experiences that reflect continual transformation and energy."""

#! python 3
function_code = """def create_twisted_volumes_model(base_radius=5, height=10, twist_angle=30, num_layers=5):
    \"""
    Creates an architectural Concept Model based on the 'Twisted volumes' metaphor.
    
    This function generates a series of entwined and contorted geometric forms that embody fluidity and tension,
    leading to dynamic and expressive silhouettes. The design captures the transformative essence of the twisting action 
    and explores innovative spatial experiences and circulation paths.

    Parameters:
    - base_radius: The radius of the base circle for the twisted forms (in meters).
    - height: The height of each twisted volume (in meters).
    - twist_angle: The angle of twist applied to each layer (in degrees).
    - num_layers: The number of twisted layers to be generated.

    Returns:
    - A list of RhinoCommon Brep objects representing the 3D geometry of the twisted volumes.
    \"""
    import Rhino.Geometry as rg
    import math

    breps = []

    # Compute the angle increment for each twist
    angle_increment = math.radians(twist_angle / num_layers)

    # Create twisted layers
    for i in range(num_layers):
        # Create a base circle at the current height
        base_circle = rg.Circle(rg.Plane.WorldXY, base_radius)
        base_circle.Transform(rg.Transform.Translation(0, 0, i * height))

        # Create a twisted shape by rotating the base circle around the Z-axis
        twist_transform = rg.Transform.Rotation(angle_increment * i, rg.Vector3d.ZAxis, base_circle.Center)
        twisted_circle = rg.Circle(base_circle.Plane, base_circle.Radius)  # Fix: Specify plane and radius
        twisted_circle.Transform(twist_transform)

        # Loft between the base and twisted circle
        loft = rg.Brep.CreateFromLoft([base_circle.ToNurbsCurve(), twisted_circle.ToNurbsCurve()], rg.Point3d.Unset, rg.Point3d.Unset, rg.LoftType.Normal, False)
        
        if loft:
            breps.append(loft[0])

    return breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_twisted_volumes_model(base_radius=4, height=12, twist_angle=45, num_layers=6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_twisted_volumes_model(base_radius=3, height=15, twist_angle=60, num_layers=8)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_twisted_volumes_model(base_radius=6, height=8, twist_angle=90, num_layers=4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_twisted_volumes_model(base_radius=5, height=20, twist_angle=15, num_layers=10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_twisted_volumes_model(base_radius=7, height=18, twist_angle=75, num_layers=3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
