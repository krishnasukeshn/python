class Solution:
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """

    
        def solve(bo):
            pos = find_empty(bo)
            #print(pos)
            if not pos:
                #print("set true")
                return True
            for x in range(1,10):
                #print(x)
                #print("check is valid")
                #print(x)
                #print(pos)
                #print("check is valid end")
                if isValid(bo, str(x), pos):
                    #print("valid: " + str(x))
                    bo[pos[0]][pos[1]] = str(x)
                    #print_board(board)
                    #print("                                           ")
                    #print("___________________________________________")
                    #print("                                           ")
                    if solve(bo):
                        #print(bo)
                        return  True
                    bo[pos[0]][pos[1]] = '.'

            #print("set false")

            return False




        def find_empty(bo):
            for x in range(len(bo)):
                for y in range(len(bo[0])):
                    if bo[x][y] == '.':
                        return (x,y)
            return None

        def isValid(bo, num, pos):

            #check row
            for x in range(9):
                if bo[pos[0]][x] == num and x != pos[1]:
                    return False
            
            #check col
            for x in range(9):
                if bo[x][pos[1]] == num and x != pos[0]:
                    return False

            #check box
            box_x = int(pos[0]/3)
            box_y = int(pos[1]/3)
            #for x in range(int(pos[0]/3), int(pos[0]/3) + 3):
            for x in range(box_x*3 ,(box_x*3) + 3 ):
                #for y in range(int(pos[1]/3), int(pos[1]/3) + 3):
                for y in range(box_y*3 ,(box_y*3) + 3 ):
                    #print(str(x) + "  "+ str(y))
                    if bo[x][y] == num and x != pos[0] and y != pos[1]:
                        return False
            
            return True

        def print_board(bo):
            for i in range(len(bo)):
                if i % 3 == 0 and i != 0:
                    print("- - - - - - - - - - - - - ")

                for j in range(len(bo[0])):
                    if j % 3 == 0 and j != 0:
                        print(" | ", end="")

                    if j == 8:
                        print(bo[i][j])
                    else:
                        print(str(bo[i][j]) + " ", end="")
        

        ##print(find_empty(board))
        #print(isValid(board, "8", (0,5)))
        #print(board)        
        solve(board)
        #print(board)        

