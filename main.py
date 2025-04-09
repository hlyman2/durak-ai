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

allegation = game.deck.draw()
for card in game.players[0].hand:
    if game.can_beat(card, allegation):
        print(f"{card} can beat {allegation}")
    else:
        print(f"{card} can't beat {allegation}")
