# Created for 0014_0005_porous_fractured_monolith.json

""" Summary:
The provided function, `create_porosity_fractured_monolith`, generates an architectural concept model based on the metaphor of a "Porous fractured monolith." It begins by creating a solid base mass, representing the monolithic form, and then introduces a series of voids that vary in size and orientation, embodying the metaphors dynamic and complex nature. By randomly positioning these voids within the solid mass, the function simulates the interplay between solidity and permeability. The resulting model visually captures the balance between robust enclosure and lightness, encouraging spatial exploration and interaction while reflecting the architectural essence of the metaphor."""

#! python 3
function_code = """def create_porosity_fractured_monolith(base_length, base_width, base_height, num_voids, seed):
    import Rhino.Geometry as rg
    import random

    random.seed(seed)

    # Create the base monolithic mass
    base_point = rg.Point3d(0, 0, 0)
    base_box = rg.Box(rg.Plane.WorldXY, rg.Interval(0, base_length), rg.Interval(0, base_width), rg.Interval(0, base_height))
    base_brep = base_box.ToBrep()

    voids = []
    for _ in range(num_voids):
        # Randomly generate position and dimensions for each void
        void_length = random.uniform(base_length * 0.1, base_length * 0.3)
        void_width = random.uniform(base_width * 0.1, base_width * 0.3)
        void_height = random.uniform(base_height * 0.1, base_height * 0.3)

        void_x = random.uniform(0, base_length - void_length)
        void_y = random.uniform(0, base_width - void_width)
        void_z = random.uniform(0, base_height - void_height)

        void_box = rg.Box(rg.Plane.WorldXY, rg.Interval(void_x, void_x + void_length), 
                          rg.Interval(void_y, void_y + void_width), rg.Interval(void_z, void_z + void_height))
        void_brep = void_box.ToBrep()
        
        # Subtract void from the base mass
        result = rg.Brep.CreateBooleanDifference(base_brep, void_brep, 0.01)
        if result:  # Check if result is not empty
            base_brep = result[0]
        voids.append(void_brep)
    
    return [base_brep] + voids"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_porosity_fractured_monolith(10, 5, 2, 3, 42)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_porosity_fractured_monolith(15, 10, 5, 4, 99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_porosity_fractured_monolith(12, 6, 3, 5, 21)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_porosity_fractured_monolith(8, 4, 2, 2, 37)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_porosity_fractured_monolith(20, 10, 8, 6, 56)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
