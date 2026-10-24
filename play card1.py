
SUITS = ['clubs', 'diamonds', 'Hearts', 'spades']
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10',
         'jack', 'queen', 'king', 'Ace']

import random

rank = random.randrange(0, len(RANKS))
suit = random.randrange(0, len(SUITS))

print(RANKS[rank] + ' of ' + SUITS[suit])
