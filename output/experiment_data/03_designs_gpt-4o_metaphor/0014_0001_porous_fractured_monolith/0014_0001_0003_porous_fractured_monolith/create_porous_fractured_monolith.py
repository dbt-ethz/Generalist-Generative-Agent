# Created for 0014_0001_porous_fractured_monolith.json

""" Summary:
The function `create_porous_fractured_monolith` generates an architectural concept model inspired by the metaphor of a "Porous fractured monolith." It creates a solid monolithic form defined by specified dimensions, while introducing voids to enhance permeability and openness, reflecting the metaphor's duality. The function randomly sizes and places these voids within the monolith, fostering interaction between interior and exterior spaces. Additionally, it incorporates fractures, adding complexity and movement, which aligns with the metaphor's emphasis on tension and irregularity. The resulting 3D geometries embody the essence of the metaphor, yielding a cohesive yet dynamic architectural model."""

#! python 3
function_code = """def create_porous_fractured_monolith(base_length, base_width, height, num_voids, void_max_size, fracture_intensity):
    \"""
    Creates an architectural Concept Model based on the metaphor 'Porous fractured monolith'.
    
    The model is characterized by a solid, unified mass that is punctuated by voids, creating a sense of lightness and openness. 
    It also incorporates a fractured aspect, introducing complexity and a sense of movement or tension within the structure.

    Parameters:
    - base_length (float): The length of the base of the monolith in meters.
    - base_width (float): The width of the base of the monolith in meters.
    - height (float): The height of the monolith in meters.
    - num_voids (int): The number of voids to introduce into the monolith.
    - void_max_size (float): The maximum size of the voids in meters.
    - fracture_intensity (float): A value between 0 and 1 representing the intensity of the fracturing effect.

    Returns:
    - List: A list of RhinoCommon Brep objects representing the 3D geometries of the concept model.
    \"""
    import Rhino.Geometry as rg
    import random

    random.seed(42)  # Ensure replicability

    # Create the base solid monolith
    box = rg.Box(rg.Plane.WorldXY, rg.Interval(0, base_length), rg.Interval(0, base_width), rg.Interval(0, height))
    monolith = box.ToBrep()

    # Create voids
    voids = []
    for _ in range(num_voids):
        void_length = random.uniform(0.1, void_max_size)
        void_width = random.uniform(0.1, void_max_size)
        void_height = random.uniform(0.1, void_max_size)

        x = random.uniform(0, base_length - void_length)
        y = random.uniform(0, base_width - void_width)
        z = random.uniform(0, height - void_height)

        void_box = rg.Box(rg.Plane.WorldXY, rg.Interval(x, x + void_length), rg.Interval(y, y + void_width), rg.Interval(z, z + void_height))
        voids.append(void_box.ToBrep())

    # Subtract voids from the monolith
    monolith_with_voids = monolith
    for void in voids:
        result = rg.Brep.CreateBooleanDifference([monolith_with_voids], [void], 0.001)
        if result:  # Check if the result is not empty
            monolith_with_voids = result[0]

    # Introduce fractures
    fractures = []
    num_fractures = int(fracture_intensity * 10)  # Arbitrary scale for number of fractures
    for _ in range(num_fractures):
        fracture_plane = rg.Plane(
            rg.Point3d(random.uniform(0, base_length), random.uniform(0, base_width), random.uniform(0, height)),
            rg.Vector3d(random.uniform(-1, 1), random.uniform(-1, 1), random.uniform(-1, 1))
        )
        fracture_surface = rg.PlaneSurface(fracture_plane, rg.Interval(-base_length, base_length), rg.Interval(-height, height))
        fractures.append(fracture_surface.ToBrep())

    # Apply fractures
    fractured_monolith = monolith_with_voids
    for fracture in fractures:
        result = rg.Brep.CreateBooleanDifference([fractured_monolith], [fracture], 0.001)
        if result:  # Check if the result is not empty
            fractured_monolith = result[0]

    return [fractured_monolith]"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_porous_fractured_monolith(5.0, 3.0, 10.0, 6, 1.5, 0.8)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_porous_fractured_monolith(4.0, 2.5, 8.0, 4, 1.0, 0.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_porous_fractured_monolith(6.0, 4.0, 12.0, 8, 2.0, 0.6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_porous_fractured_monolith(7.0, 5.0, 15.0, 10, 2.5, 0.7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_porous_fractured_monolith(3.0, 2.0, 5.0, 5, 1.0, 0.9)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
