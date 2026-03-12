# Created for 0012_0005_twisted_volumes.json

""" Summary:
The function `create_twisted_volume_pyramid` generates an architectural concept model by embodying the "Twisted volumes" metaphor through a stepped pyramid structure. Each level of the pyramid is progressively twisted and contorted, creating dynamic geometric forms that evoke fluidity, tension, and movement. The function allows for varying base sizes, heights, twist angles, and levels, facilitating diverse spatial experiences and circulation paths. By manipulating the geometry, the model emphasizes the interplay of light and shadow, enhancing visual connections between the interior and exterior. Ultimately, the generated forms reflect the transformative essence of the metaphor in their design."""

#! python 3
function_code = """def create_twisted_volume_pyramid(base_size=10, height=15, twist_angle=45, levels=6):
    \"""
    Creates an architectural Concept Model based on the "Twisted volumes" metaphor.

    This function generates a stepped pyramid structure with each level twisted,
    creating a dynamic and fluid form that embodies tension and fluidity.

    Parameters:
    - base_size: The size of the base square of the pyramid in meters.
    - height: The total height of the pyramid in meters.
    - twist_angle: The total twist angle in degrees applied from base to top.
    - levels: The number of stepped levels in the pyramid.

    Returns:
    - A list of RhinoCommon Brep objects representing the 3D geometries of the twisted pyramid.
    \"""
    import Rhino.Geometry as rg
    import math

    geometries = []
    level_height = height / levels
    twist_per_level = math.radians(twist_angle) / levels
    base_half_size = base_size / 2

    for i in range(levels):
        # Calculate the current level's size reduction and twist
        size_factor = 1 - (i / levels)
        current_size = base_size * size_factor
        current_twist = twist_per_level * i

        # Create a square base for the current level
        base_corners = [
            rg.Point3d(-current_size/2, -current_size/2, i * level_height),
            rg.Point3d(current_size/2, -current_size/2, i * level_height),
            rg.Point3d(current_size/2, current_size/2, i * level_height),
            rg.Point3d(-current_size/2, current_size/2, i * level_height)
        ]
        base_polygon = rg.Polyline(base_corners + [base_corners[0]]).ToNurbsCurve()

        # Create a top square for the current level
        top_corners = [
            rg.Point3d(-current_size/2, -current_size/2, (i + 1) * level_height),
            rg.Point3d(current_size/2, -current_size/2, (i + 1) * level_height),
            rg.Point3d(current_size/2, current_size/2, (i + 1) * level_height),
            rg.Point3d(-current_size/2, current_size/2, (i + 1) * level_height)
        ]
        top_polygon = rg.Polyline(top_corners + [top_corners[0]]).ToNurbsCurve()

        # Apply twist to the top polygon
        twist_transform = rg.Transform.Rotation(current_twist, rg.Vector3d.ZAxis, rg.Point3d(0, 0, (i + 1) * level_height))
        top_polygon.Transform(twist_transform)

        # Loft between the base and top polygons
        loft = rg.Brep.CreateFromLoft([base_polygon, top_polygon], rg.Point3d.Unset, rg.Point3d.Unset, rg.LoftType.Normal, False)
        if loft:
            geometries.append(loft[0])

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_twisted_volume_pyramid(base_size=20, height=30, twist_angle=90, levels=8)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_twisted_volume_pyramid(base_size=15, height=25, twist_angle=60, levels=5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_twisted_volume_pyramid(base_size=25, height=40, twist_angle=120, levels=10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_twisted_volume_pyramid(base_size=18, height=20, twist_angle=75, levels=7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_twisted_volume_pyramid(base_size=12, height=18, twist_angle=30, levels=4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
