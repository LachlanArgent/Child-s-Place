import time
from random import *
#Decision 1
def dec1():
    points = 0
    dec1in = input("Which way do you want to go? Left or Right? ")
    time.sleep(0.5)
    dec1in = dec1in.lower()
    
    if dec1in == "left":
        points = points + 100
        print("You continue left along a long path")
        time.sleep(0.5)
        dec2()
    

    elif dec1in == "right":
        print("You walk along a path for a while until you come to a rope bridge")
        time.sleep(0.5)
        dec3()


    elif dec1in == "up up down down left right left right b a":
        time.sleep(1)
        print("***************************************************************")
        print("""
01011001 01001111 01010101 00100000 01000110 01001111
01010101 01001110 01000100 00100000 01001001 01010100
00100001 00100001 00100001 00001010 01000111 01101111
00100000 01110100 01101111 00100000 01110100 01101000
01100101 00100000 01110000 01101100 01100001 01100011
01100101 00100000 01101001 00100000 01101100 01101111
01110110 01100101 01100100 00100000 01100001 01110011
00100000 01100001 00100000 01100011 01101000 01101001
01101100 01100100 00101110 00100000 01010100 01101000
01100101 00100000 01100011 01101111 01100100 01100101
00100000 01110111 01101001 01101100 01101100 00100000
01100010 01100101 00100000 01110100 01101000 01100101
01110010 01100101 00101110 00001010 00001010 01010100
01101000 01100101 00100000 01010100 01111001 01110000
01100101 00100000 00110001 00110110 00110101 00110100
00100000 01110111 01101000 01100101 01101110 00100000
01101001 01110100 00100000 01100001 01110011 01101011
01110011 00100000 01111001 01101111 01110101 00100000
01101001 01100110 00100000 01111001 01101111 01110101
00100000 01110111 01100001 01101110 01110100 00100000
01110100 01101111 00100000 01100111 01101111 
""")
        print("***************************************************************")

        input()
        easterIn = input("Do you wish to go? Yes or No. ")
        easterIn = easterIn.lower()

        if easterIn == "1654":
            time.sleep(0.5)
            easter()

        if easterIn == "no":
            time.sleep(0.5)
            dec1()
            

    else:
        print("Thats not an option. Please try again")
        dec1()

    return None

#Decision 2
def dec2():
    print()
    print("You find a chest")
    time.sleep(0.5)
    dec2in = input("Do you want to open the chest? Yes or No. ")
    time.sleep(0.5)
    dec2in = dec2in.lower()
    
    if dec2in == "yes":
        global key
        key = 1
        print("""You find a key""")

        print("     _____________  ")
        print("    /      _      \ ")
        print("    [] :: (_) :: [] ")
        print("    [] ::::::::: [] ")
        print("    [] ::::::::: [] ")
        print("    [] ::::::::: [] ")
        print("    [] ::::::::: [] ")
        print("    [_____________] ")
        print("        I     I     ")
        print("        I_   _I     ")
        print("         /   \      ")
        print("         \   /      ")
        print("         (   )      ")
        print("         /   \      ")
        print("         \___/      ")
        print("")
        dec4()

    if dec2in == "no":
        dec4()

    else:
        print("Thats not an option. Please try again")
        dec2()
    
#Decision 3
def dec3():
    print()
    dec3in = input("You are faced with another decision. Will you cross the bridge? yes or no. ")
    dec3in = dec3in.lower()
    time.sleep(0.5)

    if dec3in == "yes":
        print("""You walk accross the bridge, feeling uncertain.
Half way across you feel the rope give way.
You fell to your death.""")
        time.sleep(0.5)
        END()

    elif dec3in == "no":
        print("You walk back along the path you came and take the other route.")
        print()
        dec4()
        time.sleep(0.5)

    else:
        print("Thats not an option. Please try again")
        dec3()
        time.sleep(0.5)
        
