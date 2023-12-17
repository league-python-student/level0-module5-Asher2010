"""
Go to the recipe to run the demonstration before starting this program
"""
x1 = 250
x2 = 500
y = 250
speed1 = 5
speed2 = -5


def setup():
    # Set the size of your sketch to be a rectangle like in the recipe demonstration
    size(750, 500)
    # Call the noFill() command so all the ellipses will be transparent
    noFill()
def draw():
    global x1
    global x2
    global y
    global speed1
    global speed2
    ringSize = 500
    background(255)
    # Use a for loop to make the first set of rings that will start in the left half
    # of the window.
    for i in range(100):
        circle(x1, y, ringSize)
        circle(x2, y, ringSize)
        ringSize = ringSize - 5
    # Make this set of rings move across the sketch to the right 
    # Hint: Make two variables, one for x and another for the speed. 
    #       Then increase x by the amount in speed.

    # When the rings reach the right side of the sketch, reverse the direction so
    # they move.
    # Hint: speed = -speed */
    if x1 > 500:
        speed1 = speed1 * -1
    if x1 < 250:
        speed1 = speed1 * -1
    x1 = x1 + speed1
    if x2 < 250:
        speed2 = speed2 * -1
    if x2 > 500:
        speed2 = speed2 * -1
    x2 = x2 + speed2     
    # When the rings reach the left side of the sketch, reverse the direction again
        
    # CHALLENGE - to finish the Amazing Rings
     
    # Add another for loop to draw the second set of rings that will start in the
    # right half of the window
    # Make this set of rings move in the opposite direction to the other rings
    # These rings must also "bounce" off the sides of the window.
