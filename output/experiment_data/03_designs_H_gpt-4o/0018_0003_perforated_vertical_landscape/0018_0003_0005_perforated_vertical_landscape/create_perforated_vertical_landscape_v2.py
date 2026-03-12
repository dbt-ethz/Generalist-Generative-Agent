# Created for 0018_0003_perforated_vertical_landscape.json

""" Summary:
The function `create_perforated_vertical_landscape_v2` generates an architectural concept model by conceptualizing the 'Perforated vertical landscape' metaphor. It constructs a series of vertical fins or ribs, spaced apart to create voids that allow light and air to penetrate the structure, enhancing its interaction with the environment. Parameters such as height, width, fin thickness, and void height influence the model's dimensions and aesthetics. The function introduces randomness in void placement, simulating natural patterns and variability. The resulting 3D geometries reflect a rhythmic interplay between solid and void, embodying the metaphor's focus on verticality and permeability."""

#! python 3
function_code = """def create_perforated_vertical_landscape_v2(height, width, depth, fin_thickness, fin_spacing, void_height, randomness_seed=42):
    \"""
    Creates a conceptual architectural model based on the 'Perforated vertical landscape' metaphor.

    This function generates a structure with vertical fins or ribs, incorporating voids that allow light and air to penetrate,
    emphasizing vertical rhythm and interaction with the environment.

    Parameters:
    - height (float): The total height of the structure in meters.
    - width (float): The overall width of the structure in meters.
    - depth (float): The overall depth of the structure in meters.
    - fin_thickness (float): The thickness of each vertical fin in meters.
    - fin_spacing (float): The spacing between each vertical fin in meters.
    - void_height (float): The height of each void in meters.
    - randomness_seed (int): The seed for random number generation to ensure replicability.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of 3D geometries (breps) representing the fins with voids.
    \"""
    import Rhino.Geometry as rg
    import random

    random.seed(randomness_seed)  # Set seed for randomness

    geometries = []  # List to store resulting geometries

    # Calculate the number of fins based on width, fin thickness, and spacing
    num_fins = int((width - fin_thickness) / (fin_thickness + fin_spacing))

    for i in range(num_fins):
        # Calculate the position of each fin
        x_position = i * (fin_thickness + fin_spacing)

        # Create the vertical fin as a box
        fin_box = rg.Box(
            rg.Plane.WorldXY,
            rg.Interval(x_position, x_position + fin_thickness),
            rg.Interval(0, depth),
            rg.Interval(0, height)
        ).ToBrep()

        # Calculate potential positions for voids along the fin height
        void_positions = list(range(0, int(height), int(void_height * 2)))

        # Randomly choose positions for voids
        selected_voids = random.sample(void_positions, len(void_positions) // 2)

        void_breps = []
        for vp in selected_voids:
            # Create a void as a box at the selected position
            void_box = rg.Box(
                rg.Plane.WorldXY,
                rg.Interval(x_position, x_position + fin_thickness),
                rg.Interval(0, depth),
                rg.Interval(vp, vp + void_height)
            ).ToBrep()
            void_breps.append(void_box)

        # Subtract the voids from the fin
        if void_breps:
            voids_combined = rg.Brep.JoinBreps(void_breps, 0.01)
            if voids_combined:
                fin_box = rg.Brep.CreateBooleanDifference(fin_box, voids_combined[0], 0.01)
                if fin_box:
                    fin_box = fin_box[0]

        # Add the perforated fin to the list of geometries
        geometries.append(fin_box)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_perforated_vertical_landscape_v2(10.0, 5.0, 2.0, 0.1, 0.2, 1.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_perforated_vertical_landscape_v2(15.0, 7.0, 3.0, 0.05, 0.15, 0.5, randomness_seed=21)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_perforated_vertical_landscape_v2(8.0, 4.0, 1.5, 0.2, 0.25, 0.75, randomness_seed=10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_perforated_vertical_landscape_v2(12.0, 6.0, 2.5, 0.15, 0.3, 0.8, randomness_seed=100)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_perforated_vertical_landscape_v2(5.0, 3.0, 1.0, 0.1, 0.1, 0.5, randomness_seed=5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
