from pprint import pprint

from deck import create_deck, shuffle_deck, deal_deck

if __name__ == '__main__':
	# Shuffle a deck.
	d = create_deck()
	shuffle_deck(d)
	pprint(d)

	# Deal the deck into 2 hands, one for each player.
	hands = deal_deck(d, 2)
	user_hand = hands[0]
	computer_hand = hands[1]

	while len(user_hand) > 0 and len(computer_hand) > 0:
		s = input('Enter "p" to play a card or "q" to quit: ')
		if s == 'p':
			# TODO: play 1 card from each hand and see who won
			print('You played a card!')
		elif s == 'q':
			print('Goodbye.')
			break
		else:
			print('Sorry, didn\'t recognize your command: {}'.format(s))
