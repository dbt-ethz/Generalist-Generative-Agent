# Created for 0018_0003_perforated_vertical_landscape.json

""" Summary:
The provided function, `create_perforated_vertical_landscape`, generates an architectural concept model based on the "Perforated vertical landscape" metaphor. It creates a series of vertical fins, integrating dynamic perforations to symbolize natural interactions with light and air. Parameters such as base dimensions, number of fins, fin thickness, and void heights are utilized to define the model's structure. The function employs randomization to introduce variability in the voids, enhancing the visual rhythm and permeability of the design. The result is a collection of geometrical representations that embody the metaphors essence, emphasizing the relationship between the building and its environment."""

#! python 3
function_code = """def create_perforated_vertical_landscape(base_width, base_depth, height, num_fins, fin_thickness, max_void_height):
    \"""
    Creates an architectural Concept Model based on the 'Perforated vertical landscape' metaphor.

    The model consists of vertical fins with dynamic perforations that allow light and air to penetrate,
    creating a rhythmic and permeable structure inspired by natural landscapes.

    Parameters:
    - base_width (float): The overall width of the structure in meters.
    - base_depth (float): The depth of the structure in meters.
    - height (float): The height of the structure in meters.
    - num_fins (int): The number of vertical fins or ribs.
    - fin_thickness (float): The thickness of each fin in meters.
    - max_void_height (float): The maximum height of each void in meters.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep geometries representing the vertical fins with perforations.
    \"""
    import Rhino.Geometry as rg
    import random

    # Set seed for randomness to ensure replicability
    random.seed(42)

    # Calculate spacing between fins based on the number of fins and their thickness
    fin_spacing = (base_width - (num_fins * fin_thickness)) / (num_fins + 1)

    # List to hold the resulting Brep geometries
    geometries = []

    for i in range(num_fins):
        # Calculate the position of each fin
        x_position = fin_spacing + i * (fin_thickness + fin_spacing)

        # Create the fin as a vertical box
        fin_box = rg.Box(
            rg.Plane.WorldXY,
            rg.Interval(x_position, x_position + fin_thickness),
            rg.Interval(0, base_depth),
            rg.Interval(0, height)
        )
        fin_brep = fin_box.ToBrep()

        # Add perforations randomly along the height of the fin
        num_voids = random.randint(3, 5)  # Random number of voids per fin
        voids = []
        for _ in range(num_voids):
            void_height = random.uniform(0.1, max_void_height)
            void_base_height = random.uniform(0, height - void_height)
            void_center = rg.Point3d(x_position + fin_thickness / 2, base_depth / 2, void_base_height + void_height / 2)
            void_box = rg.Box(
                rg.Plane.WorldXY,
                rg.Interval(x_position, x_position + fin_thickness),
                rg.Interval(0, base_depth),
                rg.Interval(void_base_height, void_base_height + void_height)
            )
            voids.append(void_box.ToBrep())

        # Subtract voids from the fin
        if voids:
            voids_brep = rg.Brep.JoinBreps(voids, 0.01)
            if voids_brep:
                result = rg.Brep.CreateBooleanDifference(fin_brep, voids_brep[0], 0.01)
                if result:
                    fin_brep = result[0]

        # Add the resulting perforated fin to the geometries list
        if fin_brep:
            geometries.append(fin_brep)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_perforated_vertical_landscape(10.0, 2.0, 5.0, 5, 0.1, 1.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_perforated_vertical_landscape(15.0, 3.0, 6.0, 7, 0.2, 2.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_perforated_vertical_landscape(12.0, 4.0, 8.0, 6, 0.15, 1.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_perforated_vertical_landscape(20.0, 5.0, 10.0, 8, 0.25, 3.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_perforated_vertical_landscape(8.0, 1.5, 4.0, 4, 0.05, 0.8)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
