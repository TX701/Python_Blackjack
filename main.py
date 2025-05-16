from logic import create_deck, starting_hands, hit_stand_loop
    
def game_loop():
    dealer_wins = 0; player_wins = 0
                  
    while True:
        print(f"=== Dealer: {dealer_wins} Player: {player_wins} ===\n")
        deck = create_deck()
        dealer_hand = []; player_hand = []
        
        dealer_hand, player_hand, deck = starting_hands(dealer_hand, player_hand, deck)
        
        outcome = hit_stand_loop(dealer_hand, player_hand, deck)
        
        if outcome == "D":
            print("Dealer wins\n")
            dealer_wins += 1
        elif outcome == "P":
            print("Player wins\n")
            player_wins += 1
        elif outcome == "Q":
            break
        else: print("Draw\n")
    
if __name__ == "__main__":
    game_loop()