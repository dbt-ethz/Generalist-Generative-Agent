# Created for 0005_0004_distorted_puzzle.json

""" Summary:
The provided function generates an architectural concept model embodying the "Distorted puzzle" metaphor by creating interconnected, irregularly shaped units that suggest tension rather than perfect alignment. It utilizes a cubic grid to position units, applying random twists and tilts to each to create dynamic and skewed forms. This approach fosters non-linear spatial relationships, forming niches that encourage exploration while maintaining coherence through aligned visual axes. The functions random parameters ensure variability in the design, allowing for unexpected connections and complexity, ultimately capturing the essence of a distorted yet cohesive architectural puzzle."""

#! python 3
function_code = """def create_distorted_puzzle_concept_model(base_dimension, num_units, angle_variation, random_seed):
    \"""
    Creates an architectural Concept Model based on the 'Distorted puzzle' metaphor.

    This function generates a series of interconnected yet irregularly shaped units, each comprising twisted and skewed surfaces 
    that suggest dynamic alignment. The design emphasizes non-linear spatial flow, forming niches and inviting exploration, while 
    maintaining coherence through key visual axes.

    Parameters:
    - base_dimension (float): The base dimension for the grid in meters.
    - num_units (int): The number of units to generate.
    - angle_variation (float): Maximum angle variation in degrees for twisting and tilting.
    - random_seed (int): Seed for the random number generator to ensure replicability.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep objects representing the 3D geometries of the Concept Model.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    random.seed(random_seed)

    geometries = []
    grid_size = math.ceil(num_units ** (1/3))  # Approximate a cubic grid

    # Create a base grid of points
    for x in range(grid_size):
        for y in range(grid_size):
            for z in range(grid_size):
                if len(geometries) >= num_units:
                    break

                # Calculate the center of each unit
                center = rg.Point3d(x * base_dimension, y * base_dimension, z * base_dimension)

                # Create a box-shaped unit
                box = rg.Box(
                    rg.Plane(center, rg.Vector3d.ZAxis),
                    rg.Interval(-base_dimension/2, base_dimension/2),
                    rg.Interval(-base_dimension/2, base_dimension/2),
                    rg.Interval(-base_dimension/2, base_dimension/2)
                )

                # Apply random twist and tilt
                twist_angle = math.radians(random.uniform(-angle_variation, angle_variation))
                tilt_angle = math.radians(random.uniform(-angle_variation, angle_variation))

                twist_transform = rg.Transform.Rotation(twist_angle, rg.Vector3d.ZAxis, center)
                tilt_transform_x = rg.Transform.Rotation(tilt_angle, rg.Vector3d.XAxis, center)
                tilt_transform_y = rg.Transform.Rotation(tilt_angle, rg.Vector3d.YAxis, center)

                box.Transform(twist_transform)
                box.Transform(tilt_transform_x)
                box.Transform(tilt_transform_y)

                # Convert to brep and add to geometries
                geometries.append(box.ToBrep())

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_distorted_puzzle_concept_model(5.0, 10, 30.0, 42)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_distorted_puzzle_concept_model(3.0, 20, 45.0, 7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_distorted_puzzle_concept_model(4.0, 15, 60.0, 99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_distorted_puzzle_concept_model(2.5, 8, 15.0, 21)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_distorted_puzzle_concept_model(6.0, 12, 25.0, 15)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
