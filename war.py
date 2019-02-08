#!/usr/bin/env python

from pprint import pprint

from deck import create_deck, shuffle_deck, deal_deck

def war(hand1, hand2, played_cards=[]):

    if len(hand1) == 0 and len(hand2) > 0:
        print("Hand 2 wins the game!")
        return
    elif len(hand1) > 0 and len(hand2) == 0:
        print("Hand 1 wins the game!")
        return
    elif len(hand1) == 0 and len(hand2) == 0:
        # Ran out of cards at the same time.
        print("TIE!")
        return

    print("WAR!")
    l = 0

    # Get 4 cards from each hand.
    hand1_cards = []
    card_count = 4 if len(hand1) >= 4 else len(hand1)
    for i in range(card_count):
        hand1_cards.append(hand1.pop())
    print("Hand 1 played:")
    pprint(hand1_cards)

    hand2_cards = []
    card_count = 4 if len(hand2) >= 4 else len(hand2)
    for i in range(card_count):
        hand2_cards.append(hand2.pop())
    print("Hand 2 played:")
    pprint(hand2_cards)

    # Compare the last card dealt from each hand.
    hand1_last_card = hand1_cards[-1]
    hand2_last_card = hand2_cards[-1]
    print("Your Knight is:" )
    pprint(hand1_last_card)
    print("The computer's Knight is:" )
    pprint(hand2_last_card)
    played_cards += hand1_cards + hand2_cards
    if hand1_last_card['value'] > hand2_last_card['value']:
        # Hand 1 wins, so it gets all the cards.
        print("Hand 1 wins!")
        print('Your deck is {} cards long'.format(len(user_hand)))
        print('The Enemy\'s deck is {} cards long'.format(len(computer_hand)))
        card_count = 10 * l
        for n in card_count:
            print("Played cards:")
            pprint(played_cards)
            win_card = played_cards.pop()
            hand1.append(win_card)
            print(hand1)
            pprint(hand1)
    elif hand1_last_card['value'] < hand2_last_card['value']:
        # Hand 2 wins, so it gets all the cards.
        print("Hand 2 wins!")
        print('Your deck is {} cards long'.format(len(user_hand)))
        print('The Enemy\'s deck is {} cards long'.format(len(computer_hand)))
        card_count = 10 * l
        for n in card_count:
            print("Played cards:")
            pprint(played_cards)
            win_card = played_cards.pop()
            hand2.append(win_card)
            print("hand2")
            pprint(hand2)
    else:
        # We have another war.
        print('Your deck is {} cards long'.format(len(user_hand)))
        print('The Enemy\'s deck is {} cards long'.format(len(computer_hand)))
        war(hand1, hand2, played_cards)
        l += 1

def war_original(user_hand, computer_hand):
    print("WAR!")
    user_war1 = user_hand.pop()
    user_war2 = user_hand.pop()
    user_war3 = user_hand.pop()
    user_knight = user_hand.pop()
    computer_war1 = computer_hand.pop()
    computer_war2 = computer_hand.pop()
    computer_war3 = computer_hand.pop()
    computer_knight = computer_hand.pop()                                                                    
    if user_knight['value'] > computer_knight['value']: 
        print('Your Knight: {}'.format(user_knight))
        print('The Enemy\'s Knight: {}'.format(computer_knight))
        print('You win!')
        print('Your cards: {}, {}, {}'.format(user_war1, user_war2, user_war3))
        print('The Enemy\'s cards: {}, {}, {}'.format(computer_war1, computer_war2, computer_war3))
        user_hand.append(user_war1)
        user_hand.append(user_war2)
        user_hand.append(user_war3)
        user_hand.append(user_knight)
        user_hand.append(computer_war1)
        user_hand.append(computer_war2)
        user_hand.append(computer_war3)
        user_hand.append(computer_knight)
        print('Your deck is {} cards long'.format(len(user_hand)))
        print('The computer\'s deck is {} cards long'.format(len(computer_hand)))
    elif user_knight['value'] < computer_knight['value']:
        print('Your Knight: {}'.format(user_knight))
        print('The Enemy\'s Knight: {}'.format(computer_knight))
        print('You Lose')
        print('Your cards: {}, {}, {}'.format(user_war1, user_war2, user_war3))
        print('The Enemy\'s cards: {}, {}, {}'.format(computer_war1, computer_war2, computer_war3))
        computer_hand.append(user_war1)
        computer_hand.append(user_war2)
        computer_hand.append(user_war3)
        computer_hand.append(user_knight)
        computer_hand.append(computer_war1)
        computer_hand.append(computer_war2)
        computer_hand.append(computer_war3)
        computer_hand.append(computer_knight)
        print('Your deck is {} cards long'.format(len(user_hand)))
        print('The computer\'s deck is {} cards long'.format(len(computer_hand)))
    else:
        print('Your Knight: {}'.format(user_knight))
        print('The Enemy\'s Knight: {}'.format(computer_knight))
        war(user_hand, computer_hand)

