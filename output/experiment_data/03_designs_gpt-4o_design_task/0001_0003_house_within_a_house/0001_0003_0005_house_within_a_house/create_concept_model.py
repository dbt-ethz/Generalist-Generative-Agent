# Created for 0001_0003_house_within_a_house.json

""" Summary:
The function `create_concept_model` generates an architectural concept model that embodies the "House within a house" metaphor by creating a layered structure. It defines an inner sanctuary with specified dimensions and an outer protective layer that encapsulates the inner space, promoting duality. The model utilizes the Rhino.Geometry library to create 3D geometries, including a staircase to enhance spatial connections and movement between layers. By employing contrasting dimensions and a boolean difference operation, the function visually represents the interplay between public and private realms, effectively illustrating the nested spatial hierarchy and varied experiences inherent in the design task."""

#! python 3
function_code = """def create_concept_model(inner_length, inner_width, inner_height, outer_thickness, seed=42):
    \"""
    Creates an architectural Concept Model embodying the 'House within a house' metaphor.
    
    Parameters:
    - inner_length (float): The length of the inner sanctuary.
    - inner_width (float): The width of the inner sanctuary.
    - inner_height (float): The height of the inner sanctuary.
    - outer_thickness (float): The thickness of the outer protective layer.
    - seed (int): Seed for randomness to ensure replicable results.
    
    Returns:
    - List: A list of 3D geometries (breps) representing the Concept Model.
    \"""
    import Rhino.Geometry as rg
    import random
    
    random.seed(seed)
    
    # Create the inner sanctuary
    inner_box = rg.Box(rg.Plane.WorldXY, rg.Interval(0, inner_length), rg.Interval(0, inner_width), rg.Interval(0, inner_height))
    inner_brep = inner_box.ToBrep()
    
    # Create the outer protective layer
    outer_length = inner_length + 2 * outer_thickness
    outer_width = inner_width + 2 * outer_thickness
    outer_height = inner_height + 2 * outer_thickness
    
    outer_box = rg.Box(rg.Plane.WorldXY, rg.Interval(-outer_thickness, outer_length - outer_thickness), 
                       rg.Interval(-outer_thickness, outer_width - outer_thickness), 
                       rg.Interval(-outer_thickness, outer_height - outer_thickness))
    outer_brep = outer_box.ToBrep()
    
    # Subtract the inner sanctuary from the outer layer to create a hollow space
    hollow_outer_brep = rg.Brep.CreateBooleanDifference([outer_brep], [inner_brep], 0.01)
    if hollow_outer_brep:
        hollow_outer_brep = hollow_outer_brep[0]
    
    # Create interlocking geometries (e.g., a central staircase)
    staircase_width = inner_width / 4
    staircase_length = inner_length / 2
    staircase_height = inner_height
    
    staircase = rg.Box(rg.Plane.WorldXY, rg.Interval(inner_length/4, inner_length/4 + staircase_length), 
                       rg.Interval(inner_width/2 - staircase_width/2, inner_width/2 + staircase_width/2), 
                       rg.Interval(0, staircase_height))
    staircase_brep = staircase.ToBrep()
    
    # Generate the final list of geometries
    geometries = [hollow_outer_brep, inner_brep, staircase_brep]
    
    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_concept_model(inner_length=10.0, inner_width=8.0, inner_height=6.0, outer_thickness=2.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_concept_model(inner_length=15.0, inner_width=10.0, inner_height=8.0, outer_thickness=3.0, seed=100)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_concept_model(inner_length=12.0, inner_width=9.0, inner_height=5.0, outer_thickness=1.5, seed=56)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_concept_model(inner_length=20.0, inner_width=15.0, inner_height=10.0, outer_thickness=4.0, seed=77)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_concept_model(inner_length=5.0, inner_width=4.0, inner_height=3.0, outer_thickness=1.0, seed=20)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
