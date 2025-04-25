# the 8 queen probem is a classic problem in which we have to place 8 queens on a chess board such that no two queens are attacking each other.

#we can solve the problem by python
#first step is to create a chess board by using numpy

# import numpy as np#numpy is a library in python which is used for mathematical operations
# chessboard = np.zeros((8,8))#np.zeros is used to create a matrix of 8*8 with all elementds as 0

#in this problem we have to follow some constraints
#1. each row should have only one queen
#2. each column should have only one queen
#3. no queens are attacking each other

#so the first step is to check whether the queen can be placed in the given position or not


# def is_safe(chessboard,row,col):
#     for i in range(8):#this loop is used to check whether the queen can be placed in the given position or not
#         if chessboard[i][col]==1:#this condition is used to check whether the queen is already placed in the given column
#             return False
#         if chessboard[row][i]==1:#this condition is used to check whether the queen is already placed in the given row
#             return False
#     for i in range(8):#this loop is used to check whether the queen can be placed in the given position or not
#         for j in range(8):
#             if i+j==row+col or i-j==row-col:#this condition is used to check whether the queen is attacking each other or not
#                 if chessboard[i][j]==1:
#                     return False
#     return True


import numpy as np


cb = np.zeros((8,8))


def safe(num):



    


