# Created for 0018_0002_perforated_vertical_landscape.json

""" Summary:
The function `create_perforated_vertical_landscape` generates an architectural concept model inspired by the "Perforated Vertical Landscape" metaphor. It creates a 3D structure composed of staggered terraces, allowing light and air to permeate through perforated elements. By defining parameters like base dimensions, levels, and perforation ratios, the function models the interplay between solid and void. Each level is offset randomly, mimicking natural formations, while strategic voids evoke the filtering of light akin to tree canopies. The resulting geometries highlight verticality and spatial connectivity, embodying the essence of the metaphor through dynamic layering and interaction with the environment."""

#! python 3
function_code = """def create_perforated_vertical_landscape(base_dim, levels, total_height, terrace_depth, perforation_ratio, seed=42):
    \"""
    Create an architectural Concept Model based on the 'Perforated Vertical Landscape' metaphor.

    This function generates a 3D model consisting of layered terraces and platforms, with strategic voids to allow light and air 
    to penetrate the structure. The design emphasizes verticality, permeability, and visual connectivity, resembling a vertical landscape.

    Parameters:
    - base_dim (float): The base dimension of the structure in meters.
    - levels (int): The number of staggered terraces or levels.
    - total_height (float): The total height of the structure in meters.
    - terrace_depth (float): Depth of each terrace level in meters.
    - perforation_ratio (float): A ratio between 0 and 1 indicating the proportion of each terrace that should be perforated.
    - seed (int): Seed for randomness to ensure replicable results. Default is 42.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of 3D geometries representing the concept model.
    \"""
    import Rhino.Geometry as rg
    import random

    # Initialize random seed for reproducibility
    random.seed(seed)

    # Calculate the height of each terrace
    level_height = total_height / levels

    # Initialize list to store the resulting 3D geometries
    geometries = []

    for i in range(levels):
        # Calculate staggered offset for the current level
        offset_x = random.uniform(-0.2, 0.2) * base_dim
        offset_y = random.uniform(-0.2, 0.2) * base_dim

        # Define the base plane for the current level
        level_plane = rg.Plane.WorldXY
        level_plane.Translate(rg.Vector3d(offset_x, offset_y, i * level_height))

        # Create the terrace geometry
        terrace_rect = rg.Rectangle3d(level_plane, base_dim, terrace_depth)
        terrace_surface = rg.Brep.CreatePlanarBreps(terrace_rect.ToNurbsCurve())[0]

        # Calculate number of perforations based on perforation_ratio
        num_perforations = int(perforation_ratio * 10)

        # Add perforations to the terrace
        for _ in range(num_perforations):
            perf_size = random.uniform(0.1, 0.3) * terrace_depth
            perf_offset_x = random.uniform(-0.4, 0.4) * base_dim
            perf_offset_y = random.uniform(-0.4, 0.4) * terrace_depth

            perf_plane = rg.Plane(level_plane)
            perf_plane.Translate(rg.Vector3d(perf_offset_x, perf_offset_y, 0))
            perf_circle = rg.Circle(perf_plane, perf_size)
            perf_brep = rg.Brep.CreatePlanarBreps(perf_circle.ToNurbsCurve())

            if perf_brep and len(perf_brep) > 0:
                difference_result = rg.Brep.CreateBooleanDifference([terrace_surface], [perf_brep[0]], 0.01)
                if difference_result and len(difference_result) > 0:
                    terrace_surface = difference_result[0]

        # Append the final terrace with perforations to the geometries
        geometries.append(terrace_surface)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_perforated_vertical_landscape(10, 5, 15, 2, 0.5)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_perforated_vertical_landscape(8, 4, 12, 1.5, 0.3, seed=100)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_perforated_vertical_landscape(12, 6, 20, 3, 0.7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_perforated_vertical_landscape(15, 3, 10, 2.5, 0.4, seed=50)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_perforated_vertical_landscape(9, 8, 18, 2, 0.6, seed=25)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
