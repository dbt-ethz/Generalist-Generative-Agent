# Created for 0009_0002_cantilevering_corners.json

""" Summary:
The function `generate_cantilevering_concept_model` creates an architectural concept model inspired by the metaphor of "Cantilevering corners." It generates a central core structure surrounded by multiple layers of cantilevered sections, which project outward at varying angles and lengths. This design captures the dynamic balance between stability and movement, as defined in the metaphor. By manipulating parameters such as core dimensions, layer heights, and cantilever variations, the model embodies intriguing spatial relationships and contrasts. The result is a complex interplay of volumes that invites exploration and emphasizes the interaction of light, shadow, and the environment, reflecting the essence of the metaphor."""

#! python 3
function_code = """def generate_cantilevering_concept_model(core_dimension=8.0, layer_height=3.0, cantilever_variation=4, seed=24):
    \"""
    Creates an architectural Concept Model based on the metaphor of 'Cantilevering corners'.
    
    This function models a structure with a central core and multiple layers of cantilevered sections.
    These sections project outward at varying angles and lengths to create a dynamic balance between 
    the stable core and the extended elements, capturing the essence of movement and equilibrium.

    Parameters:
    - core_dimension (float): The dimension of the central core cube in meters.
    - layer_height (float): The height of each layer in meters.
    - cantilever_variation (int): The number of cantilevered projections per layer.
    - seed (int): Seed for randomness to ensure replicability.

    Returns:
    - list: A list of Rhino.Geometry.Brep representing the 3D geometries of the concept model.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    random.seed(seed)
    
    # Create the central core
    core = rg.Box(rg.Plane.WorldXY, rg.Interval(-core_dimension/2, core_dimension/2), 
                  rg.Interval(-core_dimension/2, core_dimension/2), rg.Interval(0, core_dimension))
    geometries = [core.ToBrep()]

    total_height = 0

    # Create layered cantilevers
    for layer in range(cantilever_variation):
        layer_base_height = total_height
        total_height += layer_height

        for _ in range(cantilever_variation):
            # Determine cantilever length and orientation
            length = random.uniform(core_dimension * 0.5, core_dimension * 1.5)
            angle = random.uniform(-45, 45)
            direction = rg.Vector3d(random.choice([-1, 1]), random.choice([-1, 1]), 0)
            
            # Create cantilevered section
            cantilever_box = rg.Box(rg.Plane.WorldXY, rg.Interval(0, core_dimension * 0.5), 
                                    rg.Interval(0, core_dimension * 0.5), rg.Interval(0, layer_height))
            cantilever_brep = cantilever_box.ToBrep()
            
            # Apply transformations
            rotation = rg.Transform.Rotation(math.radians(angle), rg.Vector3d.ZAxis, rg.Point3d.Origin)
            translation = rg.Transform.Translation(direction * length + rg.Vector3d(0, 0, layer_base_height))
            cantilever_brep.Transform(rotation)
            cantilever_brep.Transform(translation)
            
            geometries.append(cantilever_brep)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = generate_cantilevering_concept_model(10.0, 2.5, 5, 42)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = generate_cantilevering_concept_model(12.0, 4.0, 3, 10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = generate_cantilevering_concept_model(9.0, 3.5, 6, 15)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = generate_cantilevering_concept_model(7.0, 2.0, 4, 30)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = generate_cantilevering_concept_model(11.0, 3.0, 7, 5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