#Decision 4
def dec4():
    print()
    print("You hear a russtling in the bushes")
    time.sleep(0.5)
    print("Out jumps a monster")
    time.sleep(0.5)
    dec4in = input("Do you want to ATTACK or RUN? ")
    time.sleep(0.5)
    dec4in = dec4in.lower()

    if dec4in == "attack":
        power = randint(1, 1101)
        print("You draw your", weapon)
        if power > int(strength):
            time.sleep(0.5)
            print("The monster is much stronger than you")
            time.sleep(0.5)
            print("you cannot fight it off")
            time.sleep(0.5)
            END()

        else:
            print("You are stronger than the monster")
            time.sleep(0.5)
            print("You stun the monster")
            time.sleep(0.5)
            print()
            dec5()

    if dec4in == "run":
        odds = randint(0, 1101)
        print("You run from the monster")
        time.sleep(0.5)

        if odds <= int(intelligence):
            print("You are faster than the monster and out run it")
            time.sleep(0.5)
            print()
            dec5()

        else:
            print("You cannot outrun the monster")
            time.sleep(0.5)
            END()

    else:
        print("That is not an option. Please try again.")
        dec4()
#Decision 5
def dec5():
    global points
    print()
    print("You continue walking.")
    time.sleep(0.5)
    print("You encounter a patch of cleared trees.")
    time.sleep(0.5)
    print("In the middle is a large stone,")
    time.sleep(0.5)
    print("Carved into the shape of a bed")
    time.sleep(0.5)
    print("with channels carved into the top edge.")
    time.sleep(0.5)

    inv = input("Do you want to investigate? Yes or No. ")
    inv = inv.lower()

    if inv == "yes":
        chance = randint(0, 1101)

        if chance > int(intelligence):
            print("You walk upto the stone bed and notice engraving on the side")
            time.sleep(0.5)
            print("It appears to be a ritual site")
            time.sleep(0.5)
            print("You notice people walking in on you all around")
            time.sleep(0.5)
            END()

        if chance <= int(intelligence):
            print("You walk upto the stone bed and notice engraving on the side")
            time.sleep(0.5)
            print("It appears to be a ritual site")
            time.sleep(0.5)
            print("You don't like the look of this so you get out")
            time.sleep(0.5)
            print()
            dec6()

    elif inv == "no":
        print("This seems too suspicious.")
        time.sleep(0.5)
        print("You turn around and walk the other way")
        time.sleep(0.5)
        print()
        dec6()

    else:
        print("Thats not an option. Please try again")
        dec5()
        time.sleep(0.5)
        
#Decision 6
def dec6():
    global coin
    print()
    print("You continue to walk, much faster paced.")
    time.sleep(0.5)
    print("There is another fork in your path.")
    time.sleep(0.5)
    route = input("Do you want to go left or right? ")
    time.sleep(0.5)
    route = route.lower()

    if route == "left":
        print("You take the left path.")
        time.sleep(0.5)
        print("While walking you hear another rustling in the bushes.")
        time.sleep(0.5)
        print("Another monster appears from the bushes.")
        time.sleep(0.5)

        routeIn = input("Do you want to ATTACK or RUN? ")
        time.sleep(0.5)
        routeIn = routeIn.lower()

        if routeIn == "attack":
            power = randint(500, 1501)
            print("You draw your", weapon)
            if power > int(strength):
                time.sleep(0.5)
                print("The monster is much stronger than you")
                time.sleep(0.5)
                print("you cannot fight it off")
                time.sleep(0.5)
                END()

            else:
                print("You are stronger than the monster")
                time.sleep(0.5)
                print("You stun the monster")
                print()
                time.sleep(0.5)
                dec7()

        if routeIn == "run":
            m2odds = randint(0, 1101)
            print("You run from the monster")
            time.sleep(0.5)

            if m2odds <= int(intelligence):
                print("You are faster than the monster and out run it")
                time.sleep(0.5)
                dec7()

            else:
                print("You cannot outrun the monster")
                time.sleep(0.5)
                END()


    if route == "right":
        print()
        print("You continue your journey along the right path")
        time.sleep(0.5)
        print("On your way you find a shiny object on the ground.")
        time.sleep(0.5)
        objIn = input("Do you want to investigate this object? Yes or No. ")
        objIn = objIn.lower()

        if objIn == "yes":
            print("You investivate the shiny object.")
            time.sleep(0.5)
            print("It appears to be a golden coin.")
            time.sleep(0.5)

            coinIn = input("Do you want to collect the coin? Yes or No. ")
            coinIn = coinIn.lower()

            if coinIn == "yes":
                print("You collect the coin.")
                time.sleep(0.5)
                coin = 1
                dec7()

            if coinIn == "no":
                print("You leave the coin")
                time.sleep(0.5)
                dec7()

            else:
                print("Thats not an option. Please try again")
                dec6()
                time.sleep(0.5)

        if objIn == "no":
            print("You continue walking past the shiny object.")
            time.sleep(0.5)
            dec7()

        else:
            print("Thats not an option. Please try again")
            dec6()
            time.sleep(0.5)

