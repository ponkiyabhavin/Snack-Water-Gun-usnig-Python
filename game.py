import random


def game_Win(comp, You):

    if comp == You:
        return None

    elif comp == 's':
        if You == 'w':
            return False
        elif You == 'g':
            return True

    elif comp == 'w':
        if You == 'g':
            return False
        elif You == 's':
            return True

    elif comp == 'g':
        if You == 's':
            return False
        elif You == 'w':
            return True


print("Comp  Turn : Snake(s) Water(w) or Gun(g)?\n")
randNo = random.randint(1, 3)

if randNo == 1:
    comp = 's'
elif randNo == 2:
    comp = 'w'
elif randNo == 3:
    comp = 'g'

You = input("Your Turn : Snake(s) Water(w) or Gun(g)?\n")

a = game_Win(comp, You)

print(f"Computer choose {comp}")
print(f"You choose {You}")
if a == None:
    print("The game is a tie!")
elif a:
    print("You win!")
else:
    print("You Lose!")
