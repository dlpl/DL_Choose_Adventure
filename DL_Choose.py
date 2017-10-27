import random
import time


def bad_input():
    print("\nI do not understand your input. \n"
          "Please check for typos and try again. \n")


def help_with_choice():
    print("\n"
          "1: When selecting your choice, you can type \n"
          "   the number the your choice corresponds to \n"
          "  (In this choice, yes is 1 and no is 2) \n"
          "2: You can type out the entire choice \n"
          "   In this choice, you can type out 'yes' or 'no' \n"
          "3: You can also type the first letter of the word. \n"
          "   In this case, it would be 'y' or 'n'\n"
          "4: You can also type out the first word of the choice \n"
          "   although this choice is only one word each. \n \n")


def choose_1():
    print("\nYou wander up to her stand\n"
          "wondering if it's a scam. \n"
          "You're curious to see what she has.\n"
          " She hands you one of her pamphlets. \n"
          "\nFortune reading - $100 \n"
          "Luck charms - $30 each \n"
          "Magical candy - $15 each \n"
          "Magic Wand - $300 \n \n"
          "Looks like a scam. What will you do?\n"
          " \n"
          "Walk away \n"
          "Buy something \n \n ")


def choose_2():
    print("\nYou try and go walk away, \n"
          "but she hands you a pamphlet anyway.\n"
          " \n"
          "Read it \n"
          "Walk away \n \n ")


def throw_away_end():
    print("\nYou walk away, ignoring her. You notice a trash \n"
          "can just a few meters away, and drop her pamphlet \n"
          "into it. You enjoy a pleasant walk and return home.\n")


def choose_4():
    print("\nFortune reading - $100 \n"
          "Luck charms - $30 each \n"
          "Magical candy - $15 each \n"
          "Magic Wand - $300 \n"
          " \n"
          "Looks like a scam. What will you do?\n"
          " \n"
          "Buy something \n"
          "Walk away \n \n ")


def choose_5():
    print("\n'Wait!', she shouts. 'I know it might be a bit \n"
          "expensive, but I'll offer you one of my goods \n"
          "for free! Then you'll see I'm the real deal!'\n"
          " \n"
          "Try something out \n"
          "Walk away \n"
          "\n ")


def choose_6():
    print("\nSince it's free, you decide to try something out.\n"
          "But what will you try out? \n"
          " \n"
          "Fortune Reading \n"
          "Luck Charm \n"
          "Magical Candy \n"
          "Wand \n \n ")


def choose_7():
    print("\n'Huh', she mutters. 'It kind of looks like there's \n"
          "going to be bird poop on you. \n"
          " \n"
          "Accept your fate \n"
          "Resist destiny \n"
          "Look up into the sky"
          "\n ")


def bird_hair_end():
    print("\nYou accept your fate. Now, how will \n"
          "you accept the fact that there's currently\n"
          "bird poop in your hair? \n")


def choose_9():
    print("\nYou decide you must resist destiny. \n"
          "But how? \n"
          " \n"
          "Buy a luck charm \n"
          "Hide in the bathroom \n"
          "\n ")


def look_up_end():
    print("\nYou look up into the sky\n"
          "and you ask yourself why \n"
          "as you hear that big splatter\n"
          "of something that's not water.\n"
          "What fell right on your face\n"
          "is a bird's pile of waste.\n")


def choose_11():
    print("\nYou dash to a bathroom and head inside.\n"
          "Nothing will happen if you just go hide. \n"
          "But there's something you didn't realize\n"
          "something that will lead to your demise\n"
          "The bathroom is actually really far away\n"
          "But there's a luck charm. Will you pay?\n"
          "\n"
          "Pay\n"
          "Nay\n")


def pay_end():
    print("\n ")

    print("\nYou take out 30 dollars from your wallet and \n"
          "quickly buy a luck charm. You anxiously walk \n"
          "around the next five minutes. No bird poops on \n"
          "you. As you start heading home, you wonder \n"
          "if it was the luck charm that stopped destiny \n"
          "or if a bird never was going to poop on you \n"
          "in the first place. Well, at least you weren't \n"
          "pooped on. \n")


