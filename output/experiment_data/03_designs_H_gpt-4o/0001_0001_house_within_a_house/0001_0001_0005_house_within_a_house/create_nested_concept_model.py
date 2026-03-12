# Created for 0001_0001_house_within_a_house.json

""" Summary:
The function `create_nested_concept_model` generates an architectural concept model based on the "House within a house" metaphor by creating a series of nested spherical volumes. Each sphere represents different levels of privacy and function: the innermost sphere symbolizes the core sanctuary, while the outer spheres depict transitional and protective layers. By manipulating the radii of these spheres, the function visually communicates the notion of layered spatial hierarchy, emphasizing the progression from public to private spaces. This approach creatively embodies the metaphor's themes of nesting, protection, and varied spatial experiences through geometry and materiality."""

#! python 3
function_code = """def create_nested_concept_model(inner_sphere_radius=2.0, middle_sphere_radius=4.0, outer_sphere_radius=6.0):
    \"""
    Creates a conceptual architectural model based on the 'House within a house' metaphor using nested spherical volumes.
    
    This function generates a series of nested spherical volumes, each progressively larger than the previous one,
    representing different levels of privacy and function. The innermost sphere is the core sanctuary, while the outer
    spheres suggest permeability and transition from exterior to interior spaces. The model emphasizes the spatial
    hierarchy and protective layering of the design.

    Parameters:
    - inner_sphere_radius: The radius of the innermost sphere, representing the core sanctuary.
    - middle_sphere_radius: The radius of the middle sphere, representing intermediary spaces.
    - outer_sphere_radius: The radius of the outermost sphere, representing the protective shell.

    Returns:
    - A list of Breps representing the nested spherical volumes.
    \"""
    
    import Rhino.Geometry as rg

    # List to store the generated Breps
    breps = []

    # Create the innermost sphere (core sanctuary)
    inner_sphere = rg.Sphere(rg.Point3d(0, 0, 0), inner_sphere_radius)
    inner_brep = inner_sphere.ToBrep()
    breps.append(inner_brep)

    # Create the middle sphere (intermediary space)
    middle_sphere = rg.Sphere(rg.Point3d(0, 0, 0), middle_sphere_radius)
    middle_brep = middle_sphere.ToBrep()
    breps.append(middle_brep)

    # Create the outermost sphere (protective shell)
    outer_sphere = rg.Sphere(rg.Point3d(0, 0, 0), outer_sphere_radius)
    outer_brep = outer_sphere.ToBrep()
    breps.append(outer_brep)

    return breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_nested_concept_model(3.0, 5.0, 7.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_nested_concept_model(1.5, 3.5, 5.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_nested_concept_model(2.5, 4.5, 6.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_nested_concept_model(2.0, 4.0, 8.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_nested_concept_model(2.0, 3.0, 5.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
