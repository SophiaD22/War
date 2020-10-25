# Sophia DeCleene
import random
deck = ['ace', 'two', 'three', 'four', 'five', 'six',
        'seven', 'eight', 'nine', 'ten', 'jack', 'queen', 'king',
        'ace', 'two', 'three', 'four', 'five', 'six',
        'seven', 'eight', 'nine', 'ten', 'jack', 'queen', 'king',
        'ace', 'two', 'three', 'four', 'five', 'six',
        'seven', 'eight', 'nine', 'ten', 'jack', 'queen', 'king',
        'ace', 'two', 'three', 'four', 'five', 'six',
        'seven', 'eight', 'nine', 'ten', 'jack', 'queen', 'king']

print("Stuck at home alone due to COVID?\nTired of Zoom calls and online games?"
      "\nWelcome to your virtual casino! I'd be surprised if you won...\n"
      "I am the ultimate player and will destroy you!!!")
print("Today we're playing war because that's what I want to do! ")
random.shuffle(deck)
pl1 = deck[0:27]
num1 = 0
num2 = 0
shuf = 10
pl2 = deck[27:len(deck)]
while len(pl1) != 0 or len(pl2) != 0:
    if shuf == 0:
        random.shuffle(deck)
        shuf = 10
    else:
        shuf -= 1
    print("MY CARD: ", pl1[0], "\nYour card: ", pl2[0])
    if pl1[0] == "ace":
        num1 = 14  # Aces beat kings
    elif pl1[0] == "two":
        num1 = 2
    elif pl1[0] == "three":
        num1 = 3
    elif pl1[0] == "four":
        num1 = 4
    elif pl1[0] == "five":
        num1 = 5
    elif pl1[0] == "six":
        num1 = 6
    elif pl1[0] == "seven":
        num1 = 7
    elif pl1[0] == "eight":
        num1 = 8
    elif pl1[0] == "nine":
        num1 = 9
    elif pl1[0] == "ten":
        num1 = 10
    elif pl1[0] == "jack":
        num1 = 11
    elif pl1[0] == "queen":
        num1 = 12
    elif pl1[0] == "king":
        num1 = 13
    if pl2[0] == "ace":
        num2 = 14  # Aces beat kings
    elif pl2[0] == "two":
        num2 = 2
    elif pl2[0] == "three":
        num2 = 3
    elif pl2[0] == "four":
        num2 = 4
    elif pl2[0] == "five":
        num2 = 5
    elif pl2[0] == "six":
        num2 = 6
    elif pl2[0] == "seven":
        num2 = 7
    elif pl2[0] == "eight":
        num2 = 8
    elif pl2[0] == "nine":
        num2 = 9
    elif pl2[0] == "ten":
        num2 = 10
    elif pl2[0] == "jack":
        num2 = 11
    elif pl2[0] == "queen":
        num2 = 12
    elif pl2[0] == "king":
        num2 = 13
    if num1 > num2:
        print("ALL MINE!")
        pl1.append(pl1.pop(0))
        pl1.append(pl2.pop(0))
    elif num2 > num1:
        print("Ugh, fine. You get my card...")
        pl2.append(pl1.pop(0))
        pl2.append(pl2.pop(0))
    elif num1 == num2:
        while num1 == num2:
            print("Keep hitting ENTER: ")
            print("I-\n")
            input()
            print("De-\n")
            input()
            print("clare\n")
            input()
            print("WAR!\nplayer 1: ", pl1[4], " player2: ", pl2[4])
            if pl1[4] == "ace":
                num1 = 100  # Aces beat kings
            elif pl1[4] == "two":
                num1 = 2
            elif pl1[4] == "three":
                num1 = 3
            elif pl1[4] == "four":
                num1 = 4
            elif pl1[4] == "five":
                num1 = 5
            elif pl1[4] == "six":
                num1 = 6
            elif pl1[4] == "seven":
                num1 = 7
            elif pl1[4] == "eight":
                num1 = 8
            elif pl1[4] == "nine":
                num1 = 9
            elif pl1[4] == "ten":
                num1 = 10
            elif pl1[4] == "jack":
                num1 = 11
            elif pl1[4] == "queen":
                num1 = 12
            elif pl1[4] == "king":
                num1 = 13
            if pl2[4] == "ace":
                num2 = 100  # Aces beat kings
            elif pl2[4] == "two":
                num2 = 2
            elif pl2[4] == "three":
                num2 = 3
            elif pl2[4] == "four":
                num2 = 4
            elif pl2[4] == "five":
                num2 = 5
            elif pl2[4] == "six":
                num2 = 6
            elif pl2[4] == "seven":
                num2 = 7
            elif pl2[4] == "eight":
                num2 = 8
            elif pl2[4] == "nine":
                num2 = 9
            elif pl2[4] == "ten":
                num2 = 10
            elif pl2[4] == "jack":
                num2 = 11
            elif pl2[4] == "queen":
                num2 = 12
            elif pl2[4] == "king":
                num2 = 13
            if num1 > num2:
                print("ALL MINE!\n", pl1[0:5], pl2[0:5])
                pl1.append(pl1[0:5])
                pl1 = pl1[5: len(pl1)]
                pl1.append(pl2[0:5])
                pl2 = pl2[5:len(pl1)]
            elif num2 > num1:
                print("Ugh, fine. You get my cards...\n", pl1[0:5], pl2[0:5])
                pl2.append(pl2[0:5])
                pl2 = pl2[5: len(pl2)]
                pl2.append(pl1[0:5])
                pl1 = pl1[5:len(pl1)]
            else:
                input("3\n2\n1\nHit enter to flip card: ")
    input("3\n2\n1\nHit enter to flip card: ")
if len(pl1) == 0:
    print("Fine, you win. This is stupid.")
else:
    print("HAHAHAHA TOLD YOU I WOULD WIN!!!")
