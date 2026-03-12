# Created for 0012_0003_twisted_volumes.json

""" Summary:
The function `create_twisted_volumes_concept_model` generates an architectural concept model inspired by the metaphor of "Twisted volumes." It creates a series of 3D volumetric elements with varying degrees of twist, reflecting dynamic and fluid forms. Each volume is defined by its base dimensions and a random twist angle, fostering unexpected spatial relationships and enhancing the interaction between interior and exterior spaces. The twisting action manipulates light and shadow, creating visually captivating effects. By assembling these twisted elements, the model embodies the metaphor's essence, emphasizing energy, transformation, and continuous evolution in architectural design."""

#! python 3
function_code = """def create_twisted_volumes_concept_model(base_length, base_width, base_height, twist_angle_degrees, num_volumes):
    \"""
    Generates a 3D architectural Concept Model based on the 'Twisted volumes' metaphor. The model consists of
    a series of volumetric elements that exhibit varying degrees of twist and distortion, creating a dynamic and fluid form.

    Parameters:
    - base_length: float, the base length of each volume in meters.
    - base_width: float, the base width of each volume in meters.
    - base_height: float, the height of each volume in meters.
    - twist_angle_degrees: float, the maximum twist angle applied to the volumes in degrees.
    - num_volumes: int, the number of twisted volumes to create.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of breps representing the twisted volumes.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    # Set a fixed seed for reproducibility
    random.seed(42)

    # Helper function to create a twisted box
    def create_twisted_box(base_length, base_width, base_height, twist_angle):
        # Create a base box
        base_box = rg.Box(rg.Plane.WorldXY, rg.Interval(0, base_length), rg.Interval(0, base_width), rg.Interval(0, base_height))
        
        # Define a twisting axis (vertical line through the center of the box)
        twist_axis = rg.Line(base_box.Center, base_box.Center + rg.Vector3d(0, 0, base_height))
        
        # Create the twisted box by rotating the top face around the axis
        twisted_brep = rg.Brep.CreateFromBox(base_box)
        twist_transform = rg.Transform.Rotation(math.radians(twist_angle), twist_axis.Direction, twist_axis.From)
        twisted_brep.Transform(twist_transform)
        
        return twisted_brep

    # Generate the twisted volumes
    volumes = []
    for i in range(num_volumes):
        # Calculate a random twist angle for this volume
        twist_angle = random.uniform(-twist_angle_degrees, twist_angle_degrees)
        
        # Create a twisted box
        twisted_box = create_twisted_box(base_length, base_width, base_height, twist_angle)
        
        # Translate the box to a new position to avoid overlap
        translation_vector = rg.Vector3d(i * base_length * 1.2, 0, 0)
        translation_transform = rg.Transform.Translation(translation_vector)
        twisted_box.Transform(translation_transform)
        
        volumes.append(twisted_box)

    return volumes"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_twisted_volumes_concept_model(2.0, 1.0, 3.0, 45.0, 5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_twisted_volumes_concept_model(1.5, 0.8, 2.5, 60.0, 10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_twisted_volumes_concept_model(3.0, 2.0, 4.0, 30.0, 7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_twisted_volumes_concept_model(1.0, 1.0, 1.0, 90.0, 8)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_twisted_volumes_concept_model(2.5, 1.5, 2.0, 75.0, 6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
