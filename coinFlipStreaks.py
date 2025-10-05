# Automate the Boring Stuff
# Chapter 6, Coin Flip Streaks
import random
experiments_with_streak = 0 # Original name was number_of_streaks

for experiment_number in range(10000): # Run 10.000 experiments in total.
    # Code that creates a list of 100 'heads' or 'tails' values
    some_list = []
    for i in range(100):
        some_list.append(random.randint(0,1))
    # Code that checks if there is a streak of 6 heads or tails in a row
    streak_found = False
    for i in range(len(some_list)-5): # up to index 94 (100-6) --> range(95)
        slice_6 = some_list[i:i+6]
        if slice_6 == [0] * 6 or slice_6 == [1] * 6:
            experiments_with_streak += 1
            streak_found = True 
            break # count max. 1 streak per experiment
               
print('Chance of streak: %s%%' % (experiments_with_streak / 100))