def nay_end():
    print("\n'Nay', you say. \n"
          "You will not pay. \n"
          "It's just a scam! \n"
          "Ignore that sham! \n")
    rand1 = random.randrange(1, 7)
    rand2 = random.randrange(1, 7)
    rand3 = random.randrange(1, 7)
    rand4 = random.randrange(1, 7)
    rand5 = random.randrange(1, 7)
    rand_sum = rand1 + rand2 + rand3 + rand4 + rand5
    if rand_sum < 35:
        print("\n 5 dice of fate roll")
        print(rand_sum)
        print("Oh... that's too low\n"
              "The bird has appeared,\n"
              "your pride now smeared.\n")
    else:
        print("\n 5 dice of fate roll")
        print(rand_sum)
        print("Oh that's enough!\n"
              "It was just a bluff.\n"
              "You take a quick look up high \n"
              "and there's no bird in the sky. \n")


def luck_charm_free_end():
    print("\nYou take a luck charm. \n"
          "Your phone beeps. \n"
          "You just won the lottery \n"
          "with a ticket you didn't buy. \n"
          "\n"
          "It's only $30 though. \n")


def magical_candy_end():
    rand6 = random.randrange(1, 9)
    if 1 <= rand6 <= 3:
        print("\nYou get a magical candy. It looks like \n"
              "a jelly bean. Tastes like one too. \n"
              "But you can hear dogs talking now. \n"
              "That's pretty cool. \n")
    elif 4 <= rand6 <= 6:
        print("\nYou get a magical candy. It looks like \n"
              "a jelly bean. Tastes like one too. \n"
              "Although now you're flying... up. \n"
              "You're heading towards the moon \n"
              "but you don't feel the heat from \n"
              "leaving the atmosphere. Now, how far \n"
              "is the moon again?")
        for _ in range(5):
            print("\n...\n")
            time.sleep(random.randrange(4, 7))
        print(" It might take a while. \n")
    else:
        print("\nYou get a magical candy. It looks like \n"
              "a jelly bean. Tastes like one too. \n"
              "But now, you're filled with  power. \n"
              "There is no one who can stop you now. \n"
              "Whatever you want, you can do. \n"
              " \n"
              "Use it for the greater good \n"
              "Join the dark side \n"
              "Act normal \n \n ")


def greater_good_end():
    print("\nWith your endless power, every villain \n"
          "is scared out of their wits. But now there \n"
          "are no villains, and you end up quite bored. \n")


def dark_side_end():
    print("You unleash your power and join the villains, \n"
          "hurling energy balls at random locations, \n"
          "blowing up \millions of houses and \n"
          "causing trillions in damage. \n"
          "\n"
          "You now realize that you are too powerful. \n"
          "Even being a villain is no fun if no one \n"
          "can be a hero to stop you. \n")


def normal_person_end():
    print("\nYou act like a normal person. \n"
          "You live life like a normal person \n"
          "You walk back home like a normal person. \n"
          "You forget you even had powers like a normal person. \n"
          "Your life ends as a normal person. \n")


def choose_21():
    print("\nYou get a magic wand. There's a red button \n"
          "on it. Do you want to click it? \n"
          " \n"
          "Yes \n"
          "No \n \n ")


def restart_story():
    print("\nYou click the button.\n")
    for _ in range(5):
        print("\n...\n")
        time.sleep(random.randrange(1, 3))
    main()


def choose_23():
    print("\nWhat do you want to do? \n"
          " \n"
          "Nothing \n"
          "Click the button\n"
          "Wave the wand around \n"
          "End this story \n \n ")


def choose_24():
    print("\nYou do nothing. \n"
          "What do you want to do now? \n"
          " \n"
          "Nothing \n"
          "Click the button\n"
          "Wave the wand around \n"
          "End this story \n"
          " \n ")


