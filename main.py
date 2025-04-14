import cards
import durak_game
import utils

game = durak_game.Play()

print(f"trump card: {game.deck.last()}\n")
for i in range(len(game.players)):
    print(f"player {i} hand:")
    for card in game.players[i].hand:
        print(f"  {card}")

print()

# while lopp for the continuous play of the game, doesn't work yet, but the continue_game function should
#while durak_game.continue_game():
 #   while # not AI.output == do_nothing:
  #      players[durak_game.get_player()].play_card(...) # Hopefully plays a card from the players hand
class Test:
    def __init__(self):
        print(len(game.deck))
        for x in range (5):
            game.players[1].play_card[game.players[1].hand[x]]
        print(game.players[1].hand)
        game.deal_cards(game.players[1])