#Decision 7
def dec7():
    print()
    print("You encounter a bunny")
    time.sleep(0.5)
    bun = input("Do you want to pat the bunny?Yes or No. ")
    bun = bun.lower()
    time.sleep(0.5)

    if bun == "yes":
        print("You go to pat the bunny.")
        time.sleep(0.5)
        print("As you are just about to reach it, it bites your hand clean off.")
        time.sleep(0.5)
        print("You are now squirting blood from your wound.")
        time.sleep(0.5)
        wound = input("Do you want to tie a tourniquet, scream for help or leave it alone? ")
        wound = wound.lower()
        time.sleep(0.5)

        if wound == "tourniquet" or "tie a torniquet":
            chances = randint(0, 1)

            if chances >= 1:
                print("You tie a torniquet with your belt")
                time.sleep(0.5)
                print("The bleeding slows to a stop")
                time.sleep(0.5)
                dec8()

            elif chances <= 0:
                print("You tie a torniquet with your belt")
                time.sleep(0.5)
                print("The bleeding is too much")
                time.sleep(0.5)
                print("You bleed to death")
                time.sleep(0.5)
                END()

        if wound == "help" or "scream for help" or "scream":
            chances = randint(0, 1)

            if chances >= 1:
                print("You scream for help.")
                time.sleep(0.5)
                print("Thankfully someone comes to your aid")
                time.sleep(0.5)
                print("After a few weeks of recovery you return to the same place")
                time.sleep(0.5)
                print("Minus your hand")
                time.sleep(0.5)
                dec8()
    
            elif chances <= 0:
                print("You scream for help.")
                time.sleep(0.5)
                print("No one hears you.")
                time.sleep(0.5)
                print("You bleed to death.")
                time.sleep(0.5)
                END()
    
        if wound == "leave" or "leave it alone" or "leave it":
            print("You leave the wound alone.")
            time.sleep(0.5)
            print("You continue to bleed out.")
            time.sleep(0.5)
            print("You bleed to death.")
            time.sleep(0.5)
            END()

        else:
            print("That is not an option. Please try again.")
            time.sleep(0.5)
            dec7()

    if bun == "no":
        print("You leave the bunny alone and continue on your adventure")
        time.sleep(0.5)
        dec8()

    else:
        print("Thats not an option. Please try again")
        dec7()
        time.sleep(0.5)
        
