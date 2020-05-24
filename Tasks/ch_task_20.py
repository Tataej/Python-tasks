##20. Don't Roll Doubles!
##John is playing a dice game. The rules are as follows.
##Roll two dice.
##Add the numbers on the dice together.
##Add the total to your overall score.
##Repeat this for three rounds.
##But if you roll DOUBLES, your score is instantly wiped to 0 and your
##game ends immediately!
##Create a function that takes in a list of tuples as input, and return
##John's score after his game has ended.
##Examples
##dice_game([(1, 2), (3, 4), (5, 6)]) ➞ 21
## 
##dice_game([(1, 1), (5, 6), (6, 4)]) ➞ 0
## 
##dice_game([(4, 5), (4, 5), (4, 5)]) ➞ 27
##Notes
##Ignore all other tuples in the list if a throw happens to be doubles
##and go straight to returning 0.
##John only has two dice and will always give you outcomes for three rounds.

from random import *

def dice_game(game):
    if game[0][0] == game[0][1] or game[1][0] == game[1][1] or game[2][0] == game[2][1]:
        print('dice_game(',game,') --> 0')
        return('0')            
    else:
        count = 0
        result = 0
        result1 = 0
        for elements in game:
            for i in elements:
                result2 = elements[0] + elements[1]
            result1 += result2
        result +=result1
        count += result
        print('dice_game(',game,') --> %d' %(count))
        return(count)



##game = []
##for i in range(3):
##    elements = []
##    for j in range(2):
##        elements.append(int(randint(1,6)))
##    game.append(elements)
##
##dice_game(game)
            
        
        


