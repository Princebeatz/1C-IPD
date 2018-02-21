import random
####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'The name the team gives to itself' # Only 10 chars displayed.
strategy_name = 'The name the team gives to this strategy'
strategy_description = 'How does this strategy decide? '
def placeholder(my_history, their_history, my_score, their_score, betraypercent, real_result ):
    if their_history[-10: -1]:
        def move(my_history, their_history, my_score, their_score):
         if 'bbbbb' in their_history[-100:-10]:
             betraypercent = -60
        if 'ccccc' in my_history[-100:-10]:
             betraypercent = -40
        if betraypercent < -50:
               their_history = random.choice['b','b','b','b','c']
        else:
               my_history = random.choice['b','b','c','c','c']
    if my_score > -140 and their_history[-10] == 'b':
      return 'b'
    elif my_score > -140 and their_history[-10] == 'c':
          return 'c' 
    
    ''' Arguments accepted: my_history, their_history are strings.
    my_score, their_score are ints.
    
    Make my move.
    Returns 'c' or 'b'. 
    '''

    # my_history: a string with one letter (c or b) per round that has been played with this opponent.
    # their_history: a string of the same length as history, possibly empty. 
    # The first round between these two players is my_history[0] and their_history[0].
    # The most recent round is my_history[-1] and their_history[-1].
    
    # Analyze my_history and their_history and/or my_score and their_score.
    # Decide whether to return 'c' or 'b'.
    
    return 'c'
    
def test_move(my_history, their_history, my_score, their_score, result):
    '''calls move(my_history, their_history, my_score, their_score)
    from this module. Prints error if return value != result.
    Returns True or False, depending on whether result was as expected.'''
    
    real_result = test_move (my_history, their_history, my_score, their_score, result)             
 
     
    # Test 1: Betray on first move.
    if test_move(my_history='',
              their_history='', 
              my_score=0,
              their_score=0,
              result ='b'):
         print 'Test passed'
     # Test 2: Continue betraying if they collude despite being betrayed.
    test_move(my_history='bbbbb',
              their_history='bbbbb', 
              # Note the scores are for testing move().
              # The history and scores don't need to match unless
              # that is relevant to the test of move(). Here,
              # the simulation (if working correctly) would have awarded 
              # 300 to me and -750 to them. This test will pass if and only if
              # move('bbb', 'ccc', 0, 0) returns 'b'.
              my_score=0, 
              their_score=0,
              result='b') 
              
    