global main_comand
global two_comand
global buy_tikets
global together
global control
control = 0
global N 
N = 9
global M
M = 5
global letters
letters = ['A','B','C','D','E','F','G','H','I']

def create_start_arr():
    start_arr = []
    for i in range(N):
        mini_row = []
        for j in range(M):
            mini_row.append('O')
        start_arr.append(mini_row)
    return start_arr

while 1:

    if control == 0:
            arr = create_start_arr()
            control = 1

    comand = input("")
    arr_main_comand = comand.split()

    if comand == '':
        print('The command is not correct! Try another one.')
        continue
    elif len(arr_main_comand) == 1:
        main_comand = arr_main_comand[0]
    elif len(arr_main_comand) == 2:
        main_comand = arr_main_comand[0]
        two_comand = arr_main_comand[1]
    elif len(arr_main_comand) == 3:
        main_comand = arr_main_comand[0]
        two_comand = arr_main_comand[1]
        three_comand = arr_main_comand[2]
    else:
        print('The command is not correct! Try another one.')
        continue

    if (main_comand == 'buy' or main_comand == "Buy") and len(arr_main_comand)==3:
        buy_tikets = two_comand
        if control == 0:
            arr = create_start_arr()
            control = 1
            continue        
        number_free_row = 0
        for i in arr:
            free_places = 0
            count = 0
            check = False
            for j in i:
                if j == 'O':
                    free_places += 1         
            for place in i:
                if place=='O':
                    count += 1
                    if count==int(buy_tikets):
                        check = True
                        break
                elif place=='X':
                    count = 0
            if free_places >= int(buy_tikets) and check==True:
                print(i)
                print(f'There are {free_places} empty seats in the {letters[number_free_row]} row')
                print()
            number_free_row += 1
        if free_places < int(buy_tikets):
            print(f'There are no more places available for {buy_tikets} people!')

        for i in range(int(buy_tikets)):
            reserve_place = input('What place do you want to take? Enter the capital letter of the row and the seat number. ' )
            param = 0
            if len(reserve_place) != 2:
                print("The command is not correct!")
                continue
            for i in letters:
                if i == reserve_place[0]:
                    row = param
                    break
                param +=1 
                if param > N:
                    print("The command is not correct!")
                    break
                continue 
            place = int(reserve_place[1])-1
            if place+1 > M:
                print(f'The command is not correct! Try another one. Maximum number of seats in a row {M}')
                continue
            for i in range(N):  
                        for j in range(M):   
                                if i==int(row) and j==int(place):
                                    if arr[i][j]=="X":
                                        print('This place is already taken, choose another place!')   
                                    else:
                                        arr[i][j] = ("X")
            print(f'Place {reserve_place} occupied')
        
    elif (main_comand == 'buy' or main_comand == "Buy") and len(arr_main_comand)==2:
        buy_tikets = two_comand
        for i in range(int(buy_tikets)):
            reserve_place = input('What place do you want to take? Enter the capital letter of the row and the seat number. ' )
            param = 0
            if len(reserve_place) != 2:
                 print("The command is not correct!")
                 continue
            for i in letters:
                if i == reserve_place[0]:
                    row = param
                    break
                param +=1 
                if param > N:
                    print("The command is not correct!")
                    break
                continue 
            place = int(reserve_place[1])-1
            if place+1 > M:
                 print(f'The command is not correct! Try another one. Maximum number of seats in a row {M}')
                 continue
            for i in range(N):  
                        for j in range(M):   
                                if i==int(row) and j==int(place):
                                    if arr[i][j]=="X":
                                        print('This place is already taken, choose another place!')   
                                    else:
                                        arr[i][j] = ("X")  
            print(f'Place {reserve_place} occupied')                        
    elif main_comand == 'show' or main_comand == 'Show':
        if control == 0:
            arr = create_start_arr()
            control = 1
            continue
        for i in range(N):
            print(f'{letters[i] } {arr[i]}') 
            print()
    elif (main_comand == 'return' or main_comand == "Return") and len(arr_main_comand)==2:
                    return_tikets = two_comand
                    for i in range(int(return_tikets)):
                        reserve_place = input('What place do you want to take? Enter the capital letter of the row and the seat number. ' )  
                        param = 0  
                        for i in letters:
                            if i == reserve_place[0]:
                                row = param
                                break
                            param +=1 
                            if param > N:
                                print("The command is not correct!")
                                break
                            continue     
                        place = int(reserve_place[1])-1
                        N = 9
                        M = 5
                        for i in range(N):  
                            for j in range(M):   
                                    if i==int(row) and j==int(place):
                                        if arr[i][j]=="O":
                                            print('Entered incorrectly! this place is free')  
                                            continue 
                                        else:
                                            arr[i][j] = ("O")
                                            print(f'Place {reserve_place} freed')   
    else:
        print('The command is not correct! Try another one.')
        continue






