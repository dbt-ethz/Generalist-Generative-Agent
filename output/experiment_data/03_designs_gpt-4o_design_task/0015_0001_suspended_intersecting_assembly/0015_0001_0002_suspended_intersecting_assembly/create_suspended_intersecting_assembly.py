# Created for 0015_0001_suspended_intersecting_assembly.json

""" Summary:
The provided function generates an architectural concept model based on the metaphor of "Suspended intersecting assembly." It creates a series of elevated, intersecting planes that symbolize lightness and fluidity. By defining multiple layers at varying heights and randomly positioning planes within these layers, the function promotes dynamic spatial relationships. Each planes dimensions and angles are randomized to enhance the complexity of the design, reflecting the interconnectedness and balance suggested by the metaphor. The resulting geometries, represented as 3D models, embody a delicate network that visually conveys the concept of suspension and movement, aligning with the design task's requirements."""

#! python 3
function_code = """def create_suspended_intersecting_assembly(base_length, base_width, height, num_layers, seed=42):
    \"""
    Creates an architectural Concept Model embodying the 'Suspended intersecting assembly' metaphor using lightweight,
    intersecting elements. The design features elevated components that appear to float and intersect within the space,
    promoting visual interconnectivity and structural transparency.

    Parameters:
    - base_length (float): The length of the base area of the conceptual model in meters.
    - base_width (float): The width of the base area of the conceptual model in meters.
    - height (float): The total height of the conceptual model in meters.
    - num_layers (int): The number of layers or levels of intersecting elements in the model.
    - seed (int, optional): Seed for random number generation to ensure replicability. Default is 42.

    Returns:
    - List of RhinoCommon Brep: A list of 3D geometries representing the concept model.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    random.seed(seed)
    geometries = []

    # Define base plane
    base_plane = rg.Plane.WorldXY

    # Create layers of intersecting planes
    for layer in range(num_layers):
        # Determine the z position of this layer
        z_pos = (layer + 0.5) * (height / num_layers)
        
        # Create a plane at this height
        layer_plane = rg.Plane(base_plane)
        layer_plane.Translate(rg.Vector3d(0, 0, z_pos))

        # Define number of planes in this layer
        num_planes = random.randint(3, 6)

        for _ in range(num_planes):
            # Randomly determine the angle and length of the intersecting plane
            angle = random.uniform(0, 180)
            plane_length = random.uniform(base_length / 4, base_length / 2)
            plane_width = random.uniform(base_width / 4, base_width / 2)

            # Create a rectangle representing the plane
            rect_corners = [
                rg.Point3d(-plane_length / 2, -plane_width / 2, 0),
                rg.Point3d(plane_length / 2, -plane_width / 2, 0),
                rg.Point3d(plane_length / 2, plane_width / 2, 0),
                rg.Point3d(-plane_length / 2, plane_width / 2, 0),
                rg.Point3d(-plane_length / 2, -plane_width / 2, 0)  # Close the polyline
            ]

            rect = rg.Polyline(rect_corners)

            # Create a surface from the rectangle
            surface = rg.Brep.CreatePlanarBreps([rect.ToNurbsCurve()])[0]

            # Rotate the surface around the z-axis
            surface.Rotate(math.radians(angle), layer_plane.ZAxis, layer_plane.Origin)

            # Translate the surface to the current layer's height
            move_vector = rg.Vector3d(0, 0, z_pos)
            surface.Translate(move_vector)

            # Add the surface to the list of geometries
            geometries.append(surface)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_suspended_intersecting_assembly(10.0, 5.0, 15.0, 4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_suspended_intersecting_assembly(12.0, 6.0, 20.0, 3, seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_suspended_intersecting_assembly(8.0, 4.0, 10.0, 5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_suspended_intersecting_assembly(15.0, 10.0, 25.0, 6, seed=7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_suspended_intersecting_assembly(5.0, 3.0, 12.0, 2, seed=21)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
