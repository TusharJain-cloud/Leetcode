class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows, columns = len(matrix), len(matrix[0])
        row_zero = False

        #Determine where to put zero.
        for r in range(rows):
            for c in range(columns):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        row_zero = True

        #Put zeros
        for r in range(1,rows):
            for c in range(1,columns):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0
            
        if matrix[0][0] == 0:
            for r in range(rows):
                matrix[r][0] = 0
        
        if row_zero:
            for c in range(columns):
                matrix[0][c] = 0

        

        