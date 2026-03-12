# Created for 0011_0001_shifted_grid.json

""" Summary:
The provided function, `create_shifted_grid_concept_model`, generates an architectural concept model inspired by the "Shifted Grid" metaphor. By creating a base grid with shifted alignments across multiple floors, it introduces dynamic spatial arrangements that foster movement and fluidity. Each floor's grid cells are offset, resulting in innovative intersections and varied circulation paths. The model incorporates vertical elements, like walls, that align with the grid, enhancing adaptability and playfulness in light and shadow interactions. This approach encapsulates the metaphor's essence by encouraging exploration and diverse spatial experiences within the architectural design."""

#! python 3
function_code = """def create_shifted_grid_concept_model(grid_size, shift_amount, floor_height, num_floors):
    \"""
    Creates an architectural Concept Model based on the "Shifted Grid" metaphor.
    
    Parameters:
    grid_size (float): The size of each grid cell in meters.
    shift_amount (float): The amount by which each subsequent floor grid is shifted.
    floor_height (float): The height of each floor in meters.
    num_floors (int): The total number of floors in the building.
    
    Returns:
    List[Rhino.Geometry.Brep]: A list of 3D geometries representing the concept model using Breps.
    \"""
    import Rhino.Geometry as rg
    import random
    
    # Set a random seed for reproducibility
    random.seed(42)

    # Initialize a list to store the resulting geometries
    geometries = []

    # Create the base grid
    for i in range(num_floors):
        # Calculate shift for the current floor
        x_shift = (i * shift_amount) % grid_size
        y_shift = ((i * shift_amount) // grid_size) * shift_amount
        
        # Create a grid of rectangles
        for x in range(0, int(10 * grid_size), int(grid_size)):
            for y in range(0, int(10 * grid_size), int(grid_size)):
                # Calculate the shifted position
                pt1 = rg.Point3d(x + x_shift, y + y_shift, i * floor_height)
                pt2 = rg.Point3d(x + grid_size + x_shift, y + y_shift, i * floor_height)
                pt3 = rg.Point3d(x + grid_size + x_shift, y + grid_size + y_shift, i * floor_height)
                pt4 = rg.Point3d(x + x_shift, y + grid_size + y_shift, i * floor_height)

                # Create a planar surface for each grid cell
                corners = [pt1, pt2, pt3, pt4, pt1]  # Add pt1 again to close the polyline
                polyline = rg.Polyline(corners)
                surface = rg.Brep.CreatePlanarBreps(polyline.ToNurbsCurve())[0]

                # Add the surface to the geometries list
                geometries.append(surface)
        
        # Optionally add vertical elements like walls or columns that follow the grid pattern
        wall_thickness = 0.2  # meters
        for x in range(0, int(10 * grid_size), int(grid_size)):
            for y in range(0, int(10 * grid_size), int(grid_size)):
                # Create a wall along one edge of the grid cell
                wall_start = rg.Point3d(x + x_shift, y + y_shift, 0)
                wall_end = rg.Point3d(x + x_shift, y + y_shift, i * floor_height)
                line = rg.Line(wall_start, wall_end)
                wall_curve = line.ToNurbsCurve()
                
                # Offset the curve to create wall thickness
                if wall_curve:
                    wall1 = wall_curve.Offset(rg.Plane.WorldXY, wall_thickness / 2, 0.01, rg.CurveOffsetCornerStyle.Sharp)
                    wall2 = wall_curve.Offset(rg.Plane.WorldXY, -wall_thickness / 2, 0.01, rg.CurveOffsetCornerStyle.Sharp)

                    if wall1 and wall2 and len(wall1) > 0 and len(wall2) > 0:
                        wall_surface = rg.Brep.CreateFromLoft([wall1[0], wall2[0]], rg.Point3d.Unset, rg.Point3d.Unset, rg.LoftType.Normal, False)[0]
                        geometries.append(wall_surface)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_shifted_grid_concept_model(5.0, 1.0, 3.0, 4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_shifted_grid_concept_model(10.0, 2.0, 3.5, 6)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_shifted_grid_concept_model(4.0, 0.5, 2.5, 5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_shifted_grid_concept_model(6.0, 1.5, 3.0, 3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_shifted_grid_concept_model(8.0, 1.2, 3.0, 5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
