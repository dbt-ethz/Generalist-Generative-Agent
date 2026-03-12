# Created for 0020_0003_stacked_forests.json

""" Summary:
The provided function generates an architectural concept model inspired by the "Stacked forests" metaphor. It constructs a vertically tiered structure by creating staggered layers that evoke the complexity of a forest ecosystem. Each layer's size decreases incrementally, with random horizontal offsets to mimic natural irregularities. The function also incorporates vertical and diagonal circulation paths, enhancing movement through the structure similar to traversing forest altitudes. The interplay of solid and void is represented through the varying densities of the layers, while the overall silhouette reflects the dynamic nature of a forest canopy, capturing both stability and movement in the design."""

#! python 3
function_code = """def create_stacked_forests_concept(base_size=10.0, height_increment=3.0, num_layers=5, offset_factor=0.3, circulation_width=1.0):
    \"""
    Creates a conceptual architectural model based on the 'Stacked forests' metaphor.
    
    Parameters:
    - base_size (float): The size of the base layer in meters.
    - height_increment (float): The height of each layer in meters.
    - num_layers (int): The number of vertical layers in the structure.
    - offset_factor (float): The maximum offset factor for each subsequent layer.
    - circulation_width (float): The width of vertical and diagonal circulation paths.
    
    Returns:
    - list: A list of RhinoCommon Brep objects representing the 3D geometry of the concept model.
    \"""
    import Rhino.Geometry as rg
    import random
    
    random.seed(42)  # Ensuring replicability

    geometries = []

    # Create layered structures with staggered offsets
    for i in range(num_layers):
        # Determine the size and offset for the current layer
        layer_size = base_size * (1 - (i * offset_factor / num_layers))
        offset_x = random.uniform(-offset_factor, offset_factor) * base_size
        offset_y = random.uniform(-offset_factor, offset_factor) * base_size

        # Create the base surface for the layer
        base_plane = rg.Plane.WorldXY
        base_plane.Origin += rg.Vector3d(offset_x, offset_y, i * height_increment)
        rectangle = rg.Rectangle3d(base_plane, layer_size, layer_size)
        surface = rg.Brep.CreateFromCornerPoints(rectangle.Corner(0), rectangle.Corner(1),
                                                 rectangle.Corner(2), rectangle.Corner(3), 0.01)

        # Add the layer to the geometries
        geometries.append(surface)

    # Add circulation paths (vertical and diagonal)
    for i in range(1, num_layers):
        # Vertical paths
        start_point = rg.Point3d(0, 0, (i - 1) * height_increment)
        end_point = rg.Point3d(0, 0, i * height_increment)
        vertical_path = rg.Line(start_point, end_point).ToNurbsCurve()
        vertical_brep = rg.Brep.CreatePipe(vertical_path, circulation_width / 2, True, rg.PipeCapMode.Flat, True, 0.01, 0.01)
        geometries.append(vertical_brep)

        # Diagonal paths
        diagonal_start = rg.Point3d(random.uniform(-circulation_width, circulation_width),
                                    random.uniform(-circulation_width, circulation_width),
                                    (i - 1) * height_increment)
        diagonal_end = rg.Point3d(random.uniform(-circulation_width, circulation_width),
                                  random.uniform(-circulation_width, circulation_width),
                                  i * height_increment)
        diagonal_path = rg.Line(diagonal_start, diagonal_end).ToNurbsCurve()
        diagonal_brep = rg.Brep.CreatePipe(diagonal_path, circulation_width / 3, True, rg.PipeCapMode.Flat, True, 0.01, 0.01)
        geometries.append(diagonal_brep)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_stacked_forests_concept(base_size=15.0, height_increment=4.0, num_layers=6, offset_factor=0.4, circulation_width=1.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_stacked_forests_concept(base_size=12.0, height_increment=2.5, num_layers=4, offset_factor=0.2, circulation_width=0.8)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_stacked_forests_concept(base_size=20.0, height_increment=5.0, num_layers=3, offset_factor=0.5, circulation_width=2.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_stacked_forests_concept(base_size=18.0, height_increment=3.5, num_layers=7, offset_factor=0.25, circulation_width=1.2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_stacked_forests_concept(base_size=14.0, height_increment=6.0, num_layers=5, offset_factor=0.35, circulation_width=1.0)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
