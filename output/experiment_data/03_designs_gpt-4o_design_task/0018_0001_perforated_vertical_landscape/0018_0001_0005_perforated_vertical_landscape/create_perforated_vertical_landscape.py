# Created for 0018_0001_perforated_vertical_landscape.json

""" Summary:
The function `create_perforated_vertical_landscape` generates an architectural concept model based on the "Perforated vertical landscape" metaphor by creating a vertical structure with alternating solid and void elements. It employs parameters such as height, width, depth, and layers to define the model's dimensions and complexity. Utilizing randomization, the function creates perforated panels that allow light and air to permeate the structure, simulating natural erosion and geological textures. The result is a dynamic interplay of light and shadow, enhancing spatial relationships and maintaining a balance between transparency and privacy, effectively embodying the metaphor's essence."""

#! python 3
function_code = """def create_perforated_vertical_landscape(height=30, width=15, depth=10, num_layers=5, randomness_seed=42):
    \"""
    Create an architectural Concept Model embodying the 'Perforated vertical landscape' metaphor.
    
    This function generates a vertical structure with alternating solid and void elements, aiming to create a dynamic interplay between light, shadow, and spatial relationships. The design is inspired by natural landscapes, incorporating layers, textures, and perforations that mimic geological formations.
    
    Parameters:
    - height (float): The total height of the structure in meters.
    - width (float): The width of the structure in meters.
    - depth (float): The depth of the structure in meters.
    - num_layers (int): The number of vertical layers or zones in the structure.
    - randomness_seed (int): Seed for random number generator to ensure replicable results.
    
    Returns:
    - List of RhinoCommon Brep objects: The generated 3D geometries representing the concept model.
    \"""
    import Rhino.Geometry as rg
    import random
    
    random.seed(randomness_seed)
    geometries = []
    
    layer_height = height / num_layers
    void_probability = 0.3  # Probability to create a void instead of solid
    
    # Function to create a perforated panel
    def create_perforated_panel(base_surface, void_density=0.2):
        panel_breps = []
        u_divisions = int(width // 2)
        v_divisions = int(layer_height // 2)
        
        u_domain = base_surface.Domain(0)
        v_domain = base_surface.Domain(1)
        
        # Iterate over a grid on the surface
        for i in range(u_divisions):
            for j in range(v_divisions):
                # Determine the subdomain for the grid cell
                u0 = u_domain.ParameterAt(i / u_divisions)
                u1 = u_domain.ParameterAt((i + 1) / u_divisions)
                v0 = v_domain.ParameterAt(j / v_divisions)
                v1 = v_domain.ParameterAt((j + 1) / v_divisions)
                
                subdomain = rg.Interval(u0, u1), rg.Interval(v0, v1)
                sub_surface = base_surface.Trim(subdomain[0], subdomain[1])
                
                # Randomly decide if this cell should be a void
                if random.random() > void_density:
                    panel_breps.append(sub_surface.ToBrep())
        
        return panel_breps
    
    # Create layers
    for i in range(num_layers):
        # Base position for this layer
        base_z = i * layer_height
        layer_base = rg.Plane(rg.Point3d(0, 0, base_z), rg.Vector3d.ZAxis)
        
        # Create a layer surface and perforate it
        layer_surface = rg.Surface.CreateExtrusion(rg.LineCurve(rg.Point3d(0, 0, base_z), rg.Point3d(0, depth, base_z)).ToNurbsCurve(), rg.Vector3d(width, 0, 0))
        perforated_panels = create_perforated_panel(layer_surface)
        
        geometries.extend(perforated_panels)
        
        # Randomly decide if this layer should be solid or void
        if random.random() > void_probability:
            solid_brep = rg.Brep.CreateFromBox(rg.BoundingBox(rg.Point3d(0, 0, base_z), rg.Point3d(width, depth, base_z + layer_height)))
            geometries.append(solid_brep)
    
    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_perforated_vertical_landscape(height=40, width=20, depth=15, num_layers=6, randomness_seed=123)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_perforated_vertical_landscape(height=25, width=10, depth=5, num_layers=4, randomness_seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_perforated_vertical_landscape(height=35, width=25, depth=12, num_layers=7, randomness_seed=77)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_perforated_vertical_landscape(height=50, width=30, depth=20, num_layers=8, randomness_seed=56)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_perforated_vertical_landscape(height=45, width=18, depth=14, num_layers=5, randomness_seed=88)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