def test_recursive_war():
    d = create_deck()
    assert len(d) == 52

    # Split an unshuffled into 2 hands that should be in the exact same order as each other.
    h1 = d[0:26]
    h2 = d[26:]
    assert len(h1) == 26
    assert len(h2) == 26

    # TODO: return a value from war() that tells us who won or if we got a tie.
    # assert result == tie
    war(h1, h2)
    assert len(h1) == 0
    assert len(h2) == 0

def practice_recursive_war():
    d = create_deck()

    # Split an unshuffled into 2 hands that should be in the exact same order as each other.
    h1 = d[0:26]
    h2 = d[26:]

    # TODO: return a value from war() that tells us who won or if we got a tie.
    # assert result == tie
    war(h1, h2)

def practice_semi_recursive_war():
    d = create_deck()

    # Split an unshuffled into 2 hands that should be in the exact same order as each other.
    h1 = d[0:26]
    h2 = d[26:]

    # Take the bottom thirteen cards from h1 and move them to h2.
    h3 = h1[0:13]
    h4 = h2 + h3

    # TODO: return a value from war() that tells us who won or if we got a tie.
    # assert result == tie
    war(h1, h4)

if __name__== '__main__':
    
    # Shuffle a deck.
    d = create_deck()
    shuffle_deck(d)

    # Deal the deck into 2 hands, one for each player.
    hands = deal_deck(d, 2)
    user_hand = hands[0]
    computer_hand = hands[1]

    while len(user_hand) > 0 and len(computer_hand) > 0:
        cmd = input('Enter "p" to play a card or "q" to quit: ')
        if cmd == 'p':
            user_card = user_hand.pop()
            print(user_card)
            computer_card = computer_hand.pop()
            print(computer_card)
            if user_card['value'] > computer_card['value']: 
                print('You: {}'.format(user_card))
                print('The Enemy: {}'.format(computer_card))
                print('You win!')
                user_hand.append(computer_card)
                user_hand.append(user_card)
                print('Your deck is {} cards long'.format(len(user_hand)))
                print('The Enemy\'s deck is {} cards long'.format(len(computer_hand)))
            elif user_card['value'] < computer_card['value']:
                print('You: {}'.format(user_card))
                print('The Enemy: {}'.format(computer_card))
                print('You lose')
                computer_hand.append(computer_card)
                computer_hand.append(user_card)                
                print('Your deck is {} cards long'.format(len(user_hand)))
                print('The Enemy\'s deck is {} cards long'.format(len(computer_hand)))    
            else:
                print('You: {}'.format(user_card))
                print('The Enemy: {}'.format(computer_card))
                war(user_hand, computer_hand, [user_card, computer_card])
        elif cmd == 'q':
            print('Goodbye.')
            break
        elif cmd == 'test':
            practice_recursive_war()
        elif cmd == 'test2':
            practice_semi_recursive_war()
        else:
            print('Sorry, didn\'t recognize your command: {}'.format(cmd))
    if len(user_hand) == 0:
        print('You have lost the game.')
    elif len(computer_hand) == 0:
        print('You win!')