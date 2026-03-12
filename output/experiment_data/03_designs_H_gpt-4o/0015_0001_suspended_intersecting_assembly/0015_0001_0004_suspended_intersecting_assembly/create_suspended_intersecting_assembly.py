# Created for 0015_0001_suspended_intersecting_assembly.json

""" Summary:
The function `create_suspended_intersecting_assembly` generates an architectural concept model inspired by the metaphor of "Suspended intersecting assembly." It creates a series of lightweight, wireframe structures that appear to float and intersect within a defined space, embodying lightness and fluidity. By randomizing the size, position, and orientation of each component, the function produces a dynamic network of interconnections that suggests movement and balance. The use of transparent surfaces enhances the visual effect of suspension, while the overall geometry reflects a delicate interplay between form and space, aligning with the metaphor's emphasis on structural transparency and connectivity."""

#! python 3
function_code = """def create_suspended_intersecting_assembly(num_elements, max_dimension, seed=42):
    \"""
    Generate an architectural Concept Model embodying the 'Suspended intersecting assembly' metaphor.

    This function creates a series of intersecting wireframe structures and transparent surfaces
    that appear to float and intersect within a defined space. The design emphasizes lightness,
    fluidity, and structural transparency by using lightweight and delicate elements.

    Parameters:
    - num_elements (int): Number of wireframe and surface elements to create.
    - max_dimension (float): Maximum dimension for the bounding box of the elements.
    - seed (int, optional): Seed for random number generation to ensure replicability.

    Returns:
    - List of Rhino.Geometry.Brep: A list of 3D geometries representing the concept model.
    \"""
    import Rhino.Geometry as rg
    import random
    import math

    # Set the random seed for repeatability
    random.seed(seed)

    # Initialize a list to hold the resulting Breps
    breps = []

    # Base plane for element creation
    base_plane = rg.Plane.WorldXY

    for _ in range(num_elements):
        # Randomize the size and position of each wireframe
        width = random.uniform(0.1, max_dimension * 0.3)
        height = random.uniform(0.1, max_dimension * 0.3)
        length = random.uniform(0.1, max_dimension * 0.3)

        x_translation = random.uniform(-max_dimension / 2, max_dimension / 2)
        y_translation = random.uniform(-max_dimension / 2, max_dimension / 2)
        z_translation = random.uniform(0, max_dimension)

        # Create a wireframe box
        box = rg.Box(base_plane, rg.Interval(0, width), rg.Interval(0, height), rg.Interval(0, length))
        wireframe = box.ToBrep().GetWireframe(0.01)

        # Randomize rotation in space
        rotation_angle = math.radians(random.uniform(0, 360))
        rotation_axis = rg.Vector3d(random.uniform(-1, 1), random.uniform(-1, 1), random.uniform(-1, 1))
        rotation_axis.Unitize()

        rotation_transform = rg.Transform.Rotation(rotation_angle, rotation_axis, rg.Point3d.Origin)

        # Apply translation and rotation to the wireframe
        translation_transform = rg.Transform.Translation(x_translation, y_translation, z_translation)
        for curve in wireframe:
            curve.Transform(translation_transform)
            curve.Transform(rotation_transform)

        # Create transparent surface from wireframe for visual effect
        for curve in wireframe:
            surface = rg.Brep.CreatePlanarBreps(curve, 0.01)
            if surface:
                breps.extend(surface)

    return breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_suspended_intersecting_assembly(10, 5.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_suspended_intersecting_assembly(15, 3.0, seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_suspended_intersecting_assembly(20, 4.5, seed=123)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_suspended_intersecting_assembly(25, 6.0, seed=77)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_suspended_intersecting_assembly(30, 2.5, seed=56)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
