#rock paper scissors
import random
playList = ['rock','paper','scissors']
playerScore = 0
ComputerScore = 0
def play():
    global playerScore
    global ComputerScore
    player = random.choice(playList)
    inputPlay = input('Enter your choice r/p/s:')
    playerInput = ''
    if inputPlay == 'r':
        playerInput = 'rock'
    elif inputPlay == 'p':
        playerInput = 'paper'
    elif inputPlay == 's':
        playerInput = 'scissors'
    else:
        print('Please enter correct choice.')
        inputPlay = input('Enter your choice r/p/s:')
    print('Computer said :',player)
    print('You said :',playerInput)

    while True:
        if playerInput == 'rock' and player == 'paper':
            print('computer wins.')
            ComputerScore += 1
            print('Computer :',ComputerScore)
            print('player :',playerScore)
            break
        elif playerInput == 'paper' and player == 'scissors':
            print('computer wins.')
            ComputerScore += 1
            print('Computer :',ComputerScore)
            print('player :',playerScore)
            break
        elif playerInput == 'scissors' and player == 'rock':
            print('computer wins.')
            ComputerScore += 1
            print('Computer :',ComputerScore)
            print('player :',playerScore)
            break
        elif player == 'rock' and playerInput == 'paper':
            print('You win.')
            playerScore += 1
            print('Computer :',ComputerScore)
            print('player :',playerScore)
            break
        elif player == 'paper' and playerInput == 'scissors':
            print('You win.')
            playerScore += 1
            print('Computer :',ComputerScore)
            print('player :',playerScore)
            break
        elif player == 'scissors' and playerInput == 'rock':
            print('You win.')
            playerScore += 1
            print('Computer :',ComputerScore)
            print('player :',playerScore)
            break
        player = random.choice(playList)
        inputPlay = input('Enter your choice r/p/s:')
        if inputPlay == 'r':
            playerInput = 'rock'
        elif inputPlay == 'p':
            playerInput = 'paper'
        elif inputPlay == 's':
            playerInput = 'scissors'
        else:
            playerInput = ''
            print('Please enter correct choice.')
            play()
        print('Computer said :',player)
        print('You said :',playerInput)

while ComputerScore < 3 or playerScore < 3:
    play()

    if ComputerScore == 3:
        print('Computer has 3 points. computer wins.')
        break
    
    if playerScore == 3:
        print('Player has 3 points. player wins.')
        break