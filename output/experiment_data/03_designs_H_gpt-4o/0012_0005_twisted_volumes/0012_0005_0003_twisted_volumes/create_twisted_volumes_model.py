# Created for 0012_0005_twisted_volumes.json

""" Summary:
The provided function, `create_twisted_volumes_model`, generates an architectural concept model by translating the metaphor of "Twisted volumes" into 3D geometric forms. It constructs a series of interwoven, contorted shapes that embody fluidity and tension, reflecting dynamic movement. By adjusting parameters like base radius, height, twist angle, and the number of layers, the function creates layered, twisted volumes that enhance unique spatial experiences and innovative circulation paths. The lofted surfaces capture light and shadow interactions, resulting in a visually engaging structure that embodies the essence of transformation, aligning with the metaphors implications for architectural design."""

#! python 3
function_code = """def create_twisted_volumes_model(base_radius=4, height=12, twist_angle=45, num_layers=6):
    \"""
    Creates an architectural Concept Model based on the 'Twisted volumes' metaphor.

    This function generates a series of entwined and contorted geometric forms that embody fluidity and tension,
    leading to dynamic and expressive silhouettes. The design captures the transformative essence of the twisting action
    and explores innovative spatial experiences and circulation paths.

    Parameters:
    - base_radius: The radius of the base circle for the twisted forms (in meters).
    - height: The height of each twisted volume (in meters).
    - twist_angle: The total twist angle applied to the entire structure (in degrees).
    - num_layers: The number of twisted layers to be generated.

    Returns:
    - A list of RhinoCommon Brep objects representing the 3D geometry of the twisted volumes.
    \"""
    import Rhino.Geometry as rg
    import math

    breps = []
    layer_height = height / num_layers
    twist_per_layer = math.radians(twist_angle) / num_layers

    for i in range(num_layers):
        # Create a base circle at the current height
        base_circle = rg.Circle(rg.Plane.WorldXY, base_radius)
        base_circle.Transform(rg.Transform.Translation(0, 0, i * layer_height))

        # Define the upper circle with a twist
        top_circle = rg.Circle(rg.Plane.WorldXY, base_radius)
        top_circle.Transform(rg.Transform.Translation(0, 0, (i + 1) * layer_height))
        top_circle.Transform(rg.Transform.Rotation((i + 1) * twist_per_layer, rg.Vector3d.ZAxis, top_circle.Center))

        # Loft between the base and top circles
        loft = rg.Brep.CreateFromLoft([base_circle.ToNurbsCurve(), top_circle.ToNurbsCurve()], 
                                       rg.Point3d.Unset, rg.Point3d.Unset, rg.LoftType.Normal, False)
        if loft:
            breps.append(loft[0])

    return breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_twisted_volumes_model(base_radius=5, height=15, twist_angle=60, num_layers=8)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_twisted_volumes_model(base_radius=3, height=10, twist_angle=90, num_layers=4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_twisted_volumes_model(base_radius=6, height=20, twist_angle=30, num_layers=10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_twisted_volumes_model(base_radius=4, height=8, twist_angle=75, num_layers=5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_twisted_volumes_model(base_radius=7, height=18, twist_angle=120, num_layers=12)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
