# Created for 0019_0004_subterranean_cavern.json

""" Summary:
The provided function, `create_subterranean_cavern_model`, generates an architectural concept model inspired by the metaphor of a subterranean cavern. It constructs a series of nested, curvilinear volumes that simulate the immersive qualities of cave-like spaces. By adjusting parameters such as radius, height, and translucency, the model creates varying layers that transition from intimate to expansive environments. The use of organic shapes and varied shell thicknesses evokes a sense of depth and discovery, while the incorporation of light variations enhances the atmosphere of mystery. This approach effectively embodies the metaphor's emphasis on exploration, refuge, and connection to nature."""

#! python 3
function_code = """def create_subterranean_cavern_model(base_radius, height, num_layers, shell_thickness, seed=42):
    \"""
    Generates an architectural concept model inspired by the 'subterranean cavern' metaphor.

    This function creates a series of nested, curvilinear volumes that transition from intimate to open spaces,
    using a combination of organic forms and material translucency to evoke exploration and mystery.

    Parameters:
    - base_radius (float): The radius of the outermost layer in meters.
    - height (float): The total height of the model in meters.
    - num_layers (int): The number of nested curvilinear volumes.
    - shell_thickness (float): The thickness of each shell or layer in meters.
    - seed (int): Seed for random number generation for replicable randomness.

    Returns:
    - List of RhinoCommon Brep objects representing the 3D geometries of the concept model.
    \"""
    import Rhino.Geometry as rg
    import random

    # Set the random seed for reproducibility
    random.seed(seed)

    geometries = []
    layer_height = height / num_layers

    for i in range(num_layers):
        # Calculate parameters for each layer
        layer_radius = base_radius * (1 - (i / num_layers) * 0.5)
        layer_translucency = 1 - (i / num_layers) * 0.1  # Decreasing translucency with depth

        # Create a curvilinear path for lofting
        base_circle = rg.Circle(rg.Point3d(0, 0, i * layer_height), layer_radius)
        offset_distance = random.uniform(0.1, 0.2) * layer_radius
        base_curve = base_circle.ToNurbsCurve()
        
        # Create an offset curve to define the organic shell
        offset_curve = base_curve.Offset(rg.Plane.WorldXY, offset_distance, 0.01, rg.CurveOffsetCornerStyle.Round)[0]
        
        # Create shell curves by translating the offset curve upwards to create a volume
        shell_curves = [base_curve]
        for j in range(1, int(layer_height / shell_thickness)):
            moved_curve = offset_curve.DuplicateCurve()
            move_transform = rg.Transform.Translation(0, 0, j * shell_thickness)
            moved_curve.Transform(move_transform)
            shell_curves.append(moved_curve)

        # Loft the curves to create a shell
        loft = rg.Brep.CreateFromLoft(shell_curves, rg.Point3d.Unset, rg.Point3d.Unset, rg.LoftType.Normal, False)
        if loft:
            brep = loft[0]
            brep.SetUserString("LayerTranslucency", str(layer_translucency))  # Store translucency data
            geometries.append(brep)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_subterranean_cavern_model(5.0, 20.0, 10, 0.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_subterranean_cavern_model(7.5, 15.0, 8, 0.3, seed=123)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_subterranean_cavern_model(10.0, 30.0, 12, 0.7, seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_subterranean_cavern_model(4.0, 25.0, 6, 0.4, seed=56)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_subterranean_cavern_model(6.0, 18.0, 15, 0.6, seed=77)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
