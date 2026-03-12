# Created for 0014_0002_porous_fractured_monolith.json

""" Summary:
The function `create_porous_fractured_monolith` generates an architectural concept model inspired by the metaphor "Porous fractured monolith." It begins by creating a solid, monolithic shape using specified dimensions. It then introduces a series of voids that penetrate this form, varying in size and orientation to emphasize the fractured quality. These voids facilitate light penetration and airflow, promoting interaction between interior and exterior spaces. By subtracting the voids from the solid base, the function achieves a complex spatial experience, encapsulating the duality of mass and openness, embodying the metaphor's essence in a tangible model."""

#! python 3
function_code = """def create_porous_fractured_monolith(base_length, base_width, base_height, num_voids, void_max_size, seed=42):
    \"""
    Creates an architectural concept model based on the 'Porous fractured monolith' metaphor.
    
    The function generates a solid monolithic form and introduces a series of voids that penetrate 
    the form, creating interconnected spaces that emphasize light penetration and airflow. The voids 
    are designed to vary in size and orientation, promoting a dynamic spatial experience.
    
    Parameters:
    - base_length (float): The length of the base monolithic form in meters.
    - base_width (float): The width of the base monolithic form in meters.
    - num_voids (int): The number of voids to create within the monolithic form.
    - void_max_size (float): The maximum size of the voids in meters.
    - seed (int): Seed for the random number generator to ensure replicability.
    
    Returns:
    - list: A list of RhinoCommon Brep objects representing the monolithic form and its voids.
    \"""
    import Rhino.Geometry as rg
    import random

    random.seed(seed)
    
    # Base monolithic form
    base_box = rg.Box(rg.Plane.WorldXY, rg.Interval(0, base_length), rg.Interval(0, base_width), rg.Interval(0, base_height))
    base_brep = base_box.ToBrep()
    
    # Generate voids
    voids = []
    for _ in range(num_voids):
        void_length = random.uniform(void_max_size * 0.2, void_max_size)
        void_width = random.uniform(void_max_size * 0.2, void_max_size)
        void_height = random.uniform(void_max_size * 0.2, void_max_size)
        
        void_x = random.uniform(0, base_length - void_length)
        void_y = random.uniform(0, base_width - void_width)
        void_z = random.uniform(0, base_height - void_height)
        
        void_box = rg.Box(rg.Plane.WorldXY, 
                          rg.Interval(void_x, void_x + void_length), 
                          rg.Interval(void_y, void_y + void_width), 
                          rg.Interval(void_z, void_z + void_height))
        void_brep = void_box.ToBrep()
        voids.append(void_brep)
    
    # Subtract voids from the base form
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
    geometry = create_porous_fractured_monolith(10.0, 5.0, 3.0, 15, 2.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_porous_fractured_monolith(8.0, 4.0, 6.0, 10, 1.5, seed=101)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_porous_fractured_monolith(12.0, 6.0, 4.0, 20, 3.0, seed=7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_porous_fractured_monolith(15.0, 7.0, 5.0, 12, 2.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_porous_fractured_monolith(9.0, 4.5, 2.5, 8, 1.0, seed=50)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
