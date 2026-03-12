# Created for 0018_0003_perforated_vertical_landscape.json

""" Summary:
The provided function generates an architectural concept model by interpreting the 'Perforated vertical landscape' metaphor through the creation of vertical fins or ribs. It constructs a structure with dynamic perforations that let light and air flow, reflecting the metaphor's emphasis on permeability and interaction with the environment. Parameters such as base dimensions, fin thickness, and spacing guide the model's design, while random variations in fin height and void placement create a natural silhouette and visual interest. The resulting geometries embody a rhythmic interplay of solid and void, enhancing the spatial experience and connection to the surrounding landscape."""

#! python 3
function_code = """def create_perforated_vertical_landscape_model(base_width, base_depth, height, fin_thickness, fin_spacing, vertical_variation, random_seed=42):
    \"""
    Creates an architectural Concept Model based on the 'Perforated vertical landscape' metaphor.

    This function generates a structure composed of vertical fins or ribs with interspersed voids.
    The model emphasizes vertical rhythm, texture, and permeability, allowing light, air, and views to penetrate.

    Parameters:
    - base_width (float): The width of the building base in meters.
    - base_depth (float): The depth of the building base in meters.
    - height (float): The height of the structure in meters.
    - fin_thickness (float): The thickness of each vertical fin in meters.
    - fin_spacing (float): The spacing between each vertical fin in meters.
    - vertical_variation (float): The variation in fin height to create a natural silhouette.
    - random_seed (int): Seed for random number generation to ensure replicability.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep geometries representing the building structure.
    \"""
    import Rhino.Geometry as rg
    import random

    # Set randomness seed for replicability
    random.seed(random_seed)

    # List to store the resulting Brep geometries
    geometries = []

    # Define the number of fins based on the base width and fin spacing
    num_fins = int(base_width / (fin_thickness + fin_spacing))

    for i in range(num_fins):
        # Calculate the position of each fin
        x_position = i * (fin_thickness + fin_spacing)

        # Determine the height variation for the natural silhouette
        varied_height = height * (1 + vertical_variation * (random.uniform(-0.5, 0.5)))

        # Create a vertical fin as a box from the base to the varied height
        fin_base = rg.Box(rg.Plane.WorldXY, rg.Interval(x_position, x_position + fin_thickness), rg.Interval(0, base_depth), rg.Interval(0, varied_height))
        fin_brep = fin_base.ToBrep()

        # Create perforations as rectangular holes
        num_voids = random.randint(2, 5)  # Random number of voids per fin
        for _ in range(num_voids):
            # Random position for each void within the fin
            void_height = random.uniform(fin_thickness, varied_height - fin_thickness)
            void_width = random.uniform(fin_thickness, base_depth - fin_thickness)
            void_x = random.uniform(x_position, x_position + fin_thickness)
            void_y = random.uniform(0, base_depth - void_width)

            void_box = rg.Box(rg.Plane.WorldXY, rg.Interval(void_x, void_x + fin_thickness), rg.Interval(void_y, void_y + void_width), rg.Interval(0, void_height))
            void_brep = void_box.ToBrep()

            # Subtract the void from the fin
            result = rg.Brep.CreateBooleanDifference(fin_brep, void_brep, 0.01)
            if result:
                fin_brep = result[0]

        # Add the perforated fin to the list of geometries
        geometries.append(fin_brep)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_perforated_vertical_landscape_model(10.0, 5.0, 15.0, 0.2, 0.5, 0.1)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_perforated_vertical_landscape_model(12.0, 6.0, 20.0, 0.3, 0.4, 0.2, random_seed=10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_perforated_vertical_landscape_model(8.0, 4.0, 10.0, 0.15, 0.3, 0.05, random_seed=7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_perforated_vertical_landscape_model(15.0, 7.0, 25.0, 0.25, 0.6, 0.15, random_seed=5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_perforated_vertical_landscape_model(14.0, 8.0, 18.0, 0.2, 0.7, 0.3, random_seed=15)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
