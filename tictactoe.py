#this is a (shitty) version of tic tac toe. I can't believe it took me pretty much a year to make this. idk if all the cases even work. 

def get_input(): #number gets returned as a string, so make sure to cast it into an int first.
    is_num = False

    while is_num == False:
        acceptable_values = [0,1,2,3,4,5,6,7,8,9] #try and implement this
        choice = input("Location from 0-8: ")

        if choice.isdigit() == True and int(choice) <= 9:
            is_num = True
            break
        else:
            pass

    return int(choice)

board_data = [0,1,2,3,4,5,6,7,8] 

#display board
def disp(data): #if you wanna improve this, reverse the way that the data is sliced and printed. 
    temp_data = data
    print(temp_data[0:3])
    print(temp_data[3:6])
    print(temp_data[6:9])

def write(symbol, position, data):
    data[position] = symbol

    return data

def check_win(data):
    #create checks, return true or false afterwards
    #not sure if this is the best way to do it, idk if py has switch statements
    if data[0] == data[1] == data[2]:
        print("game won!")
        return True
    elif data[3] == data[4] == data[5]:
        print("game won!")
        return True
    elif data[6] == data[7] == data[8]:
        print("game won!")
        return True
    elif data[0] == data[3] == data[6]:
        print("game won!")
        return True
    elif data[1] == data[4] == data[7]:
        print("game won!")
        return True
    elif data[2] == data[5] == data[8]:
        print("game won!")
        return True
    elif data[6] == data[4] == data[2] and not ' ':
        print("game won!")
        return True
    elif data[0] == data[4] == data[8] and not ' ':
        print("game won!")
        return True
    else:
        return False

#ask if player 1 chooses x or o::

def player_choice():
    choice = input("Player 1: X/O? > ")

    return choice

#tie in board writer and printer
#get board and display it
def game():
    game_won = False
    temp_d = board_data

    p1 = player_choice()
    p2 = 'o'
    if p1 == 'x':
        p2 = 'o'
    else:
        p2 = 'x'
    #this would be the main game loop
    while game_won == False:
        #ask if p1 chooses x or o

        disp(temp_d)
        print("Player 1 turn!")

        place = get_input()
    
        #write to the board, which in this case is temp_d
        write(p1, place, temp_d)

        disp(temp_d)

        game_won = check_win(temp_d)
        if game_won == True:
            break
        else:
            pass

        #implement p2's turn into the game

        print("Player 2 turn!")

        place = get_input()

        write(p2, place, temp_d)


#testing area

game()
