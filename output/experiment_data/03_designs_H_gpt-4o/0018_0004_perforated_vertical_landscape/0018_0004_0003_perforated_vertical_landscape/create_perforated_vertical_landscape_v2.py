# Created for 0018_0004_perforated_vertical_landscape.json

""" Summary:
The provided function generates an architectural concept model inspired by the metaphor of a "Perforated Vertical Landscape." It creates a vertical grid-like structure using intertwined tubular elements, emphasizing a dynamic interplay of solid and void. The function allows customization of dimensions, grid density, and perforation size, ensuring adaptability to different design requirements. By randomly determining which sections are solid tubes versus open spaces, the model captures the essence of permeability and connectivity to the environment. The resulting geometries evoke a natural lattice, enhancing spatial interaction between interior and exterior, and reinforcing the metaphor's themes of openness and integration."""

#! python 3
function_code = """def create_perforated_vertical_landscape_v2(height, width, depth, grid_density, perforation_radius):
    \"""
    Creates a Concept Model of a 'Perforated Vertical Landscape' using intertwined tubular elements.

    Parameters:
    - height (float): The total height of the structure in meters.
    - width (float): The total width of the structure in meters.
    - depth (float): The total depth of the structure in meters.
    - grid_density (int): The number of divisions in the grid along width and depth.
    - perforation_radius (float): The radius of the tubular elements representing the perforations.

    Returns:
    - List of Rhino.Geometry.Brep: A list of 3D geometries representing the architectural concept model.
    \"""
    import Rhino.Geometry as rg
    import random

    random.seed(42)  # Ensure replicability

    breps = []

    # Calculate spacing based on grid density
    x_spacing = width / (grid_density + 1)
    z_spacing = depth / (grid_density + 1)

    # Create intertwined tubular structure
    for i in range(1, grid_density + 1):
        for j in range(1, grid_density + 1):
            # Calculate grid point positions
            x = i * x_spacing
            z = j * z_spacing

            # Create vertical path for tubes
            start = rg.Point3d(x, 0, z)
            end = rg.Point3d(x, height, z)
            line = rg.Line(start, end)

            # Randomly decide if this line should be a solid tube
            if random.random() > 0.5:  # 50% chance of being a solid tube
                # Create a solid tube
                curve = line.ToNurbsCurve()
                tube = rg.Cylinder(rg.Circle(rg.Plane(start, rg.Vector3d.ZAxis), perforation_radius), height)
                breps.append(tube.ToBrep(True, True))

            # Create horizontal interconnections
            if i < grid_density and j < grid_density:
                next_x = (i + 1) * x_spacing
                next_z = (j + 1) * z_spacing

                # Horizontal connections
                horiz_start = rg.Point3d(x, height / 2, z)
                horiz_end_x = rg.Point3d(next_x, height / 2, z)
                horiz_end_z = rg.Point3d(x, height / 2, next_z)

                horiz_line_x = rg.Line(horiz_start, horiz_end_x)
                horiz_line_z = rg.Line(horiz_start, horiz_end_z)

                curve_x = horiz_line_x.ToNurbsCurve()
                curve_z = horiz_line_z.ToNurbsCurve()

                if random.random() > 0.5:
                    tube_x = rg.Cylinder(rg.Circle(rg.Plane(horiz_start, rg.Vector3d(1, 0, 0)), perforation_radius), x_spacing)
                    breps.append(tube_x.ToBrep(True, True))

                if random.random() > 0.5:
                    tube_z = rg.Cylinder(rg.Circle(rg.Plane(horiz_start, rg.Vector3d(0, 0, 1)), perforation_radius), z_spacing)
                    breps.append(tube_z.ToBrep(True, True))

    return breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_perforated_vertical_landscape_v2(10.0, 5.0, 3.0, 4, 0.2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_perforated_vertical_landscape_v2(15.0, 8.0, 4.0, 6, 0.3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_perforated_vertical_landscape_v2(12.0, 6.0, 5.0, 5, 0.1)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_perforated_vertical_landscape_v2(8.0, 4.0, 2.0, 3, 0.15)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_perforated_vertical_landscape_v2(20.0, 10.0, 6.0, 8, 0.25)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
