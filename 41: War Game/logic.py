import player_class
import deck_class


player_one = player_class.Player("One")
player_two = player_class.Player("Two")

new_deck = deck_class.Deck()
new_deck.shuffle()

for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())

game_on = True
round_num = 0

while game_on:
    round_num += 1
    print(f"Round {round_num}")

    if len(player_one.all_cards) == 0:
        print("Player One is out of cards, Player Two wins!")
        game_on = False
        break

    if len(player_two.all_cards) == 0:
        print("Player Two is out of cards, Player One wins!")
        game_on = False
        break

    player_one_cards = [player_one.remove_one()]

    player_two_cards = [player_two.remove_one()]

    at_war = True
    while at_war:
        if player_one_cards[-1].value > player_two_cards[-1].value:
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)
            at_war = False
        elif player_two_cards[-1].value > player_one_cards[-1].value:
            player_two.add_cards(player_one_cards)
            player_two.add_cards(player_two_cards)
            at_war = False
        else:
            print("War!")
            if len(player_one.all_cards) < 5:
                print("Player One is unable to declare war\nPlayer Two wins")
                game_on = False
                break
            elif len(player_two.all_cards) < 5:
                print("Player Two is unable to declare war\nPlayer One wins")
                game_on = False
                break
            else:
                for num in range(5):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())
