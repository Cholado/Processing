# setup is static and draw works with frames
# depending where you put the background affects output a lot
height = 600
width = 600
def setup():
    size(height, width)
    stroke(255)
      
def draw():
    """
    Draws a line from the center of the canvas
    """
    line(height/2, width/2, mouseX, mouseY)
     
def mousePressed():
    """
    Interactive change background color on click
    """
    background(random(255), random(255), random(255))
