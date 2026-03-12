# Created for 0018_0001_perforated_vertical_landscape.json

""" Summary:
The function `create_perforated_vertical_landscape` generates a 3D architectural concept model inspired by the metaphor of a "perforated vertical landscape." It constructs multiple layers of solid boxes representing the structure's mass, while introducing random voids (perforations) that facilitate light and air flow, embodying the metaphor's key traits. Each layer's dimensions and the number of voids can vary, creating a dynamic interplay of solid and void. The method allows for replicable designs through a seed parameter, ensuring diverse yet coherent outputs that evoke a natural, vertical landscape experience, seamlessly blending interior and exterior environments."""

#! python 3
function_code = """def create_perforated_vertical_landscape(base_width, base_depth, height, num_layers, max_voids, seed=42):
    \"""
    Creates a concept model of a perforated vertical landscape using RhinoCommon. This function generates a structure 
    that integrates verticality with porous elements, allowing light, air, and views to penetrate through its form.

    Parameters:
    - base_width (float): The width of the base of the structure in meters.
    - base_depth (float): The depth of the base of the structure in meters.
    - height (float): The total height of the structure in meters.
    - num_layers (int): The number of vertical layers in the structure.
    - max_voids (int): The maximum number of voids (perforations) in each layer.
    - seed (int): Seed for random number generator to ensure replicability.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep geometries representing the 3D concept model.
    \"""
    import Rhino
    from Rhino.Geometry import Point3d, Box, Brep, Interval, Plane
    import random

    random.seed(seed)
    breps = []
    layer_height = height / num_layers

    for i in range(num_layers):
        # Create the solid part of the layer as a Box
        base_origin = Point3d(0, 0, i * layer_height)
        base_box = Box(Plane.WorldXY, Interval(0, base_width), Interval(0, base_depth), Interval(i * layer_height, (i + 1) * layer_height))
        breps.append(base_box.ToBrep())

        # Add voids (perforations) to the layer
        num_voids = random.randint(1, max_voids)
        for _ in range(num_voids):
            void_width = random.uniform(base_width * 0.1, base_width * 0.3)
            void_depth = random.uniform(base_depth * 0.1, base_depth * 0.3)
            void_height = random.uniform(layer_height * 0.3, layer_height * 0.7)

            void_origin_x = random.uniform(0, base_width - void_width)
            void_origin_y = random.uniform(0, base_depth - void_depth)
            void_origin_z = i * layer_height + random.uniform(0, layer_height - void_height)

            void_origin = Point3d(void_origin_x, void_origin_y, void_origin_z)
            void_box = Box(
                Plane.WorldXY,
                Interval(void_origin_x, void_origin_x + void_width),
                Interval(void_origin_y, void_origin_y + void_depth),
                Interval(void_origin_z, void_origin_z + void_height)
            )
            void_brep = void_box.ToBrep()
            breps.append(void_brep)

    return breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_perforated_vertical_landscape(10.0, 5.0, 15.0, 4, 5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_perforated_vertical_landscape(12.0, 6.0, 20.0, 3, 10, seed=123)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_perforated_vertical_landscape(8.0, 4.0, 10.0, 5, 3, seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_perforated_vertical_landscape(15.0, 7.0, 25.0, 6, 8, seed=2023)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_perforated_vertical_landscape(9.0, 4.5, 18.0, 5, 6, seed=77)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
