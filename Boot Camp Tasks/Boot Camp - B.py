import sys
import collections 
import random
sys.setrecursionlimit(30000)

items = {1 : 'rock', 2 : 'scissors', 3 : 'paper'}
players = {}

def get_random_item(strategy):
    r = 100
    distrib = []
    if strategy == 'rock':
        distrib = [1,2,3]
    elif strategy == 'scissors':
        distrib = [2,1,3]
    elif strategy == 'paper':
        distrib = [3,1,2]
    randval = round(random.uniform(0,r))
    if randval < r/2:
        return items[distrib[0]]
    elif randval >= (r//2) and randval <= (3*r//4):
        return items[distrib[1]]
    elif randval > (3*r//4):
        return items[distrib[2]]

def sim_round(player1,player2):
    first_wins,second_wins = 0,0
    while second_wins < 2 and first_wins < 2:
        it1 = get_random_item(players[player1])
        it2 = get_random_item(players[player2])
        if (it1 != it2):
            if (it1 == 'rock'):
                if (it2 == 'scissors'):
                    first_wins += 1
                elif (it2 == 'paper'):
                    second_wins += 1
            if (it1 == 'scissors'):
                if (it2 == 'paper'):
                    first_wins += 1
                elif (it2 == 'rock'):
                    second_wins += 1
            if (it1 == 'paper'):
                if (it2 == 'rock'):
                    first_wins += 1
                elif( it2 == 'scissors'):
                    second_wins += 1
    ##print('player',winner,'wins with score',first_wins,':',second_wins)
    if first_wins > second_wins:
        return [player1,player2]
    else:
        return [player2,player1]

def main():
    rounds_count = int(input())
    playes_count = 1 << rounds_count
    for i in range(1,playes_count+1):
        randval = round(random.uniform(1,3))
        strategy = items[randval]
        players[i] = strategy
        sys.stdout.write("player %s: %s\n" %(i,strategy))
    sys.stdout.write('\n')
    losers = set()
    current_round = 0
    while (playes_count > 1):
        if (current_round < rounds_count - 1):
            sys.stdout.write('round %s\n' % (current_round + 1))
        else:
            sys.stdout.write('final round\n')
        enemy = -1
        forbid = set()
        for player in players.keys():
            if player in forbid or player in losers:
                continue 
            forbid.add(player)
            enemy = player 
            while (enemy in forbid or enemy in losers):
                enemy = random.choice(list(players.keys())) 
            forbid.add(enemy)
            winner,loser = sim_round(player,enemy)
            sys.stdout.write('player %s vs player %s: the winner is player %s\n' % (player,enemy,winner))
            losers.add(loser)       
        playes_count >>= 1
        current_round += 1
        sys.stdout.write('\n')
if __name__ == "__main__":
    ##sys.stdin = open('f.in','r')
    ##sys.stdout = open('f.out','w')
    main()
    ##sys.stdin.close()
    ##sys.stdout.close()