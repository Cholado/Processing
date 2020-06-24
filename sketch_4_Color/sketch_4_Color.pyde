size(400, 200)     # setting canvas
background(255)    # Setting the background to white
stroke(0)          # Setting the outline (stroke) to black
fill(150)          # Setting the interior of a shape (fill) to grey 
rect(50,50,75,100) # Drawing the rectangle
stroke(255, 0, 0)  # setting the outline (stroke) to red
noFill()           # Eliminating the filling of a shape
ellipse(160,160,50,50) #Drawing the ellipse
noStroke()
# Bright red
fill(255, 0, 0)
ellipse(20, 20, 16, 16)

# Dark red
fill(127, 0, 0)
ellipse(40, 20, 16, 16)

# Pink (pale red)
fill(255, 200, 200)
ellipse(60, 20, 16, 16)

# No fourth argument means 100% opacity.
fill(0, 0, 255)
rect(200, 0, 100, 200)

# 255 means 100% opacity.
fill(255, 0, 0, 255)
rect(200, 0, 200, 40)

# 75% opacity.
fill(255, 0, 0, 191)
rect(200, 50, 200, 40)

# 55% opacity.
fill(255, 0, 0, 127)
rect(200, 100, 200, 40)

# 25% opacity.
fill(255, 0, 0, 63)
rect(200, 150, 200, 40)
