board=[
    
]

def solve(bo):
    find = check_empty(bo);

    if not find:
        return True
    else:
        row,col=find

    for i in range(1,10):

        if valid(bo,i,(row,col)):
            bo[row][col]=i

            if solve(bo):
                return True
            
            bo[row][col]=0

    return False



def valid(bo,num,pos):
    
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and bo[pos[1]]!=i:
            return False
        
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and bo[pos[0]]!=i:
            return False
    
    box_x=pos[0]//3
    box_y=pos[1]//3

    for i in range(box_x*3,(box_x*3)+3):
        for j in range(box_y*3,box_y*3+3):
            if bo[i][j]==num and (i,j)!= pos:
                return False
    
    return True

        
    

def print_board(bo):
    for i in range(len(bo)):
        if i%3==0 and i!=0:
            print("---------------------")
        
        for j in range(len(bo[0])):
            if j%3==0 and j!=0:
                print("|",end=" ");
            if j==8:
                print(bo[i][j])
            else:
                print(bo[i][j],end=" ")

def check_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if(bo[i][j]==0):
                return (i,j)
            
    return None



print("Please enter a sudoku board replace empty spaces with 0:")
for i in range(9):
    r=[]
    r=[int(x) for x in input().split()]
    board.append(r)

print("The entered board is:")
print_board(board)
solve(board)
print("\nThe solved one is:\n")
print_board(board)