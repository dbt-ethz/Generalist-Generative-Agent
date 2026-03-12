# Created for 0016_0002_curved_partitions.json

""" Summary:
The provided function generates an architectural concept model inspired by the metaphor of "curved partitions." It creates a landscape-like structure through multiple layers of sweeping curves, simulating organic forms reminiscent of hills or waves. By adjusting parameters such as layer count, spacing, and curve variability, the model embodies fluidity and dynamic spatial relationships. Each curve is formed using control points and is revolved around a vertical axis to produce a three-dimensional surface. This approach not only emphasizes aesthetic qualities but also facilitates light interaction and spatial transitions, inviting exploration and enhancing the sensory experience of the environment."""

#! python 3
function_code = """def create_curved_partitions_model(num_layers=5, layer_spacing=1.5, curve_extent=15.0, curve_variation=2.0, seed=42):
    \"""
    Generate an architectural Concept Model using the metaphor of 'curved partitions' with RhinoCommon.

    This function constructs a series of sweeping, layered curves that form a landscape-like structure. The curves
    mimic natural landscapes, creating a dynamic form that guides circulation and interaction with light.

    Parameters:
    - num_layers (int): Number of curved layers to generate.
    - layer_spacing (float): Vertical distance between each layer.
    - curve_extent (float): Horizontal extent of each curve.
    - curve_variation (float): Variability in the curve's form.
    - seed (int): Seed for random number generator to ensure replicability.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep objects representing the 3D geometries of the concept model.
    \"""
    import Rhino.Geometry as rg
    import random

    random.seed(seed)

    geometries = []

    for i in range(num_layers):
        height = i * layer_spacing
        control_points = []
        for j in range(8):  # Using 8 control points for a smoother curve
            x = j * (curve_extent / 7)
            y = random.uniform(-curve_variation, curve_variation) if j % 2 == 0 else -random.uniform(-curve_variation, curve_variation)
            control_points.append(rg.Point3d(x, y, height))

        # Create a curve through the control points
        curve = rg.Curve.CreateInterpolatedCurve(control_points, 3)

        # Create a surface by revolving the curve around the Z-axis
        axis = rg.Line(rg.Point3d(0, 0, height), rg.Point3d(0, 0, height + 1))  # Create a vertical axis for revolution
        surface = rg.Brep.CreateFromRevSurface(rg.RevSurface.Create(curve, axis), True, False)

        # Add the surface to the list of geometries
        geometries.append(surface)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_curved_partitions_model(num_layers=10, layer_spacing=2.0, curve_extent=20.0, curve_variation=3.0, seed=7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_curved_partitions_model(num_layers=7, layer_spacing=1.0, curve_extent=10.0, curve_variation=1.5, seed=21)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_curved_partitions_model(num_layers=6, layer_spacing=1.0, curve_extent=25.0, curve_variation=4.0, seed=15)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_curved_partitions_model(num_layers=8, layer_spacing=2.5, curve_extent=18.0, curve_variation=2.5, seed=35)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_curved_partitions_model(num_layers=4, layer_spacing=1.2, curve_extent=12.0, curve_variation=1.0, seed=10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
