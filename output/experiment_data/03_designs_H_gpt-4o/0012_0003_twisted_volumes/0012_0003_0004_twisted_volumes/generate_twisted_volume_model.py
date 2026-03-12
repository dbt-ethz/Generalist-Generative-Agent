# Created for 0012_0003_twisted_volumes.json

""" Summary:
The function `generate_twisted_volume_model` creates an architectural concept model by generating a series of interconnected volumetric elements that embody the 'Twisted volumes' metaphor. It employs parameters such as base radius, volume height, twist factor, and the number of elements to produce dynamic forms characterized by rotation and distortion. By manipulating curves through a series of twists, the model reflects fluidity and spatial innovation, fostering unexpected relationships and enhancing movement. The resulting 3D geometries capture light and shadow dramatically, reinforcing the sense of transformation and interaction between interior and exterior spaces, thus effectively translating the metaphor into a tangible design."""

#! python 3
function_code = """def generate_twisted_volume_model(base_radius, volume_height, twist_factor, num_elements, seed=42):
    \"""
    Creates a dynamic architectural Concept Model inspired by the 'Twisted volumes' metaphor. This function generates
    a composition of volumetric elements that exhibit varying degrees of twist and distortion, emphasizing movement and spatial fluidity.

    Parameters:
    - base_radius (float): The base radius of the circular segments that form each volumetric element in meters.
    - volume_height (float): The height of each volumetric element in meters.
    - twist_factor (float): A factor determining the degree of twist applied to the elements.
    - num_elements (int): The number of volumetric elements to generate.
    - seed (int): Optional seed for randomness to ensure replicability.

    Returns:
    - List of RhinoCommon.Geometry.Brep: A list of 3D geometries representing the twisted volumes.
    \"""
    import Rhino.Geometry as rg
    import random
    import math
    random.seed(seed)

    elements = []

    for i in range(num_elements):
        # Create a base circle for the volume
        base_circle = rg.Circle(rg.Plane.WorldXY, base_radius)

        # Generate the series of twisted curves
        twisted_curves = []
        num_segments = 10
        for j in range(num_segments + 1):
            t = j / num_segments
            z = t * volume_height
            rotation_angle = twist_factor * t * math.pi * 2  # Full twist factor over the height

            # Create a plane for each segment and apply twist
            segment_plane = rg.Plane.WorldXY
            segment_plane.Translate(rg.Vector3d(0, 0, z))
            segment_plane.Rotate(rotation_angle, segment_plane.ZAxis)

            # Create a circle at each segment
            twisted_circle = rg.Circle(segment_plane, base_radius * (1 + 0.1 * math.sin(j * math.pi / num_segments)))
            twisted_curves.append(twisted_circle.ToNurbsCurve())

        # Loft the twisted curves to form the volumetric element
        loft_brep = rg.Brep.CreateFromLoft(twisted_curves, rg.Point3d.Unset, rg.Point3d.Unset, rg.LoftType.Normal, False)[0]
        elements.append(loft_brep)

        # Translate each element to avoid overlap
        translation_vector = rg.Vector3d(i * base_radius * 2.5, 0, 0)
        translation_transform = rg.Transform.Translation(translation_vector)
        loft_brep.Transform(translation_transform)

    return elements"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = generate_twisted_volume_model(1.0, 2.0, 0.5, 5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = generate_twisted_volume_model(0.5, 3.0, 1.0, 10, seed=100)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = generate_twisted_volume_model(2.0, 4.0, 0.75, 8)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = generate_twisted_volume_model(1.5, 1.5, 0.3, 6, seed=24)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = generate_twisted_volume_model(1.2, 3.5, 0.6, 7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
