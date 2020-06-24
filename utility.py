from collections import defaultdict

''' This is my attempt at doing this from scratch.
	Helper file for encoding the Suduko Board.
	
	The display function is borrowed from a course.
	This question was inspired from a course on AI and deep-learning       
'''

# Variables to encode the board. Rows are horizontal labels. I'm directionally impaired.
rows = 'ABCDEFGHI'
cols = '123456789'
boxes = [r + c for r in rows for c in cols]

def extract_unit(unitList, boxes):
# Extract the units, each box has respective units as per the game of Suduko.
# The rows, coloumns and squares in which each box are present.

# Argument: unitList, list that contains all the boxes in general.
#			boxes, all the squares.

# Returns:	Dictionary with units for each box.

	unitDict = defaultdict(list)
	for box in boxes:
		for item in unitList:
			if box in item:
				unitDict[box].append(item)
	return unitDict

def extract_peers(unit, boxes):
# Read extract_Unit.
# This encodes box:unit in dictionary form.
# unit is what extract_unit returns.

	peerDict = defaultdict(set) # to remove duplication
	for box in boxes:
		for item in unit[box]:
			for unitBoxes in item:
				peerDict[box].add(unitBoxes)
	return peerDict			



def cross(rows, cols):
# Refactor crossing code.
	return [r + c for r in rows for c in cols]


def generate_dictionary(grid, boxes):   
# Generate the key:Value mapping for boxes:values. I.e, A1 is the upper most top left box that may have '1' lets say.
# Grid is the string that holds the encoded table with 'x' or '.' representing an empty box.
# The output is the dictionary with Box:Number.
	dictionary = dict(zip(boxes,grid))
	for item in dictionary:
		if dictionary[item] == '.' or dictionary[item] == 'x':
			dictionary[item] = '123456789'
		else:
			dictionary[item] = dictionary[item]
	return dictionary



def display(values):


	width = 1+max(len(values[s]) for s in boxes)
	line = '+'.join(['-'*(width*3)]*3)
	for r in rows:
		print(''.join(values[r+c].center(width)+('|' if c in '36' else '')
					  for c in cols))
		if r in 'CF': print(line)
	print()

def menu():
# Menu to display all options.
# Has some basic test cases that were ranked "Evil" on many websites.
# Most of them were used extensively in debugging.

	print('\n')
	print ('\tMenu\t')
	print ('1 - Try test case 1')
	print ('2 - Try test case 2')
	print ('3 - Try a difficult test case!')
	print ('4 - Try out your own')
	print('\n')

	inputChoice = input('\n\nEnter your choice: ')
	print('\n\n')
	if (inputChoice == '1'):
		diag_sudoku_grid = '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
	elif (inputChoice == '2'):
		diag_sudoku_grid = '.8..1..7.7..6.3..5..4...3...4.2.1.3.8.......7.7.8.6.4...1...2..9..4.2..8.2..6..9.' 
	elif (inputChoice == '3'):
		diag_sudoku_grid = '1...5...4.4.6.7.5...3...1...8.5.1.6.6.......2.2.4.6.1...4...7...3.2.4.8.9...6...5'
	elif (inputChoice == '4'):
		diag_sudoku_grid = ''
		print('Enter the input in rows. If a box is empty, enter . \nFor example, if the first row has 1 in the first box and 0 in the last, enter 1........0')
		print('You can also use x to denote empty boxes.')
		for i in range (0,9):
			inputString = input('\n\nEnter the row: ')

			if (len(inputString) != 9):
				print('Something went wrong, not 9 values.')
				print('\n\tTry Again\n\n')
				exit()
			diag_sudoku_grid += inputString
	else:
		print('Invalid String, restart program')

	return diag_sudoku_grid

# Main
diag_sudoku_grid = menu()
myDict = generate_dictionary(diag_sudoku_grid, boxes)
display(myDict)
