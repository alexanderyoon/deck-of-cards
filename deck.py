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

def shuffle_deck(deck, hands=None, shuffle_count=200):
    """Shuffle the deck.

    """
    if hands:
        # Add hands back into the deck.
        for hand in hands:
            deck += hand
        
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

def deal_deck(deck, hand_count, cards_per_hand=None):
    """Deal the deck into the specified number of hands (minimum of 2).

    """
    assert(hand_count >= 2)
    hands = []

    # Create the specified number of hands as empty lists.
    for i in range(hand_count):
        hand = []
        hands.append(hand)

    if cards_per_hand:
        cards_to_deal = hand_count * cards_per_hand
    else:
        cards_to_deal = len(deck)
    print('{} cards to deal.'.format(cards_to_deal))
    
    i = 0
    while cards_to_deal > 0:
        card = deck.pop()
        hand = hands[i]
        hand.append(card)
        
        # Deal the next card to the next hand.
        i += 1
        if i == hand_count:
            i = 0

        cards_to_deal -= 1

    return hands

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

    hand_count = 2
    print('Let\'s deal {} hands:'.format(hand_count))
    print()
    hands = deal_deck(deck, hand_count)
    for i, hand in enumerate(hands):
        print('Here is hand #{}:'.format(i))
        pprint(hand)
        print()

    shuffle_deck(deck, hands)
    
    hand_count = 2
    cards_per_hand = 5
    print('Let\'s deal {} hands, {} cards each:'.format(
        hand_count, cards_per_hand))
    print()
    hands = deal_deck(deck, hand_count, cards_per_hand)
    for i, hand in enumerate(hands):
        print('Here is hand #{}:'.format(i))
        pprint(hand)
        print()
    print('Here is the rest of the deck ({} cards left):'.format(len(deck)))
    pprint(deck)
    print()
