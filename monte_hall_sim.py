import random

wins = 0
losses = 0
trials = 10000

for int in range(trials):
    car = random.randint(1,3)
    pick = random.randint(1,3)
    
    if car == pick:
        losses += 1
    
    else:
        wins += 1

print("Total Wins: " + str(wins))
print("Total Losses: " + str(losses))
win_per = wins / trials
print("Win Percentage: " + str(win_per * 100) + "%")