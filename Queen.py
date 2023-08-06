import numpy as np 
#__________________________________________



a = np.array( [ [0] * 4 ] * 4 )
n = len(a)


def is_valid(board, r, c):
    
    for i in range(r):
        if board[i][c] == 1:
            return False
  
   
    for i, j in zip(range(r, -1, -1), range(c, -1, -1)):
        if board[i][j] == 1:
            return False
    
     
    for i, j in zip(range(r, n, 1), range(c, -1, -1)):
        if board[i][j] == 1:
            return False
  
    return True



def q(board, r):
       
    if r >= n :
        return True
   
    for i in range(n):
  
        if is_valid(board, r, i):
            
            board[r][i] = 1
            print(board , "\n")
           
            if q(board, r + 1) == True:
                return True
                
            board[r][i] = 0
  
    return False





q(a,0)

    
    
