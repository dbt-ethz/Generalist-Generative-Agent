# Created for 0018_0001_perforated_vertical_landscape.json

""" Summary:
The function `create_perforated_vertical_landscape` generates an architectural concept model based on the metaphor of a "Perforated vertical landscape." It creates a solid base structure and integrates perforations that allow light, air, and views to permeate through the form. By controlling the base dimensions and perforation density, the function simulates a rhythmic interplay of solid and void, evoking a vertical landscape. Randomized cylindrical voids are subtracted from the base to achieve the desired perforation effect, resulting in a dynamic geometry that reflects the metaphors essence of interaction between interior and exterior environments."""

#! python 3
function_code = """def create_perforated_vertical_landscape(base_width, base_depth, height, perforation_density, randomness_seed=42):
    \"""
    Creates an architectural Concept Model based on the metaphor 'Perforated vertical landscape'.
    
    The design integrates verticality with porous elements, creating a structure that allows light, air, and views to penetrate through its form.
    It features a rhythmic interplay between solid and void, evoking a natural landscape in a vertical orientation with perforations serving as pathways for interaction.

    Parameters:
    - base_width (float): The width of the base of the structure in meters.
    - base_depth (float): The depth of the base of the structure in meters.
    - height (float): The height of the structure in meters.
    - perforation_density (float): A value between 0 and 1 representing the density of perforations.
    - randomness_seed (int, optional): Seed for the random number generator to ensure replicability. Default is 42.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of 3D geometries representing the concept model.
    \"""
    import Rhino.Geometry as rg
    import random
    
    random.seed(randomness_seed)
    
    # Create the base solid mass
    base_box = rg.Box(rg.Plane.WorldXY, rg.Interval(0, base_width), rg.Interval(0, base_depth), rg.Interval(0, height))
    base_brep = base_box.ToBrep()
    
    # Determine the number of perforations based on density
    num_perforations = int(perforation_density * 10)  # Arbitrary scaling factor for demonstration
    
    perforation_geometries = []
    
    for _ in range(num_perforations):
        # Randomize position within the base box
        x = random.uniform(0, base_width)
        y = random.uniform(0, base_depth)
        z = random.uniform(0, height)
        
        # Create a cylindrical void
        radius = random.uniform(0.5, 1.5)  # Random radius between 0.5 and 1.5 meters
        base_point = rg.Point3d(x, y, 0)
        axis_vector = rg.Vector3d(0, 0, 1)
        axis = rg.Line(base_point, rg.Point3d(x, y, height))
        plane = rg.Plane(base_point, axis_vector)
        cylinder = rg.Cylinder(rg.Circle(plane, radius), height)
        
        # Subtract the void from the base brep
        cylinder_brep = cylinder.ToBrep(True, True)
        perforation_geometries.append(cylinder_brep)
    
    # Create a brep boolean difference to simulate perforation
    perforated_brep = base_brep
    for void in perforation_geometries:
        perforated_brep = rg.Brep.CreateBooleanDifference([perforated_brep], [void], 0.01)[0]
    
    return [perforated_brep]"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_perforated_vertical_landscape(10, 5, 20, 0.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_perforated_vertical_landscape(15, 10, 30, 0.3, randomness_seed=24)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_perforated_vertical_landscape(12, 8, 25, 0.7, randomness_seed=100)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_perforated_vertical_landscape(20, 15, 40, 0.6, randomness_seed=10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_perforated_vertical_landscape(8, 4, 15, 0.4, randomness_seed=56)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
