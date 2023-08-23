# n Queens Problem 

In this folder, you will find the solution for the classical n Queens Problem which was first proposed by the German chess enthusiast Max Bezzel for the standard 8*8 board.
Also solution of this problem is attached as a c++ code file.

# Problem statement 

You have to place n queens on a n*n chessboard so that no two queens are attacking each other, where n is a positive integer.
Here, this means that no two queens should be on the same row, same column or same diagonal.
We have to take the value of n as input and then we have to output a chess board with queens placed on squares so that it satisfies the above condition.

# Logic of the solution

We can do this problem with the concept of recursion.
So to solve this problem we will simply place a queen one by one on a row where it can be placed and then with all the posibility of placing that in the row we will again call the function to place another queen and if we find that that particular position for the queen is not possible for that row then we will not recall it because then we will be sure that it is going to break the rules. So here as you can see that the positions of a queen in a row totally depends on the previous positions of queen which we have placed previously. So recursion tree of this recursion will look like below. (Given tree is for 4*4 chess board)



Now, we will make a funciton which will tell us that if the positions of queens which we have given to the function as input is valid or not (acccording to the conditions of problem statement).
