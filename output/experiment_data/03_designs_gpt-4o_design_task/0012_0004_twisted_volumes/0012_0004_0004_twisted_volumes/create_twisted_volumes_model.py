# Created for 0012_0004_twisted_volumes.json

""" Summary:
The function `create_twisted_volumes_model` generates an architectural concept model based on the metaphor of "Twisted volumes." It constructs a series of overlapping, twisted volumes by defining parameters such as base dimensions and twist angles. Each volume is created from a rectangular box that undergoes a rotation transformation, simulating dynamic motion and complexity. The incorporation of transparency cutouts enhances the interplay of light and shadow, aligning with the metaphor's emphasis on spatial fluidity and connection between interior and exterior spaces. The resulting model embodies a balance of stability and movement, capturing the transformative essence of the metaphor through geometry."""

#! python 3
function_code = """def create_twisted_volumes_model(base_length=10, base_width=8, height=15, twist_angle=30, volume_count=3, transparency_factor=0.2):
    \"""
    Creates an architectural Concept Model based on the 'Twisted volumes' metaphor. 
    The model consists of intersecting and overlapping twisted volumes, simulating dynamic and fluid forms.

    Parameters:
    - base_length (float): The base length of each volume.
    - base_width (float): The base width of each volume.
    - height (float): The height of each volume.
    - twist_angle (float): The angle of twist applied to each volume.
    - volume_count (int): The number of overlapping volumes to generate.
    - transparency_factor (float): Factor for transparency cutouts, between 0 and 1.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of brep geometries representing the twisted volumes.
    \"""
    import Rhino
    import System
    from Rhino.Geometry import Box, Point3d, Vector3d, Plane, Brep, Transform, NurbsSurface, Interval
    from System import Random

    random_gen = Random(42)  # Seed for reproducibility
    volumes = []

    for i in range(volume_count):
        # Define base plane for the box
        base_plane = Plane(Point3d(0, 0, i * (height / 2)), Vector3d.ZAxis)
        # Create a box as the starting volume
        x_interval = Interval(0, base_length)
        y_interval = Interval(0, base_width)
        z_interval = Interval(0, height)
        box = Box(base_plane, x_interval, y_interval, z_interval)
        brep = box.ToBrep()

        # Calculate the twist transformation
        twist_transform = Transform.Rotation(
            System.Math.PI / 180 * twist_angle * (random_gen.NextDouble() - 0.5),  # Randomize slight twist
            base_plane.Origin,
            Vector3d.ZAxis
        )
        brep.Transform(twist_transform)

        # Create transparency cutouts
        if transparency_factor > 0:
            cutout_points = [
                Point3d(0, 0, 0), 
                Point3d(base_length * transparency_factor, 0, 0),
                Point3d(0, base_width * transparency_factor, 0), 
                Point3d(base_length * transparency_factor, base_width * transparency_factor, 0)
            ]
            cutout_surface = NurbsSurface.CreateFromPoints(
                cutout_points,
                2, 2, 2, 2
            )
            cutout_brep = Brep.CreateFromSurface(cutout_surface)
            boolean_diff = Brep.CreateBooleanDifference(brep, cutout_brep, 0.01)
            if boolean_diff:
                brep = boolean_diff[0]

        volumes.append(brep)

    return volumes"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_twisted_volumes_model(base_length=12, base_width=10, height=20, twist_angle=45, volume_count=5, transparency_factor=0.3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_twisted_volumes_model(base_length=15, base_width=12, height=10, twist_angle=60, volume_count=4, transparency_factor=0.1)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_twisted_volumes_model(base_length=9, base_width=7, height=18, twist_angle=25, volume_count=6, transparency_factor=0.4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_twisted_volumes_model(base_length=14, base_width=10, height=25, twist_angle=15, volume_count=2, transparency_factor=0.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_twisted_volumes_model(base_length=11, base_width=9, height=22, twist_angle=35, volume_count=3, transparency_factor=0.2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
