# Created for 0019_0001_subterranean_cavern.json

""" Summary:
The provided function, `create_subterranean_cavern_model`, generates an architectural concept model inspired by the metaphor of a subterranean cavern. It creates organic forms through random placement of interconnected chambers, simulating the undulating and irregular shapes found in natural caves. By adjusting parameters like base radius, height variation, and chamber count, the model achieves varied spatial qualities, reflecting intimacy and exploration. The function employs random deformations to enhance the organic feel, while the resulting geometries can be visualized to capture the mysterious and immersive essence of a cavernous environment, effectively embodying the design task outlined in the metaphor."""

#! python 3
function_code = """def create_subterranean_cavern_model(base_radius=10.0, height_variation=5.0, chamber_count=5, seed=42):
    \"""
    Generates a concept model representing a subterranean cavern using organic, curvilinear forms with varied levels.
    
    Parameters:
    base_radius (float): The base radius for the cavernous forms, representing the scale of the spaces.
    height_variation (float): Maximum variation in height to create undulating ceiling and floor levels.
    chamber_count (int): The number of interconnected chambers to form the model.
    seed (int): Seed for the random number generator to ensure replicability.
    
    Returns:
    List[Rhino.Geometry.Brep]: A list of Breps representing the 3D geometry of the concept model.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    random.seed(seed)
    geometries = []
    
    # Create base point for the cavern
    base_center = rg.Point3d(0, 0, 0)

    for i in range(chamber_count):
        # Generate random angles and distances for chamber placement
        angle = random.uniform(0, 2 * math.pi)
        distance = random.uniform(base_radius * 0.5, base_radius * 1.5)
        height_offset = random.uniform(-height_variation, height_variation)
        
        # Determine the center for each chamber
        chamber_center = rg.Point3d(
            base_center.X + distance * math.cos(angle),
            base_center.Y + distance * math.sin(angle),
            height_offset
        )
        
        # Create an organic shape using a sphere as a base and deforming it
        sphere = rg.Sphere(chamber_center, random.uniform(base_radius * 0.5, base_radius))
        sphere_brep = sphere.ToBrep()
        
        # Apply random deformations to the sphere to mimic organic forms
        deform_factor = random.uniform(0.8, 1.2)
        deform_vector = rg.Vector3d(random.uniform(-1, 1), random.uniform(-1, 1), random.uniform(-1, 1))
        deform_vector.Unitize()
        deform_vector *= deform_factor
        deform_point = chamber_center + deform_vector
        
        # Morph the sphere to create an organic shape
        morphed_brep = sphere_brep.DuplicateBrep()
        translation = rg.Transform.Translation(deform_vector)
        morphed_brep.Transform(translation)
        
        # Add the morphed brep to the list of geometries
        geometries.append(morphed_brep)
    
    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_subterranean_cavern_model(base_radius=15.0, height_variation=10.0, chamber_count=7, seed=123)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_subterranean_cavern_model(base_radius=12.0, height_variation=6.0, chamber_count=4, seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_subterranean_cavern_model(base_radius=8.0, height_variation=3.0, chamber_count=6, seed=56)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_subterranean_cavern_model(base_radius=20.0, height_variation=8.0, chamber_count=10, seed=77)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_subterranean_cavern_model(base_radius=9.0, height_variation=4.0, chamber_count=3, seed=10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
