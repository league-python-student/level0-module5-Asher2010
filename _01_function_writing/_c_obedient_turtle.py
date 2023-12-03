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
    def square(forward, left):
        turt.forward(forward)
        turt.left(left)
        turt.forward(forward)
        turt.left(left)
        turt.forward(forward)
        turt.left(left)
        turt.forward(forward)
    def triangle(left1, forward1):
        turt.left(left1)
        turt.forward(forward1)
        turt.left(left1)
        turt.forward(forward1)
        turt.left(left1)
        turt.forward(forward1)
    def circle(radius):
        turt.circle(radius)
    #   3. Ask the user for the for a shape to draw.
    question = simpledialog.askstring(title="Shape", prompt="What shape would you like to draw?")
    #   4. Draw the appropriate shape depending on their answer (call the right
    #      function)
    if question == 'square':
        square(90, 90)
    elif question == 'triangle':
        triangle(120, 90)
    elif question == 'circle':
        circle(100)
    pass
