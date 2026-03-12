# Created for 0018_0002_perforated_vertical_landscape.json

""" Summary:
The provided function, `create_perforated_vertical_landscape`, generates an architectural concept model based on the "Perforated vertical landscape" metaphor. It creates a series of staggered, layered platforms with varying heights and dimensions, simulating a vertical natural landscape. The function incorporates random offsets to enhance the cascading effect, while voids are strategically placed to allow light and air flow, reflecting the metaphor's essence. By adjusting parameters like base dimensions, height, number of levels, and void percentage, the model achieves a balance between solid and void, fostering dynamic spatial interconnections and visual pathways that bridge the interior and exterior environments."""

#! python 3
function_code = """def create_perforated_vertical_landscape(base_length, base_width, height, num_levels, void_percentage):
    \"""
    Creates an architectural Concept Model embodying the 'Perforated vertical landscape' metaphor.
    
    This function generates a series of staggered, layered platforms with perforations to allow light and air
    to flow through the structure. The model incorporates terraces and niches, emphasizing permeability, 
    verticality, and spatial interconnection.

    Parameters:
    - base_length (float): The length of the base of the structure in meters.
    - base_width (float): The width of the base of the structure in meters.
    - height (float): The total height of the structure in meters.
    - num_levels (int): The number of staggered levels or platforms in the structure.
    - void_percentage (float): The percentage of each platform's area that should be voids, ranging from 0 to 1.

    Returns:
    - List[Rhino.Geometry.Brep]: A list of 3D geometries representing the conceptual model.
    \"""
    import Rhino.Geometry as rg
    import random

    # Initialize random seed for reproducibility
    random.seed(42)

    # Calculate the height of each level
    level_height = height / num_levels

    # Initialize list to hold the Brep geometries
    geometries = []

    for i in range(num_levels):
        # Calculate the offset for the current level to create staggered effect
        offset_x = random.uniform(-0.5, 0.5) * base_length * 0.1
        offset_y = random.uniform(-0.5, 0.5) * base_width * 0.1

        # Create the base rectangle for the current level
        base_plane = rg.Plane.WorldXY
        base_plane.OriginZ = i * level_height
        rectangle = rg.Rectangle3d(base_plane, base_length, base_width)
        
        # Apply translation using transformation
        translation = rg.Transform.Translation(rg.Vector3d(offset_x, offset_y, 0))
        rectangle.Transform(translation)

        # Convert rectangle to a surface
        surface = rg.Brep.CreatePlanarBreps(rectangle.ToNurbsCurve())[0]

        # Determine number of voids based on percentage
        num_voids = int(void_percentage * 10)

        # Create voids (holes) in the surface
        for _ in range(num_voids):
            void_length = random.uniform(base_length * 0.05, base_length * 0.2)
            void_width = random.uniform(base_width * 0.05, base_width * 0.2)
            void_x = random.uniform(rectangle.Corner(0).X, rectangle.Corner(1).X - void_length)
            void_y = random.uniform(rectangle.Corner(0).Y, rectangle.Corner(3).Y - void_width)

            void_plane = rg.Plane(base_plane)
            void_plane.OriginX = void_x
            void_plane.OriginY = void_y
            void_rectangle = rg.Rectangle3d(void_plane, void_length, void_width)
            void_surface = rg.Brep.CreatePlanarBreps(void_rectangle.ToNurbsCurve())[0]

            # Subtract void from surface
            surface = rg.Brep.CreateBooleanDifference([surface], [void_surface], 0.01)[0]

        # Convert the final surface to a Brep and add to the list
        brep = surface
        geometries.append(brep)

    return geometries"""

try:
    exec(function_code)
    import ghpythonlib.treehelpers as th
    from Grasshopper.Kernel.Data import GH_Path
    geometry_states = []
    # Generate sample geometry 1/5
    geometry = create_perforated_vertical_landscape(10.0, 5.0, 15.0, 4, 0.3)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 2/5
    geometry = create_perforated_vertical_landscape(12.0, 6.0, 20.0, 5, 0.25)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 3/5
    geometry = create_perforated_vertical_landscape(8.0, 4.0, 10.0, 3, 0.2)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 4/5
    geometry = create_perforated_vertical_landscape(15.0, 7.0, 25.0, 6, 0.4)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Generate sample geometry 5/5
    geometry = create_perforated_vertical_landscape(14.0, 8.0, 18.0, 5, 0.35)
    geometry = list(geometry) if not isinstance(geometry, list) else geometry
    geometry_states.append(geometry)

    # Convert the list of geometries to a Grasshopper DataTree
    geometry_states = th.list_to_tree(geometry_states)

    print("success")
except Exception as e:
    print("Error: ", e)
