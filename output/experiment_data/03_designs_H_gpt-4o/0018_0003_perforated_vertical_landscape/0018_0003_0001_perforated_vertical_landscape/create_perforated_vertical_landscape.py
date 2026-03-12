# Created for 0018_0003_perforated_vertical_landscape.json

""" Summary:
The provided function, `create_perforated_vertical_landscape`, generates an architectural concept model based on the "Perforated vertical landscape" metaphor. It creates a series of vertical fins or ribs, incorporating voids to enhance light and air interaction. By defining parameters like height, width, depth, number of fins, and void frequency, the model reflects rhythmic verticality and textures, reminiscent of natural landscapes. The function employs randomization for void placement, ensuring unique designs that embody permeability. Ultimately, the output consists of 3D geometries that visualize the metaphor's essence, facilitating a dynamic relationship between the building and its environment."""

#! python 3
function_code = """def create_perforated_vertical_landscape(height, width, depth, fin_count, fin_thickness, void_frequency, randomness_seed=42):
    \"""
    Creates an architectural Concept Model based on the 'Perforated vertical landscape' metaphor.

    This function generates a structure composed of vertical fins or ribs with interspersed voids.
    The model emphasizes vertical rhythm, texture, and permeability, allowing light, air, and views to penetrate.

    Parameters:
    - height (float): The total height of the model in meters.
    - width (float): The overall width of the model in meters.
    - depth (float): The overall depth of the model in meters.
    - fin_count (int): The number of vertical fins or ribs to generate.
    - fin_thickness (float): The thickness of each vertical fin in meters.
    - void_frequency (int): The number of voids to create per fin.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of 3D geometries (breps) representing the fins with voids.
    \"""
    import Rhino.Geometry as rg
    import random

    random.seed(randomness_seed)  # Ensures replicable randomness
    geometries = []

    # Calculate the space required for each fin
    total_fin_width = fin_thickness + ((width - fin_thickness * fin_count) / (fin_count - 1))
    
    for i in range(fin_count):
        # Calculate the position of the current fin
        x_position = i * total_fin_width
        
        # Create a vertical fin
        fin_box = rg.Box(rg.Plane.WorldXY, rg.Interval(x_position, x_position + fin_thickness), rg.Interval(0, depth), rg.Interval(0, height))
        fin_brep = fin_box.ToBrep()

        # Create voids as spherical perforations
        voids = []
        for _ in range(void_frequency):
            void_center = rg.Point3d(
                x_position + random.uniform(0, fin_thickness),
                random.uniform(0, depth),
                random.uniform(0, height)
            )
            void_radius = random.uniform(0.2, 0.5) * min(fin_thickness, depth, height) / 2
            void_sphere = rg.Sphere(void_center, void_radius).ToBrep()
            voids.append(void_sphere)

        # Subtract the voids from the fin
        if voids:
            result = rg.Brep.CreateBooleanDifference([fin_brep], voids, 0.01)
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
    geometry = create_perforated_vertical_landscape(height=3.0, width=1.0, depth=0.5, fin_count=5, fin_thickness=0.1, void_frequency=3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_perforated_vertical_landscape(height=4.0, width=2.0, depth=1.0, fin_count=6, fin_thickness=0.15, void_frequency=2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_perforated_vertical_landscape(height=5.0, width=1.5, depth=0.75, fin_count=8, fin_thickness=0.05, void_frequency=4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_perforated_vertical_landscape(height=2.5, width=1.2, depth=0.6, fin_count=4, fin_thickness=0.2, void_frequency=5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_perforated_vertical_landscape(height=6.0, width=2.5, depth=1.2, fin_count=7, fin_thickness=0.08, void_frequency=6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
