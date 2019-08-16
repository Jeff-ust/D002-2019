def printcell(cells):
    print("-" * 29)
    for i in range(0, 6):
        for j in range(0, 7):
            print("| %s " % cells[i][j], end="")
        print("|")
        print("-" * 29)



cells = [[" "," "," "," "," "," "," "], [" "," "," "," "," "," "," "], \
         [" "," "," "," "," "," "," "], [" "," "," "," "," "," "," "], \
         [" "," "," "," "," "," "," "], [" "," "," "," "," "," "," "]]
         


def check_row(cells):
    for row in range(0, 6):
        for col in range(0, 4):
            if cells[row][col] == cells[row][col+1] == cells[row][col+2] \
                == cells[row][col+3] != " ":
                return True
    return False



def check_col(cells):
    for row in range(0, 6):
        for col in range(0, 3):
            if cells[row][col] == cells[row-1][col] == cells[row-2][col] \
                == cells[row-3][col] != " ":                
                return True
    return False



def check_TLBR(cells):
    for row in range(0, 3):
        for col in range(0, 4):
            if cells[row][col] == cells[row + 1][col + 1] == cells[row + 2][col + 2] ==\
                cells[row + 3][col + 3] != " ":
                return True
    return False
                


def check_BLTR(cells):
    for row in range(5, 2, -1): 
        for col in range(0, 4):
            if cells[row][col] == cells[row - 1][col + 1] == cells[row - 2][col + 2] ==\
                cells[row - 3][col + 3] != " ":
                return True
    return False
               


def check(cells):
    if check_row(cells) or check_col(cells) or check_TLBR(cells) or check_BLTR(cells): 
        return True
    return False



def check_draw(cells):
    if cells[0][0] == cells[0][1] == cells[0][2] == cells[0][3] == cells[0][4] == cells[0][5] == cells[0][6] != " ":
        return True
    return False
        

turn = 1
printcell(cells)
while True:
    if turn %2 != 0:
        row = 5
        col = int(input("Player 1, please enter column. From 0 to 6.\t"))
        while col < 0 or col > 6: 
            print("Invalid input!")
            col = int(input("Player 1, please enter column again.\t"))
            
        while cells[row][col] != " ":
            row = row - 1
                      
            if row < 0 :
                print("The column is full!")
                col = int(input("Player 1, please enter column again.\t"))
                row = 5
        else:    
            cells[row][col] = "O"                                                                                                                            
            printcell(cells)
            turn = turn + 1
            if check(cells) == True:
                print("Player 1 wins!")
                break
            if check_draw(cells) == True:
                print("Draw!")
                break

    else:
        row = 5
        col = int(input("Player 2, please enter column. From 0 to 6.\t"))
        while col < 0 or col > 6:
            print("Invalid input!")
            col = int(input("Player 2, please enter column again.\t"))

        while cells[row][col] != " ":
            row = row - 1

            if row < 0 :
                print("The column is full!")
                col = int(input("Player 2, please enter column again.\t"))
                row = 5

        else:        
            cells[row][col] = "X"
            printcell(cells)
            turn = turn + 1
            if check(cells) == True:
                print("Player 2 wins!")
                break
            if check_draw(cells) == True:
                print("Draw!")
                break


        

    
