import math
import random
import turtle

import numpy


def population(populationSz):
    """
    This function will generate population
    of chromosomes as per populationSz

    :type populationSz: int
    """
    l1 = [i for i in range(1, populationSz + 1)]
    random.shuffle(l1)
    return l1


def selection(total_population, percentage):
    """
    This method will select top most fit
    candidates or population as per percentage provided
    :param total_population: Total list of chromosome
    :param percentage: Top fit percentage to retain
    :return: sub list to most fit population
    """
    return total_population[:math.ceil(len(total_population) * percentage)]


def fitness(chromosome, sz):
    """
    Returns Fitness of each chromosome
    where 0 means chromosome is fittest

    :param chromosome: list containing chromosome
    :param sz: size of chromosome
    :return: int
    """
    ctr1 = 0
    ctr2 = 0
    f1 = []
    f2 = []
    for i in range(sz):
        f1.append(chromosome[i] - (i + 1))
        f2.append(sz - chromosome[i] - (i + 1))
    list.sort(f1)
    list.sort(f2)
    for i in range(1, sz):
        if f1[i] == f1[i - 1]:
            ctr1 += 1
        if f2[i] == f2[i - 1]:
            ctr2 += 1
    return ctr1 + ctr2


def crossover(p1: list, p2: list) -> tuple:
    """
    Takes in 2 chromosomes and preforms a
    crossover between them
    :param p1: chromosome 1
    :param p2: chromosome 2
    :return: tuple
    """
    sz = len(p1)
    child1 = []
    child2 = []
    for i in range(sz):
        child1.append(-1)
        child2.append(-1)
    pt1 = random.randint(0, sz - 1)
    pt2 = getAnotherPoint(pt1, sz)
    if pt1 > pt2:
        tmp = pt1
        pt1 = pt2
        pt2 = tmp
    for i in range(pt1, pt2):
        child1[i] = p1[i]
        child2[i] = p2[i]
    child1 = fillEmpty(child1, p2)
    child2 = fillEmpty(child2, p1)
    return child1, child2


def getAnotherPoint(pt1, sz):
    """
    Returning a random point different
    from pt1 based on range 0 to sz
    :rtype: int
    """
    pt2 = random.randint(1, sz - 1)
    if pt2 != pt1:
        return pt2
    else:
        return getAnotherPoint(pt1, sz)


def fillEmpty(child, parent):
    """
    This function is a helper for
    crossover as it fills all the empty
    slots in child chromosomes (in our case -1)
    with values of parent which are not present in child
    :param child: list
    :param parent: list
    :return: list
    """
    childSz = len(child)
    sz = len(parent)
    for i in range(childSz):
        for j in range(sz):
            if child[i] == -1 and (parent[j] not in child):
                child[i] = parent[j]
    return child


def mutation(chromosome, factor):
    """
    Changes the chromosome by
    swapping the indexes of element
    if a random number is greater than
    mutation factor
    :param chromosome: list
    :param factor: float
    :return: list
    """
    number = random.uniform(0, 1)
    if number >= factor:
        rand1 = random.randint(0, len(chromosome) - 1)
        rand2 = random.randint(0, len(chromosome) - 1)
        if rand1 != rand2:
            tmp = chromosome[rand1]
            chromosome[rand1] = chromosome[rand2]
            chromosome[rand2] = tmp

    return chromosome


def nQueen(bordSize, totalPop, maxGeneration, totalItr=0, mutationFactor=0.5):
    """
    Main function to provide
    solution to n-queens
    :param mutationFactor: Mutation factor
    :param bordSize: Size of n x n board
    :param totalPop: starting point of populations
    :param maxGeneration: total number of recursions
    :param totalItr: current recursion number
    :return: list
    """
    if totalItr > maxGeneration:
        return "No solution found after generation %d"%totalItr
    totalItr += 1
    fitnessValues = []
    for j in range(len(totalPop)):
        fitValue = fitness(totalPop[j], bordSize)
        if fitValue == 0:
            print("Got solution in generation " + str(totalItr))
            return totalPop[j]
        fitnessValues.append(fitValue)
    populationFitness = list(zip(fitnessValues, totalPop))
    populationFitness.sort(key=lambda x: x[0])
    newRange = math.ceil(math.sqrt(len(totalPop)))
    if newRange < 2:
        return "No solution found"
    topFitPopulation = []
    for j in range(newRange):
        if len(populationFitness) >= j:
            topFitPopulation.append(populationFitness[j])
    topFitPopulation = list(zip(topFitPopulation[::2], topFitPopulation[1::2]))
    finalPopulation = []
    for topPair in topFitPopulation:
        child1, child2 = crossover(topPair[0][1], topPair[1][1])
        child1 = mutation(child1, mutationFactor)
        child2 = mutation(child2, mutationFactor)
        finalPopulation.append(child1)
        finalPopulation.append(child2)
    return nQueen(bordSize, finalPopulation, maxGeneration, totalItr)


def draw_box(t, x, y, size, fill_color):
    """
    Helper method to draw chess
    board
    Source: https://www.quickprogrammingtips.com/python/python-program-to-draw-a-square-and-chess-board-using-turtle.html
    """
    t.penup()  # no drawing!
    t.goto(x, y)  # move the pen to a different position
    t.pendown()  # resume drawing

    t.fillcolor(fill_color)
    t.begin_fill()  # Shape drawn after this will be filled with this color!

    for i in range(0, 4):
        board.forward(size)  # move forward
        board.right(90)  # turn pen right 90 degrees

    t.end_fill()  # Go ahead and fill the rectangle!


def draw_chess_board(bordSz, solvedBoard):
    """
    Helper method to draw chess
    board modified for our problem
    Original Source: https://www.quickprogrammingtips.com/python/python-program-to-draw-a-square-and-chess-board-using-turtle.html
    """
    square_color = "black"  # first chess board square is black
    start_x = 0  # starting x position of the chess board
    start_y = 0  # starting y position of the chess board
    box_size = 30  # pixel size of each square in the chess board
    for i in range(0, bordSz):  # bordSz x bordSz chess board
        for j in range(0, bordSz):
            if solvedBoard[i][j] != 1:
                draw_box(board, start_x + j * box_size, start_y + i * box_size, box_size, square_color)
            else:
                draw_box(board, start_x + j * box_size, start_y + i * box_size, box_size, 'green')
            square_color = 'black' if square_color == 'white' else 'white'  # toggle after a column
        square_color = 'black' if square_color == 'white' else 'white'  # toggle after a row!


populationSize = 8
totalPopulation = []
n = 8
for ielem in range(populationSize):
    totalPopulation.append(population(n))

itrs = 0
solvedQueens = nQueen(n, totalPopulation, 1000, itrs)
if isinstance(solvedQueens, str):
    print(solvedQueens)
    exit(0)
print(solvedQueens)
solved_2d_array = numpy.zeros((n, n))
for ielem in range(n):
    solved_2d_array[ielem][solvedQueens[ielem] - 1] = 1

print(solved_2d_array)
# Comment the following code to stop the animation
board = turtle.Turtle()
board.speed(0)
draw_chess_board(n, solved_2d_array)
turtle.done()
