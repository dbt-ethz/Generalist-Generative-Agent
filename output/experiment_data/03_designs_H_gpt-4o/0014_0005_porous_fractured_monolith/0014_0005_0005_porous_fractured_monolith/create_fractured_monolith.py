# Created for 0014_0005_porous_fractured_monolith.json

""" Summary:
The provided function `create_fractured_monolith` generates an architectural concept model based on the metaphor "Porous fractured monolith." It begins by creating a solid rectangular base to represent the monolithic form. The function then introduces spherical voids of varying sizes, which symbolize the permeability and dynamic nature of the design. Additionally, it applies random fractures to the base, enhancing the model's complexity and movement. The resulting structure showcases a balance between solidity and openness, with voids fostering connectivity and exploration embodying the essence of the metaphor. Overall, it translates abstract concepts into a tangible architectural form."""

#! python 3
function_code = """def create_fractured_monolith(base_length=30, base_width=20, base_height=15, num_voids=6, void_radius_range=(1, 3), fracture_angle_range=(5, 25), seed=123):
    \"""
    Creates a 'Porous fractured monolith' architectural concept model.

    This model is composed of a solid monolithic base with strategically placed spherical voids. 
    Fractures are created by rotating portions of the base around randomly selected angles and axes, 
    enhancing the dynamic and fragmented nature of the metaphor.

    Parameters:
    - base_length (float): Length of the base mass in meters.
    - base_width (float): Width of the base mass in meters.
    - base_height (float): Height of the base mass in meters.
    - num_voids (int): Number of spherical voids to create within the monolith.
    - void_radius_range (tuple): Range (min, max) of radii for the spherical voids in meters.
    - fracture_angle_range (tuple): Range (min, max) of angles for fractures in degrees.
    - seed (int): Seed for random number generator to ensure replicability.

    Returns:
    - A list of RhinoCommon Brep objects representing the modified monolith with voids and fractures.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    random.seed(seed)

    # Define the monolithic base block
    monolith = rg.Box(rg.Plane.WorldXY, rg.Interval(0, base_length), rg.Interval(0, base_width), rg.Interval(0, base_height))
    monolith_brep = monolith.ToBrep()

    # Generate spherical voids
    voids = []
    for _ in range(num_voids):
        void_radius = random.uniform(*void_radius_range)
        void_center = rg.Point3d(
            random.uniform(void_radius, base_length - void_radius),
            random.uniform(void_radius, base_width - void_radius),
            random.uniform(void_radius, base_height - void_radius)
        )
        void_sphere = rg.Sphere(void_center, void_radius)
        void_brep = void_sphere.ToBrep()
        voids.append(void_brep)

    # Create fractures by rotating sections of the monolith
    fractured_breps = [monolith_brep]
    for _ in range(num_voids):
        fracture_angle = random.uniform(*fracture_angle_range)
        fracture_axis = rg.Vector3d(
            random.choice([-1, 1]) * random.uniform(0.3, 1.0),
            random.choice([-1, 1]) * random.uniform(0.3, 1.0),
            random.choice([-1, 1]) * random.uniform(0.3, 1.0)
        )
        fracture_point = rg.Point3d(
            random.uniform(0, base_length),
            random.uniform(0, base_width),
            random.uniform(0, base_height)
        )
        rotation_transform = rg.Transform.Rotation(math.radians(fracture_angle), fracture_axis, fracture_point)
        
        fractured_brep = fractured_breps[-1].Duplicate()
        fractured_brep.Transform(rotation_transform)
        fractured_breps.append(fractured_brep)

    # Subtract voids from the fractured monolith
    result_brep = fractured_breps[-1]
    for void in voids:
        boolean_difference = rg.Brep.CreateBooleanDifference([result_brep], [void], 0.01)
        if boolean_difference:
            result_brep = boolean_difference[0]

    return [result_brep]"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_fractured_monolith(base_length=40, base_width=25, base_height=20, num_voids=8, void_radius_range=(2, 4), fracture_angle_range=(10, 30), seed=456)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_fractured_monolith(base_length=35, base_width=22, base_height=18, num_voids=5, void_radius_range=(1, 2), fracture_angle_range=(8, 20), seed=789)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_fractured_monolith(base_length=50, base_width=30, base_height=25, num_voids=10, void_radius_range=(1.5, 3.5), fracture_angle_range=(15, 35), seed=101)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_fractured_monolith(base_length=45, base_width=28, base_height=22, num_voids=7, void_radius_range=(2, 5), fracture_angle_range=(12, 28), seed=999)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_fractured_monolith(base_length=32, base_width=18, base_height=15, num_voids=4, void_radius_range=(1, 2.5), fracture_angle_range=(6, 15), seed=111)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
