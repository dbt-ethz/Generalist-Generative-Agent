# Created for 0018_0003_perforated_vertical_landscape.json

""" Summary:
The function `create_perforated_vertical_landscape` generates an architectural concept model inspired by the "Perforated vertical landscape" metaphor. It creates a series of vertical fins or ribs that mimic natural formations, integrating voids that allow light and air to permeate through the structure. Parameters such as height, width, and fin characteristics define the model's dimensions and appearance. By randomly determining voids' presence, the function ensures a dynamic interplay of solid and void, reflecting the metaphor's focus on vertical rhythm and spatial adaptability. The resulting geometries visually connect the interior with the surrounding environment, embodying the metaphor's essence."""

#! python 3
function_code = """def create_perforated_vertical_landscape(height, width, depth, fin_count, fin_thickness, fin_spacing, void_probability):
    \"""
    Create an architectural Concept Model based on the 'Perforated vertical landscape' metaphor.
    
    This function generates a structure composed of vertical fins or ribs with interspersed voids.
    The model emphasizes vertical rhythm, texture, and permeability, allowing light, air, and views to penetrate.
    
    Parameters:
    - height (float): The total height of the model in meters.
    - width (float): The overall width of the model in meters.
    - depth (float): The overall depth of the model in meters.
    - fin_count (int): The number of vertical fins or ribs to generate.
    - fin_thickness (float): The thickness of each vertical fin in meters.
    - fin_spacing (float): The spacing between each vertical fin in meters.
    - void_probability (float): The probability (0 to 1) that a section of a fin will be void (open).

    Returns:
    - List[Rhino.Geometry.Brep]: A list of 3D geometries (breps) representing the fins with voids.
    \"""
    import Rhino.Geometry as rg
    import random

    random.seed(42)  # Ensures replicable randomness
    geometries = []

    # Calculate the space required for each fin
    total_fin_width = fin_thickness + fin_spacing

    for i in range(fin_count):
        # Calculate the position of the current fin
        x_position = i * total_fin_width

        if x_position + fin_thickness > width:
            break  # Stop if the fins exceed the specified width

        # Create full height fin
        fin_box = rg.Box(rg.Plane.WorldXY, rg.Interval(x_position, x_position + fin_thickness), rg.Interval(0, depth), rg.Interval(0, height))

        # Subdivide the height of the fin to create potential voids
        subdivisions = int(height / 2)  # Number of subdivisions along the height
        void_sections = []

        for j in range(subdivisions):
            if random.random() < void_probability:
                # Create a void section by removing a part of the fin
                void_height = height / subdivisions
                void_box = rg.Box(rg.Plane.WorldXY, rg.Interval(x_position, x_position + fin_thickness), rg.Interval(0, depth), rg.Interval(j * void_height, (j + 1) * void_height))
                void_sections.append(void_box.ToBrep())

        # Subtract void sections from the fin
        fin_brep = fin_box.ToBrep()
        if void_sections:
            fin_brep = rg.Brep.CreateBooleanDifference([fin_brep], void_sections, 0.01)

        if fin_brep:
            geometries.append(fin_brep)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_perforated_vertical_landscape(height=5.0, width=3.0, depth=1.0, fin_count=10, fin_thickness=0.1, fin_spacing=0.2, void_probability=0.3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_perforated_vertical_landscape(height=6.0, width=4.0, depth=2.0, fin_count=15, fin_thickness=0.15, fin_spacing=0.25, void_probability=0.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_perforated_vertical_landscape(height=7.0, width=5.0, depth=1.5, fin_count=8, fin_thickness=0.2, fin_spacing=0.3, void_probability=0.4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_perforated_vertical_landscape(height=4.0, width=2.5, depth=1.2, fin_count=12, fin_thickness=0.05, fin_spacing=0.15, void_probability=0.2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_perforated_vertical_landscape(height=8.0, width=6.0, depth=2.5, fin_count=20, fin_thickness=0.2, fin_spacing=0.3, void_probability=0.6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
