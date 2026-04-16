

# ---------------------------------------------------------------------------
# Run the generator
# ---------------------------------------------------------------------------
generate_pattern()
import maya.cmds as cmds

# Clear the scene.
cmds.file(new=True, force=True)

box_width = 4
box_height = 6
box_depth = 4
Orb_radius = 2



def generate_pattern():
    box_width = 4
    box_height = 6
    box_depth = 4
    Orb_radius = 2
    num_rows = 5        # Number of rows in the pattern.
    num_cols = 5        # Number of columns in the pattern.
    spacing = 3.0       # Distance between object centers.
    x_pos = 12
    z_pos = -12
     
    for row in range(num_rows):
        for col in range(num_cols):
            # Calculate position
            x_pos = col * spacing
            z_pos = row * spacing
            if (row + col) % 2 == 0:
                box = cmds.polyCube(
                    name="box_01",
                    width=box_width,
                    height=box_height,
                    depth=box_depth,
                )
                cmds.move(x_pos, box_height /2, z_pos, box)
            else:
                Orb= cmds.polySphere(
                    name="Orb_01",
                    radius=Orb_radius,
                )
                cmds.move(x_pos, Orb_radius, z_pos, Orb)
              

    



# ---------------------------------------------------------------------------
# Run the generator
# ---------------------------------------------------------------------------
generate_pattern()

import maya.cmds as cmds

# Clear the scene.
cmds.file(new=True, force=True)


def generate_pattern():
    """Generate a procedural pattern of objects using nested loops.

    This function should:
        1. Define variables for rows, columns, and spacing.
        2. Use a nested for-loop to iterate over rows and columns.
        3. Inside the loop, use a conditional to vary object properties.
        4. Create and position each object.
    """
    # --- Configuration variables ---
    num_rows = 5        # Number of rows in the pattern.
    num_cols = 5        # Number of columns in the pattern.
    spacing = 3.0       # Distance between object centers.

    # TODO: Create a nested loop that iterates over rows and columns.
    #
    # HINT -- your loop structure should look something like this:
    #
    #   for row in range(num_rows):
    #       for col in range(num_cols):
    #           # Calculate position
    #           x_pos = col * spacing
    #           z_pos = row * spacing
    #
    #           # TODO: Add a conditional here that changes something
    #           # based on row, col, or (row + col).
    #           # For example:
    #           #   if (row + col) % 2 == 0:
    #           #       create a cube
    #           #   else:
    #           #       create a sphere
    #
    #           # TODO: Create the object using cmds.polyCube(), etc.
    #
    #           # TODO: Position the object using cmds.move().
    #
    #           # TODO: (Optional) Vary the scale using cmds.scale().
import maya.cmds as cmds

# Clear the scene.
cmds.file(new=True, force=True)





def generate_pattern():
    box_width = 1
    box_height = 1
    box_depth = 1
    Orb_radius = 1
    num_rows = 5        # Number of rows in the pattern.
    num_cols = 5        # Number of columns in the pattern.
    spacing = 3.0       # Distance between object centers.
    x_pos = 12
    z_pos = -12
     
    for row in range(num_rows):
        for col in range(num_cols):
            # Calculate position
            x_pos = col * spacing
            z_pos = row * spacing
            if (row + col) % 2 == 0:
                box = cmds.polyCube(
                    name="box_01",
                    width=box_width,
                    height=box_height,
                    depth=box_depth,
                )
                cmds.move(x_pos, box_height /2, z_pos, box)
            else:
                Orb= cmds.polySphere(
                    name="Orb_01",
                    radius=Orb_radius,
                )
                cmds.move(x_pos, Orb_radius, z_pos, Orb)
# ---------------------------------------------------------------------------
# Run the generator
# ---------------------------------------------------------------------------
generate_pattern()

# Frame everything in the viewport.
cmds.viewFit(allObjects=True)
print("Pattern generated successfully!")

Pattern generated successfully!
select -cl  ;
