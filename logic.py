import random, time

class Card:
  def __init__(self, value, suit):
    self.value = value
    self.suit = suit
    
  def __str__(self):
    return f"{self.value}{self.suit}"
    
def create_deck():
    deck = []
    
    for i in range(1, 14): # for 1 through 13
        deck.append(Card(number_to_value(i), "♠")) # get i♠
        deck.append(Card(number_to_value(i), "♡")) # get i♡
        deck.append(Card(number_to_value(i), "♣")) # get i♣
        deck.append(Card(number_to_value(i), "♢")) # get i♢
        
    return deck # return the deck

def print_cards(card_list, hide_second):
    hand_string = ""
    for i in range(0, len(card_list)):
        if hide_second and i == 1: # if it is the second card and if the second is not supposed to be shown replace with ??
            hand_string += "?? "
        else: hand_string += str(card_list[i]) + " " # add the cards string form to the string
    
    return hand_string # return string

def print_state(dealer_hand, player_hand, hide_dealer_hand):
    if hide_dealer_hand: # hides the second dealer card and does not show the dealers value
        print(f"Dealer:\t{print_cards(dealer_hand, hide_dealer_hand)}\nYou:\t{print_cards(player_hand, False)} ({hand_to_value(player_hand)})\n")
    else: print(f"Dealer:\t{print_cards(dealer_hand, hide_dealer_hand)} ({hand_to_value(dealer_hand)})\nYou:\t{print_cards(player_hand, False)} ({hand_to_value(player_hand)})\n")

def deal(deck):
    if len(deck) == 0: # if the deck is empty
        print(-1)
        return -1 # return -1
    card = deck.pop(random.randint(0, len(deck) - 1))
    return card, deck # else remove a random element from deck, return that element and the deck

def starting_hands(dealer_hand, player_hand, deck):
    dealer_hand = []; player_hand = [] 
    
    for i in range(2): # run twice
        dealer_card, deck = deal(deck) # remove a random card from the deck
        dealer_hand.append(dealer_card) # and add it to the dealers hand
        
        player_card, deck = deal(deck) # remove a random card from the deck
        player_hand.append(player_card) # and add it to the players hand
        
    return dealer_hand, player_hand, deck # return both hands and the deck

number_dictonary = {"A" : 1, "J": 11, "Q": 12, "K": 13}
  
def number_to_value(number):
    if 1 < number and number < 11: # if the number is between 1 and 11
        return number # return the number
    
    return list(number_dictonary.keys())[list(number_dictonary.values()).index(number)] # else get the face cards value from the dictionary

def card_to_value(card):
    if isinstance(card.value, str): # if the value of the card is a string
        if card.value == "A": # if the value is an ace return 11
            return 11
        return 10 # if it is a face card that is not an ace return 10
    
    return card.value # if it is not a face card just return the number on the card

def hand_to_value(hand):
    hand_value = []
    
    if len(hand) == 0:
        print("No cards in hand")
        return -1
    
    for card in hand:
        hand_value.append(card_to_value(card)) # convert all the cards to their values and add to the hand_value array
    
    while 21 < sum(hand_value): # if the sum of hand_value is over 21 
        if 11 in hand_value: # and if one of the values is 11
            hand_value[hand_value.index(11)] = 1 # change the first seen 11 into a 1
        else: break
        
    return sum(hand_value) # return the sum of the values in hand_value

def dealer_turn(dealer_hand, player_hand, deck):
    time.sleep(1)
    print("\nStarting dealer's turn") # inform player dealers turn is starting 
    
    while hand_to_value(dealer_hand) < 17: # if the deals hand is under 17
        time.sleep(1)
        print_state(dealer_hand, player_hand, False) # print the state and show the dealers full hand and value
        new_card, deck = deal(deck) # remove a card from the deck
        dealer_hand.append(new_card) # add that card to the dealers hand
    
    time.sleep(1)
    print_state(dealer_hand, player_hand, False) # print the state and show the dealers full hand and value
    return dealer_hand, deck

def determine_winner(dealer_hand, player_hand):
    dealer_value = hand_to_value(dealer_hand)
    player_value = hand_to_value(player_hand)
    
    if dealer_value < player_value:
        return "P"
    if player_value < dealer_value:
        return "D"
    
    return "T"

def hit_stand_loop(dealer_hand, player_hand, deck):
    player_input = " "
    
    while player_input != "S" and hand_to_value(player_hand) < 21: # if the player is not standing and their value is under 21
        print_state(dealer_hand, player_hand, True) # print state without showing dealers value
        print("Hit (H) or Stay (S)") # ask what player wants to do
        
        player_input = str(input()).upper() # convert input to a string and make it uppercase
        
        if player_input == "H": # if it is H
            new_card, deck = deal(deck) # take a card from the deck
            player_hand.append(new_card) # and add it to the players hand
        elif player_input == "Q":
            return "Q"
        elif player_input != "S": # if it is not H or S
            print("Invalid input") # inform the player an invalid input was made
    
    print_state(dealer_hand, player_hand, True) # print state without showing dealers value
          
    if hand_to_value(player_hand) == 21: # if the player hits 21
        print("\nYou are at 21\n", end = " ") # let them know so they know why their turn ended
    elif 21 < hand_to_value(player_hand): # if the player is over 21
        print("\nYou are over 21\n", end = " ") # let them know so they know why their turn ended
    
    dealer_hand, deck = dealer_turn(dealer_hand, player_hand, deck) # dealer takes turn
    return determine_winner(dealer_hand, player_hand) # determine winner and return value corresponding to winner
        