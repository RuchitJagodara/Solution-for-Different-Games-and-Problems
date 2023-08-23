# n Queens Problem 

In this folder, you will find the solution for the classical n Queens Problem which was first proposed by the German chess enthusiast Max Bezzel for the standard 8*8 board.
Also solution of this problem is attached as a c++ code file.

# Problem statement 

You have to place n queens on a n*n chessboard so that no two queens are attacking each other, where n is a positive integer.
Here, this means that no two queens should be on the same raw, same column or same diagonal.
We have to take the value of n as input and then we have to output a chess board with queens placed on squares so that it satisfies the above condition.

# Logic of the solution

We can do this problem with the concept of recursione.

So to solve this problem we will simply 

First of all we will make a funciton which will tell us that if the positions of queens which we have given to the function as input is valid or not (acccording to the conditions of problem statement).