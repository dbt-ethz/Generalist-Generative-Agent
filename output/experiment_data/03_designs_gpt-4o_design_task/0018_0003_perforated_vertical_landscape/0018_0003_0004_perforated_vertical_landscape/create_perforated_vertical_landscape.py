# Created for 0018_0003_perforated_vertical_landscape.json

""" Summary:
The provided function, `create_perforated_vertical_landscape`, generates an architectural concept model based on the 'Perforated vertical landscape' metaphor by creating a series of vertical fins or ribs interspersed with voids. It defines parameters such as the number, height, thickness, and spacing of the fins, as well as the size of the voids. By using Rhino's geometry tools, the function constructs vertical surfaces that allow light and air to penetrate, reflecting the metaphor's emphasis on permeability and natural integration. The resulting model showcases a rhythmic interplay of solid and void, evoking a sculptural relationship between the structure and its environment."""

#! python 3
function_code = """def create_perforated_vertical_landscape(num_fins, fin_height, fin_thickness, fin_spacing, void_size, randomness_seed=42):
    \"""
    Creates an architectural Concept Model based on the 'Perforated vertical landscape' metaphor.
    
    The model consists of a series of vertical fins or ribs with interspersed voids,
    emphasizing integration with natural elements through light, air, and view permeability.
    
    Parameters:
    - num_fins: int, the number of vertical fins or ribs.
    - fin_height: float, the height of each fin in meters.
    - fin_thickness: float, the thickness of each fin in meters.
    - fin_spacing: float, the horizontal spacing between each fin in meters.
    - void_size: float, the size of each void or perforation in meters.
    - randomness_seed: int, the seed for random number generation to ensure replicability.
    
    Returns:
    - List of RhinoCommon.Brep objects representing the concept model.
    \"""
    import Rhino.Geometry as rg
    import random
    
    # Set seed for randomness
    random.seed(randomness_seed)
    
    # Initialize list to hold geometry
    geometries = []
    
    # Loop to create fins with voids
    for i in range(num_fins):
        # Base point for each fin
        base_point = rg.Point3d(i * fin_spacing, 0, 0)
        
        # Create the fin as a vertical surface
        fin_profile = rg.Line(base_point, rg.Point3d(base_point.X, 0, fin_height))
        fin_curve = fin_profile.ToNurbsCurve()
        fin = rg.Brep.CreateFromSurface(rg.Surface.CreateExtrusion(fin_curve, rg.Vector3d(0, fin_thickness, 0)))
        
        # Add voids to the fin
        num_voids = int(fin_height / (2 * void_size))
        for j in range(num_voids):
            void_center = rg.Point3d(
                base_point.X + fin_thickness / 2,
                base_point.Y,
                (j * 2 + 1) * void_size
            )
            void_radius = void_size / 2
            void_sphere = rg.Sphere(void_center, void_radius).ToBrep()
            
            # Subtract void from fin
            void_diff = rg.Brep.CreateBooleanDifference([fin], [void_sphere], 0.01)
            if void_diff:
                fin = void_diff[0]
        
        # Add the fin with voids to the geometries list
        geometries.append(fin)
    
    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_perforated_vertical_landscape(num_fins=10, fin_height=3.0, fin_thickness=0.1, fin_spacing=0.5, void_size=0.2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_perforated_vertical_landscape(num_fins=8, fin_height=4.5, fin_thickness=0.15, fin_spacing=0.6, void_size=0.3, randomness_seed=123)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_perforated_vertical_landscape(num_fins=12, fin_height=2.5, fin_thickness=0.2, fin_spacing=0.4, void_size=0.25, randomness_seed=99)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_perforated_vertical_landscape(num_fins=5, fin_height=6.0, fin_thickness=0.2, fin_spacing=0.7, void_size=0.15, randomness_seed=10)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_perforated_vertical_landscape(num_fins=15, fin_height=5.0, fin_thickness=0.2, fin_spacing=0.3, void_size=0.4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
