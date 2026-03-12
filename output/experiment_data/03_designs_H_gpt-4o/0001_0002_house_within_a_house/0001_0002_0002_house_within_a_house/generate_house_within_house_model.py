# Created for 0001_0002_house_within_a_house.json

""" Summary:
The provided function generates an architectural concept model based on the "House within a house" metaphor by creating a series of interlocking and cascading forms that embody the ideas of nesting and protection. It utilizes parameters such as base dimensions, inner scale, and the number of layers to define the outer and inner structures. Each layer is scaled down, rotated, and can incorporate voids to enhance the interaction between spaces, illustrating the transition from public to private areas. Ultimately, the model visually demonstrates a layered spatial hierarchy, emphasizing the concepts of containment and gradual discovery inherent in the metaphor."""

#! python 3
function_code = """def generate_house_within_house_model(base_length=12.0, base_width=10.0, base_height=6.0, inner_scale=0.6, num_layers=4):
    \"""
    Generates an architectural Concept Model based on the 'House within a house' metaphor. The model consists of interlocking
    and cascading forms that illustrate a sense of nesting and protection. Each form represents a different spatial function,
    encouraging exploration through a sequence of spaces from public to private.

    Parameters:
    - base_length (float): The length of the outermost form in meters.
    - base_width (float): The width of the outermost form in meters.
    - base_height (float): The height of the outermost form in meters.
    - inner_scale (float): The scale factor for the inner forms, defining their relative size.
    - num_layers (int): The number of layers to create, representing the gradual transition from outer to inner spaces.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Breps representing the 3D geometries of the concept model.
    \"""
    import Rhino.Geometry as rg
    import math
    import random

    # Ensure repeatable randomness
    random.seed(42)

    # Initialize list for storing geometries
    geometries = []

    # Parameters for creating the concentric forms
    layer_thickness = (1 - inner_scale) / num_layers
    rotation_angle = math.pi / 12  # 15 degrees in radians

    for i in range(num_layers):
        # Determine the scale for the current layer
        scale_factor = 1 - layer_thickness * i

        # Create the base box for the current layer
        box_length = base_length * scale_factor
        box_width = base_width * scale_factor
        box_height = base_height * scale_factor
        box = rg.Box(rg.Plane.WorldXY, rg.Interval(-box_length/2, box_length/2), rg.Interval(-box_width/2, box_width/2), rg.Interval(0, box_height))

        # Convert the box to a Brep
        brep = box.ToBrep()

        # Apply rotation to create dynamic interplay between layers
        rotation_axis = rg.Vector3d(0, 0, 1)  # Rotate around Z-axis
        rotation_center = rg.Point3d(0, 0, 0)
        rotation_transform = rg.Transform.Rotation(rotation_angle * i, rotation_axis, rotation_center)
        brep.Transform(rotation_transform)

        # Add the transformed Brep to the list
        geometries.append(brep)

        # Create voids in alternating layers
        if i % 2 == 1:
            void_radius = random.uniform(box_length * 0.1, box_length * 0.2)
            void_center = rg.Point3d(random.uniform(-box_length/4, box_length/4), random.uniform(-box_width/4, box_width/4), box_height / 2)
            void_sphere = rg.Sphere(void_center, void_radius)
            void_brep = void_sphere.ToBrep()

            # Subtract the void from the current layer
            brep_with_void = rg.Brep.CreateBooleanDifference([brep], [void_brep], 0.01)
            if brep_with_void:
                geometries[-1] = brep_with_void[0]

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = generate_house_within_house_model(base_length=15.0, base_width=12.0, base_height=8.0, inner_scale=0.5, num_layers=5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = generate_house_within_house_model(base_length=10.0, base_width=8.0, base_height=5.0, inner_scale=0.7, num_layers=3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = generate_house_within_house_model(base_length=20.0, base_width=15.0, base_height=10.0, inner_scale=0.4, num_layers=6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = generate_house_within_house_model(base_length=18.0, base_width=14.0, base_height=9.0, inner_scale=0.65, num_layers=4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = generate_house_within_house_model(base_length=14.0, base_width=11.0, base_height=7.0, inner_scale=0.55, num_layers=5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
