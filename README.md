# deck

## Using virtualenv

### Activation

```
> cd code/deck-of-cards
> source venv/bin/activate
```

### Deactivation

```
> deactivate
```

## War

1. shuffle a deck
1. deal all cards in deck to 2 players (the user and the computer)
1. until the game is over
   1. each player plays 1 card
   1. the higher card wins
   1. the winner takes all played cards and puts them in bottom of hand
   1. if the cards tie, then it's war
      1. each player puts down 3 cards facedown, then 1 card face up
      1. the higher card wins
      1. if the cards tie, then it's war again...
   1. the game ends when 1 player has 0 cards (or when 1 player quits)

## To Do List

### Done

- create a deck
- shuffle a deck
- deal a deck into N hands

### To Do

