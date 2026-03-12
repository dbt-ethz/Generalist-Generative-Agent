# Created for 0018_0002_perforated_vertical_landscape.json

""" Summary:
The provided function, `create_perforated_vertical_landscape`, generates an architectural concept model inspired by the metaphor of a "Perforated Vertical Landscape." It constructs a 3D structure composed of staggered, layered platforms that incorporate circular perforations, facilitating the flow of light and air. Each level is offset randomly, creating a dynamic visual effect reminiscent of natural landscapes. The model emphasizes verticality and permeability, allowing for spatial interconnections between interior and exterior environments. By varying parameters like height, number of levels, and perforation size, the function creates diverse interpretations of the metaphor, resulting in unique architectural forms."""

#! python 3
function_code = """def create_perforated_vertical_landscape(base_length, base_width, structure_height, num_levels, perforation_radius, seed_value=42):
    \"""
    Create an architectural Concept Model based on the 'Perforated Vertical Landscape' metaphor.

    This function generates a 3D model featuring staggered, layered platforms with circular perforations 
    that allow light and air to flow through the structure. The design emphasizes verticality and 
    permeability, creating dynamic spatial interconnections.

    Parameters:
    - base_length (float): The length of the base platform in meters.
    - base_width (float): The width of the base platform in meters.
    - structure_height (float): The total height of the structure in meters.
    - num_levels (int): The number of staggered levels or platforms.
    - perforation_radius (float): The radius of circular perforations in meters.
    - seed_value (int): Seed for randomness to ensure replicable results. Default is 42.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of 3D geometries representing the concept model.
    \"""
    import Rhino.Geometry as rg
    import random

    # Set the seed for randomness
    random.seed(seed_value)

    # Calculate the height of each level
    level_height = structure_height / num_levels

    # Initialize a list to store the resulting 3D geometries
    geometries = []

    # Create staggered levels with circular perforations
    for i in range(num_levels):
        # Calculate the offset for the current level to create staggered effect
        offset_x = random.uniform(-0.3, 0.3) * base_length
        offset_y = random.uniform(-0.3, 0.3) * base_width
        
        # Create the plane for the current level
        level_plane = rg.Plane.WorldXY
        level_plane.Translate(rg.Vector3d(offset_x, offset_y, i * level_height))
        
        # Create the rectangle for the current level
        level_rect = rg.Rectangle3d(level_plane, base_length, base_width)
        
        # Create the surface for the current level
        level_surface = rg.Brep.CreatePlanarBreps(level_rect.ToNurbsCurve())[0]
        
        # Generate circular perforations
        num_perforations = random.randint(1, 5)
        for _ in range(num_perforations):
            perf_x = random.uniform(-0.4 * base_length, 0.4 * base_length)
            perf_y = random.uniform(-0.4 * base_width, 0.4 * base_width)
            perf_plane = rg.Plane(level_plane)
            perf_plane.Translate(rg.Vector3d(perf_x, perf_y, 0))
            perf_circle = rg.Circle(perf_plane, perforation_radius)
            perf_brep = rg.Brep.CreatePlanarBreps(perf_circle.ToNurbsCurve())
            if perf_brep and len(perf_brep) > 0:
                # Subtract perforations from the current level
                boolean_diff = rg.Brep.CreateBooleanDifference([level_surface], [perf_brep[0]], 0.01)
                if boolean_diff and len(boolean_diff) > 0:
                    level_surface = boolean_diff[0]
        
        # Append the final level with perforations to the geometries
        geometries.append(level_surface)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_perforated_vertical_landscape(10.0, 5.0, 15.0, 4, 0.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_perforated_vertical_landscape(8.0, 4.0, 12.0, 3, 0.3, seed_value=123)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_perforated_vertical_landscape(15.0, 7.0, 20.0, 5, 0.4, seed_value=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_perforated_vertical_landscape(12.0, 6.0, 18.0, 6, 0.6, seed_value=56)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_perforated_vertical_landscape(9.0, 3.0, 10.0, 2, 0.2, seed_value=77)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
