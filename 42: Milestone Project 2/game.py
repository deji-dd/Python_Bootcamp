import deck_class
import hand_class
import function_definitions
while True:
    print('Welcome to BlackJack! Get as close to 21 as you can without going over!\nDealer hits until he reaches 17. Aces count as 1 or 11.')


    deck = deck_class.Deck()
    deck.shuffle()

    player_hand = hand_class.Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = hand_class.Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())


    function_definitions.show_some(player_hand, dealer_hand)

    while function_definitions.playing:


        function_definitions.hit_or_stand(deck, player_hand)


        function_definitions.show_some(player_hand, dealer_hand)


        if player_hand.value > 21:
            function_definitions.player_busts(player_hand, dealer_hand)
            break


    if player_hand.value <= 21:

        while dealer_hand.value < 17:
            function_definitions.hit(deck, dealer_hand)


        function_definitions.show_all(player_hand, dealer_hand)


        if dealer_hand.value > 21:
            function_definitions.dealer_busts(player_hand, dealer_hand)

        elif dealer_hand.value > player_hand.value:
            function_definitions.dealer_wins(player_hand, dealer_hand)

        elif dealer_hand.value < player_hand.value:
            function_definitions.player_wins(player_hand, dealer_hand)

        else:
            function_definitions.push(player_hand, dealer_hand)


    new_game = input("Would you like to play another hand? Enter 'y' or 'n' ")

    if new_game[0].lower() == 'y':
        playing = True
        continue
    else:
        print("Thanks for playing!")
        break
