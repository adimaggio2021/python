#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 19:34:20 2018

@author: adimaggio2021
"""
import random

class Die(object):
    
    def __init__(self, num):
        #num is the number of sides to the die
        self.sides = num
        
    def roll(self):
        holder = self.sides 
        result = random.randrange(1, holder + 1)
        return result
    
    
    
die1 = Die(6)
die2 = Die(6)
flag = False
while flag == False:
    var = input("Input number of players for the round.")
    try:
        #check to see if input is usable
        var = int(var)
    except:
        print("Only numerical inputs are valid.")
    else:
        flag = True
player = 0
high_player = 0


while var > 0:
    #reset game variables
    player += 1
    cash = 100
    games = 0
    highest = 100
    high_game = 0
    while cash > 0:
        games += 1
        total = die1.roll() + die2.roll()
        if total == 7 or total == 11:
            cash += 3
        else: 
            cash -= 1
        if cash > highest:
            #check for cash peak
            highest = cash
            high_game = games 
    var -= 1
    print ('Player '+ str(player) + ' ran out of money after ' + str(games) + " rolls. Their highest amount was " + str(highest) + " after " + str(high_game) + " rolls.")
    if games > high_player:
        #check if current player is best so far
        high_player = games
        player_id = player
        
       


print('Player ' + str(player_id) + ' won by staying in the game for ' + str(high_player) + ' rolls.')
       
   