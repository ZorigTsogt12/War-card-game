'''
Card game called war, played between two computers.
A deck of 52 cards is equally split between two players. 
The two players draw a card each and compare with each other.
If a player draws a card with a higher value than the other player, the player with the higher value card wins.
If a player wins the round, the player takes both their card and their own card to their own deck.
If both players draw the card with the same value, 
'''
import random

#Global variables
suits = ('Hearts', 'Diamond', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

#Dictionary that connects a car rank to the value
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

gameon = True

class Card:
    '''
    Card class creates an instance of a card by asking for the suit and the rank of a card
    '''

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
        
    def __str__(self):
        return self.rank + " of " + self.suit

class Deck:
    '''
    Deck class creates instances of the Card class by iterating through the ranks and values tuples and creating a card list 
    '''

    def __init__(self):
        
        self.all_cards = []
        
        for suit in suits:
            for rank in ranks:
                #Create the card object
                created_card = Card(suit, rank)
                
                self.all_cards.append(created_card)
    
    #Shuffle the order of card objects          
    def shuffle(self):
        
        random.shuffle(self.all_cards)
        
    #Remove a card from the deck, essentially a draw    
    def deal_one(self):
        return self.all_cards.pop()

class Player:
    '''
    Player class represents the players.
    Players have a list of cards, add cards, remove cards
    '''
    def __init__(self, name):
        #Player name
        self.name = name
        #The list for the players hand
        self.all_cards = []
        
    def add_cards(self, new_cards):
        # If new cards are a list of cards, extend
        # else append the single entity
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)
    
    def remove_one(self):
        return self.all_cards.pop(0)
    
    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards'

#Game Setup

#Create two players
player_one = Player('One')
player_two = Player('Two')

#Create deck and shuffle
new_deck = Deck()
new_deck.shuffle()

#Divide cards to two players
for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())

#Round counter
round_num = 0

while gameon:
    
    #Each iteration, increment the round number
    round_num += 1
    print(f'Round: {round_num}')
    
    #Player one lost check
    if len(player_one.all_cards) == 0:
        print('Player two wins')
        gameon = False
        break
    
    #Player two lost check
    if len(player_two.all_cards) == 0:
        print('Player one wins')
        gameon = False
        break
        
    #Start a new rounds by halving the deck between the two players
    player_one_cards = []
    player_one_cards.append(player_one.remove_one())
                            
    player_two_cards = []
    player_two_cards.append(player_two.remove_one())
    
    at_war = True
    
    while at_war:
        #Assumes the game is always at war

        if player_one_cards[-1].value > player_two_cards[-1].value:
            
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)
            
            at_war = False
            
        elif player_two_cards[-1].value > player_one_cards[-1].value:
            
            player_two.add_cards(player_one_cards)
            player_two.add_cards(player_two_cards)

            at_war = False
           
        # If two card values are equal then print WAR and each player draws 5 cards from their decks
        # The comparison game continues.     
        else:
            print('WAR!')
            
            if len(player_one.all_cards) < 5:
                print("Player One unable to declare war")
                print("Player two wins")
                gameon = False
                break
                
            elif len(player_two.all_cards) < 5:
                print("Player two unable to declare war")
                print("Player one wins")
                gameon = False
                break
            else:
                for num in range(5):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())
                    
        