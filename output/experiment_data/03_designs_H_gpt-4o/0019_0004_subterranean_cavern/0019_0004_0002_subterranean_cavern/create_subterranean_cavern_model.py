# Created for 0019_0004_subterranean_cavern.json

""" Summary:
The provided function generates an architectural concept model inspired by the metaphor of a "subterranean cavern." It creates a series of nested, curvilinear volumes that simulate geological layers, emphasizing immersive spatial experiences. By varying the inner and outer radii and introducing random height adjustments, the function achieves depth and complexity. Small openings are incorporated to enhance light and shadow dynamics, aligning with the metaphor of exploration and discovery. The use of natural materials and organic shapes further reinforces the connection to a secluded environment, capturing the essence of refuge and the unfolding of hidden spaces within the architectural design."""

#! python 3
function_code = """def create_subterranean_cavern_model(inner_radius, outer_radius, height, num_volumes, seed=42):
    \"""
    Generates an architectural concept model inspired by a 'subterranean cavern' using layered curvilinear forms.
    The design emphasizes transitions between nested spaces and explores light and shadow dynamics through varied
    translucency and openings.

    Parameters:
    - inner_radius (float): The radius of the innermost volume in meters.
    - outer_radius (float): The radius of the outermost volume in meters.
    - height (float): The total height of the model in meters.
    - num_volumes (int): The number of nested volumes to create.
    - seed (int): Seed for random number generation for replicable results.

    Returns:
    - List of RhinoCommon Brep objects representing the 3D geometries of the concept model.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    random.seed(seed)

    geometries = []
    volume_height = height / num_volumes

    for i in range(num_volumes):
        # Calculate the radius and height for each volume
        t = i / (num_volumes - 1)
        current_radius = inner_radius * (1 - t) + outer_radius * t
        current_height = volume_height * (1 + random.uniform(-0.1, 0.1))

        # Create a curvilinear volume using a series of arcs and lofting
        arc1 = rg.Arc(rg.Circle(rg.Plane.WorldXY, current_radius), math.pi).ToNurbsCurve()
        arc2 = rg.Arc(rg.Circle(rg.Plane(rg.Point3d(0, 0, current_height), rg.Vector3d.ZAxis), current_radius * 0.9), math.pi).ToNurbsCurve()

        loft = rg.Brep.CreateFromLoft([arc1, arc2], rg.Point3d.Unset, rg.Point3d.Unset, rg.LoftType.Normal, False)
        if loft:
            geometries.append(loft[0])

        # Add small openings for light and shadow play
        num_openings = random.randint(2, 5)
        for _ in range(num_openings):
            opening_radius = random.uniform(0.05, 0.1) * current_radius
            opening_center = rg.Point3d(random.uniform(-current_radius, current_radius), random.uniform(-current_radius, current_radius), random.uniform(0, current_height))
            sphere = rg.Brep.CreateFromSphere(rg.Sphere(opening_center, opening_radius))
            if sphere:
                cutter = sphere
                trimmed_breps = loft[0].Trim(cutter, 0.01)
                if trimmed_breps:
                    geometries[-1] = trimmed_breps[0]

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_subterranean_cavern_model(5.0, 10.0, 15.0, 8)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_subterranean_cavern_model(3.0, 7.0, 12.0, 5, seed=21)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_subterranean_cavern_model(4.0, 9.0, 20.0, 6, seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_subterranean_cavern_model(6.0, 12.0, 18.0, 10, seed=55)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_subterranean_cavern_model(2.5, 6.5, 10.0, 4, seed=30)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
