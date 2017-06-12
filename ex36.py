# To Do
## Figure out how to call style and temperature across all functions
## Change temperature from str to integer type


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


def chooseStyle():
    print("Great! What style? You've got ingredients for porter, IPA, or blonde.")
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

def chooseIngred():
    print("Do you want to add a special ingredient? y/n ")
    desireIngred = input("> ")

    if desireIngred == "y":
        print("Fantastic. What special ingredient do you want to add?")
        print("You've got chocolate, coffee, and lavender")

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

def sanitize():
    print("How do you want to sanitize your equipment?")
    print("Your choices are: heat, sanitzer, no sanitzer")
    desireSan = input("> ")

    if desireSan == "heat":
        print("Ok, what temperature (Farhenheit) should we set the autoclave for? > ")
        temperature = input()
        # Convert temperature from string to integer

        if temperature < 170:
            print("Now we're brewing.....................")
            print("......................................")
            print("Now we're tasting.....................")
            print("......................................")
            print("YUCK! This beer is spoiled, guess you didn't sanitize correctly!")

        elif temperature > 212:
            print("We can't brew because the equipment just melted!!!!!")

        else:
            print("Now we're brewing.....................")
            print("......................................")
            print("Now we're tasting.....................")
            print("......................................")
            print("YUM! This {ingredient} {style} is delicious!")
            # Call award function

    elif desireSan == "sanitizer":
        print("Ok, how much sanitizer should we use (in CCs)?")

#    elif desireSan == "no sanitizer":

#    elif desireSan == "none":

#    else:
#        print(badInput)

decision()


# If heat, prompt what temperature to set autoclave for (in F)

## If less than 100, return "Now we're brewing, now we're tasting, yuck!"

## If more than 500, return return "Now we're brewing, now we're tasting, yuck!"

## Else return "Now we're brewing, now we're tasting, this  {ingredient} {style} is delicious!"
## Call award function

# If none, ask are you sure? y/n

## If y, return "Now we're brewing, now we're tasting, yuck!"

## If n, loop back to "How do you want to santize?" function

# Award function

# "I think you shoudl enter your beer into the state fair. y/n"

# If y, ask name, gender, age, zipcode

## If gender = f, print something like "Are you sure you brewed this? this {ingredient} {style} is delicious"
## Print "wow, I've never met a woman home brewer before"
## Print "Excellent job. Well-deserved. Hope to see you again next year"

## Else print "Your  {ingredient} {style} is delicious. You've won the gold!"
## Print "Excellent job. Well-deserved. Hope to see you again next year"