def choose_25():
    print("\nYou wave the wand around. Nothing happens. \n"
          "What do you want to do now? \n"
          " \n"
          "Nothing \n"
          "Click the button\n"
          "Wave the wand around \n"
          "End this story \n"
          "\n ")


def end_story_end():
    print("\nAll stories must come to an end, and you \n"
          "decide to finally end this one. ")
    try:
        raise NameError("Magic_Wand_Virus")
    except NameError:
        print("\n"
              "This story must end. \n")
        raise


def choose_27():
    print("\nBut... it's a scam.\n"
          "Do you really want to buy something? \n"
          "\n"
          "Buy Something \n"
          "Walk Away \n"
          "\n ")


def choose_28():
    print("\nWhat do you want to buy?\n"
          " \n"
          "Fortune Reading \n"
          "Luck Charm \n"
          "Magical Candy \n"
          "Wand \n \n ")


def buy_fortune():
    print("\n'Ahh!', she shouts. 'I can see your future!' \n"
          "She waves her hands over a glass ball, peering \n"
          "into it. 'Yes, yes. Your future is bright, but \n"
          "there may be some disturbances soon...' \n"
          "\n"
          "...\n"
          "That's it\n")


def buy_luck():
    print("\nShe hand you a rubber bracelet labeled with \n"
          "'Luck'. A few minutes later, you hear a \n"
          "splat on your head. You ruffle your hair and \n"
          "feel something sticky. Oh, Bird Poop. \n"
          " \n"
          "That's never happened to you before. I wonder \n"
          "if that counts as being lucky. \n")


def buy_candy():
    print("\nShe hands you a small piece of candy. \n"
          "You pop it into your mouth. Hmm, tastes \n"
          "like a strawberry jellybean. I wonder what \n"
          "it does. \n"
          " \n")
    time.sleep(2)
    print("It does nothing because it's a strawberry jellybean. \n")


def buy_wand():
    print("\nShe hands you a plastic wand with a red \n"
          "button on it. You wave it around, and \n"
          "nothing happens. \n"
          "\n"
          "You click the red button. The wand beeps \n"
          "and starts flashing lights. Hey, that \n"
          "would be a pretty magical wand if you lived in \n"
          "a time period where electricity didn't exist. \n")


def main():
    print("                        A Nice Day \n"
          "It rained just a few hours ago and the weather is brisk. \n"
          "A few clouds shade the sun, keeping the temperature nice \n"
          "and cool. 1 pm! It's the ideal time to take a nice walk \n"
          "and enjoy this rare occasion of nice weather. You grab \n"
          "your light jacket and head out towards the park. \n"
          "At the park entrance, though, a mysterious lady seems \n"
          "to have set up some booth. Should you see what she wants? \n"
          " \n"
          "Yes \n"
          "No \n \n "
          "For help in replying, type 'help' \n")
    var0 = 1
    var1 = 0
    var2 = 0
    var3 = 0
    var5 = 0
    var6 = 0
    var7 = 0
    var9 = 0
    var10 = 0
    var11 = 0
    var13 = 0
    var14 = 0
    var15 = 0

# Should you see what she wants?
    while var0 == 1:
        choice = raw_input(">")
        if choice == "yes" or choice == "Yes" or choice == "y" or choice == "Y" or choice == "1":
            var1 = 1
            var0 = 0
            choose_1()
        elif choice == "no" or choice == "No" or choice == "n" or choice == "N" or choice == "2":
            var2 = 1
            var0 = 0
            choose_2()
        elif choice == "help":
            help_with_choice()
        else:
            bad_input()
# Looks like a scam, what should you do?
    while var1 == 1:
        choice = raw_input(">")
        if choice == "walk away" or choice == "Walk away" or choice == "walk" or choice == "Walk" or choice == "w"\
                or choice == "W" or choice == "1":
            var3 = 1
            var1 = 0
            choose_5()
        elif choice == "buy something" or choice == "Buy something" or choice == "buy" or choice == "Buy"\
                or choice == "b" or choice == "B" or choice == "2":
            var9 = 1
            var1 = 0
            choose_27()
        elif choice == "help":
            help_with_choice()
        else:
            bad_input()
