# Created for 0001_0002_house_within_a_house.json

""" Summary:
The provided function generates an architectural concept model based on the "House within a house" metaphor by creating a layered structure with concentric forms. It begins by defining an outer protective shell and an inner sanctuary, embodying the idea of nesting and protection. Through randomization, it adds voids that serve as courtyards, facilitating light and movement, thereby enhancing the spatial experience. The use of varying radii and heights allows for a dynamic interplay between openness and enclosure. The resulting 3D geometries visually represent a hierarchical spatial organization, inviting exploration and interaction, thus effectively conveying the metaphor."""

#! python 3
function_code = """def create_concept_model(seed: int, outer_radius: float, inner_radius: float, height: float, shell_thickness: float):
    \"""
    Create an architectural Concept Model based on the 'House within a house' metaphor.
    
    This function generates a 3D model consisting of concentric or interlocking layers
    that evoke a sense of containment and gradual discovery. The model includes an outer
    protective shell and an inner sanctuary, with transitional zones and voids that encourage
    exploration and interaction with the layered environment.

    Parameters:
    - seed (int): Seed for random number generation to ensure replicability.
    - outer_radius (float): The radius of the outer shell of the model.
    - inner_radius (float): The radius of the inner sanctuary or core.
    - height (float): The uniform height of the model.
    - shell_thickness (float): The thickness of the outer shell layer.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of 3D Brep geometries representing the concept model.
    \"""
    import Rhino
    import Rhino.Geometry as rg
    import random

    # Set the random seed for replicability
    random.seed(seed)

    # Create the outer shell as a cylindrical shell
    outer_cylinder = rg.Cylinder(rg.Circle(rg.Point3d(0, 0, 0), outer_radius), height)
    outer_brep = outer_cylinder.ToBrep(True, True)

    # Create the inner sanctuary as a cylinder
    inner_cylinder = rg.Cylinder(rg.Circle(rg.Point3d(0, 0, 0), inner_radius), height)
    inner_brep = inner_cylinder.ToBrep(True, True)

    # Subtract the inner cylinder from the outer shell to create a hollow shell
    shell_brep = rg.Brep.CreateBooleanDifference([outer_brep], [inner_brep], 0.01)
    if not shell_brep:
        return []  # Return an empty list if the boolean difference fails

    shell_brep = shell_brep[0]

    # Create voids or courtyards as spheres randomly placed within the outer shell
    void_count = random.randint(2, 4)
    voids = []
    for _ in range(void_count):
        void_radius = random.uniform(inner_radius * 0.2, inner_radius * 0.4)
        void_center = rg.Point3d(random.uniform(-outer_radius + void_radius, outer_radius - void_radius),
                                 random.uniform(-outer_radius + void_radius, outer_radius - void_radius),
                                 random.uniform(0, height))
        void_sphere = rg.Sphere(void_center, void_radius)
        voids.append(void_sphere.ToBrep())

    # Subtract voids from the shell to create courtyards
    final_shell = shell_brep
    if voids:
        final_shell_result = rg.Brep.CreateBooleanDifference([shell_brep], voids, 0.01)
        if final_shell_result:
            final_shell = final_shell_result[0]

    # Return the resulting 3D geometries
    return [final_shell, inner_brep] + voids"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_concept_model(seed=42, outer_radius=10.0, inner_radius=5.0, height=15.0, shell_thickness=1.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_concept_model(seed=7, outer_radius=12.0, inner_radius=6.0, height=20.0, shell_thickness=2.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_concept_model(seed=15, outer_radius=8.0, inner_radius=4.0, height=10.0, shell_thickness=1.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_concept_model(seed=25, outer_radius=9.0, inner_radius=3.0, height=12.0, shell_thickness=0.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_concept_model(seed=30, outer_radius=11.0, inner_radius=7.0, height=18.0, shell_thickness=1.2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
