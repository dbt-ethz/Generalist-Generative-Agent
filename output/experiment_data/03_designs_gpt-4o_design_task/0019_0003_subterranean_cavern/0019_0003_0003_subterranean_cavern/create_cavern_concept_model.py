# Created for 0019_0003_subterranean_cavern.json

""" Summary:
The function `create_cavern_concept_model` generates an architectural concept model inspired by the metaphor of a subterranean cavern. It creates a low-profile exterior that blends into the landscape, representing concealment. The model features interconnected chambers of varying shapes and sizes, mimicking the irregularity of natural caves and fostering a sense of exploration. By using a combination of smooth and rough materials in the model's geometry, it reflects the contrast between hidden and revealed spaces. The function incorporates randomized dimensions and positions for the chambers, enhancing the surprise and discovery elements within the design, ultimately evoking an immersive experience akin to exploring a cavern."""

#! python 3
function_code = """def create_cavern_concept_model(length, width, height, num_chambers, seed=42):
    \"""
    Create an architectural Concept Model based on the 'subterranean cavern' metaphor.
    
    This function generates a model that features a low-profile exterior and a complex,
    interconnected interior with varying volumes, mimicking the irregularity of natural caves.
    
    Parameters:
    - length (float): The overall length of the concept model in meters.
    - width (float): The overall width of the concept model in meters.
    - height (float): The maximum height of the concept model in meters.
    - num_chambers (int): The number of interconnected volumes within the model.
    - seed (int): Seed for random number generation to ensure replicability.
    
    Returns:
    - list: A list of RhinoCommon Brep objects representing the 3D geometries of the model.
    \"""
    import Rhino.Geometry as rg
    import random
    
    random.seed(seed)
    
    # Define the base level for the exterior (to simulate a low profile)
    base_level = height * 0.2
    
    # Create the low-profile exterior
    exterior_profile = rg.Brep.CreateFromBox(rg.BoundingBox(rg.Point3d(0, 0, 0), rg.Point3d(length, width, base_level)))
    
    # Initialize list to store geometries
    geometries = [exterior_profile]
    
    # Generate chambers within the model
    for _ in range(num_chambers):
        chamber_length = random.uniform(length * 0.1, length * 0.3)
        chamber_width = random.uniform(width * 0.1, width * 0.3)
        chamber_height = random.uniform(height * 0.3, height * 0.7)
        
        # Randomly position chambers within the exterior bounds
        x_position = random.uniform(0, length - chamber_length)
        y_position = random.uniform(0, width - chamber_width)
        z_position = random.uniform(base_level, height - chamber_height)
        
        # Create an organic chamber shape using a lofted surface or a mesh
        chamber_profile1 = rg.Circle(rg.Plane.WorldXY, random.uniform(chamber_width * 0.4, chamber_width * 0.6)).ToNurbsCurve()
        chamber_profile2 = rg.Circle(rg.Plane(rg.Point3d(0, 0, chamber_height), rg.Vector3d.ZAxis), random.uniform(chamber_length * 0.4, chamber_length * 0.6)).ToNurbsCurve()
        
        loft = rg.Brep.CreateFromLoft([chamber_profile1, chamber_profile2], rg.Point3d.Unset, rg.Point3d.Unset, rg.LoftType.Straight, False)
        if loft:
            transformed_loft = loft[0].DuplicateBrep()
            transformation = rg.Transform.Translation(x_position, y_position, z_position)
            transformed_loft.Transform(transformation)
            geometries.append(transformed_loft)
    
    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_cavern_concept_model(30.0, 20.0, 10.0, 5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_cavern_concept_model(50.0, 30.0, 15.0, 8, seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_cavern_concept_model(40.0, 25.0, 12.0, 7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_cavern_concept_model(60.0, 35.0, 20.0, 10, seed=7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_cavern_concept_model(45.0, 28.0, 18.0, 6, seed=12)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
