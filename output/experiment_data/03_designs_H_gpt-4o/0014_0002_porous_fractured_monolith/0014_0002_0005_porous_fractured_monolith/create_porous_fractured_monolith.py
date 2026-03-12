# Created for 0014_0002_porous_fractured_monolith.json

""" Summary:
The provided function, `create_porous_fractured_monolith`, generates an architectural concept model based on the metaphor of a "Porous fractured monolith." It starts by creating a solid, monolithic geometric form as a base. The function then introduces multiple layers of voids that penetrate this solid structure, emphasizing the metaphor's themes of mass and fragmentation. Each void varies in size and orientation, fostering spatial connections and enhancing light penetration. This design approach reflects the duality of heaviness and lightness, encouraging movement and interaction between spaces while showcasing the interplay between the solid mass and dynamic voids."""

#! python 3
function_code = """def create_porous_fractured_monolith(base_length=30, base_width=20, base_height=10, void_layers=3, seed=42):
    \"""
    Creates an architectural Concept Model of a 'Porous fractured monolith'.

    The function begins with a solid, monolithic form and introduces layers of voids
    that penetrate the form, creating a sense of permeability and progression. 
    The void layers vary in size and orientation, emphasizing spatial connections 
    and light penetration. The focus is on creating a sense of movement and interaction 
    through interconnected voids.

    Parameters:
        base_length (float): Length of the base monolith in meters.
        base_width (float): Width of the base monolith in meters.
        base_height (float): Height of the base monolith in meters.
        void_layers (int): Number of layers of voids to create within the monolith.
        seed (int): Seed for randomness to ensure replicability.

    Returns:
        List[Rhino.Geometry.Brep]: A list of 3D Brep geometries representing the monolithic form with voids.
    \"""
    import Rhino.Geometry as rg
    import random

    random.seed(seed)
    
    # Create the base monolithic form
    base_box = rg.Box(rg.Plane.WorldXY, rg.Interval(0, base_length), rg.Interval(0, base_width), rg.Interval(0, base_height))
    base_brep = base_box.ToBrep()
    
    voids = []
    layer_height = base_height / void_layers
    
    # Generate layers of voids
    for i in range(void_layers):
        # Layer-specific properties
        height_offset = i * layer_height
        void_length = random.uniform(0.2 * base_length, 0.5 * base_length)
        void_width = random.uniform(0.2 * base_width, 0.5 * base_width)
        void_height = random.uniform(0.6 * layer_height, layer_height)
        
        void_x = random.uniform(0, base_length - void_length)
        void_y = random.uniform(0, base_width - void_width)
        void_z = height_offset
        
        # Create a void box for the layer
        void_box = rg.Box(rg.Plane.WorldXY, rg.Interval(void_x, void_x + void_length), rg.Interval(void_y, void_y + void_width), rg.Interval(void_z, void_z + void_height))
        void_brep = void_box.ToBrep()
        
        # Add the void to the list
        voids.append(void_brep)
    
    # Subtract the voids from the base form
    porous_monolith = base_brep
    for void in voids:
        result = rg.Brep.CreateBooleanDifference([porous_monolith], [void], 0.01)
        if result:
            porous_monolith = result[0]
    
    return [porous_monolith]"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_porous_fractured_monolith(base_length=40, base_width=25, base_height=15, void_layers=5, seed=123)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_porous_fractured_monolith(base_length=50, base_width=30, base_height=20, void_layers=4, seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_porous_fractured_monolith(base_length=35, base_width=22, base_height=12, void_layers=6, seed=56)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_porous_fractured_monolith(base_length=45, base_width=28, base_height=18, void_layers=7, seed=84)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_porous_fractured_monolith(base_length=32, base_width=18, base_height=11, void_layers=2, seed=77)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
