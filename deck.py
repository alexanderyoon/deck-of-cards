import random
from pprint import pprint

def create_deck():
    """Create a list of 52 cards, where each card is a dictionary with 2
    fields: 'suit' and 'rank'.
    """
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
            
    return deck

def shuffle_deck(deck, shuffle_count=200):
    """Shuffle the deck.

    """
    for i in range(shuffle_count):
        # Pick a random index.
        i = random.randint(0, len(deck) - 1)
        
        # Pick a 2nd random index, and make sure that it is different
        # from the 1st.
        j = i
        while j == i:
            j = random.randint(0, len(deck) - 1)

        # Swap the 2 cards.
        deck[i], deck[j] = deck[j], deck[i]

        
if __name__ == '__main__':
    print('Here is a deck:')
    deck = create_deck()
    pprint(deck)
    print()

    print('Let\'s shuffle the deck:')
    shuffle_deck(deck)
    pprint(deck)
    print()

    print('Let\'s shuffle the deck again:')
    shuffle_deck(deck)
    pprint(deck)
    print()
