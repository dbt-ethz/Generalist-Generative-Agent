# Created for 0009_0003_cantilevering_corners.json

""" Summary:
The provided function generates an architectural concept model based on the metaphor of "Cantilevering corners." It creates a central mass, representing stability, from which multiple cantilevered sections extend in various orientations and heights, embodying a dynamic balance of weight and motion. By using randomization for cantilever placement and height variation, the model reflects the metaphor's essence, fostering exploration and interaction through its dramatic projections. The inclusion of voids beneath the cantilevers enhances the sense of suspension and movement, while the interplay of light and shadows accentuates the architectural form's visual intrigue and contextual engagement."""

#! python 3
function_code = """def create_cantilevering_corners_model(base_length, base_width, base_height, num_cantilevers, cantilever_length, cantilever_height_variation, seed=42):
    \"""
    Creates an architectural Concept Model embodying the metaphor of 'Cantilevering corners'.
    
    Parameters:
    - base_length (float): The length of the central mass.
    - base_width (float): The width of the central mass.
    - base_height (float): The height of the central mass.
    - num_cantilevers (int): The number of cantilevered sections to create.
    - cantilever_length (float): The length of each cantilevered section.
    - cantilever_height_variation (float): The maximum height variation for the cantilevered sections.
    - seed (int): The seed for random number generation to ensure replicability.

    Returns:
    - List of RhinoCommon Brep objects representing the 3D geometries of the concept model.
    \"""
    import Rhino.Geometry as rg
    import random

    random.seed(seed)
    geometries = []

    # Create the central base mass
    base_corners = [
        rg.Point3d(0, 0, 0),
        rg.Point3d(base_length, 0, 0),
        rg.Point3d(base_length, base_width, 0),
        rg.Point3d(0, base_width, 0),
        rg.Point3d(0, 0, base_height),
        rg.Point3d(base_length, 0, base_height),
        rg.Point3d(base_length, base_width, base_height),
        rg.Point3d(0, base_width, base_height)
    ]
    base_box = rg.Box(rg.Plane.WorldXY, base_corners)
    geometries.append(base_box.ToBrep())

    # Create cantilevered sections
    for i in range(num_cantilevers):
        # Randomly choose a corner of the base to start the cantilever
        corner_index = random.randint(0, 3)
        base_point = base_corners[corner_index]
        
        # Randomly choose the direction and orientation of the cantilever
        direction = rg.Vector3d(random.choice([-1, 1]), random.choice([-1, 1]), 0)
        height_variation = random.uniform(0, cantilever_height_variation)

        # Create the cantilever geometry
        cantilever_corners = [
            base_point,
            base_point + rg.Vector3d(cantilever_length * direction.X, 0, 0),
            base_point + rg.Vector3d(cantilever_length * direction.X, cantilever_length * direction.Y, 0),
            base_point + rg.Vector3d(0, cantilever_length * direction.Y, 0),
            base_point + rg.Vector3d(0, 0, base_height + height_variation),
            base_point + rg.Vector3d(cantilever_length * direction.X, 0, base_height + height_variation),
            base_point + rg.Vector3d(cantilever_length * direction.X, cantilever_length * direction.Y, base_height + height_variation),
            base_point + rg.Vector3d(0, cantilever_length * direction.Y, base_height + height_variation)
        ]
        cantilever_box = rg.Box(rg.Plane.WorldXY, cantilever_corners)
        geometries.append(cantilever_box.ToBrep())

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_cantilevering_corners_model(10.0, 5.0, 3.0, 4, 2.0, 1.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_cantilevering_corners_model(15.0, 7.0, 4.0, 3, 3.0, 2.0, seed=100)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_cantilevering_corners_model(12.0, 6.0, 5.0, 5, 2.5, 1.5, seed=21)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_cantilevering_corners_model(20.0, 10.0, 6.0, 6, 4.0, 3.0, seed=77)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_cantilevering_corners_model(8.0, 4.0, 2.0, 2, 1.5, 0.5, seed=55)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
