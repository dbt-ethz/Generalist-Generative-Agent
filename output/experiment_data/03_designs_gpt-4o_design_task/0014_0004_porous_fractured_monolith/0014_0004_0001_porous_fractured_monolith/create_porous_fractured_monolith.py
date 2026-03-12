# Created for 0014_0004_porous_fractured_monolith.json

""" Summary:
The function `create_porous_fractured_monolith` generates an architectural concept model based on the metaphor "Porous fractured monolith" by creating a robust monolithic structure and strategically carving voids into it. It begins by defining a solid rectangular prism that represents the monolith. Then, it randomly generates voids of varying sizes and orientations, which are subtracted from the main mass. This design approach emphasizes the balance between solidity and openness, enhancing natural light and ventilation while creating dynamic paths for exploration within the space. The resulting model visually encapsulates the metaphor's themes of permanence, fluidity, and spatial connectivity."""

#! python 3
function_code = """def create_porous_fractured_monolith(base_length, base_width, base_height, num_voids, seed=42):
    \"""
    Create a conceptual architectural model representing a 'Porous fractured monolith'.
    
    This function generates a monolithic mass and strategically carves out voids to create 
    a balance of solidity and permeability. The voids vary in size and orientation, 
    providing a sense of complexity and dynamism.

    Parameters:
    - base_length (float): The length of the monolithic base in meters.
    - base_width (float): The width of the monolithic base in meters.
    - base_height (float): The height of the monolithic base in meters.
    - num_voids (int): The number of voids to carve out from the base.
    - seed (int): Seed for the random number generator to ensure replicability.

    Returns:
    - List of RhinoCommon Brep objects representing the 3D geometries of the concept model.
    \"""
    import Rhino.Geometry as rg
    import random

    # Set the random seed for replicability
    random.seed(seed)

    # Create the main monolithic block
    base_corners = [
        rg.Point3d(0, 0, 0),
        rg.Point3d(base_length, 0, 0),
        rg.Point3d(base_length, base_width, 0),
        rg.Point3d(0, base_width, 0),
        rg.Point3d(0, 0, base_height),
        rg.Point3d(base_length, 0, base_height),
        rg.Point3d(base_length, base_width, base_height),
        rg.Point3d(0, base_width, base_height)
    ]
    monolith_brep = rg.Brep.CreateFromBox(base_corners)

    voids = []

    # Create voids by subtracting smaller random boxes from the monolith
    for _ in range(num_voids):
        void_length = random.uniform(base_length * 0.1, base_length * 0.4)
        void_width = random.uniform(base_width * 0.1, base_width * 0.4)
        void_height = random.uniform(base_height * 0.1, base_height * 0.4)

        void_x = random.uniform(0, base_length - void_length)
        void_y = random.uniform(0, base_width - void_width)
        void_z = random.uniform(0, base_height - void_height)

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
        void_brep = rg.Brep.CreateFromBox(void_corners)
        voids.append(void_brep)

    # Subtract voids from the monolithic brep
    for void in voids:
        result = rg.Brep.CreateBooleanDifference(monolith_brep, void, 0.001)
        if result:  # Check if the result is not empty
            monolith_brep = result[0]

    return [monolith_brep]"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_porous_fractured_monolith(10.0, 5.0, 3.0, 7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_porous_fractured_monolith(15.0, 8.0, 4.0, 10, seed=24)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_porous_fractured_monolith(12.0, 6.0, 5.0, 5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_porous_fractured_monolith(20.0, 10.0, 6.0, 12, seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_porous_fractured_monolith(8.0, 4.0, 2.0, 3, seed=10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
