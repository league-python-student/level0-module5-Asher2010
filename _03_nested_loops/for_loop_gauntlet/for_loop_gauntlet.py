"""
Create algorithms and use to solve
https://central.jointheleague.org/levels/Level0/Recipes/ForLoopGauntlet.html
"""


if __name__ == '__main__':
    pass

for i in range(100):
    print(i+1)

for i in range(100):
    print((i+2)-1)

for i in range(100):
    if i % 2 == 0:
        print(i+2)

for i in range(100):
    if i % 2 == 1:
        print(i)

for i in range(500):
    if i % 2 == 1:
        print(str(i+1) + " is even")
    else:
        print(str(i+1) + " is odd")

for i in range(777):
    if i % 7 == 0:
        print(i)

year = 2010
for i in range(13):
    print("In " + str(year) + " I was " + str(i) + " years old")
    year += 1

for i in range(3):
    for j in range(3):
        print(str(i) + " " + str(j))

h = 0
for i in range(3):
    for j in range(i, i+3):
            h += 1
            print(str(h), end=" ")
    print()

h = 0
for i in range(10):
    for j in range(i, i + 10):
        h += 1
        print(str(h), end=" ")
    print()



for i in range(8):
    for j in range(i):
        print("*", end=" ")
    print()










