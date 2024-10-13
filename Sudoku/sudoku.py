#in backtracking, once the last box is filled, it means that the problem is solved as each box is solved as it goes, not all at once  

board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

#backtracking 
#use recursive function: call the function from inside itself 
def solve(bo):
    
    #base case: the board is full/filled up 
    find = find_empty(bo)
    if not find:
        return True
    else: 
        row, col = find
    
    for i in range(1,10):
        #check if the number is valid in the board
        if correct(bo, i, (row, col)):
            #insert the valid number into the board
            bo[row][col] = i 
            
            if solve(bo):
                return True
            
            #resets
            bo[row][col] = 0
            
    return False 
            
            

def correct(bo, num, pos):
    #check row by looping through all col in the row 
    for i in range(len(bo[0])):
        #check each col/ each element in the row if it is equal to the number we are trying to place juts added in AND 
        # ignore it the element being checked is the pos where the num was just added in
        if bo[pos[0]][i] == num and pos[1] != i:
            return False 
    
    #check col
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False 
    
    #check box 
    #for 3x3 box, top left corner is (0,0) and bottom right corner is (2,2)
    box_x = pos[1] // 3
    box_y = pos[0] // 3
    
    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x*3, box_x*3 + 3):
            if bo[i][j] == num and (i,j) != pos:
                return False
    
    return True 
        




#column=x  row=y 
#creating the sudoku board layout 
def print_board(bo):
    
    for i in range (len(bo)):
        #create the vertical separation between the 3x3 boxes 
        if i % 3 ==0 and i != 0:
            print("-------------------------")
        
        #create the horizontal separation between the 3x3 boxes
        for j in range (len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")    #end="" is used to print the next print statement in the same lines
            
            if j == 8:
                print(bo[i][j])
                
            else:
                print(str(bo[i][j]) + " ", end="")



#find the empty places in the board 
def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i,j) #row, column (y,x)
    
    return None    


solve(board)
print_board(board)             