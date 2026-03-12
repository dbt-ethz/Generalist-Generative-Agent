# Created for 0019_0004_subterranean_cavern.json

""" Summary:
The given function `create_cavernous_volume_model` generates an architectural concept model inspired by the metaphor of a subterranean cavern. It creates a series of interconnected, curvilinear volumes that reflect the immersive and layered qualities of a cavern, with varying scales to transition from intimate spaces to larger areas. By employing elliptical and wavy profiles, the design mimics natural forms, while the introduction of openings allows dynamic lighting to enhance the atmosphere of mystery and discovery. This approach encapsulates the essence of exploration and refuge, using organic shapes and natural materials to foster a connection with the earth."""

#! python 3
function_code = """def create_cavernous_volume_model(base_radius, height, layer_count, seed=42):
    \"""
    Generates an architectural concept model embodying the 'subterranean cavern' metaphor.
    
    The model is composed of a series of interconnected, curvilinear volumes that suggest exploration
    and refuge. The design features organic, flowing shapes with varying scales, offering a transition
    from intimate, secluded spaces to larger, open areas. The model also incorporates openings for dynamic
    lighting effects, enhancing the atmosphere of mystery and discovery.

    Parameters:
    - base_radius (float): The initial radius of the largest volume.
    - height (float): The total height of the concept model.
    - layer_count (int): The number of nested volumes to create.
    - seed (int): Random seed to ensure replicable results.

    Returns:
    - List of RhinoCommon Breps: A list of 3D geometries representing the concept model.
    \"""
    import Rhino.Geometry as rg
    import random
    
    random.seed(seed)
    geometries = []
    layer_height = height / layer_count

    for i in range(layer_count):
        # Define the radius and height for current layer
        current_radius = base_radius * (1 - 0.3 * (i / layer_count))
        current_height = layer_height * (1 + random.uniform(-0.1, 0.1))

        # Create an elliptical profile for the cavern volume
        ellipse = rg.Ellipse(rg.Plane.WorldXY, current_radius, current_radius * 0.7)
        ellipse_curve = ellipse.ToNurbsCurve()

        # Create a wavy profile for more organic appearance
        wave_amplitude = current_radius * 0.1
        wave_frequency = 3 + random.randint(-1, 1)
        wave_points = [rg.Point3d(x, wave_amplitude * random.uniform(-1, 1), 0) for x in range(wave_frequency)]
        wave_curve = rg.Curve.CreateInterpolatedCurve(wave_points, 3)
        scale_factor = current_radius / wave_frequency
        wave_curve.Transform(rg.Transform.Scale(rg.Point3d.Origin, scale_factor))

        # Loft the base ellipse with the wave curve to form a volume
        loft_curves = [ellipse_curve, wave_curve]
        loft = rg.Brep.CreateFromLoft(loft_curves, rg.Point3d.Unset, rg.Point3d.Unset, rg.LoftType.Normal, False)
        
        if loft:
            volume = loft[0]
            # Apply height transformation
            volume.Transform(rg.Transform.Translation(0, 0, i * current_height))
            geometries.append(volume)

    # Create openings for light interplay
    for geom in geometries:
        num_openings = random.randint(1, 3)
        for _ in range(num_openings):
            opening_radius = random.uniform(0.1, 0.2) * base_radius
            opening_center = rg.Point3d(
                random.uniform(-base_radius, base_radius),
                random.uniform(-base_radius, base_radius),
                random.uniform(0, height)
            )
            sphere = rg.Brep.CreateFromSphere(rg.Sphere(opening_center, opening_radius))
            if sphere:
                cutter = sphere
                trimmed_breps = geom.Trim(cutter, 0.01)
                if trimmed_breps:
                    geom = trimmed_breps[0]

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_cavernous_volume_model(5.0, 10.0, 7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_cavernous_volume_model(3.5, 12.0, 5, seed=123)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_cavernous_volume_model(4.0, 8.0, 6, seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_cavernous_volume_model(6.0, 15.0, 10, seed=2023)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_cavernous_volume_model(7.0, 20.0, 8, seed=56)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