#Decision 8
def dec8():
    global torch
    print()
    print("You walk along a smaller path.")
    time.sleep(0.5)
    print("It leads you to an intersection.")
    time.sleep(0.5)
    print("There are 3 ways you can go. North, East, or West")
    time.sleep(0.5)
    travel = input("Which way do you want to go? ")
    travel = travel.lower()

    if travel == "north":
        print("You continue north.")
        time.sleep(0.5)
        print("You walk along a narrow path.")
        time.sleep(0.5)
        print("You have come to a blockage")
        time.sleep(0.5)
        northIn = input("Do you want to CLEAR the blockage or TURN around? ")
        northIn = northIn.lower()
        time.sleep(0.5)

        if "clear" in northIn:
            print("You begin to clear the blockage.")
            time.sleep(0.5)
            print("You hear a the sound of cracking wood.")
            time.sleep(0.5)
            print("A tree begins to fall, on top of where you are working")
            time.sleep(0.5)
            print("The tree crushes you.")
            time.sleep(0.5)
            END()

        if "turn" in northIn:
            print("You turn aroung along the path you came.")
            time.sleep(0.5)
            print("You arrive at the intersection again.")
            time.sleep(0.5)
            turnIn = input("Do you want to travel EAST or WEST? ")
            turnIn = turnIn.lower()
            time.sleep(0.5)

            if turnIn == "east":
                print("You continue your journey to the east.")
                time.sleep(0.5)
                dec9()

            if turnIn == "west":
                print("You travel west.")
                print("You see a light shining.")
                print("It looks out of the ordinary.")
                westIn = input("Do you want to investigate this light?Yes or No. ")
                westIn = westIn.lower()

                
                if westIn == "yes":
                    print("You walk towards the light.")
                    print("You find a torch, dropped on the ground.")
                    torchIn = input("Do you want to pick up the torch?Yes or No. ")
                    torchIn = torchIn.lower()

                    if torchIn == "yes":
                        print("You pick up the torch.")
                        torch = 1
                        print("As you stand back up a large monster is standing there.")
                        m3 = input("Do you want to ATTACK or RUN? ")
                        time.sleep(0.5)
                        m3 = m3.lower()

                        if m3 == "attack":
                            power = randint(750, 1101)
                            print("You draw your", weapon)
                            if power > int(strength):
                                time.sleep(0.5)
                                print("The monster is much stronger than you")
                                time.sleep(0.5)
                                print("you cannot fight it off")
                                time.sleep(0.5)
                                END()

                            else:
                                print("You are stronger than the monster")
                                time.sleep(0.5)
                                print("You stun the monster")
                                time.sleep(0.5)
                                print()
                                dec9()

                        if m3 == "run":
                            odds = randint(100, 1101)
                            print("You run from the monster")
                            time.sleep(0.5)

                            if odds <= int(intelligence):
                                print("You are faster than the monster and out run it")
                                time.sleep(0.5)
                                print()
                                dec9()

                            else:
                                print("You cannot outrun the monster")
                                time.sleep(0.5)
                                END()

                        else:
                            print("That is not an option. Please try again.")
                            dec8()

                if westIn == "no":
                    print("You leave the light and continue walking.")
                    time.sleep(0.5)
                    dec9()

                else:
                    print("That is not an option. Please try again.")
                    dec8()

            else:
                print("That is not an option. Please try again.")
                dec8()

    elif travel == "east":
        print("You continue your journey to the east.")
        time.sleep(0.5)
        dec9()

    elif travel == "west":
        print("You travel west.")
        time.sleep(0.5)
        print("You see a light shining.")
        time.sleep(0.5)
        print("It looks out of the ordinary.")
        time.sleep(0.5)
        westIn = input("Do you want to investigate this light?Yes or No. ")
        westIn = westIn.lower()

        
        if westIn == "yes":
            print("You walk towards the light.")
            time.sleep(0.5)
            print("You find a torch, dropped on the ground.")
            time.sleep(0.5)
            torchIn = input("Do you want to pick up the torch?Yes or No. ")
            torchIn = torchIn.lower()
            time.sleep(0.5)

            if torchIn == "yes":
                print("You pick up the torch.")
                time.sleep(0.5)
                torch = 1
                print("As you stand back up a large monster is standing there.")
                time.sleep(0.5)
                m3 = input("Do you want to ATTACK or RUN? ")
                time.sleep(0.5)
                m3 = m3.lower()

                if m3 == "attack":
                    power = randint(750, 1101)
                    print("You draw your", weapon)
                    if power > int(strength):
                        time.sleep(0.5)
                        print("The monster is much stronger than you")
                        time.sleep(0.5)
                        print("you cannot fight it off")
                        time.sleep(0.5)
                        END()

                    else:
                        print("You are stronger than the monster")
                        time.sleep(0.5)
                        print("You stun the monster")
                        time.sleep(0.5)
                        print()
                        dec9()

                if m3 == "run":
                    odds = randint(100, 1101)
                    print("You run from the monster")
                    time.sleep(0.5)

                    if odds <= intelligence:
                        print("You are faster than the monster and out run it")
                        time.sleep(0.5)
                        print()
                        dec9()

                    else:
                        print("You cannot outrun the monster")
                        time.sleep(0.5)
                        END()

                else:
                    print("That is not an option. Please try again.")
                    dec8()

        if westIn == "no":
            print("You leave the light and continue walking.")
            time.sleep(0.5)
            dec9()

        else:
            print("That is not an option. Please try again.")
            dec8()

    else:
        print("That is not an option. Please try again.")
        dec8()
        
