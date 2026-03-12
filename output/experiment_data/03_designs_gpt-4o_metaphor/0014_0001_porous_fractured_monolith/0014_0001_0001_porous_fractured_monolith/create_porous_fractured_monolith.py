# Created for 0014_0001_porous_fractured_monolith.json

""" Summary:
The function `create_porous_fractured_monolith` generates an architectural concept model inspired by the metaphor "Porous fractured monolith." It creates a solid monolithic structure defined by specified dimensions, which embodies unity and strength. This structure is then punctuated by randomly generated voids, enhancing permeability and allowing light and air to flow through, thereby facilitating interaction between spaces. Additionally, fractures are introduced to reflect the metaphor's complexity and movement, creating a dynamic form. The result is a collection of geometries that visually represent the duality of solidity and openness characteristic of the metaphor."""

#! python 3
function_code = """def create_porous_fractured_monolith(base_length, base_width, base_height, void_count, seed=42):
    \"""
    Creates an architectural Concept Model representing a 'Porous fractured monolith'.
    
    This model combines a unified monolithic form with voids and fractures that introduce lightness and permeability.
    The form allows for interaction between interior and exterior spaces and introduces complexity through deliberate 
    irregular division.

    Parameters:
    - base_length (float): The length of the monolithic base in meters.
    - base_width (float): The width of the monolithic base in meters.
    - base_height (float): The height of the monolithic base in meters.
    - void_count (int): The number of voids to introduce into the monolith.
    - seed (int, optional): Seed for random number generation to ensure replicability.

    Returns:
    - list: A list of RhinoCommon Brep objects representing the solid and void geometries of the concept model.
    \"""
    
    import Rhino.Geometry as rg
    import random
    
    random.seed(seed)
    
    # Create the monolithic base as a box
    base_box = rg.Box(rg.Plane.WorldXY, rg.Interval(0, base_length), rg.Interval(0, base_width), rg.Interval(0, base_height))
    base_brep = base_box.ToBrep()
    
    # Generate voids within the monolith
    voids = []
    for _ in range(void_count):
        void_length = random.uniform(base_length * 0.1, base_length * 0.3)
        void_width = random.uniform(base_width * 0.1, base_width * 0.3)
        void_height = random.uniform(base_height * 0.1, base_height * 0.3)
        
        void_x = random.uniform(0, base_length - void_length)
        void_y = random.uniform(0, base_width - void_width)
        void_z = random.uniform(0, base_height - void_height)
        
        void_box = rg.Box(rg.Plane.WorldXY, rg.Interval(void_x, void_x + void_length), 
                          rg.Interval(void_y, void_y + void_width), 
                          rg.Interval(void_z, void_z + void_height))
        void_brep = void_box.ToBrep()
        voids.append(void_brep)
    
    # Subtract the voids from the base
    porous_monolith = base_brep
    for void in voids:
        diff_result = rg.Brep.CreateBooleanDifference([porous_monolith], [void], 0.01)
        if diff_result:  # Check if the result is not empty
            porous_monolith = diff_result[0]
    
    # Introduce fractures
    fractures = []
    fracture_count = int(void_count / 2)  # Half the number of voids as fractures
    for _ in range(fracture_count):
        # Random planes to create fractures
        fracture_plane = rg.Plane(
            rg.Point3d(random.uniform(0, base_length), random.uniform(0, base_width), random.uniform(0, base_height)),
            rg.Vector3d(random.uniform(-1, 1), random.uniform(-1, 1), random.uniform(-1, 1))
        )
        
        # Fracture surface
        fracture_surface = rg.PlaneSurface(fracture_plane, rg.Interval(-base_length, base_length), rg.Interval(-base_height, base_height))
        fracture_brep = fracture_surface.ToBrep()
        
        # Cut the monolith with the fracture
        fracture_result = rg.Brep.CreateBooleanDifference([porous_monolith], [fracture_brep], 0.01)
        if fracture_result:  # Check if the result is not empty
            porous_monolith = fracture_result[0]
    
    return [porous_monolith]"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_porous_fractured_monolith(10.0, 5.0, 3.0, 4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_porous_fractured_monolith(8.0, 4.0, 2.5, 6, seed=123)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_porous_fractured_monolith(12.0, 6.0, 4.0, 5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_porous_fractured_monolith(15.0, 7.0, 5.0, 8, seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_porous_fractured_monolith(9.0, 4.5, 3.5, 3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
