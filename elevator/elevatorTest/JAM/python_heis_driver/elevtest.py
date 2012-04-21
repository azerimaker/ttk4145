int elevator_number = 0
Q = [0]*12
emptyorder = 

def addToQ(floor, direction):
	i
	order thisOrder
	for i in range(12):
		if Q[i].floor == floor and Q[i].direction == direction:
			break
		if floor == currentFloor and state == OPEN_STATE:
			if direction == 2
				internalOrdersQ[floor] = 0
			break
		if Q[i].floor != -1:
			continue
		else:
			thisOrder.floor = floor
			thisOrder.direction = direction
			thisOrder.elevNr = elevatorNumber
			Q[i] = thisOrder
			if direction == 2:
				elev_set_button_lamp(direction, floor, 1)
			break
			
def addToButtonQ(floor, direction):
	if direction == 0:
		buttonUpQ[floor] = 1
	if dir == 1:
		if floor == 3:
			buttonDownQ[0] = 1
		if floor == 2:
			buttonDownQ[1] = 1
		if floor == 1:
			buttonDownQ[2] = 1

def print_it():
	i = 1, j = 0, k = 0, l = 0
	
	print "\nN_Q = ", N_Q
	
	print "\nOrder nr: \t",
	while i < N_Q + 1:
		print i, "\t",
		i += 1
		
	print "\nFloor nr: \t"
	while j < N_Q:
		print Q[j].floor, "\t",
		j += 1
	
	print "\nDir: \t\t",
	while k < N_Q:
		print Q[k].direction, "\t",
		k += 1
	
	print "\nElevator nr: \t",
	while l < N_Q:
		print Q[l].elevNr, "\t",
	
	print "\nstate =", state, "\n"
	
	print "buttonUpQ = ", buttonUpQ[0], buttonUpQ[1], buttonUpQ[2]
	print "buttonDownQ = ", buttonDownQ[0], buttonDownQ[1], buttonDownQ[2]
	print "elevatorStates =", elevatorStates[0], "\n"
	print "elevatorPositions =", elevatorPositions[0], "\n"
	
	print "\n\n------------ BackupOrders -------------\n\n"
	print "\nOrder nr: \t"
	
	i = 1
	j = 0
	k = 0
	l = 0
	
	while i < N_Q + 1:
		print i, "\t"
		i += 1
	
	print "\nFloor nr: \t",
	while j < N_Q:
		print backupQ[j].floor, "\t"
		j += 1
	
	print "\nDir : \t\t",
	while k < N_Q:
		print backupQ[k].direction, "\t"
		k += 1
		
	print "\nElevator nr: \t",
	while l < N_Q:
		print backupQ[l].elevNr, "\t"
		l += 1
		
	print "\n\n"
	
	
def checkPriority():
	i = 0
	print_it()
	print "Checking Priority!\nN_Q = ", N_Q, "\ncurrentFloor = ", currentFloor, "\n"
	
	while i < N_Q:
		if (state == UP_STATE and Q[i].direction == 2 and Q[i].floor < currentOrder.floor and Q[i].floor > currentFloor) or (state == DOWN_STATE and Q[i].direction == 2 and Q[i].dir == 2 and Q[i].floor > currentOrder.floor and Q[i].floor < currentFloor):
			print "prioritizing number", i, "in Q\n"
			prioritize(i)
		i += 1
		

def prioritize(position):
	temp = ""
	i = 0, j = position
	while i < position:
		temp = Q[j-1]
		Q[j-1] = Q[j]
		Q[j] = temp
		i += 1
		j = j-1
		
	currentOrder = Q[0]
	print_it()
	
def orderCompleted(order):
	
	
	
	
	
	
	
	
		