#Decision 9
def dec9():
    print()
    print("It begins to get dark.")
    time.sleep(0.5)
    print("You continue along a path.")
    time.sleep(0.5)
    print("Another intersection separates you from completing your journey")
    time.sleep(0.5)
    print("There are two paths you can take")
    time.sleep(0.5)
    dec9In = input("Do you want to go LEFT or RIGHT? ")
    dec9In = dec9In.lower()
    time.sleep(0.5)

    if dec9In == "left":
        print("You travel along the left path.")
        time.sleep(0.5)
        print("You walk further until the sunlight outlines a large object")
        time.sleep(0.5)
        dec10()

    if dec9 == "right":
        print("You travel right.")
        time.sleep(0.5)
        print("You see a cave.")
        time.sleep(0.5)
        print("A monster starts running toward you.")
        time.sleep(0.5)

        m4 = input("Do you want to ATTACK or RUN? ")
        time.sleep(0.5)
        m3 = m3.lower()

        if m4 == "attack":
            power = randint(750, 1101)
            print("You draw your", weapon)
            if power > int(strength):
                time.sleep(0.5)
                print("The monster is much stronger than you")
                time.sleep(0.5)
                print("you cannot fight it off")
                time.sleep(0.5)
                END()

            else:
                print("You are stronger than the monster")
                time.sleep(0.5)
                print("You stun the monster")
                time.sleep(0.5)
                print()
                dec10()

        if m4 == "run":
            odds = randint(100, 1101)
            print("You run from the monster")
            time.sleep(0.5)

            if odds <= intelligence:
                print("You are faster than the monster and out run it")
                time.sleep(0.5)
                print()
                dec10()

            else:
                print("You cannot outrun the monster")
                time.sleep(0.5)
                END()

        else:
            print("That is not an option. Please try again.")
            dec9()

    else:
        print("That is not an option. Please try again.")
        dec9()
        
    
#Decision 10
def dec10():
    global torch
    print()
    time.sleep(0.5)
    print("     /\     ")
    print("    /..\    ")
    print("   //..\\\  ")
    print("  ///..\\\\\ ")
    print(" ////..\\\\\\\ ")
    print("============")
    print("|..........|")
    print("|..........|")
    print("|..........|")
    print("|..........|")
    print("|..........|")
    print("|..........|")
    print("|..........|")
    print("|..../\....|")
    print("|...|  |]..|")
    print("|...|  |...|")
    print("============")
    print("    /  \    ")
    print("   /    \   ")
    print("  /      \  ")
    print(" /________\ ")
    print("You find a rusty tin spaceship sitting there, nature is taking it back")
    time.sleep(1)
    print("You walk to the door and see a number panel")
    time.sleep(0.5)
    numbero()
    
def numbero():
    numdec = input("Do you want to try the number pad? Yes or No.")
    time.sleep(0.5)
    numdec = numdec.lower()
    if numdec == "yes":
        npad()

    elif numdec == "no":
        ENDg()

    else:
        print("That is not an option. Please try again.")
        numbero()

def npad():
        numpad = input("Enter a 6 digit number: ")

        
            
        if len(numpad) == 6 and numpad.isdigit:
            
            
            if numpad == "556545" and key == 1:
                time.sleep(0.5)
                print("""
The old, rusty door slides open and stops with a clunk.
The inside of the spaceship is suprisingly clean.
You walk in. It is dark inside.
""")
                if torch == 1:
        
                
                    print("""
You turn on your torch.
You find a piece of paper on the ground.

        /\/\/\/\/\/\/\

         33 32 2e 38
         39 39 35 c2
         b0 20 4e 2c
         20 31 30 35
         2e 39 36 30
         33 c2 b0 20
         57
         
        \/\/\/\/\/\/\/
        """)
                ENDg()

            elif numpad == "556545" and key == 0:
                time.sleep(0.5)
                print("""
        The numpad asks you to insert a key
        You don't have a key
        """)
                
                ENDg()

            elif numpad != numpad.isdigit():
                print("The numpad only accepts a 6 digit number")
                aden()
                
            else:
                print("*******************")
                time.sleep(0.5)
                print("ACCESS DENIED")
                time.sleep(0.5)
                print("*******************")
                time.sleep(0.5)
                aden()

        elif numpad != numpad.isdigit():
            print("The numpad only accepts a 6 digit number")
            aden()

        elif len(numpad) < 6:
             print("That number is too short")
             print("The number must be 6 digits")
             aden()

        elif len(numpad) > 6:
            print("That number is too long")
            print("The number must be 6 digits")
            aden()


