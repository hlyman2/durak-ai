import cards
import durak_game
import utils


def Test():
    handLen = len(game.players[1].hand) - 1

    for  i in range (6):
        print(game.players[1].play_card(game.players[1].hand[handLen - i]))
        print(game.players[1].isOut())
    for  i in range (4):
        print(game.players[0].play_card(game.players[0].hand[handLen - i]))
    print(game.count_players())
    print(game.players[0].hand)
    game.deal_cards(game.players[1])

    print(game.players[0].hand)
    print(game.players[1].hand)
    print(game.players[2].hand)
    print(game.players[3].hand)

    game.next_turn()
    game.next_turn()
    game.next_turn()


game = durak_game.Play()
'''
print(f"trump card: {game.deck.last()}\n")
for i in range(len(game.players)):
    print(f"player {i} hand:")
    for card in game.players[i].hand:
        print(f"  {card}")
'''
print()

Test()

# while lopp for the continuous play of the game, doesn't work yet, but the continue_game function should
#while durak_game.continue_game():
 #   while # not AI.output == do_nothing:
  #      players[durak_game.get_player()].play_card(...) # Hopefully plays a card from the players hand
