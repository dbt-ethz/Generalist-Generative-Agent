# Created for 0012_0005_twisted_volumes.json

""" Summary:
The function `create_twisted_volumes_model` generates an architectural concept model inspired by the metaphor of "Twisted volumes." It constructs a series of intertwined geometric shapes through a defined height, base radius, twist angle, and segmentation levels. By applying a calculated twist to circular forms at various heights, the function creates a dynamic and fluid structure that embodies tension and movement. The resulting model features unique spatial relationships and innovative circulation paths, while also emphasizing light and shadow interplay. This process ultimately captures the essence of transformation and energy central to the metaphor, aligning the form with the intended spatial experience."""

#! python 3
function_code = """def create_twisted_volumes_model(height, radius, twist_angle, num_levels):
    \"""
    Creates an architectural Concept Model based on the "Twisted volumes" metaphor.
    
    This function generates a series of entwined and contorted geometric shapes 
    that suggest a sense of tension and fluidity. The result is a dynamic and 
    expressive silhouette, evoking a sense of motion and continual transformation.
    
    Parameters:
    - height: The total height of the model in meters.
    - radius: The base radius of the volumes in meters.
    - twist_angle: The total twist angle in degrees applied to the volumes.
    - num_levels: The number of levels or segments in the model.
    
    Returns:
    - A list of RhinoCommon Brep objects representing the 3D geometries.
    \"""
    import Rhino.Geometry as rg
    import math
    
    geometries = []
    level_height = height / num_levels
    twist_per_level = math.radians(twist_angle) / num_levels

    for i in range(num_levels):
        # Calculate the current level's twist
        current_twist = twist_per_level * i

        # Create a circle at the base
        circle = rg.Circle(rg.Plane.WorldXY, radius)
        
        # Create a loftable curve by rotating the circle
        twisted_circle = circle.ToNurbsCurve()
        twisted_circle.Transform(rg.Transform.Rotation(current_twist, rg.Vector3d.ZAxis, rg.Point3d.Origin))
        
        # Move the circle to the current level's height
        twisted_circle.Transform(rg.Transform.Translation(0, 0, level_height * i))

        # Collect curves for lofting
        if i == 0:
            base_curve = twisted_circle
        else:
            loft_curves = [base_curve, twisted_circle]
            loft = rg.Brep.CreateFromLoft(loft_curves, rg.Point3d.Unset, rg.Point3d.Unset, rg.LoftType.Normal, False)
            if loft:
                geometries.append(loft[0])
            base_curve = twisted_circle

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_twisted_volumes_model(height=10, radius=2, twist_angle=360, num_levels=5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_twisted_volumes_model(height=15, radius=3, twist_angle=720, num_levels=8)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_twisted_volumes_model(height=12, radius=1.5, twist_angle=180, num_levels=6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_twisted_volumes_model(height=20, radius=4, twist_angle=540, num_levels=10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_twisted_volumes_model(height=8, radius=2.5, twist_angle=450, num_levels=4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