def aden():
    ndec = input("Do you want to try again? Yes or No. ")
    time.sleep(0.5)
    ndec = ndec.lower()

    if ndec == "yes":
        npad()

    elif ndec == "no":
        ENDg()

def easter():
    time.sleep(0.5)
    print("***************************************************************")
    time.sleep(0.5)
    print("""
01000101 01101110 01110100 01100101 01110010 00100000 00110101
00110101 00110110 00110101 00110100 00110101 00100000 01101111
01101110 00100000 01110100 01101000 01100101 00100000 01110011
01110000 01100001 01100011 01100101 01110011 01101000 01101001
01110000 00100000 01100100 01101111 01101111 01110010 
""")
    time.sleep(0.5)
    print("***************************************************************")
    time.sleep(0.5)
    dec1()
    

def END():
    health = 0
    time.sleep(0.5)
    print("")
    print("***************************")
    print("         GAME OVER         ")
    print("       YOU HAVE DIED       ")
    print("***************************")
    time.sleep(0.5)
    print("          Results          ")
    print("***************************")
    time.sleep(0.5)
    print("NAME:", name)
    time.sleep(0.5)
    print("WEAPON:", weapon)
    time.sleep(0.5)
    print("***************************")
    time.sleep(0.5)
    print("Strength:    ", strength    )
    time.sleep(0.5)
    print("Intelligence:", intelligence)
    time.sleep(0.5)
    print("Points:      ", points      )
    time.sleep(0.5)
    print("Items Collected:")
    if key == 1:
        print("Key")

    elif coin == 1:
        print("Coin")

    if coin == 0 and key == 0:
        print("You collected no items.")

    time.sleep(0.5)
    print("***************************")
    rply()

def rply():
    replay = input("Do you wish to play again? ")
    replay = replay.lower()

    if replay == "yes":
        print("******************************")
        print("")
        print("You come to a fork in the road")
        time.sleep(0.5)
        dec1()

    elif replay == "no":
        print("")
        time.sleep(0.5)
        print("******************************")
        print("           GOOD BYE           ")
        print("******************************")
        time.sleep(1)
        print("""
  __  __           _        ____        
 |  \/  |         | |      |  _ \       
 | \  / | __ _  __| | ___  | |_) |_   _ 
 | |\/| |/ _` |/ _` |/ _ \ |  _ <| | | |
 | |  | | (_| | (_| |  __/ | |_) | |_| |
 |_|  |_|\__,_|\__,_|\___| |____/ \__, |
                                   __/ |
                                  |___/  
""")
        time.sleep(1)

        print("""
  _                _     _             
 | |              | |   | |            
 | |     __ _  ___| |__ | | __ _ _ __  
 | |    / _` |/ __| '_ \| |/ _` | '_ \ 
 | |___| (_| | (__| | | | | (_| | | | |
 |______\__,_|\___|_| |_|_|\__,_|_| |_|
""")
        time.sleep(1)

        print("""
                                _   
     /\                        | |  
    /  \   _ __ __ _  ___ _ __ | |_ 
   / /\ \ | '__/ _` |/ _ \ '_ \| __|
  / ____ \| | | (_| |  __/ | | | |_ 
 /_/    \_\_|  \__, |\___|_| |_|\__|
                __/ |               
               |___/
""")
        time.sleep(1)
        print("Ascii text by: http://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20")
        time.sleep(1)
        print("""Ascii art by:
http://ascii.co.uk/art/key
           and           
Lachlan Argent (Rocket)""")
        time.sleep(1)

        print("""
01001101 01100001 01100100 01100101 00100000 01100010 01111001 00001010 
01001100 01100001 01100011 01101000 01101100 01100001 01101110 00100000 
01000001 01110010 01100111 01100101 01101110 01110100 00001010 
01011001 01100101 01100001 01110010 00100000 00110001 00110001 00100000
00110010 00110000 00110001 00111000

https://www.binaryhexconverter.com/binary-to-ascii-text-converter
https://www.asciitohex.com/
""")
        time.sleep(3)
        
        exit()
        

    else:
        print("That is not an option. Please try again.")
        rply()

