####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'E1'
strategy_name = 'Probability'
strategy_description = 'Tries to calculate the probability of collusion and betrayl using the history. Depending on which has a higher chance, it will either collude or betray.'

def move(my_history, their_history, my_score, their_score):
    '''Make my move based on the history with this player.
    
    history: a string with one letter (c or b) per round that has been played with this opponent.
    their_history: a string of the same length as history, possibly empty. 
    The first round between these two players is my_history[0] and their_history[0]
    The most recent round is my_history[-1] and their_history[-1]
    
    Returns 'c' or 'b' for collude or betray.
    '''
    import random
    choices = [1, 2]
    descision = random.choice(choices)
    prob_c = 0
    prob_b = 0
    start = False
    
    for move_my, move_their in zip(my_history, their_history):
      if move_my == 'b' and move_their == 'c':
        prob_b += 1
      elif move_my == 'b' and move_their == 'b':
        prob_c += 1
      elif move_my == 'c' and move_their == 'b':
        prob_b += 1
      elif move_my == 'c' and move_their == 'c':
        prob_b += 1
        prob_c += 1
      else:
        start = True
    
    if prob_c > prob_b: #if probability of c is higher, then it will randomly return c or b
      if descision == 1:
        return 'c'
      else:
        return 'b'
    elif prob_c < prob_b: #if probability of b is higher, then it will return b
      return 'b'
    elif start == True: #it will always start with c
      return 'c'