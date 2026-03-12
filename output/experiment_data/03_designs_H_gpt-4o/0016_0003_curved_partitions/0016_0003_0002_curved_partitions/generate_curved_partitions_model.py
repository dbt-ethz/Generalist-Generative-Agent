# Created for 0016_0003_curved_partitions.json

""" Summary:
The function `generate_curved_partitions_model` creates an architectural concept model inspired by the metaphor of "curved partitions." By generating a series of interconnected curvilinear elements, it embodies both division and continuity, reflecting organic movement and fluidity. The function uses parameters like `curve_count`, `base_radius`, and `wave_intensity` to define the partitions' shapes and arrangements. Employing random wave-like undulations, it enhances the spatial narrative, guiding movement through gentle transitions. The resulting 3D geometries evoke a dynamic interplay of light and shadow, fostering exploration and creating intimate zones within an elegant, flowing design aligned with the metaphor."""

#! python 3
function_code = """def generate_curved_partitions_model(curve_count=6, base_radius=12, partition_height=4, wave_intensity=0.3, seed=42):
    \"""
    Generates an architectural Concept Model inspired by the 'curved partitions' metaphor.

    This function creates a series of interconnected curvilinear partitions that embody both division and continuity.
    The design uses rhythmic curves to define spaces, enhancing the experiential quality through the interplay of
    light, shadow, and organic movement.

    Parameters:
    - curve_count (int): The number of curved partitions to generate.
    - base_radius (float): The base radius around which the partitions are arranged.
    - partition_height (float): The height of each partition.
    - wave_intensity (float): Intensity of the undulating wave applied to the partitions.
    - seed (int): Seed for randomness to ensure replicability.

    Returns:
    - List of Breps: A list of 3D Brep geometries representing the curved partitions.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    random.seed(seed)
    partitions = []
    angle_step = 2 * math.pi / curve_count

    for i in range(curve_count):
        angle = i * angle_step
        center = rg.Point3d(base_radius * math.cos(angle), base_radius * math.sin(angle), 0)

        # Generate control points with a wave-like undulation
        control_points = []
        wave_amplitude = random.uniform(0.1, wave_intensity)
        for j in range(5):
            x = center.X + random.uniform(-wave_amplitude, wave_amplitude)
            y = center.Y + wave_amplitude * math.sin(j * math.pi / 2)
            z = j * partition_height / 4
            control_points.append(rg.Point3d(x, y, z))

        nurbs_curve = rg.NurbsCurve.Create(False, 3, control_points)

        # Offset the curve to create thickness
        offset_curve = nurbs_curve.Offset(rg.Plane.WorldXY, 0.2, 0.01, rg.CurveOffsetCornerStyle.Smooth)[0]

        # Loft between original and offset curves
        loft = rg.Brep.CreateFromLoft([nurbs_curve, offset_curve], rg.Point3d.Unset, rg.Point3d.Unset, rg.LoftType.Normal, False)
        
        if loft:
            # Cap the lofted surface to form a closed Brep
            brep = loft[0].CapPlanarHoles(0.01)
            if brep:
                partitions.append(brep)

    return partitions"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = generate_curved_partitions_model(curve_count=8, base_radius=10, partition_height=5, wave_intensity=0.5, seed=123)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = generate_curved_partitions_model(curve_count=10, base_radius=15, partition_height=6, wave_intensity=0.4, seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = generate_curved_partitions_model(curve_count=5, base_radius=20, partition_height=3, wave_intensity=0.2, seed=56)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = generate_curved_partitions_model(curve_count=7, base_radius=18, partition_height=4.5, wave_intensity=0.6, seed=77)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = generate_curved_partitions_model(curve_count=9, base_radius=14, partition_height=7, wave_intensity=0.1, seed=45)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
