# Created for 0020_0002_stacked_forests.json

""" Summary:
The provided function generates an architectural concept model inspired by the metaphor of "Stacked forests." It creates a series of vertically arranged, interlocking volumes that simulate the layers of a forest. Each layer features organic shapes with varying densities and open spaces, resembling the complexity of a forest ecosystem. The function incorporates vertical pathways to mimic natural trails, enhancing the spatial experience. Randomized elements ensure uniqueness in form, while voids represent clearings, contributing to the model's dynamism. Overall, the output reflects the layered hierarchy and organic growth patterns characteristic of a forest, fulfilling the design task effectively."""

#! python 3
function_code = """def create_stacked_forests_concept_model(base_size=5.0, num_layers=6, layer_height=3.0, seed=42):
    \"""
    Generates an architectural Concept Model inspired by the 'Stacked forests' metaphor.

    The model consists of a series of interlocking volumes, each layer representing a forest stratum.
    It is characterized by dense and open sections, with pathways that mimic natural trails.

    Parameters:
    - base_size (float): The approximate size of each layer in meters.
    - num_layers (int): The number of vertical layers to represent the forest's tiers.
    - layer_height (float): The height of each layer in meters.
    - seed (int): Seed for randomness to ensure replicable results.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep objects representing the 3D geometries of the concept model.
    \"""
    import Rhino.Geometry as rg
    import random
    random.seed(seed)

    geometries = []

    # Create each layer
    for i in range(num_layers):
        # Determine the center of the layer
        z_position = i * layer_height
        
        # Create a base curve for the layer
        base_curve = rg.Circle(rg.Plane.WorldXY, base_size * (1 + random.uniform(-0.1, 0.1))).ToNurbsCurve()
        base_curve.Translate(rg.Vector3d(0, 0, z_position))
        
        # Create a distorted organic shape by moving control points
        control_points = base_curve.Points
        for j in range(control_points.Count):
            move_vector = rg.Vector3d(random.uniform(-0.2, 0.2), random.uniform(-0.2, 0.2), 0)
            control_points[j].Location += move_vector
        
        # Rebuild the curve to smooth the shape
        point_list = [control_points[j].Location for j in range(control_points.Count)]
        organic_curve = rg.Curve.CreateControlPointCurve(point_list, 3)
        
        # Create a lofted surface from the base
        loft_brep = rg.Brep.CreateFromLoft([base_curve, organic_curve], rg.Point3d.Unset, rg.Point3d.Unset, rg.LoftType.Normal, False)
        
        if loft_brep and len(loft_brep) > 0:
            geometries.append(loft_brep[0])
        
        # Create vertical circulation paths
        if i < num_layers - 1:
            path_start = rg.Point3d(random.uniform(-base_size, base_size), random.uniform(-base_size, base_size), z_position)
            path_end = rg.Point3d(path_start.X, path_start.Y, z_position + layer_height)
            path_curve = rg.Line(path_start, path_end).ToNurbsCurve()
            path_brep = rg.Brep.CreatePipe(path_curve, 0.1, False, rg.PipeCapMode.Flat, True, 0.01, 0.01)
            if path_brep and len(path_brep) > 0:
                geometries.append(path_brep[0])
        
        # Optionally add voids
        if random.random() < 0.4:
            void_center = rg.Point3d(random.uniform(-base_size, base_size), random.uniform(-base_size, base_size), z_position + layer_height / 2)
            void_radius = random.uniform(0.5, 1.5)
            void_sphere = rg.Brep.CreateFromSphere(rg.Sphere(void_center, void_radius))
            if void_sphere:
                geometries.append(void_sphere)
    
    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_stacked_forests_concept_model(base_size=6.0, num_layers=8, layer_height=4.0, seed=123)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_stacked_forests_concept_model(base_size=7.0, num_layers=5, layer_height=2.5, seed=10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_stacked_forests_concept_model(base_size=5.5, num_layers=10, layer_height=3.5, seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_stacked_forests_concept_model(base_size=8.0, num_layers=7, layer_height=3.0, seed=2023)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_stacked_forests_concept_model(base_size=4.0, num_layers=12, layer_height=2.0, seed=42)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
