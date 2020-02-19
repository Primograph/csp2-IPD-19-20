####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'E2'
strategy_name = 'Experience-based'
strategy_description = 'Collude once, Betray four times, then decide to collude/betray based on the results of the past 5 rounds'
    
def move(my_history, their_history, my_score, their_score):
    '''Make my move based on the history with this player.
    
    history: a string with one letter (c or b) per round that has been played with this opponent.
    their_history: a string of the same length as history, possibly empty. 
    The first round between these two players is my_history[0] and their_history[0]
    The most recent round is my_history[-1] and their_history[-1]
    
    Returns 'c' or 'b' for collude or betray.
    '''
    start = True
    count_4 = [1, 2, 3, 4]
    num_b = 0
    num_c = 0

    if start == True: #always starts with c
      start = False
      return 'c'
    
    for number in count_4: #always returns 5 b's right after
      return 'b'
    
    for letter in their_history: # checks if there are nore c's or b's
      if letter == 'c':
        num_c += 1
      elif letter == 'b':
        num_b += 1
    
    if num_c > num_b: # if there are more c's then it will betray. If there are more b's then it will collude.
      return 'b'
    else:
      return 'c'
