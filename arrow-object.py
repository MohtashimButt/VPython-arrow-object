from vpython import *
  
arrow(pos = vector(0, 0, 0),
      opacity = 1,
      length = 3,
      color = color.yellow)

arrow(pos = vector(4, 0, 0),
      axis = vector(1,1,1),
      opacity = 0.3,
      length = 3,
      color = color.orange)


arrow(pos = vector(0, 2, 0),
      opacity = 1,
      length = 6,
      color = color.red)
  
arrow(pos = vector(0, 5, 0),
      opacity = 1,
      length = 3,
      shaftwidth = 4,
      color = color.blue)

arrow(pos = vector(0, -3, 0),
      opacity = 1,
      length = 3,
      headwidth = 4,
      color = color.cyan)

arrow(pos = vector(0, -6, 0),
      opacity = 1,
      length = 3,
      headlength = 4,
      color = color.magenta)


# Create X-axis arrow
arrow_x = arrow(pos=vector(0, 0, 0), axis=vector(1, 0, 0), color=color.red, shaftwidth=0.05, length = 10)

# Create Y-axis arrow
arrow_y = arrow(pos=vector(0, 0, 0), axis=vector(0, 1, 0), color=color.green, shaftwidth=0.05, length = 10)

# Create Z-axis arrow
arrow_z = arrow(pos=vector(0, 0, 0), axis=vector(0, 0, 1), color=color.blue, shaftwidth=0.05, length = 10)