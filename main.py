import cards
import durak_game
import utils

game = durak_game.Play()

for i in range(len(game.players)):
    print(f"player {i} hand:")
    for card in game.players[i].hand:
        print(f"  {card.getValue()} {card.getSuit()}")