# She hands you a pamphlet
    while var2 == 1:
        choice = raw_input(">")
        if choice == "read it" or choice == "Read it" or choice == "read" or choice == "Read" or choice == "r"\
                or choice == "R" or choice == "1":
            var5 = 1
            var2 = 0
            choose_4()
        elif choice == "walk away" or choice == "Walk away" or choice == "walk" or choice == "Walk" or choice == "w"\
                or choice == "W" or choice == "2":
            var2 = 0
            throw_away_end()
        elif choice == "help":
            help_with_choice()
        else:
            bad_input()
# Wow, looks like a scam, what should you do?
    while var5 == 1:
        choice = raw_input(">")
        if choice == "buy something" or choice == "Buy something" or choice == "buy" or choice == "Buy"\
                or choice == "b" or choice == "B" or choice == "1":
            var9 = 1
            var5 = 0
            choose_27()
        elif choice == "walk away" or choice == "Walk away" or choice == "walk" or choice == "Walk" or choice == "w"\
                or choice == "W" or choice == "2":
            var3 = 1
            var5 = 0
            choose_5()
        elif choice == "help":
            help_with_choice()
        else:
            bad_input()
# Do you really want to buy something?
    while var9 == 1:
        choice = raw_input(">")
        if choice == "buy something" or choice == "Buy something" or choice == "buy" or choice == "Buy"\
                or choice == "b" or choice == "B" or choice == "1":
            var7 = 1
            var9 = 0
            choose_28()
        elif choice == "walk away" or choice == "Walk away" or choice == "walk" or choice == "Walk" or choice == "w"\
                or choice == "W" or choice == "2":
            var3 = 1
            var9 = 0
            choose_5()
        elif choice == "help":
            help_with_choice()
        else:
            bad_input()
# What do you want to buy?
    while var7 == 1:
        choice = raw_input(">")
        if choice == "fortune reading" or choice == "Fortune reading" or choice == "fortune" or choice == "Fortune"\
                or choice == "f" or choice == "F" or choice == "1" or choice == "Fortune Reading":
            var7 = 0
            buy_fortune()
        elif choice == "luck charm" or choice == "Luck charm" or choice == "luck" or choice == "Luck"\
                or choice == "l" or choice == "L" or choice == "2" or choice == "Luck Charm":
            var7 = 0
            buy_luck()
        elif choice == "magical candy" or choice == "Magical candy" or choice == "magical" or choice == "Magical"\
                or choice == "m" or choice == "M" or choice == "3" or choice == "Magical Candy":
            var7 = 0
            buy_candy()
        elif choice == "wand" or choice == "Wand" or choice == "w" or choice == "W" or choice == "4":
            var7 = 0
            buy_wand()
        elif choice == "help":
            help_with_choice()
        else:
            bad_input()
# If it's free, how bad could it be?
    while var3 == 1:
        choice = raw_input(">")
        if choice == "try something out" or choice == "Try something out" or choice == "try" or choice == "Try"\
                or choice == "t" or choice == "T" or choice == "1":
            var6 = 1
            var3 = 0
            choose_6()
        elif choice == "walk away" or choice == "Walk away" or choice == "walk" or choice == "Walk" or choice == "w"\
                or choice == "W" or choice == "2":
            var3 = 0
            throw_away_end()
        elif choice == "help":
            help_with_choice()
        else:
            bad_input()
