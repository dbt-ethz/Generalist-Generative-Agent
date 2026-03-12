# Created for 0020_0002_stacked_forests.json

""" Summary:
The function `create_stacked_forests_concept_model` generates an architectural concept model inspired by the metaphor of "Stacked forests." It constructs a series of vertically interlocking, organically shaped volumes that represent distinct forest layers. The model balances density and openness by incorporating both solid and void spaces, simulating natural clearings. Additionally, it integrates vertical and horizontal pathways resembling forest trails, enhancing exploration at various heights. By using random scaling and positioning, the function emulates the complexity and hierarchy of a forest ecosystem, resulting in a dynamic, organic structure that reflects the metaphor's essence."""

#! python 3
function_code = """def create_stacked_forests_concept_model(base_length=10.0, base_width=8.0, total_height=30.0, num_layers=6, seed=42):
    \"""
    Generates an architectural Concept Model inspired by the 'Stacked forests' metaphor.

    This function constructs a series of interlocking, organically shaped volumes that mimic a forest's complex ecosystem.
    Each volume represents a distinct layer of the forest and features both solid and void spaces, emulating the density
    and openness found in natural environments. Vertical and horizontal pathways are incorporated to simulate trails
    through the forest.

    Parameters:
    - base_length (float): The length of the base of the model in meters.
    - base_width (float): The width of the base of the model in meters.
    - total_height (float): The total height of the model in meters.
    - num_layers (int): The number of vertical layers to create.
    - seed (int, optional): Seed for randomness to ensure replicable results. Default is 42.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep objects representing the 3D geometries of the concept model.
    \"""
    import Rhino.Geometry as rg
    import random

    random.seed(seed)
    
    # Calculate layer height
    layer_height = total_height / num_layers
    
    # Initialize the list to store geometries
    geometries = []

    for i in range(num_layers):
        # Calculate z position for the current layer
        z_position = i * layer_height
        
        # Base rectangle for the current layer
        base_rect = rg.Rectangle3d(rg.Plane.WorldXY, base_length, base_width)
        base_rect.Transform(rg.Transform.Translation(0, 0, z_position))

        # Create an organic shape by scaling the base rectangle
        scale_factor_x = random.uniform(0.8, 1.2)
        scale_factor_y = random.uniform(0.8, 1.2)
        
        scaled_rect = rg.Rectangle3d(base_rect.Plane, base_length * scale_factor_x, base_width * scale_factor_y)
        scaled_rect.Transform(rg.Transform.Translation(0, 0, z_position))
        
        # Loft between base and scaled rectangle to form a volume
        loft_brep = rg.Brep.CreateFromLoft([base_rect.ToNurbsCurve(), scaled_rect.ToNurbsCurve()], rg.Point3d.Unset, rg.Point3d.Unset, rg.LoftType.Normal, False)
        
        if loft_brep and len(loft_brep) > 0:
            geometries.append(loft_brep[0])
        
        # Introduce voids to simulate natural clearings
        if random.random() < 0.4:
            void_radius = random.uniform(0.5, 1.5)
            void_center = rg.Point3d(random.uniform(0, base_length), random.uniform(0, base_width), z_position + layer_height / 2)
            void_sphere = rg.Brep.CreateFromSphere(rg.Sphere(void_center, void_radius))
            if void_sphere:
                geometries.append(void_sphere)
        
        # Create pathways simulating trails
        if random.random() < 0.3:
            path_start = rg.Point3d(random.uniform(0, base_length), random.uniform(0, base_width), z_position)
            path_end = rg.Point3d(path_start.X, path_start.Y, z_position + layer_height)
            path_curve = rg.Line(path_start, path_end).ToNurbsCurve()
            path_tube = rg.Brep.CreatePipe(path_curve, 0.1, False, rg.PipeCapMode.Flat, True, 0.01, 0.01)
            if path_tube and len(path_tube) > 0:
                geometries.append(path_tube[0])

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_stacked_forests_concept_model(base_length=15.0, base_width=10.0, total_height=40.0, num_layers=8, seed=123)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_stacked_forests_concept_model(base_length=12.0, base_width=9.0, total_height=25.0, num_layers=5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_stacked_forests_concept_model(base_length=20.0, base_width=15.0, total_height=50.0, num_layers=10, seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_stacked_forests_concept_model(base_length=18.0, base_width=12.0, total_height=35.0, num_layers=7, seed=2023)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_stacked_forests_concept_model(base_length=14.0, base_width=11.0, total_height=45.0, num_layers=9, seed=56)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
