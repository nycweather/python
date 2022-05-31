"""
Implement the card game war. Rules are:

1. Deal out deck of 52 cards between two users.
2. Each player plays a card. Higher card wins. Winner takes both cards.
3. If players tie, then each player puts down three cards, and the third
   card competes.
   If a player has less than 3 cards, then they put down all of their cards
   and their final card competes against the other player's third card.
   Continue doing this until tie is broken.
   Winner takes all cards.
4. Game is over when a player doesn't have any cards. The player with
   cards remaining is the winner.
"""
import random
#Standard deck of cards using a list to generate the deck/compare values later
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs') #set
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace') #set
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14} #dictionary

#Card class has two valued the suit and the value of the card
class Card:
  def __init__(self,suit,rank):
    self.suit=suit 
    self.rank=rank
    self.value=values[rank] #references the string with the int value using the dictionary
  def __str__(self): #str method incase we need to print out which card is being held on hand and at which index
    return self.rank+' of '+self.suit
#Deck class to create a shuffled deck using the sets from the beginning
    
class Deck:
  def __init__(self):
    self.all_cards=[] #creating empty list in the class
    for suit in suits:
      for rank in ranks: #goes through the loop 4*13 cards
        created_card=Card(suit,rank) #creates unique card
        self.all_cards.append(created_card) #card is storred in the list
  def shuffle (self):
     random.shuffle(self.all_cards) #shuffle cards
  def deal_one(self):
    return self.all_cards.pop() #take away from which ever player lost the fight
    
#player class
class Player:
  def __init__(self,name):
    self.name=name #name of the player
    self.all_cards=[] 
  def remove_one(self): #removes card if player lost the battle
    return self.all_cards.pop(0)
  def add_cards(self,new_cards):
    if type(new_cards)==type([]): #case where they goto war and have more than one card on the board
      self.all_cards.extend(new_cards)
    else: #add the single card to the other players list
      self.all_cards.append(new_cards)      
  def __str__(self):
    return f'Player {self.name} has {len(self.all_cards)} cards'

    
#Main game logic
player_one=Player('Player-1')
player_two=Player('Player-2')
new_deck=Deck() #makes new deck
new_deck.shuffle() #shuffles new deck

for x in range(26): #add cards to each players hand
  player_one.add_cards(new_deck.deal_one()) 
  player_two.add_cards(new_deck.deal_one())
game_on=True #start game
round=1 #round counter

while game_on: #game is set to true so the main while loop will check the played cards and count score accordingly
  round+=1
  #starting here
  print(f"Player 1 cards on hand: {len(player_one.all_cards)}") #shows how many cards are on the players hand
  for x in range(len(player_one.all_cards)): #prints the cards on the players hand
    print(player_one.all_cards[x])  
  print(f"\n\nPlayer 2 cards on hand: {len(player_two.all_cards)}") #shows how many cards are on the players hand
  for b in range(len(player_two.all_cards)):
    print(player_two.all_cards[b])  #prints the cards on the players hand
  print('\n\n')
  print(f'Currently On Round Number: {round}') #print which number of round we are in
  #to here is not necessary for the game logic it just shows the hand of the players
  
  if len(player_one.all_cards)==0: #if the player does not have any more cards on hand other player wins
    print ('Player 2 won!')
    game_on=False #exits main while loop because game is over
    break
  if len(player_two.all_cards)==0: #if the player does not have any more cards on hand other player wins
    print ('Player 1 won!')
    game_on=False  #exits main while loop because game is over 
    break
  player_one_cards=[] #temporary list to store the played cards
  player_one_cards.append(player_one.remove_one()) #removes card from player's hand
  player_two_cards=[] #temporary list to store the played cards
  player_two_cards.append(player_two.remove_one()) #removes card from player's hand
  
  war=True
  while war:
    if player_one_cards[-1].value > player_two_cards[-1].value: #checks if the numerical value of the card is more or less than the card opposite player has played
      print("Player 1 scored!\n")
      player_one.add_cards(player_one_cards) #adds players cards to the players deck
      player_one.add_cards(player_two_cards) #adds player twos cards to  player ones deck
      war=False
    elif player_one_cards[-1].value < player_two_cards[-1].value: #checks if the numerical value of the card is more or less than the card opposite player has played
      print("Player 2 scored!\n")
      player_two.add_cards(player_two_cards)  #adds players cards to the players deck
      player_two.add_cards(player_one_cards) #adds player ones cards to  player twos deck
      war=False
    else: #if the values of the two cards are same it will start war
      print("War!")
      if len(player_one.all_cards) < 3: #checks if the player can bring 3 more cards to risk
        print('Player One unable to declare war') #if not the other player wins
        print('Player Two wins')
        game_on=False #breaks out of the main loop
        break
      elif len(player_two.all_cards) < 3: #checks if the player can bring 3 more cards to risk
        print('Player Two unable to declare war') #if not the other player wins
        print('Player One wins')
        game_on=False #breaks out of the main loop
        break
      else: #if the player has cards avaiable they are put in the temporary list
        for num in range(3):
          player_one_cards.append(player_one.remove_one()) #removes cards from the players decks
          player_two_cards.append(player_two.remove_one())


'''
If we wanted to make the program computer vs player we could store all the cards in a dictionary 
and reference them from 1 to 52 this way when the cards are shuffled we will use 1-52 as the primary keys


'''
