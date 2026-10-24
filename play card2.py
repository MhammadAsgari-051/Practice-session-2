
import random

SUITS = ['clubs', 'diamonds', 'Hearts', 'spades']
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10',
         'jack', 'queen', 'king', 'Ace']

deck = []

for suit in SUITS:
    for rank in RANKS:
        deck.append(rank + ' of ' + suit)

n = len(deck)

for i in range(n):
    r = random.randrange(0, i + 1)
    temp = deck[r]
    deck[r] = deck[i]
    deck[i] = temp

print(deck)
