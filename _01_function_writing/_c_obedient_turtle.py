"""
Make an obedient turtle that will obey commands to draw shapes.
"""
from tkinter import messagebox, simpledialog, Tk
import turtle


if __name__ == '__main__':
    # TODO)
    #   1. Create a turtle.
    turt = turtle.Turtle()
    #   2. Write 3 method definitions for drawing a square, triangle, and
    #      circle.
    square(forward1, left1, forward2, left2, forward3, left3, forward4):
    #   3. Ask the user for the for a shape to draw.
    question = simpledialog.askstring(title="Shape", prompt="What shape would you like to draw?")
    #   4. Draw the appropriate shape depending on their answer (call the right
    #      function)
    if question == 'square':
        square()
    elif question == 'triangle':
        triangle()
    elif question == 'circle':
        circle()
    pass
