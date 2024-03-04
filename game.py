intro = ("""
 __          __  _                          
 \ \        / / | |                         
  \ \  /\  / /__| | ___ ___  _ __ ___   ___ 
   \ \/  \/ / _ \ |/ __/ _ \| '_ ` _ \ / _ )
    \  /\  /  __/ | (_| (_) | | | | | |  __/
     \/  \/ \___|_|\___\___/|_| |_| |_|\___|...
    To...
    The Game Made Without Any Imports!! (.com)
""")

print(intro)


def option1():
    print("You Walk Down The Hallway...")
    print("You See... A Big Monster!")
    print("The Monster Eats You.")
    print("""
* _ __   ___  _ __ ___    _ __   ___  _ __ ___    _ __   ___  _ __ ___ *
 | '_ \ / _ \| '_ ` _ \  | '_ \ / _ \| '_ ` _ \  | '_ \ / _ \| '_ ` _ \ 
 | | | | (_) | | | | | | | | | | (_) | | | | | | | | | | (_) | | | | | |
 |_| |_|\___/|_| |_| |_| |_| |_|\___/|_| |_| |_| |_| |_|\___/|_| |_| |_|
""")
    print("You Lost!")

def option2():
    print("You Walk Down The Stairs...")
    print("You See.. The Exit!")
    print("You Won! You Get Nothing... HAHhaHAHaHaHaHaH")

def option3():
    print("You Run Down The Hallway...")
    print("You Fall Down A Hole, A Trapdoor Opened Below You.")
    print("You Fall Into A Pit Of Zombies!")
    print("""
*_ __   ___  _ __ ___    _ __   ___  _ __ ___    _ __   ___  _ __ ___ *
 | '_ \ / _ \| '_ ` _ \  | '_ \ / _ \| '_ ` _ \  | '_ \ / _ \| '_ ` _ \ 
 | | | | (_) | | | | | | | | | | (_) | | | | | | | | | | (_) | | | | | |
 |_| |_|\___/|_| |_| |_| |_| |_|\___/|_| |_| |_| |_| |_|\___/|_| |_| |_|
""")
    print("You Lost!")

def main():
    print("You Find Yourself Trapped In A Room, Spikes Are Slowly Coming Towards You.\nThere Are 3 Doors Infront Of You.\nWhich One Do You Go Through?\n1, 2, 3, or '0 (No Door)'")
    option = input("What Will You Choose?: ")

    if option == '1':
        option1()
    elif option == '2':
        option2()
    elif option == '3':
        option3()
    elif option == '0':
        print("The Spikes Impale You & You Die.\nYou Lost!")

    else:
        print("Incorrect Option!")

if __name__ == "__main__":
        main()