def ENDg():
    print()
    time.sleep(0.5)
    print("***************************")
    print("      CONGRATULATIONS      ")
    print("  YOU MADE IT TO THE END   ")
    print("***************************")
    time.sleep(0.5)
    print("          Results          ")
    print("***************************")
    time.sleep(0.5)
    print("NAME:", name)
    print("WEAPON:", weapon)
    time.sleep(0.5)
    print("***************************")
    time.sleep(0.5)
    print("Strength:    ", strength    )
    time.sleep(0.5)
    print("Intelligence:", intelligence)
    time.sleep(0.5)
    print("Points:      ", points      )
    time.sleep(0.5)
    print("Items Collected:")
    if key == 1:
        print("Key")

    if coin == 1:
        print("Coin")

    if torch == 1:
        print("Torch")

    if coin == 0 and key == 0 and torch == 0:
        print("You collected no items.")

    time.sleep(0.5)
    print("***************************")
    rply()

health       = 100
points       = 0



def start():
    global strength
    global intelligence
    strength = input("Strength: ")
    intelligence = input("Intelligence: ")
    
    if strength.isdigit():
        if int(strength) > 1000:
            print("Thats too overpowered")
            time.sleep(0.25)
            print("Your strength is set to 1000")
            time.sleep(0.25)
            strength = 1000

    else:
        time.sleep(0.25)
        print("You must enter a number for strength")
        start()

    
    
    if intelligence.isdigit():
        if int(intelligence) > 1000:
            print("You can't be that smart")
            time.sleep(0.25)
            print("Your intelligence is set to 1000")
            time.sleep(0.25)
            intelligence = 1000

    else:
        time.sleep(0.25)
        print("You must enter a number for intelligence")
        time.sleep(0.25)
        start()

    print("********************")
    


key = 0
coin = 0
torch = 0

print("""
    Copyright (C) 2018  Lachlan Argent

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
    """)
time.sleep(2.5)
print("""
    Childs Place  Copyright (C) 2018  Lachlan Argent
    This program comes with ABSOLUTELY NO WARRANTY; for details type `show w'.
    This is free software, and you are welcome to redistribute it
    under certain conditions; type `show c' for details.
    """)
time.sleep(2.5)

def strtlic():
    print("Press enter to continue")
    lic = input("Input: ")
    lic = lic.lower()

    if lic == "show w" or lic == "showw" or lic == "show  w":
        print("""
    GNU GENERAL PUBLIC LICENSE
    Version 3, 29 June 2007

    Copyright © 2007 Free Software Foundation, Inc. <https://fsf.org/>

    15. Disclaimer of Warranty.
    THERE IS NO WARRANTY FOR THE PROGRAM, TO THE EXTENT PERMITTED BY APPLICABLE LAW.
    EXCEPT WHEN OTHERWISE STATED IN WRITING THE COPYRIGHT HOLDERS AND/OR OTHER PARTIES
    PROVIDE THE PROGRAM “AS IS” WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR IMPLIED,
    INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
    FOR A PARTICULAR PURPOSE. THE ENTIRE RISK AS TO THE QUALITY AND PERFORMANCE OF THE
    PROGRAM IS WITH YOU. SHOULD THE PROGRAM PROVE DEFECTIVE, YOU ASSUME THE COST OF ALL
    NECESSARY SERVICING, REPAIR OR CORRECTION.
    """)
        strtlic()
        

    elif lic == "show c" or lic == "showc" or lic == "show  c":
        print("""
    GNU GENERAL PUBLIC LICENSE
    Version 3, 29 June 2007

    Copyright © 2007 Free Software Foundation, Inc. <https://fsf.org/>

    2. Basic Permissions.
    All rights granted under this License are granted for the term of copyright on the Program,
    and are irrevocable provided the stated conditions are met. This License explicitly affirms
    your unlimited permission to run the unmodified Program. The output from running a covered
    work is covered by this License only if the output, given its content, constitutes a covered
    work. This License acknowledges your rights of fair use or other equivalent, as provided by
    copyright law.

    You may make, run and propagate covered works that you do not convey, without conditions so
    long as your license otherwise remains in force. You may convey covered works to others for
    the sole purpose of having them make modifications exclusively for you, or provide you with
    facilities for running those works, provided that you comply with the terms of this License
    in conveying all material for which you do not control copyright. Those thus making or running
    the covered works for you must do so exclusively on your behalf, under your direction and
    control, on terms that prohibit them from making any copies of your copyrighted material
    outside their relationship with you.

    Conveying under any other circumstances is permitted solely under the conditions stated below.
    Sublicensing is not allowed; section 10 makes it unnecessary.

    5. Conveying Modified Source Versions.
    You may convey a work based on the Program, or the modifications to produce it from the Program,
    in the form of source code under the terms of section 4, provided that you also meet all of these
    conditions:

    a) The work must carry prominent notices stating that you modified it, and giving a relevant date.
    b) The work must carry prominent notices stating that it is released under this License and any
    conditions added under section 7. This requirement modifies the requirement in section 4 to “keep
    intact all notices”.
    c) You must license the entire work, as a whole, under this License to anyone who comes into
    possession of a copy. This License will therefore apply, along with any applicable section 7
    additional terms, to the whole of the work, and all its parts, regardless of how they are packaged.
    This License gives no permission to license the work in any other way, but it does not invalidate
    such permission if you have separately received it.
    d) If the work has interactive user interfaces, each must display Appropriate Legal Notices; however,
    if the Program has interactive interfaces that do not display Appropriate Legal Notices, your work
    need not make them do so.
    A compilation of a covered work with other separate and independent works, which are not by their
    nature extensions of the covered work, and which are not combined with it such as to form a larger
    program, in or on a volume of a storage or distribution medium, is called an “aggregate” if the
    compilation and its resulting copyright are not used to limit the access or legal rights of the
    compilation's users beyond what the individual works permit. Inclusion of a covered work in an aggregate
    does not cause this License to apply to the other parts of the aggregate.
    """)
        strtlic()
