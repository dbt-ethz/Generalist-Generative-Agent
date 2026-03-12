# Created for 0020_0004_stacked_forests.json

""" Summary:
The provided function `create_stacked_forests_concept_model` generates an architectural concept model inspired by the "Stacked forests" metaphor. It constructs a lattice-like structure through interwoven vertical and horizontal elements, mimicking the intertwined roots and branches of a forest. The function utilizes parameters for base size, height levels, and densities to create a diverse range of geometries, including cylindrical trunks and canopy-like surfaces. This approach encapsulates the complex spatial relationships and layered intersections typical of a forest, fostering exploration and dynamic interaction. The result is a richly textured silhouette that embodies the organic growth and connectivity found in natural ecosystems."""

#! python 3
function_code = """def create_stacked_forests_concept_model(base_size=10, height_levels=5, horizontal_density=3, vertical_density=3):
    \"""
    Creates an architectural Concept Model embodying the 'Stacked forests' metaphor by developing a lattice-like structure 
    composed of interwoven horizontal and vertical elements. The function returns a list of 3D geometries representing 
    the model, using a combination of rectilinear and organic shapes to reflect the natural complexity and order found in 
    forest ecosystems.

    Inputs:
        base_size (float): The size of the base square in meters.
        height_levels (int): The number of vertical layers or levels.
        horizontal_density (int): The number of horizontal elements per layer.
        vertical_density (int): The number of vertical elements per layer.

    Outputs:
        List[Rhino.Geometry.Brep]: A list of Brep geometries representing the concept model.

    \"""
    import Rhino
    import Rhino.Geometry as rg
    import random

    # Set a seed for randomness
    random.seed(42)
    
    geometries = []
    
    # Define base plane
    base_plane = rg.Plane.WorldXY
    
    # Create vertical elements resembling trunks
    for i in range(vertical_density):
        for j in range(vertical_density):
            x = base_size / vertical_density * (i + 0.5)
            y = base_size / vertical_density * (j + 0.5)
            start_point = rg.Point3d(x, y, 0)
            end_point = rg.Point3d(x, y, height_levels * base_size)
            line = rg.Line(start_point, end_point)
            cylinder = rg.Cylinder(rg.Circle(line.From, base_size * 0.05), line.Length).ToBrep(True, True)
            geometries.append(cylinder)
    
    # Create horizontal elements resembling branches
    for level in range(height_levels):
        z = level * base_size
        for _ in range(horizontal_density):
            x1 = random.uniform(0, base_size)
            y1 = random.uniform(0, base_size)
            x2 = random.uniform(0, base_size)
            y2 = random.uniform(0, base_size)
            start_point = rg.Point3d(x1, y1, z)
            end_point = rg.Point3d(x2, y2, z)
            line = rg.Line(start_point, end_point)
            cylinder = rg.Cylinder(rg.Circle(line.From, base_size * 0.02), line.Length).ToBrep(True, True)
            geometries.append(cylinder)
    
    # Create canopy-like surfaces
    for level in range(1, height_levels):
        z = level * base_size - base_size * 0.5
        control_points = [
            rg.Point3d(random.uniform(0, base_size), random.uniform(0, base_size), z) for _ in range(4)
        ]
        nurbs_surface = rg.NurbsSurface.CreateFromPoints(control_points, 2, 2, 2, 2)
        geometries.append(nurbs_surface)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_stacked_forests_concept_model(base_size=15, height_levels=4, horizontal_density=5, vertical_density=5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_stacked_forests_concept_model(base_size=12, height_levels=6, horizontal_density=4, vertical_density=6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_stacked_forests_concept_model(base_size=20, height_levels=3, horizontal_density=2, vertical_density=4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_stacked_forests_concept_model(base_size=8, height_levels=7, horizontal_density=6, vertical_density=2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_stacked_forests_concept_model(base_size=18, height_levels=5, horizontal_density=3, vertical_density=3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
