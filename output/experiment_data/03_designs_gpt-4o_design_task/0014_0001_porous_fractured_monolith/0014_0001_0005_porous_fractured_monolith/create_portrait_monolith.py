# Created for 0014_0001_porous_fractured_monolith.json

""" Summary:
The `create_portrait_monolith` function generates an architectural concept model based on the metaphor of a "Porous fractured monolith." It constructs a solid block representing the monolithic form, then introduces strategically placed, irregular voids to embody the porous and fractured qualities. The function uses random parameters to create varied void shapes, ensuring each model maintains a dynamic interplay of light and shadow, reflecting the metaphor's duality of solidity and permeability. By facilitating connections between interior and exterior spaces, the model enhances flow and interaction while embodying the intricate spatial relationships inherent in the design task."""

#! python 3
function_code = """def create_portrait_monolith(base_length, base_width, base_height, num_voids, void_depth, seed):
    \"""
    Creates an architectural Concept Model embodying the 'Porous fractured monolith' metaphor.
    
    This function generates a monolithic block with strategically placed voids to represent the porous, fractured quality while maintaining a balance between solid and void. The voids are irregular, enhancing the dynamic interplay of light, shadow, and spatial relationships.

    Parameters:
    - base_length (float): The length of the monolithic block in meters.
    - base_width (float): The width of the monolithic block in meters.
    - base_height (float): The height of the monolithic block in meters.
    - num_voids (int): The number of voids to cut into the block.
    - void_depth (float): The maximum depth of each void into the block in meters.
    - seed (int): The seed for the random number generator to ensure replicability.

    Returns:
    - list: A list of RhinoCommon Brep objects representing the main solid and voids.
    \"""
    import Rhino.Geometry as rg
    import random

    # Set the random seed
    random.seed(seed)

    # Create the base monolithic block
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
    
    base_faces = rg.Brep.CreateFromBox(base_corners)

    # Create voids by cutting irregular shapes from the monolith
    voids = []
    for _ in range(num_voids):
        # Randomly define the plane for the void
        x = random.uniform(0, base_length)
        y = random.uniform(0, base_width)
        z = random.uniform(0, base_height)
        
        # Define a random direction and size for the void
        dir_vector = rg.Vector3d(random.uniform(-1, 1), random.uniform(-1, 1), random.uniform(-1, 1))
        dir_vector.Unitize()
        
        # Create a box to represent the void
        box_corner1 = rg.Point3d(x, y, z)
        box_corner2 = rg.Point3d(x + void_depth * dir_vector.X, y + void_depth * dir_vector.Y, z + void_depth * dir_vector.Z)
        void_box = rg.Brep.CreateFromBox([box_corner1, box_corner2])
        
        # Subtract the void from the base block
        if void_box:
            base_faces = rg.Brep.CreateBooleanDifference(base_faces, void_box, 0.01)
            voids.append(void_box)
    
    # If the result of the subtraction is a list, take the first element
    if isinstance(base_faces, list):
        base_faces = base_faces[0]

    return [base_faces] + voids"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_portrait_monolith(5.0, 3.0, 2.5, 10, 1.0, 42)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_portrait_monolith(10.0, 5.0, 4.0, 15, 2.0, 100)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_portrait_monolith(7.5, 4.0, 3.0, 8, 1.5, 2023)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_portrait_monolith(6.0, 3.5, 3.0, 12, 1.2, 1987)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_portrait_monolith(8.0, 6.0, 5.0, 20, 2.5, 2021)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