# Since it's free, you decide to try something out
    while var6 == 1:
        choice = raw_input(">")
        if choice == "fortune reading" or choice == "Fortune reading" or choice == "fortune" or choice == "Fortune"\
                or choice == "f" or choice == "F" or choice == "1" or choice == "Fortune Reading":
            var10 = 1
            var6 = 0
            choose_7()
        elif choice == "luck charm" or choice == "Luck charm" or choice == "luck" or choice == "Luck"\
                or choice == "l" or choice == "L" or choice == "2" or choice == "Luck Charm":
            var6 = 0
            luck_charm_free_end()
        elif choice == "magical candy" or choice == "Magical candy" or choice == "magical" or choice == "Magical"\
                or choice == "m" or choice == "M" or choice == "3" or choice == "Magical Candy":
            var6 = 0
            magical_candy_end()
        elif choice == "wand" or choice == "Wand" or choice == "w" or choice == "W" or choice == "4":
            var11 = 1
            var6 = 0
            choose_21()
        elif choice == "help":
            help_with_choice()
        else:
            bad_input()
# Looks like there's bird poop on you?
    while var10 == 1:
        choice = raw_input(">")
        if choice == "accept your fate" or choice == "Accept your fate" or choice == "accept" or choice == "Accept"\
                or choice == "a" or choice == "A" or choice == "1":
            var10 = 0
            bird_hair_end()
        elif choice == "resist destiny" or choice == "Resist destiny" or choice == "resist" or choice == "Resist"\
                or choice == "r" or choice == "R" or choice == "2":
            var13 = 1
            var10 = 0
            choose_9()
        elif choice == "look up into the sky" or choice == "Look up into the sky" or choice == "look"\
                or choice == "Look" or choice == "l" or choice == "L" or choice == "3":
            var10 = 0
            look_up_end()
        elif choice == "help":
            help_with_choice()
        else:
            bad_input()
# Magic wand. Click the button?
    while var11 == 1:
        choice = raw_input(">")
        if choice == "yes" or choice == "Yes" or choice == "y" or choice == "Y" or choice == "1":
            var11 = 0
            restart_story()
        elif choice == "no" or choice == "No" or choice == "n" or choice == "N" or choice == "2":
            var14 = 1
            var11 = 0
            choose_23()
        elif choice == "help":
            help_with_choice()
        else:
            bad_input()
# What to do?
    while var14 == 1:
        choice = raw_input(">")
        if choice == "nothing" or choice == "Nothing" or choice == "n" or choice == "N" or choice == "1":
            choose_24()
        elif choice == "click the button" or choice == "Click the button" or choice == "click" or choice == "Click"\
                or choice == "c" or choice == "C" or choice == "2":
            var14 = 0
            restart_story()
        elif choice == "wave the wand around" or choice == "Wave the wand around" or choice == "wave"\
                or choice == "Wave" or choice == "w" or choice == "W" or choice == "3":
            choose_25()
        elif choice == "end this story" or choice == "End this story" or choice == "end" or choice == "End"\
                or choice == "e" or choice == "E" or choice == "4":
            var14 = 0
            end_story_end()
        elif choice == "help":
            help_with_choice()
        else:
            bad_input()
# How resist fate?
    while var13 == 1:
        choice = raw_input(">")
        if choice == "buy a luck charm" or choice == "Buy a luck charm" or choice == "buy" or choice == "Buy"\
                or choice == "b" or choice == "B" or choice == "1":
            var13 = 0
            pay_end()
        elif choice == "hide in the bathroom" or choice == "Hide in the bathroom" or choice == "hide"\
                or choice == "Hide" or choice == "h" or choice == "H" or choice == "2":
            var15 = 1
            var13 = 0
            choose_11()
        elif choice == "help":
            help_with_choice()
        else:
            bad_input()
# Pay or Nay
    while var15 == 1:
        choice = raw_input(">")
        if choice == "pay" or choice == "Pay" or choice == "p" or choice == "P" or choice == "1":
            var15 = 0
            pay_end()
        elif choice == "nay" or choice == "Nay" or choice == "n" or choice == "N" or choice == "2":
            var15 = 0
            nay_end()
        elif choice == "help":
            help_with_choice()
        else:
            bad_input()

main()
