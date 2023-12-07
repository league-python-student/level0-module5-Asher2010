"""
Write code that can tell if a number is prime.
A prime number is a number that is only divisible by 1 and itself.
"""
from tkinter import messagebox, simpledialog, Tk

window = Tk()
window.withdraw()


if __name__ == '__main__':
    # TODO)
    #  1. Ask the user for a number
    #  2. Use a for loop, if statement, and modulo to find if the number
    #     is prime.
    #  3. If the number is divisible by any number other than 1 or itself,
    #     the number is not prime.
    number = simpledialog.askstring(title=None, prompt="Pick a number")
    if int(number) % 2 == 0 or int(number) % 3 == 0:
        messagebox.showinfo(title=None, message="Your number is not prime")
    else:
        messagebox.showinfo(title=None, message="Your number is prime")
    pass
