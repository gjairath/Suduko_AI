from utility import *


# Variables taken from utility file: 
#	myDict: Dictionary with box:value mapping
# 	rows: Each row is laballed A through I. 9 rows in total.
#   cols: Each coloumn is laballed 1 through 9. 9 coloums in total.
#   boxes: A cross of A1 .... I9. 81 items in total 9x9 matrix.


# Below are helper values.
rowUnits = [cross(r, cols) for r in rows] 
colUnits = [cross(rows, c) for c in cols]
squareUnits = [cross(r, c) for r in ['ABC', 'DEF', 'GHI'] for c in ['123', '456', '789']]

unitList = rowUnits + colUnits + squareUnits # The units that make up a box

#this unit list will be used to extract it for specific requirements
unit = extract_unit(unitList, boxes)
peers = extract_peers(unit, boxes)

 
 
def eliminate_puzzle(values):
	# If a box has one value, remove it from the rows, coloumns and squares.
	
	# Argument: values or myDict. Box:Value mapping.
	# Returns: values, the same dictionary, modified.
	
	for box in boxes:
		if len(values[box]) == 1:
			constrainedValue = values[box]
			for item in peers[box]:
				if len(values[item]) != 1:
					values[item] = values[item].replace(constrainedValue, '')
	return values	

def only_one_choice(values):
	
	# If a box contains a value unique to its peers, prune it.
	
	# Arguments: values, myDict.
	# Returns: modified dictionary.

    for unit in unitList:
	    for digit in '123456789':
	        someList = []
	        for box in unit:
	            if digit in values[box]:
	                someList.append(box)
	        if (len(someList) == 1):
	               values[someList[0]] = digit
    return values
    
    
def reduce_puzzle(values):
	
	# Reduce the puzzle using the above two helper functions.
	# Ensure it does not get caught in infinite loop.
	
    isStalled = False
    while not isStalled:
        solvedBefore = len([box for box in values.keys() if len(values[box]) == 1])
        values = eliminate_puzzle(values)
        values = only_one_choice(values)

        solvedAfter = len([box for box in values.keys() if len(values[box]) == 1])

        isStalled = solvedBefore == solvedAfter

        if len([box for box in values.keys() if len(values[box]) == 0]):
            return False
    return values
	
def sanityCheck(values, unitType):
	
	# Debugger function to ensure DFS is not producing wrong output.
	# Very useful to ensure that the answer is correct for more difficult puzzles.
	
	# Arguments: values, myDict.
	#			 unitType, the type of unit, row/coloumn/square.
	
	# Returns: Bool 
	
	for item in unitType:
		emptySet = set()
		for box in item:
			emptySet.add(values[box])
		if (len(emptySet) != 9):
			return False
		#print(emptySet)
	return True
		
		
def search(values):

	# TODO: Check how to sanity check the DFS OUTPUT
	#		Ensure that the output is correct at the end.

	# 		if (values['A2'] == values['A8'] or values['G9'] == values['H9']):
	#		This is fucking stupid lol
	
	values = reduce_puzzle(values) # reduce the puzzle for easier search
	

	if values is False: # no possible solution, iterate through the rest, BACKTRACK alert.
		print('No Solution Found!')
		return False
	
	if all(len(values[s]) == 1 for s in boxes):
		truthClause = sanityCheck(values, rowUnits)
		truthClause2 = sanityCheck(values, colUnits)
		truthClause3 = sanityCheck(values, squareUnits)
		if truthClause is False or truthClause2 is False or truthClause3 is False:
			return False
		print('\nSanity Checks have passed for a Normal Suduko Game')
		return values
		
	n,s = min((len(values[s]), s) for s in boxes if len(values[s]) > 1)
	
	for item in values[s]:
		print('Trying Possible Attempt!')
		copiedValues = values.copy() #deep copy
		copiedValues[s] = item
		attemptedSearch = search(copiedValues)
		if attemptedSearch:
			return attemptedSearch
	
# Main
myDict = search(myDict)
print('\n\nSolution:\n')

display(myDict)

