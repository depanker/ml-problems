# ml-problems
Solving n-queens problem using GA

This implementation is based on solution provided in paper https://arxiv.org/pdf/1802.02006.pdf:


Following are the assumption and terminology used
1. For the sake of understanding we are taking an 8 queen problem
2. Encoding and 8 x 8 board is done using a list or size 8. [2,1,4,5,3,6,7,8]
3. In the above mentioned list index of the list denote the column number of chess board and value placed at the index denote row number
Explanation: [2,1,4,5,3,6,7,8] in this list first entry 2 placed in index 0 means that there is a queen place in second row and first column
4. Having unique number in the list means that there will not be two queens in same row or column
5. This list like this [2,1,4,5,3,6,7,8] will be referred in the code as chromosome
6. variable _n_ refers to  _n x n_ board so for 8 queens **n=8**
7. Size of population means number of chromosomes, it is referred as _totalPopulation_
8. Total recursion made _maxGeneration_

### Function used:
1. `def population(populationSz):` _generates random list of chromosome, size to list is equal to populationSz _
2. `def selection(total_population, percentage):` _This method will select top most fit candidates or population as per percentage provided, in the example this i not used, will update example_
3. `def fitness(chromosome, sz):`  _This determines fitness of a chromosome, in our case it return count of queens attacking each other, so chromosome with the fitness = 0 is the solution_
4. `def crossover(p1: list, p2: list) -> tuple` _return a new generation of two childrens, by crossing parent chromosome_
5. `def mutation(chromosome, factor)` _Changes the chromosome by swapping the indexes of element if a random number is greater than mutation factor_ in this example we took a mutation factor of 0.1
6. `def draw_box(t, x, y, size, fill_color) and  def draw_chess_board(bordSz, solvedBoard)` _This code is used to draw chess board, where Green squares represent placement of queens, these_

Liberaries used:
1. math, random  for core implementation
2. numpy to represent the solution in form of 2D matrix
3. turtle to draw chess board.

import 
Resources:
1. https://arxiv.org/pdf/1802.02006.pdf (used for creating an implementation of the problem)
2. https://www.quickprogrammingtips.com/python/python-program-to-draw-a-square-and-chess-board-using-turtle.html (used to draw chess board)
