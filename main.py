#Nothing important, just cosmetics
if __name__ == '__main__':
    print("-----------------------------------------------------------------------\n"
          "___  ___                          _               _   _  __   _____ \n"
          "|  \\/  |                         (_)             | | | |/  | |  _  ||\n"
          "| .  . | ___ _ __ ___   ___  _ __ _ ___  ___ _ __| | | |`| | | |/' |\n"
          "| |\\/| |/ _ \\ '_ ` _ \\ / _ \\| '__| / __|/ _ \\ '__| | | | | | |  /| |\n"
          "| |  | |  __/ | | | | | (_) | |  | \\__ \\  __/ |  \\ \\_/ /_| |_\\ |_/ /\n"
          "\\_|  |_/\\___|_| |_| |_|\\___/|_|  |_|___/\\___|_|   \\___/ \\___(_)___/\n"
          "                                            ______\n"
          "                                           |______|\n"
          "-----------------------------------------------------------------------")
    print(
        '     Welcome to Memoriser Offline Desktop Version V1.0 by Atomowyy\n------------------------------------------'
        '-----------------------------')
    while True:
        print('1. Editing mode\n2. Learning mode\n3. Exit')
        try:
            user_choice: int = int(input('Make your choice: '))
        except ValueError:
            print('You\'ve entered wrong option, try again.')
        else:
            match user_choice:
                case 1:
                    print('Editing mode. Work in progress...')
                case 2:
                    print('Learning mode. Work in progress...')
                case 3:
                    print('EXIT IS ALSO WORK IN PROGRESS, YOU CANT ESCAPE')
                    print('just joking')
                    break
                case _:
                    print("why")

