import random as rd

cards = ["king", "queen", "jack"]

for i in cards:
    rd.shuffle(cards)
    print(i)
