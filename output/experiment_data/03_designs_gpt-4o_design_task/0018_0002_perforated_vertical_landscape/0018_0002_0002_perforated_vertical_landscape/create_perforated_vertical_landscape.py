# Created for 0018_0002_perforated_vertical_landscape.json

""" Summary:
The function `create_perforated_vertical_landscape` generates a 3D architectural concept model inspired by the "Perforated vertical landscape" metaphor. It creates a series of staggered, layered platforms, where each level varies in size and is offset horizontally, mimicking natural topographies. The design incorporates perforations to allow light and air to flow through, enhancing the interaction between interior and exterior spaces. By adjusting parameters such as base size, number of levels, and perforation density, the model reflects the metaphor's essence of verticality, permeability, and dynamic spatial connections, ultimately resulting in a visually engaging and functional architecture."""

#! python 3
function_code = """def create_perforated_vertical_landscape(base_size=10, num_levels=5, max_offset=3, perforation_density=0.3, seed=42):
    \"""
    Generates a 3D architectural concept model based on the 'Perforated vertical landscape' metaphor.
    
    The design features a series of staggered, layered platforms, using a combination of solid and perforated elements 
    to balance mass and void. The model incorporates terraces and niches to allow light and air to flow through, 
    creating a dynamic interaction between different levels.
    
    Parameters:
    - base_size (float): The base size of the lowest platform in meters.
    - num_levels (int): The number of staggered levels in the structure.
    - max_offset (float): The maximum horizontal offset for each level in meters.
    - perforation_density (float): The proportion of each platform's surface that is perforated.
    - seed (int): Random seed for reproducibility.
    
    Returns:
    - List[Rhino.Geometry.Brep]: A list of brep objects representing the 3D geometries of the concept model.
    \"""
    import Rhino.Geometry as rg
    import random
    
    random.seed(seed)
    geometries = []
    
    for level in range(num_levels):
        # Calculate level height
        height = level * 3  # Each level is 3 meters apart
        
        # Define the size and position of the current platform
        platform_size = base_size * (1 - 0.1 * level)  # Gradually reduce size for upper levels
        offset_x = random.uniform(-max_offset, max_offset)
        offset_y = random.uniform(-max_offset, max_offset)
        
        # Create base rectangle for the platform
        base_rect = rg.Rectangle3d(rg.Plane.WorldXY, platform_size, platform_size)
        base_rect_pln = rg.Plane(base_rect.Plane.Origin + rg.Vector3d(offset_x, offset_y, height), base_rect.Plane.XAxis, base_rect.Plane.YAxis)
        base_rect = rg.Rectangle3d(base_rect_pln, platform_size, platform_size)
        
        # Convert rectangle to surface and then to brep
        surface = rg.Brep.CreateFromSurface(rg.NurbsSurface.CreateFromCorners(base_rect.Corner(0), base_rect.Corner(1), base_rect.Corner(3), base_rect.Corner(2)))
        
        # Determine perforation
        num_perforations = int(perforation_density * 10)
        for _ in range(num_perforations):
            # Randomly place perforations
            pf_size = random.uniform(platform_size * 0.2, platform_size * 0.4)
            pf_x = random.uniform(-platform_size / 2, platform_size / 2)
            pf_y = random.uniform(-platform_size / 2, platform_size / 2)
            
            # Create a circular perforation
            center = rg.Point3d(pf_x + offset_x, pf_y + offset_y, height)
            circle = rg.Circle(center, pf_size)
            circle_breps = rg.Brep.CreatePlanarBreps([circle.ToNurbsCurve()])
            
            if circle_breps:
                circle_brep = circle_breps[0]
                # Subtract perforation from platform
                result_breps = rg.Brep.CreateBooleanDifference([surface], [circle_brep], 0.01)
                if result_breps:
                    surface = result_breps[0]
        
        geometries.append(surface)
    
    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_perforated_vertical_landscape(base_size=15, num_levels=4, max_offset=2, perforation_density=0.5, seed=10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_perforated_vertical_landscape(base_size=12, num_levels=6, max_offset=1.5, perforation_density=0.4, seed=24)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_perforated_vertical_landscape(base_size=8, num_levels=3, max_offset=5, perforation_density=0.2, seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_perforated_vertical_landscape(base_size=20, num_levels=5, max_offset=4, perforation_density=0.6, seed=7)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_perforated_vertical_landscape(base_size=18, num_levels=7, max_offset=3, perforation_density=0.25, seed=33)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
