# Car game - using while loop and conditionals
command = ""
started = False
helpText = """
start - To start the Car
stop - To stop the Car
quit - To Quit the game
"""
print('PLAY THE CAR GAME: type help for more info')
while True:  # Make it True to start the game
    command = input('> ').lower()
    if command == 'start':
        if started:
            print('Car already started...')
        else:
            started = True
            print('Car started!!!')
    elif command == 'stop':
        if not started:
            print('Car already stopped...')
        else:
            started = False
            print('Car stopped!!!')
    elif command == 'help':
        print(helpText)
    elif command == 'quit':
        print('Thanks for playing the game :)')
        break
    else:
        print("Don't know what to do? type help for instructions")
