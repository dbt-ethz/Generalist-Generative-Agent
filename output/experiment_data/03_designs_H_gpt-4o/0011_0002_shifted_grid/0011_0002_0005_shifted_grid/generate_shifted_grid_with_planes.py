# Created for 0011_0002_shifted_grid.json

""" Summary:
The function `generate_shifted_grid_with_planes` creates an architectural concept model inspired by the "Shifted Grid" metaphor. It begins with a standard grid and introduces random shifts to the grid points, allowing for dynamic and fluid reconfigurations. This results in interconnected volumes and staggered layers that deviate from traditional layouts, embodying movement and unpredictability. The model emphasizes interaction with light and shadow through the addition of vertical elements and varying orientations. By allowing for adaptability in spatial arrangements, the design fosters exploration and offers diverse experiences, aligning closely with the metaphor's essence of transformation and discovery."""

#! python 3
function_code = """def generate_shifted_grid_with_planes(grid_size=6, grid_spacing=5.0, shift_amount=1.0, layer_count=3, layer_thickness=0.2):
    \"""
    Generates an architectural Concept Model based on the 'Shifted Grid' metaphor.

    This function creates a grid framework and introduces shifts and offsets to form
    interconnected volumes with staggered planes. It emphasizes movement and fluidity,
    highlighting light and shadow interactions through projected and receding elements.

    Parameters:
    grid_size (int): Number of grid cells along one axis.
    grid_spacing (float): Distance between grid lines in meters.
    shift_amount (float): Maximum shift applied to grid points.
    layer_count (int): Number of horizontal staggered layers.
    layer_thickness (float): Thickness of each horizontal layer in meters.

    Returns:
    List[Rhino.Geometry.Brep]: A list of Brep objects representing the 3D geometries of the concept model.
    \"""
    
    import Rhino.Geometry as rg
    import random

    # Seed random number generator for replicability
    random.seed(42)

    breps = []

    # Create the grid and apply shifts
    for i in range(grid_size):
        for j in range(grid_size):
            # Base grid point
            base_x = i * grid_spacing
            base_y = j * grid_spacing

            # Apply random shifts
            shift_x = base_x + random.uniform(-shift_amount, shift_amount)
            shift_y = base_y + random.uniform(-shift_amount, shift_amount)

            # Create horizontal staggered layers
            for layer in range(layer_count):
                z_base = layer * layer_thickness * 2  # Stagger layers vertically
                plane_origin = rg.Point3d(shift_x, shift_y, z_base)

                # Define the corners of the plane
                corners = [
                    rg.Point3d(shift_x, shift_y, z_base),
                    rg.Point3d(shift_x + grid_spacing, shift_y, z_base),
                    rg.Point3d(shift_x + grid_spacing, shift_y + grid_spacing, z_base),
                    rg.Point3d(shift_x, shift_y + grid_spacing, z_base)
                ]

                # Create a surface from the corners
                surface = rg.Brep.CreateFromCornerPoints(corners[0], corners[1], corners[2], corners[3], 0.01)

                if surface:
                    breps.append(surface)
                    
                # Create a vertical element for light and shadow play
                if layer % 2 == 0:  # Only add vertical elements on every other layer
                    height = random.uniform(1.0, 2.0)  # Height variation
                    vertical_face = rg.Box(rg.Plane(plane_origin, rg.Vector3d.ZAxis),
                                           rg.Interval(0, 0.2 * grid_spacing),  # Narrow vertical face
                                           rg.Interval(0, 0.2 * grid_spacing), 
                                           rg.Interval(0, height))
                    brep_vert = vertical_face.ToBrep()
                    if brep_vert:
                        breps.append(brep_vert)

    return breps"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = generate_shifted_grid_with_planes(grid_size=8, grid_spacing=4.0, shift_amount=2.0, layer_count=5, layer_thickness=0.3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = generate_shifted_grid_with_planes(grid_size=10, grid_spacing=3.0, shift_amount=1.5, layer_count=4, layer_thickness=0.25)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = generate_shifted_grid_with_planes(grid_size=5, grid_spacing=6.0, shift_amount=1.0, layer_count=2, layer_thickness=0.15)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = generate_shifted_grid_with_planes(grid_size=7, grid_spacing=7.0, shift_amount=1.2, layer_count=6, layer_thickness=0.4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = generate_shifted_grid_with_planes(grid_size=9, grid_spacing=5.5, shift_amount=1.8, layer_count=3, layer_thickness=0.2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
