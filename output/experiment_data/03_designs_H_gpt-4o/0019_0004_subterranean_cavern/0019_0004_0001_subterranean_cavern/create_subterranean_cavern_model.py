# Created for 0019_0004_subterranean_cavern.json

""" Summary:
The provided function `create_subterranean_cavern_model` generates an architectural concept model inspired by the metaphor of a subterranean cavern. It creates a series of interconnected, organic volumes that embody an immersive experience through curvilinear shapes, layered structures, and varied translucency. The function parameters allow for customization of the model's size, height, and material properties, enhancing the sense of depth and mystery. By incorporating randomness in the design, it mimics natural cave formations, creating pockets and recesses that facilitate exploration and discovery. The final output is a collection of 3D geometries representing the nuanced interplay between enclosed and expansive spaces."""

#! python 3
function_code = """def create_subterranean_cavern_model(base_radius, height, num_layers, material_variation, seed=42):
    \"""
    Create an architectural Concept Model inspired by the 'subterranean cavern' metaphor.

    This function generates a series of interconnected, organic volumes to embody the
    immersive quality of a subterranean cavern. The model features curvilinear forms
    and varied material properties to evoke depth, mystery, and a gradual unfolding
    of spaces.

    Parameters:
    - base_radius (float): The radius of the outermost cavern layer in meters.
    - height (float): The total height of the cavern structure in meters.
    - num_layers (int): The number of nested layers or shells in the model.
    - material_variation (float): The degree of material variation (0 to 1) for translucency or texture.
    - seed (int): Seed for random number generation to ensure replicable results.

    Returns:
    - List of RhinoCommon Breps representing the 3D geometries of the concept model.
    \"""
    import Rhino.Geometry as rg
    import random

    # Set the random seed
    random.seed(seed)

    geometries = []

    # Define the vertical spacing between layers
    vertical_spacing = height / num_layers

    for i in range(num_layers):
        # Calculate the current radius and height
        current_radius = base_radius * (1 - (i / num_layers) * 0.5)
        current_height = height * (0.6 + random.uniform(-0.1, 0.1))

        # Create a base organic shape using a distorted ellipse
        ellipse = rg.Ellipse(rg.Plane.WorldXY, current_radius, current_radius * 0.7)
        ellipse_curve = ellipse.ToNurbsCurve()

        # Introduce some organic variation by applying a subtle twist
        twist_angle = random.uniform(-5, 5)  # in degrees
        twist_transform = rg.Transform.Rotation(twist_angle * (3.141592653589793 / 180), rg.Point3d(0, 0, i * vertical_spacing))
        ellipse_curve.Transform(twist_transform)

        # Create an offset curve for lofting
        offset_distance = random.uniform(0.1, 0.3) * current_radius
        offset_curve = ellipse_curve.Offset(rg.Plane.WorldXY, offset_distance, 0.01, rg.CurveOffsetCornerStyle.Round)[0]

        # Loft between original and offset curves
        loft_curves = [ellipse_curve, offset_curve]
        loft = rg.Brep.CreateFromLoft(loft_curves, rg.Point3d.Unset, rg.Point3d.Unset, rg.LoftType.Normal, False)

        if loft:
            brep = loft[0]
            # Assign material variation as a user-defined attribute (for conceptual purposes)
            material_property = 1 - (i / num_layers) * material_variation
            brep.SetUserString("MaterialProperty", str(material_property))
            geometries.append(brep)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_subterranean_cavern_model(10.0, 20.0, 5, 0.8)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_subterranean_cavern_model(15.0, 25.0, 8, 0.6, seed=123)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_subterranean_cavern_model(12.5, 30.0, 6, 0.4, seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_subterranean_cavern_model(8.0, 15.0, 4, 0.5, seed=10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_subterranean_cavern_model(20.0, 40.0, 10, 0.9, seed=7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
