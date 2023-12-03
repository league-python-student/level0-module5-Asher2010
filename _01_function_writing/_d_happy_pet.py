"""
Write methods to represent the activities that will make the user's pet happy.
"""
from tkinter import messagebox, simpledialog, Tk


if __name__ == '__main__':
    # TODO)
    #   1. Ask the user to enter the type of pet they want (give them a few
    #      choices).
    #   2. Use a loop (maybe a while loop?) to keep offering interactions with
    #      their pet until the desired pet happiness level has been reached.
    #      Examples of activities are: Feed, Walk, Play
    #   3. Write a method for each of the pet activities offered.
    #      Each activity should increase (or decrease) the pet's happiness
    #      level by a different amount, depending on the kind of pet they
    #      have. For example, a fish might not enjoy a walk!

    question = simpledialog.askstring(title="Pet", prompt="Would you like a dog, fish, or cat?")

    cat_happiness = 0
    dog_happiness = 0
    fish_happiness = 0

    if question == "cat":
        while cat_happiness < 101:
            cat_question = simpledialog.askstring(title=None, prompt="Would you like to feed, walk, or play with your cat?")
            if cat_question == "feed":
                cat_happiness += 50
            elif cat_question == "walk":
                cat_happiness += 10
            elif cat_question == "play":
                cat_happiness += 30
            else:
                break
    elif question == "dog":
        while dog_happiness < 101:
            dog_question = simpledialog.askstring(title="Activity", prompt="Would you like to feed, walk, or play with your dog?")
            if dog_question == "feed":
                dog_happiness += 30
            elif dog_question == "walk":
                dog_happiness += 40
            elif dog_question == "play":
                dog_happiness += 50
            else:
                break
    elif question == "fish":
        while fish_happiness < 101:
            fish_question = simpledialog.askstring(title="Activity", prompt="Would you like to feed, walk, or play with your fish?")
            if fish_question == "feed":
                fish_happiness += 50
            elif fish_question == "walk":
                fish_happiness -= 100
            elif fish_question == "play":
                fish_happiness += 10
            else:
                break
