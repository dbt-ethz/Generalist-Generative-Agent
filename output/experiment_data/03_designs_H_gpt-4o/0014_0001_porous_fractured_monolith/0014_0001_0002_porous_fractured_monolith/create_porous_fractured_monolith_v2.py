# Created for 0014_0001_porous_fractured_monolith.json

""" Summary:
The function `create_porous_fractured_monolith_v2` generates an architectural concept model based on the metaphor "Porous fractured monolith." It creates a singular, monolithic block and introduces irregular voids to convey the metaphors duality of solidity and transparency. By randomly determining the size and location of these voids, the function mimics a fractured structure, enhancing the interplay of light and shadow. The voids facilitate spatial connectivity, allowing for movement and interaction within the building. Ultimately, this model embodies the essence of the metaphor, reflecting the complexities of mass and void while promoting an engaging architectural experience."""

#! python 3
function_code = """def create_porous_fractured_monolith_v2(base_length, base_width, base_height, void_count, seed):
    \"""
    Creates an architectural Concept Model embodying the 'Porous fractured monolith' metaphor.

    This function generates a singular monolithic form with dynamic and irregular voids, 
    emphasizing the duality of mass and void, and the interaction of light and shadow.
    The voids are generated using a fractured pattern to suggest permeability and 
    connectivity between spaces.

    Parameters:
    - base_length (float): The length of the monolithic block in meters.
    - base_width (float): The width of the monolithic block in meters.
    - base_height (float): The height of the monolithic block in meters.
    - void_count (int): The number of voids to introduce into the block.
    - seed (int): Seed for random generator to ensure replicability.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of 3D breps representing the fractured monolithic form with voids.
    \"""
    import Rhino.Geometry as rg
    import random

    # Set the seed for reproducibility
    random.seed(seed)

    # Create the base monolithic block
    base_box = rg.Box(rg.Plane.WorldXY, rg.Interval(0, base_length), rg.Interval(0, base_width), rg.Interval(0, base_height))
    base_brep = base_box.ToBrep()

    voids = []

    # Create voids by subtracting irregular shapes from the base block
    for _ in range(void_count):
        # Random dimensions and location for the voids
        void_length = random.uniform(base_length * 0.1, base_length * 0.3)
        void_width = random.uniform(base_width * 0.1, base_width * 0.3)
        void_height = random.uniform(base_height * 0.2, base_height * 0.6)

        void_x = random.uniform(0, base_length - void_length)
        void_y = random.uniform(0, base_width - void_width)
        void_z = random.uniform(0, base_height - void_height)

        # Create an irregular void shape using a combination of boxes
        void_corners = [
            rg.Point3d(void_x, void_y, void_z),
            rg.Point3d(void_x + void_length, void_y, void_z),
            rg.Point3d(void_x + void_length, void_y + void_width, void_z),
            rg.Point3d(void_x, void_y + void_width, void_z),
            rg.Point3d(void_x, void_y, void_z + void_height),
            rg.Point3d(void_x + void_length, void_y, void_z + void_height),
            rg.Point3d(void_x + void_length, void_y + void_width, void_z + void_height),
            rg.Point3d(void_x, void_y + void_width, void_z + void_height)
        ]

        # Create a distorted shape to mimic a fracture
        for corner in void_corners:
            corner.X += random.uniform(-0.5, 0.5)
            corner.Y += random.uniform(-0.5, 0.5)
            corner.Z += random.uniform(-0.5, 0.5)

        void_brep = rg.Brep.CreateFromCornerPoints(void_corners[0], void_corners[1], void_corners[2], void_corners[3], 0.001)
        void_brep = rg.Brep.CreateFromCornerPoints(void_corners[4], void_corners[5], void_corners[6], void_corners[7], 0.001)
        
        # Subtract the voids from the base block
        if void_brep:
            boolean_difference = rg.Brep.CreateBooleanDifference([base_brep], [void_brep], 0.001)
            if boolean_difference:  # Check if the operation succeeded
                base_brep = boolean_difference[0]
                voids.append(void_brep)

    return [base_brep] + voids"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_porous_fractured_monolith_v2(10.0, 5.0, 3.0, 4, 42)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_porous_fractured_monolith_v2(15.0, 7.0, 4.0, 6, 123)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_porous_fractured_monolith_v2(8.0, 4.0, 2.5, 5, 99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_porous_fractured_monolith_v2(12.0, 6.0, 3.5, 3, 2023)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_porous_fractured_monolith_v2(20.0, 10.0, 5.0, 8, 2021)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
