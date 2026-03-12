# Created for 0001_0002_house_within_a_house.json

""" Summary:
The provided function, `create_house_within_a_house_concept_model`, generates an architectural concept model inspired by the metaphor of a "House within a house." It creates a series of concentric cylindrical layers that symbolize nesting and protection, with each layer representing varying degrees of openness and enclosure. The function allows for customization of radii, height, and the number of layers, enabling the exploration of spatial hierarchies. By implementing slight variations in height for the inner layers, it emphasizes the dynamic interplay between the inner sanctuary and the outer protective shell, visually manifesting the metaphor's themes of retreat and containment."""

#! python 3
function_code = """def create_house_within_a_house_concept_model(outer_radius, inner_radius, height, layers_count, seed=42):
    \"""
    Creates an architectural Concept Model based on the 'House within a house' metaphor. This model consists
    of concentric or overlapping forms that convey a sense of nesting and protection, with contrasting layers
    that suggest a progression from public to private spaces.

    Parameters:
        outer_radius (float): The radius of the outermost form, representing the protective shell.
        inner_radius (float): The radius of the innermost form, representing the retreat or sanctuary.
        height (float): The height of the entire model, applicable to all layers.
        layers_count (int): The number of layers to create between the outer shell and the inner sanctuary.
        seed (int, optional): A seed for random number generation to ensure replicability of the design.

    Returns:
        List[Rhino.Geometry.Brep]: A list of Breps representing the 3D geometries of the concept model layers.
    \"""
    import Rhino.Geometry as rg
    import random

    # Set the random seed for replicability
    random.seed(seed)

    geometries = []

    # Calculate the incremental reduction for each layer
    radius_step = (outer_radius - inner_radius) / (layers_count + 1)

    for i in range(layers_count + 2):
        # Calculate current layer radius
        current_radius = outer_radius - i * radius_step

        # Create a cylindrical layer
        base_circle = rg.Circle(rg.Plane.WorldXY, current_radius)
        cylinder = rg.Cylinder(base_circle, height).ToBrep(True, True)

        # Optionally add randomness to the height of each layer
        if i > 0 and i < layers_count + 1:  # Avoid randomness for the outermost and innermost layers
            offset = random.uniform(-0.2, 0.2)  # Random height variation
            cylinder = rg.Brep.CreateFromOffsetFace(cylinder.Faces[0], offset, 0.01, True, False)

        geometries.append(cylinder)

    # Return the list of Brep geometries
    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_house_within_a_house_concept_model(10, 5, 15, 3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_house_within_a_house_concept_model(12, 6, 20, 4, seed=123)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_house_within_a_house_concept_model(15, 7, 10, 5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_house_within_a_house_concept_model(8, 3, 12, 2, seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_house_within_a_house_concept_model(14, 4, 18, 6, seed=2023)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
