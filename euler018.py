'''
Maximum path sum I
Problem 18
By starting at the top of the triangle below and moving to adjacent numbers on the row below, 
the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

              75
             95 64
            17 47 82
           18 35 87 10
          20 04 82 47 65
         19 01 23 75 03 34
        88 02 77 73 07 63 67
       99 65 04 28 06 16 70 92
      41 41 26 56 83 40 80 70 33
     41 48 72 33 47 32 37 16 94 29
    53 71 44 65 25 43 91 52 97 51 14
   70 11 33 28 77 73 17 78 39 68 17 57
  91 71 52 38 17 14 91 43 58 50 27 29 48
 63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route.
However, Problem 67, is the same challenge with a triangle containing one-hundred rows; it cannot be 
solved by brute force, and requires a clever method! ;o)


Ajuda: http://stackoverflow.com/questions/8002252/euler-project-18-approach
It's something called dynamic programming.

You have such triangle:

   3
  7 4
 2 4 6  
8 5 9 3
When you move from the bottom to the top, you can calculate the best choices on last iteration. In this case you take the last row 8 5 9 3 and maximize sum in addition to previous line.

Iteration 1: Assume that you are on last-1 step.

You have line 2 4 6 let iterate on it.

From 2, you can go to either 8 or 5, so 8 is better (maximize you result from 3) so you calculate first sum 8 + 2 = 10

From 4, you can go to either 5 or 9, so 9 is better (maximize you result from 4) so you calculate second sum 9 + 4 = 13

From 6, you can go to either 9 or 3, so 9 is better again (maximize you result from 6) so you calculate third sum 9 + 6 = 15

This is the end of first iteration and you got the line of sums 10 13 15.

Now you've got triangle of lower dimension:

    3
  7  4
10 13 15  
Now go on until you get one value, which is exactly 23.
'''
from time import time
start = time()

matriz = '''75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23'''

triangulo = []

matriz = list(matriz.split("\n"))
for x in matriz:
	triangulo.append(list(x.split(" ")))

i = 0
while i < len(triangulo):
	print(triangulo[i])
	i += 1

print("Time: {0} secs".format(time()-start))