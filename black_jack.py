'''
Black Jack Game
To Do's:
Create a deck of 52 cards
Shuffle the deck
Ask the Player for their bet
Make sure that the Player's bet does not exceed their available chips
Deal two cards to the Dealer and two cards to the Player
Show only one of the Dealer's cards, the other remains hidden
Show both of the Player's cards
Ask the Player if they wish to Hit, and take another card
If the Player's hand doesn't Bust (go over 21), ask if they'd like to Hit again.
If a Player Stands, play the Dealer's hand. The dealer will always Hit until the Dealer's value meets or exceeds 17
Determine the winner and adjust the Player's chips accordingly
Ask the Player if they'd like to play again


'''

import random #to shuffle

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace') 
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}
playing= True

#card class which would connects the suits, ranks and values to each card
class Card:
  def __init__(self,suits,ranks): 
    self.suits=suits
    self.ranks=ranks 
    # self.values=values[ranks] #uses dictionary to find the numerical value of the card
  def __str__(self):
    return self.ranks + ' of ' + self.suits #returns the string value of the card

#card1=Card('Hearts','Two')
#print(card1)

#deck class that creates the deck in which cards will be taken out of
class Deck:
  def __init__(self):
    self.deck=[] #empty set so we can insert cards
    for suit in suits:
      for rank in ranks:
        #generated_card=Card(suit,rank) #hold the card in a seperate variable
        self.deck.append(generated_card) #add card to previous list 
  def __str__(self):
    deck_comp = ''  # start with an empty string
    for card in self.deck:
      deck_comp += '\n '+card.__str__() # add each Card object's print string
    return 'The deck has:' + deck_comp 
  def shuffle(self):
    random.shuffle(self.deck)
  def deal(self):
    single = self.Deck.pop() 
    return single

#test_deck = Deck()
#print(test_deck)
#hand class will add the cards
class Hand:
  def __init__(self):
    self.cards = []  # start with an empty list as we did in the Deck class
    self.value = 0   # start with zero value
    self.aces = 0    # add an attribute to keep track of aces
    
  def add_card(self,card): #this method takes the cards and adds the value
    for x in len(self.cards): #checks for the length of the list and iterates through the values
      self.value+=self.value+self.cards[x] #adds the value of the cards to self.value
    return self.value #retuns said value of the hand
    
  def adjust_for_ace(self): #incase hand goes over 21 we will consider ace as 1
    if 'Ace' in self.cards and self.value>21: #checks of ace is in the hand and if it goes over the value 21
      return self.value-10 #returns the value with 10 subtracted

class chips:
    
    def __init__(self):
        self.total = 100  # This can be set to a default value or supplied by a user input
        self.bet = 0
        
    def win_bet(self):
        self.total= self.total + self.bet #adds the bet amount to the total
    
    def lose_bet(self):
        self.total= self.total - self.bet #takes away the bet amount from total


      
#checks if wager can be taken
def take_bet():
  while True:#take in inputs until its validated
    try:
      chips.bet=int(input('How much money would you like to bet?: ')) #asks how much they would like to wager
    except:
      print("Something went wrong") #throws exception if conditions are not met
    else: #final validation
      if chips.bet>chips.total: 
        print('Sorry, balance exceeded. Avaiable funds: ',chips.total) 
      else: #leave loop because conditions are met
        break

#add a card
def hit(deck,hand):
  hand.add(deck.deal()) #add a card to the hand
  hand.adjust_for_ace() #check if over 21 and contains ace for adjustment

def hit_or_stand(deck,hand):
  global playing  # to control an upcoming while loop
  while True:
    x = input ("Would you like to Hit or Stand? Enter 'h' or 's': ")
    if x[0].lower()=='h':
      hit(deck, hand)
    elif x[0].lower()=='s':
      print('Player stands, Dealer is playing.')
      playing=False
    else:
      print('Invalid input try again.')
      continue
    break
    
def show_some(player,dealer):
    print("\nDealer's Hand:")
    print(" <card hidden>")
    print('',dealer.cards[1])  
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    
def show_all(player,dealer):
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("Dealer's Hand =",dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand =",player.value)

def player_busts(player,dealer,chips):
    print("Player busts!")
    chips.lose_bet()

def player_wins(player,dealer,chips):
    print("Player wins!")
    chips.win_bet()

def dealer_busts(player,dealer,chips):
    print("Dealer busts!")
    chips.win_bet()
    
def dealer_wins(player,dealer,chips):
    print("Dealer wins!")
    chips.lose_bet()
    
def push(player,dealer):
    print("Dealer and Player tie! It's a push.")

while True:
    # Print an opening statement
    print('Welcome to BlackJack! Get as close to 21 as you can without going over!\n\
    Dealer hits until she reaches 17. Aces count as 1 or 11.')
    
    # Create & shuffle the deck, deal two cards to each player
    deck = Deck()
    deck.shuffle()
    
    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())
    
    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())
            
    # Set up the Player's chips
    player_chips = Chips()  # remember the default value is 100    
    
    # Prompt the Player for their bet
    take_bet(player_chips)
    
    # Show cards (but keep one dealer card hidden)
    show_some(player_hand,dealer_hand)
    
    while playing:  # recall this variable from our hit_or_stand function
        
        # Prompt for Player to Hit or Stand
        hit_or_stand(deck,player_hand) 
        
        # Show cards (but keep one dealer card hidden)
        show_some(player_hand,dealer_hand)  
        
        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player_hand.value > 21:
            player_busts(player_hand,dealer_hand,player_chips)
            break        


    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17 
    if player_hand.value <= 21:
        
        while dealer_hand.value < 17:
            hit(deck,dealer_hand)    
    
        # Show all cards
        show_all(player_hand,dealer_hand)
        
        # Run different winning scenarios
        if dealer_hand.value > 21:
            dealer_busts(player_hand,dealer_hand,player_chips)

        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand,dealer_hand,player_chips)

        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand,dealer_hand,player_chips)

        else:
            push(player_hand,dealer_hand)        
    
    # Inform Player of their chips total 
    print("\nPlayer's winnings stand at",player_chips.total)
    
    # Ask to play again
    new_game = input("Would you like to play another hand? Enter 'y' or 'n' ")
    
    if new_game[0].lower()=='y':
        playing=True
        continue
    else:
        print("Thanks for playing!")
        break