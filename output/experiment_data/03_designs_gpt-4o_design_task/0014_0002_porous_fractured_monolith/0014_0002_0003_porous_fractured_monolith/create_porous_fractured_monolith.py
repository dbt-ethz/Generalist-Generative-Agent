# Created for 0014_0002_porous_fractured_monolith.json

""" Summary:
The provided function, `create_porous_fractured_monolith`, generates an architectural concept model by starting with a solid, monolithic form and introducing a network of voids that create a "porous fractured monolith." It emphasizes the metaphor's characteristics by varying the size and orientation of the voids, which penetrate deeply into the mass, fostering light penetration and airflow. The function utilizes randomization to position and size the voids, enabling unique spatial configurations. Ultimately, the model illustrates the dynamic interplay between the solid structure and the voids, facilitating movement and interaction within the architectural space."""

#! python 3
function_code = """def create_porous_fractured_monolith(base_length, base_width, base_height, num_voids, seed=42):
    \"""
    Creates an architectural Concept Model of a 'Porous fractured monolith'.
    
    The function starts with a solid, monolithic form and introduces a network of voids 
    that penetrate deeply into the form, emphasizing a fractured quality. The voids vary 
    in size and orientation to create spatial connections and transitions, focusing on 
    light penetration and airflow. The model explores the interplay between the monolithic 
    mass and dynamic voids, creating a spatial experience that encourages movement and 
    interaction.

    Parameters:
    - base_length (float): The length of the base solid in meters.
    - base_width (float): The width of the base solid in meters.
    - num_voids (int): The number of voids to create within the monolithic form.
    - seed (int): Seed for random number generation to ensure replicability.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep geometries representing the solid and voids.
    \"""
    import Rhino.Geometry as rg
    import random
    
    # Set the seed for randomness
    random.seed(seed)

    # Create the base monolithic solid
    base_box = rg.Box(rg.Plane.WorldXY, rg.Interval(0, base_length), rg.Interval(0, base_width), rg.Interval(0, base_height))
    base_brep = base_box.ToBrep()

    voids = []
    for _ in range(num_voids):
        # Randomly determine the location and size of the voids
        void_length = random.uniform(base_length * 0.1, base_length * 0.3)
        void_width = random.uniform(base_width * 0.1, base_width * 0.3)
        void_height = random.uniform(base_height * 0.1, base_height * 0.7)

        # Randomly position the void within the base
        x_pos = random.uniform(0, base_length - void_length)
        y_pos = random.uniform(0, base_width - void_width)
        z_pos = random.uniform(0, base_height - void_height)

        # Create a box as the void
        void_box = rg.Box(rg.Plane.WorldXY, rg.Interval(x_pos, x_pos + void_length),
                          rg.Interval(y_pos, y_pos + void_width), rg.Interval(z_pos, z_pos + void_height))
        
        # Convert to Brep and add to the list
        void_brep = void_box.ToBrep()
        voids.append(void_brep)

    # Subtract voids from the base brep to create the final form
    porous_monolith = base_brep
    for void in voids:
        result = rg.Brep.CreateBooleanDifference([porous_monolith], [void], 0.01)
        if result:
            porous_monolith = result[0]

    return [porous_monolith] + voids"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_porous_fractured_monolith(10, 5, 8, 15)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_porous_fractured_monolith(12, 6, 10, 20, seed=123)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_porous_fractured_monolith(15, 7, 12, 10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_porous_fractured_monolith(8, 4, 6, 25, seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_porous_fractured_monolith(20, 10, 15, 30, seed=2023)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
