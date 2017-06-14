from sys import exit

badInput = "That's not an answer. Try again"
style = ""
ingredient = ""

# Want to make a beer, y/n

def decision():
    desireBeer = input("Do you want to make a beer? y/n > ")

    if desireBeer == ("y"):
        # If yes, choose which beer to make porter, IPA, or blonde
        chooseStyle()
        # If no, return "That's a shame, bye!" and kill program
    elif desireBeer == ("n"):
        print("Oh, that's a shame. Bye then!")

    else:
        print(badInput)
        decision()


def chooseStyle():
    print("What style? You've got ingredients for porter, IPA, or blonde.")
    global style
    style = input("> ")

    if style == "porter":
        chooseIngred()
    elif style == "IPA":
        chooseIngred()
    elif style == "ipa":
        chooseIngred()
    elif style == "blonde":
        chooseIngred()
    else:
        print(badInput)
        chooseStyle()

def chooseIngred():
    print("Do you want to add a special ingredient? y/n ")
    desireIngred = input("> ")

    if desireIngred == "y":
        print("Fantastic. What special ingredient do you want to add?")
        print("You've got chocolate, coffee, and lavender")

        global ingredient
        ingredient = input("> ")
        global style
        print(f"You want to make a {ingredient} {style} beer. Awesome.")

        sanitize()

    elif desireIngred == "n":
        print("That's too bad. It would have been delicious!")
        print(f"Anyway, you want to make a {style} beer. Awesome.")

        sanitize()

    else:
        print(badInput)
        chooseIngred()

def badsan():
    print("Now we're brewing.....................")
    print("......................................")
    print("Now we're tasting.....................")
    print("......................................")
    print("YUCK! This beer is spoiled, guess you didn't sanitize correctly!")

def goodsan():
    global ingredient
    global style
    print("Now we're brewing.....................")
    print("......................................")
    print("Now we're tasting.....................")
    print("......................................")
    print(f"YUM! This {ingredient} {style} is delicious!")

def sanitize():
    print("How do you want to sanitize your equipment?")
    print("Your choices are: heat, sanitzer, no sanitzer")
    desireSan = input("> ")

    if desireSan == "heat":
        print("Ok, what temperature (Farhenheit) should we set the autoclave for? > ")
        temperature = input()
        tempInt = int(temperature)

        # check that temperature is a number, if not, throw error

        if tempInt < 170:
            badsan()

        elif tempInt > 212:
            print("We can't brew because the equipment just melted!!!!!")

        else:
            goodsan()
            award()

    elif desireSan == "sanitizer":
        print("Ok, how much sanitizer should we use (in CCs)?")
        san = input("> ")

        # check that san is an integer, if not, throw an error

        sanInt = int(san)

        if sanInt < 100:
            badsan()

        elif sanInt > 500:
            badsan()

        else:
            goodsan()
            award()

    elif desireSan == "no sanitizer":
        print("Are you sure? y/n ")
        confirmSan = input()

        if confirmSan == "y":
            badsan()

        elif confirmSan == "n":
            sanitize()

        else:
            print(badInput)
            sanitize()

    elif desireSan == "none":
        print("Are you sure? y/n ")
        confirmSan = input()

        if confirmSan == "y":
            badsan()

        elif confirmSan == "n":
            sanitize()

        else:
            print(badInput)
            sanitize()

    else:
        print(badInput)
        sanitize()

def award():
    global ingredient
    global style
    print(f"I think you should enter your {ingredient} {style} into the State Fair competition.")
    awardDec = input("Do you want to enter? y/n ")

    if awardDec == "y":
        awardName = input("What's your name?")
        awardGender = input("What's your gender?")
        awardAge = input("What's your age?")
        awardZip = input("What's your zipcode?")

        if awardGender == "female":
            print(f"Are you sure you brewed this {ingredient} {style}?")
            print("Wow, I've never met a woman home brewer before!")
            print("Well, you've won gold! Congrats. Well-deserved!")

        elif awardGender == "f":
            print(f"Are you sure you brewed this {ingredient} {style}?")
            print("Wow, I've never met a woman home brewer before!")
            print("Well, you've won gold! Congrats. Well-deserved!")

        else:
            print(f"Your {ingredient} {style} is delicious!")
            print("The judges are deliberating........")
            print("...................................")
            print("...................................")
            print("The winner is......................")
            print(f"{awardName}, age {awardAge}, from zip code {awardZip}!")
            print("CONGRATS!")

    elif awardDec == "n":
        print("That's too bad! I think you could have won gold!!!")

    else:
        print(badInput)
        award()

decision()
