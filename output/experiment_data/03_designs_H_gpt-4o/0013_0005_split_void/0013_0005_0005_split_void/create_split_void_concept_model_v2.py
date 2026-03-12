# Created for 0013_0005_split_void.json

""" Summary:
The function `create_split_void_concept_model_v2` generates an architectural concept model that embodies the 'Split void' metaphor by creating a building structure with a central void that divides the architectural mass. It can produce either a vertical or horizontal fissure, influencing the geometry and silhouette of the model. The void facilitates dynamic circulation and interaction, allowing light to penetrate and create varied shadow patterns, reinforcing the design's duality and contrast. By incorporating random openings, the model further explores spatial relationships, enhancing the building's visual identity while emphasizing the transformative role of the void in the overall design."""

#! python 3
function_code = """def create_split_void_concept_model_v2(base_length, base_width, base_height, void_width, split_type='horizontal', seed_value=42):
    \"""
    Creates an architectural Concept Model based on the 'Split void' metaphor.
    
    The function generates a building form where a central void splits the mass into distinct segments.
    Depending on the split_type, the void can be a horizontal or vertical fissure that influences
    the building's geometry and silhouette. The model explores spatial contrasts, light interaction,
    and dynamic circulation.

    Parameters:
    - base_length (float): Length of the base structure in meters.
    - base_width (float): Width of the base structure in meters.
    - base_height (float): Height of the base structure in meters.
    - void_width (float): Width of the void in meters.
    - split_type (str): Type of the split, either 'horizontal' or 'vertical'.
    - seed_value (int): Seed for random number generation to ensure replicability.

    Returns:
    - list of Rhino.Geometry.Brep: A list of Brep objects representing the 3D geometries of the model.
    \"""
    import Rhino.Geometry as rg
    import random

    # Set seed for randomness
    random.seed(seed_value)

    # Create base structure
    base_box = rg.Box(rg.Plane.WorldXY, rg.Interval(0, base_length), rg.Interval(0, base_width), rg.Interval(0, base_height)).ToBrep()

    # Define the central void as a Brep
    if split_type == 'vertical':
        void_position = rg.Interval(base_length / 2 - void_width / 2, base_length / 2 + void_width / 2)
        void_box = rg.Box(rg.Plane.WorldXY, void_position, rg.Interval(0, base_width), rg.Interval(0, base_height)).ToBrep()
    else:  # horizontal split
        void_position = rg.Interval(base_width / 2 - void_width / 2, base_width / 2 + void_width / 2)
        void_box = rg.Box(rg.Plane.WorldXY, rg.Interval(0, base_length), void_position, rg.Interval(0, base_height)).ToBrep()

    # Split the base structure with the void
    split_breps = rg.Brep.CreateBooleanDifference([base_box], [void_box], 0.01)

    if not split_breps:
        return [base_box]  # Return base structure if splitting fails

    # Explore dynamic circulation by adding random openings at each segment
    openings = []
    for brep in split_breps:
        # Randomly create some openings
        opening_count = random.randint(1, 3)
        for _ in range(opening_count):
            open_length = random.uniform(1, base_length / 4)
            open_width = random.uniform(1, base_width / 4)
            open_height = random.uniform(1, base_height / 4)
            open_x = random.uniform(0, base_length - open_length)
            open_y = random.uniform(0, base_width - open_width)
            open_z = random.uniform(0, base_height - open_height)
            
            opening_box = rg.Box(rg.Plane.WorldXY, rg.Interval(open_x, open_x + open_length),
                                 rg.Interval(open_y, open_y + open_width),
                                 rg.Interval(open_z, open_z + open_height)).ToBrep()
            openings.append(opening_box)

    # Subtract openings from the segments
    final_geometries = []
    for segment in split_breps:
        for opening in openings:
            difference = rg.Brep.CreateBooleanDifference([segment], [opening], 0.01)
            if difference:
                segment = difference[0]
        final_geometries.append(segment)

    return final_geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_split_void_concept_model_v2(10, 5, 15, 2, split_type='vertical', seed_value=123)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_split_void_concept_model_v2(8, 4, 12, 1.5, split_type='horizontal', seed_value=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_split_void_concept_model_v2(15, 10, 20, 3, split_type='vertical', seed_value=456)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_split_void_concept_model_v2(12, 6, 18, 2.5, split_type='horizontal', seed_value=789)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_split_void_concept_model_v2(20, 10, 25, 4, split_type='vertical', seed_value=101)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
