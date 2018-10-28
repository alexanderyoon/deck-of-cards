import random
from pprint import pprint

def shuffle_deck(deck):
    # Shuffle the deck.
    shuffled_deck = []
    
    print('Shuffling the deck...')
    while len(deck) > 0:
        index = random.randint(0, len(deck) - 1)
        print('Picking card #{}'.format(index))
        card = deck.pop(index)
        shuffled_deck.append(card)
        
    return shuffled_deck

# Create all the suits.
suits = ['heart', 'diamond', 'club', 'spade']

# Create all the ranks, numbers first, then face cards.
ranks = []
for n in range(2, 11):
    ranks.append(str(n))

ranks = ranks + ['jack', 'queen', 'king', 'ace']

# Create a full deck of one card of each rank for each suit.
deck = []
for s in suits:
    for r in ranks:
        card = {'suit': s, 'rank': r}
        deck.append(card)

print('Here is the deck:')
pprint(deck)
print()

print()
print('Here is the shuffled deck:')
pprint(shuffle_deck(deck))
