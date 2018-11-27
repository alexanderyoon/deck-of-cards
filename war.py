from pprint import pprint

from deck import create_deck, shuffle_deck, deal_deck

if __name__ == '__main__':
	# Shuffle a deck.
	d = create_deck()
	shuffle_deck(d)

	# Deal the deck into 2 hands, one for each player.
	hands = deal_deck(d, 2)
	user_hand = hands[0]
	computer_hand = hands[1]

def war():
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
		war()

while len(user_hand) > 0 and len(computer_hand) > 0:
	cmd = input('Enter "p" to play a card or "q" to quit: ')
	if cmd == 'p':
		user_card = user_hand.pop()
		computer_card = computer_hand.pop()
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
			war()
	elif cmd == 'q':
		print('Goodbye.')
		break
	elif cmd == 'Peace':
		print("																																																																					")
		break
	else:
		print('Sorry, didn\'t recognize your command: {}'.format(cmd))

if len(user_hand) == 0:
	print('You have lost the game.')
elif len(computer_hand) == 0:
	print('You win!') 
elif cmd == 'Peace':
	print('You win!')

