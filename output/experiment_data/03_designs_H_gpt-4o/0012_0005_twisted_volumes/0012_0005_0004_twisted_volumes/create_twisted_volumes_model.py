# Created for 0012_0005_twisted_volumes.json

""" Summary:
The function `create_twisted_volumes_model` generates an architectural concept model inspired by the metaphor of "Twisted volumes." It creates a series of intertwined cylindrical forms that reflect fluidity and tension through varying degrees of twist. By defining parameters like base radius, height, twist angle, and number of sections, the function dynamically constructs the model in segments, where each segment is rotated to create a continuous twisted effect. This design approach fosters unique spatial experiences and circulation paths, enhancing interactions between interior and exterior spaces while allowing for a captivating interplay of light and shadow, embodying the transformative essence of the metaphor."""

#! python 3
function_code = """def create_twisted_volumes_model(base_radius=5, height=15, twist_angle=45, num_sections=6):
    \"""
    Creates an architectural Concept Model based on the 'Twisted volumes' metaphor.
    
    This function generates a series of entwined and distorted cylindrical forms that suggest a sense of tension and fluidity.
    The design leverages varying degrees of twist and contortion to create dynamic spatial experiences and silhouettes.
    
    Parameters:
    - base_radius: The radius of the base circle for each cylindrical section (in meters).
    - height: The total height of the entire structure (in meters).
    - twist_angle: The total twist angle in degrees applied across the sections.
    - num_sections: The number of cylindrical sections to divide the structure into.
    
    Returns:
    - A list of RhinoCommon Brep objects representing the 3D geometry of the twisted volumes.
    \"""
    import Rhino.Geometry as rg
    import math

    breps = []
    section_height = height / num_sections
    twist_per_section = math.radians(twist_angle) / num_sections

    for i in range(num_sections):
        # Create a base circle at the current section's height
        base_plane = rg.Plane(rg.Point3d(0, 0, i * section_height), rg.Vector3d.ZAxis)
        base_circle = rg.Circle(base_plane, base_radius)

        # Calculate the top circle with a twist
        top_plane = rg.Plane(rg.Point3d(0, 0, (i + 1) * section_height), rg.Vector3d.ZAxis)
        top_plane.Rotate(twist_per_section * (i + 1), top_plane.ZAxis)
        top_circle = rg.Circle(top_plane, base_radius)

        # Loft between the base and top circle
        loft_curves = [base_circle.ToNurbsCurve(), top_circle.ToNurbsCurve()]
        loft = rg.Brep.CreateFromLoft(loft_curves, rg.Point3d.Unset, rg.Point3d.Unset, rg.LoftType.Normal, False)
        
        if loft:
            breps.append(loft[0])

    return breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_twisted_volumes_model(base_radius=7, height=20, twist_angle=90, num_sections=8)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_twisted_volumes_model(base_radius=4, height=10, twist_angle=60, num_sections=5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_twisted_volumes_model(base_radius=6, height=25, twist_angle=30, num_sections=10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_twisted_volumes_model(base_radius=5, height=18, twist_angle=75, num_sections=7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_twisted_volumes_model(base_radius=8, height=12, twist_angle=120, num_sections=4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
