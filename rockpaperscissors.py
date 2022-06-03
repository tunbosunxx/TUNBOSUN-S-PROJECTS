print('''rock paper scissors by  Tunbosun
= rock beats scissors
= paper beats rock
= scissors beats paper
''')

wins = 0
losses = 0
ties = 0

while True:
    while True:
        print('{} wins, {} losses, {} ties'.format(wins,losses,ties))
        print('ENTER YOUR MOVE: (R)OCK (p)APER (S)CISSORS or (Q)UIT')
        playermove = input('> ' ).upper()
        if playermove == 'Q':
            print('Thanks for playing!')
        
        if playermove == 'R' or playermove == 'P' or playermove == 'S':
            break
        else:
            print('Type one of R,P,S or Q')

    if playermove  == 'R':
        print('ROCK Versus....')
        playermove = 'ROCK'
    elif playermove == 'P':
        print('PAPER Versus....')
        playermove = 'PAPER'
    elif playermove ==  'S':
        print('SCISSORS Versus....')
        playermove = 'SCISSORS'
    
    random_number = random.randint(1, 3)
    if random_number == 1:
        computer_move = 'ROCK'
    elif random_number == 2:
        computer_move = 'PAPER'
    elif random_number == '3':
        computer_move = 'SCISSORS'
    print(computer_move)

    if playermove == computer_move:
        print("it's a  tie!")
        ties = ties + 1
    elif playermove == 'ROCK' and computer_move == 'SCISSORS':
        print('you win!')
        wins = wins + 1
    elif playermove == 'PAPER' and  computer_move == 'ROCK':
        print('you win!')
        wins = wins + 1
    elif playermove ==  'SCISSORS' and computer_move == 'PAPER':
        print('you win!')
        wins = wins + 1
    elif playermove == 'ROCK' and computer_move == 'PAPER':
        print('you lose!')
        losses = losses + 1
    elif playermove == 'PAPER' and computer_move == 'SCISSORS':
        print('you lose!')
        losses  = losses  + 1
    elif playermove  == 'SCISSORS' and computer_move == 'ROCK':
        print('you lose!')
        losses = losses + 1








            
        