strtlic()
print("**********************************************************************")

print("""
   ________  ________    ____  _____    ____  __    ___   ____________
  / ____/ / / /  _/ /   / __ \/ ___/   / __ \/ /   /   | / ____/ ____/
 / /   / /_/ // // /   / / / /\__ \   / /_/ / /   / /| |/ /   / __/   
/ /___/ __  // // /___/ /_/ /___/ /  / ____/ /___/ ___ / /___/ /___   
\____/_/ /_/___/_____/_____//____/  /_/   /_____/_/  |_\____/_____/   
                                                                      
""")

print("**********************************************************************")
time.sleep(0.5)
print("")
print("**********************************************************************")
name = input("NAME: ")
print("**********************************************************************")

name = name.lower()
if name == "devrights":
    weapon = "Developer Powers"
    strength = 9999999999
    intelligence = 9999999999
    dec1()

if name == "dev-dec1":
    weapon = "Sword"
    strength = 1000
    intelligence = 1000
    dec1()
    
if name == "dev-dec2":
    weapon = "Sword"
    strength = 1000
    intelligence = 1000
    dec2()

if name == "dev-dec3":
    weapon = "Sword"
    strength = 1000
    intelligence = 1000
    dec3()

if name == "dev-dec4":
    weapon = "Sword"
    strength = 1000
    intelligence = 1000
    dec4()

if name == "dev-dec5":
    weapon = "Sword"
    strength = 1000
    intelligence = 1000
    dec5()

if name == "dev-dec6":
    weapon = "Sword"
    strength = 1000
    intelligence = 1000
    dec6()

if name == "dev-dec7":
    weapon = "Sword"
    strength = 1000
    intelligence = 1000
    dec7()

if name == "dev-dec8":
    weapon = "Sword"
    strength = 1000
    intelligence = 1000
    dec8()

if name == "dev-dec9":
    weapon = "Sword"
    strength = 1000
    intelligence = 1000
    dec9()

if name == "dev-dec10k0":
    weapon = "Sword"
    strength = 1000
    intelligence = 1000
    dec10()

if name == "dev-dec10k1":
    weapon = "Sword"
    strength = 1000
    intelligence = 1000
    key = 1
    dec10()

if name == "dev-endg":
    weapon = "Sword"
    strength = 1000
    intelligence = 1000
    ENDg()

if name == "dev-end":
    weapon = "Sword"
    strength = 1000
    intelligence = 1000
    END()

if name == "dev-replay":
    weapon = "Sword"
    strength = 1000
    intelligence = 1000
    rply()


weapon = input("Weapon: ")
time.sleep(0.5)
start()
time.sleep(0.5)
print("")
print("You come to a fork in the road")
time.sleep(0.5)

dec1()

