# Created for 0018_0002_perforated_vertical_landscape.json

""" Summary:
The provided function, `create_perforated_vertical_landscape`, generates an architectural concept model based on the metaphor of a "Perforated Vertical Landscape." It constructs a series of staggered levels or terraces, each with varying dimensions and strategically placed perforations, mimicking the interplay of solid and void found in natural landscapes. By using randomization for positioning and sizing, the function ensures a dynamic effect that enhances light and air flow between layers. The model's verticality and perforations create visual connections and pathways, embodying the metaphor's essence of permeability and spatial interconnection, thus transforming the design task into a tangible architectural form."""

#! python 3
function_code = """def create_perforated_vertical_landscape(base_length, base_width, height, num_levels, seed_value=42):
    \"""
    Create an architectural Concept Model based on the 'Perforated Vertical Landscape' metaphor.

    Parameters:
    - base_length (float): The length of the base platform in meters.
    - base_width (float): The width of the base platform in meters.
    - height (float): The total height of the structure in meters.
    - num_levels (int): The number of staggered levels or platforms.
    - seed_value (int): Seed for randomness to ensure replicable results. Default is 42.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of 3D geometries representing the concept model.
    \"""
    import Rhino.Geometry as rg
    import random

    # Set the seed for randomness
    random.seed(seed_value)

    # Calculate the height of each level
    level_height = height / num_levels

    # Initialize a list to store the resulting 3D geometries
    geometries = []

    # Create the base platform
    base_plane = rg.Plane.WorldXY
    base_rect = rg.Rectangle3d(base_plane, base_length, base_width)
    base_surface = rg.Brep.CreatePlanarBreps(base_rect.ToNurbsCurve())[0]
    geometries.append(base_surface)

    # Create staggered levels with perforations
    for i in range(1, num_levels + 1):
        # Calculate the position and size variations for the current level
        level_offset_x = random.uniform(-0.5, 0.5) * base_length * 0.1
        level_offset_y = random.uniform(-0.5, 0.5) * base_width * 0.1
        level_ratio = random.uniform(0.8, 1.0)
        
        # Create the plane for the current level
        level_plane = rg.Plane(base_plane)
        level_plane.Translate(rg.Vector3d(0, 0, i * level_height))
        
        # Create the rectangle for the current level
        level_rect = rg.Rectangle3d(
            level_plane,
            base_length * level_ratio,
            base_width * level_ratio
        )
        level_rect.Transform(rg.Transform.Translation(level_offset_x, level_offset_y, 0))
        
        # Create the surface for the current level
        level_surface = rg.Brep.CreatePlanarBreps(level_rect.ToNurbsCurve())[0]
        
        # Add perforations to the current level
        perforations = []
        num_perforations = random.randint(1, 3)
        for j in range(num_perforations):
            perf_size = random.uniform(0.1, 0.3) * min(base_length, base_width)
            perf_offset_x = random.uniform(-0.4, 0.4) * base_length
            perf_offset_y = random.uniform(-0.4, 0.4) * base_width
            perf_plane = rg.Plane(level_plane)
            perf_plane.Translate(rg.Vector3d(perf_offset_x, perf_offset_y, 0))
            perf_circle = rg.Circle(perf_plane, perf_size)
            perf_brep = rg.Brep.CreatePlanarBreps(perf_circle.ToNurbsCurve())
            if perf_brep:
                perforations.append(perf_brep[0])
        
        # Subtract perforations from the current level
        for perf in perforations:
            boolean_difference = rg.Brep.CreateBooleanDifference([level_surface], [perf], 0.01)
            if boolean_difference:
                level_surface = boolean_difference[0]
        
        # Append the final level with perforations to the geometries
        geometries.append(level_surface)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_perforated_vertical_landscape(10.0, 5.0, 20.0, 4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_perforated_vertical_landscape(15.0, 7.5, 30.0, 6, seed_value=100)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_perforated_vertical_landscape(12.0, 6.0, 18.0, 5, seed_value=24)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_perforated_vertical_landscape(8.0, 4.0, 15.0, 3, seed_value=56)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_perforated_vertical_landscape(14.0, 7.0, 25.0, 5, seed_value=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
