# Created for 0014_0002_porous_fractured_monolith.json

""" Summary:
The provided function generates an architectural concept model of a "Porous fractured monolith" by starting with a solid base form and introducing a network of voids. It creates a cohesive monolithic structure characterized by varying sizes and orientations of voids that penetrate deeply, reflecting the metaphor's duality of weight and lightness. The function employs layering techniques to ensure these voids enhance light penetration and airflow, promoting interactions between interior and exterior spaces. By utilizing randomness in the void creation, the model accentuates complexity and spatial discovery, ultimately fostering movement and engagement throughout the design."""

#! python 3
function_code = """def generate_fractured_monolith(base_length=30, base_width=20, base_height=15, fracture_levels=3, seed=42):
    \"""
    Creates an architectural Concept Model of a 'Porous fractured monolith'.
    
    This function generates a solid, monolithic form and introduces a series of layered fractures
    that penetrate deeply into the form. The fractures create a network of interconnected spaces,
    promoting light penetration and airflow, and emphasizing the fractured quality.

    Parameters:
        base_length (float): Length of the base monolith in meters.
        base_width (float): Width of the base monolith in meters.
        base_height (float): Height of the base monolith in meters.
        fracture_levels (int): Number of layered fracture levels to create.
        seed (int): Seed for randomness to ensure replicability.

    Returns:
        list: A list of Rhino.Geometry.Brep objects representing the fractured monolithic form.
    \"""
    import Rhino.Geometry as rg
    import random

    random.seed(seed)
    
    # Create the base monolithic form
    base_box = rg.Box(rg.Plane.WorldXY, rg.Interval(0, base_length), rg.Interval(0, base_width), rg.Interval(0, base_height))
    base_brep = base_box.ToBrep()

    voids = []

    # Generate layered fractures
    for level in range(fracture_levels):
        layer_height = base_height / fracture_levels
        for i in range(2):  # Create two voids per level
            void_length = random.uniform(base_length * 0.3, base_length * 0.6)
            void_width = random.uniform(base_width * 0.3, base_width * 0.6)
            void_height = layer_height * random.uniform(0.5, 1.0)

            void_x = random.uniform(0, base_length - void_length)
            void_y = random.uniform(0, base_width - void_width)
            void_z = level * layer_height

            # Create a void box
            void_box = rg.Box(rg.Plane.WorldXY, rg.Interval(void_x, void_x + void_length), rg.Interval(void_y, void_y + void_width), rg.Interval(void_z, void_z + void_height))
            void_brep = void_box.ToBrep()
            
            # Add the void to the list
            voids.append(void_brep)

    # Subtract the voids from the base form
    fractured_monolith = base_brep
    for void in voids:
        result = rg.Brep.CreateBooleanDifference([fractured_monolith], [void], 0.01)
        if result:
            fractured_monolith = result[0]

    return [fractured_monolith]"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = generate_fractured_monolith(40, 25, 20, 5, 100)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = generate_fractured_monolith(50, 30, 25, 4, 10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = generate_fractured_monolith(35, 22, 18, 6, 7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = generate_fractured_monolith(45, 28, 22, 3, 99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = generate_fractured_monolith(32, 18, 12, 2, 2023)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
