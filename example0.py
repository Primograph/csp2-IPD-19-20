#### so unless i misunderstood something everyhting should b fine
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

import random

team_name = 'E0'
strategy_name = 'Random'
strategy_description = 'Randomly decides wether to collude, betray, or retaliate.'
    
def move(my_history, their_history, my_score, their_score):
    '''Make my move based on the history with this player.
    
    history: a string with one letter (c or b) per round that has been played with this opponent.
    their_history: a string of the same length as history, possibly empty. 
    The first round between these two players is my_history[0] and their_history[0]
    The most recent round is my_history[-1] and their_history[-1]
    
    Returns 'c' or 'b' for collude or betray.
    '''

    possibilities = [1, 2, 3]
    decision = random.choice(possibilities)
    if decision == 1: #colludes if 1 is chosen
      return 'c'
    elif decision == 2: #betrays if two is chosen
      return 'b'
    else:
      if len(their_history) == 0 and len(my_history) == 0:
        return 'c'
      elif their_history[-1] == 'b' and my_history[-1] == 'c':
        return 'b'
      elif their_history[-1] == 'c' and my_history[-1] == 'c':
        return 'c'
      else:
        return 'b'
