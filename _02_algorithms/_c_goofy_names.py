"""
Write an algorithm to change a string into a "goofy" version.
"""
from tkinter import messagebox, simpledialog, Tk
window = Tk()
window.withdraw()

if __name__ == '__main__':
    # TODO)
    #  1. Ask the user to enter their name.
    #  2. Use a loop to alternately modify each character of the name into
    #     uppercase and lowercase letters until a new "goofy" representation
    #     of their name has been constructed.
    #     For example, if they enter their name as Alexander Hamilton
    #     their goofy name will be AlExAnDeR HaMiLtOn
    #  3. Show the user the goofy version of their name in a pop-up.
    name = simpledialog.askstring(title=None, prompt="What is your name?")
    goofy_name = ''
    for i in range(len(name)):
        if i % 2 == 1:
            goofy_name = goofy_name + name[i].lower()
        else:
            goofy_name = goofy_name + name[i].upper()
    messagebox.showinfo(title=None, message=goofy_name)
    pass
