# Created for 0005_0005_distorted_puzzle.json

""" Summary:
The function `create_distorted_puzzle_model` generates an architectural concept model based on the "Distorted puzzle" metaphor by creating a series of fragmented, interlocking volumes. Each volume is randomly positioned and sized within specified parameters, ensuring a diverse array of asymmetric forms that vary in height. This design approach emphasizes a dynamic interplay of light and shadow, fostering a sense of tension and balance. The resulting model features distinct elements that contribute to an overall interconnected system, evoking the metaphors complexity while allowing for varied spatial experiences, reflecting the unpredictability and coherence of a puzzle."""

#! python 3
function_code = """def create_distorted_puzzle_model(base_width, base_length, max_height, num_volumes, random_seed):
    \"""
    Create an architectural Concept Model for the 'Distorted Puzzle' metaphor.

    This function generates an array of fragmented, interlocking volumes that vary in height and form,
    emphasizing a dynamic play of light and shadow. The design ensures that each volume is distinct 
    yet part of a larger interconnected system, enhancing a balance between individuality and unity.

    Parameters:
    - base_width (float): The base width of the overall model footprint.
    - base_length (float): The base length of the overall model footprint.
    - max_height (float): The maximum height for the volumes.
    - num_volumes (int): The number of fragmented volumes to generate.
    - random_seed (int): Seed for random number generation to ensure replicability.

    Returns:
    - List of RhinoCommon Brep objects: A list of 3D geometries representing the concept model.
    \"""
    
    import Rhino.Geometry as rg
    import random

    random.seed(random_seed)
    volumes = []
    
    for _ in range(num_volumes):
        # Randomly position the base of the volume
        x_pos = random.uniform(0, base_width)
        y_pos = random.uniform(0, base_length)
        
        # Randomly determine the dimensions of each volume
        width = random.uniform(0.1 * base_width, 0.3 * base_width)
        length = random.uniform(0.1 * base_length, 0.3 * base_length)
        height = random.uniform(0.2 * max_height, max_height)
        
        # Create a base rectangle
        base_point = rg.Point3d(x_pos, y_pos, 0)
        base_rect = rg.Rectangle3d(rg.Plane.WorldXY, width, length)
        base_rect.Transform(rg.Transform.Translation(base_point.X, base_point.Y, base_point.Z))
        
        # Create an extrusion to form a prism
        extrusion_vector = rg.Vector3d(0, 0, height)
        prism = rg.Brep.CreateFromBox(base_rect.BoundingBox)
        if prism:
            extruded_prism = prism.Faces[0].CreateExtrusion(extrusion_vector, True)
            if extruded_prism:
                volumes.append(extruded_prism)

    return volumes"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_distorted_puzzle_model(10.0, 15.0, 5.0, 20, 42)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_distorted_puzzle_model(8.0, 12.0, 6.0, 15, 7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_distorted_puzzle_model(12.0, 20.0, 8.0, 25, 99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_distorted_puzzle_model(5.0, 10.0, 4.0, 30, 101)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_distorted_puzzle_model(6.0, 9.0, 3.0, 10, 25)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
