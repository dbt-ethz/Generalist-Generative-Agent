# Created for 0016_0002_curved_partitions.json

""" Summary:
The provided function generates an architectural concept model based on the metaphor of "curved partitions," reflecting fluidity and organic movement. By creating a series of layered, sweeping curves, the model emulates natural landscapes, allowing for dynamic spatial relationships. Each layer's height and curvature are randomized, enhancing the organic aesthetic and creating varied zones of intimacy and openness. The function employs Rhino.Geometry to construct 3D geometries that facilitate exploration while ensuring light interplay through the curves, embodying the metaphors essence. Ultimately, the model invites viewers to engage with its flowing structure, fostering an immersive spatial experience."""

#! python 3
function_code = """def create_curved_partitions_model(num_layers=5, base_length=30.0, base_width=15.0, max_curve_height=3.0, seed=42):
    \"""
    Create an architectural Concept Model embodying the 'curved partitions' metaphor with a different approach.

    This function constructs a landscape-like form composed of layered, sweeping curves. The design
    emphasizes organic flow and interaction, creating spaces defined by the rise and fall of the curves.

    Parameters:
    - num_layers (int): Number of layered partitions to generate.
    - base_length (float): The length of the base of the model in meters.
    - base_width (float): The width of the base of the model in meters.
    - max_curve_height (float): Maximum height variation for the curves.
    - seed (int): Random seed for replicable results.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of Brep objects representing the 3D geometries of the model.
    \"""
    import Rhino.Geometry as rg
    import random

    random.seed(seed)
    geometries = []

    for i in range(num_layers):
        # Calculate the vertical position of the current layer
        z_offset = i * (max_curve_height / num_layers)

        # Define control points for a sweeping curve along the length
        control_points = []
        for j in range(8):  # Creating a curve with 8 control points
            x = j * (base_length / 7)
            y = random.uniform(-base_width / 4, base_width / 4)
            z = z_offset + random.uniform(-max_curve_height / 2, max_curve_height / 2)
            control_points.append(rg.Point3d(x, y, z))

        # Create a curve through the control points
        curve = rg.Curve.CreateInterpolatedCurve(control_points, 3)

        # Create a boundary curve for the surface
        boundary_curve = rg.Polyline([
            rg.Point3d(0, -base_width / 2, z_offset),
            rg.Point3d(base_length, -base_width / 2, z_offset),
            rg.Point3d(base_length, base_width / 2, z_offset),
            rg.Point3d(0, base_width / 2, z_offset),
            rg.Point3d(0, -base_width / 2, z_offset)
        ]).ToNurbsCurve()

        # Loft the boundary and the curve to form a surface
        loft_curves = [boundary_curve, curve]
        breps = rg.Brep.CreateFromLoft(loft_curves, rg.Point3d.Unset, rg.Point3d.Unset, rg.LoftType.Normal, False)
        
        # Check if breps is not empty and take the first element
        if breps:
            brep = breps[0]
            # Add the brep to the geometries list
            geometries.append(brep)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_curved_partitions_model(num_layers=6, base_length=40.0, base_width=20.0, max_curve_height=5.0, seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_curved_partitions_model(num_layers=4, base_length=50.0, base_width=25.0, max_curve_height=4.0, seed=10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_curved_partitions_model(num_layers=3, base_length=25.0, base_width=10.0, max_curve_height=2.0, seed=7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_curved_partitions_model(num_layers=7, base_length=35.0, base_width=18.0, max_curve_height=6.0, seed=21)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_curved_partitions_model(num_layers=5, base_length=45.0, base_width=22.0, max_curve_height=3.5, seed=15)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
