#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <assert.h>
#include <time.h>
#include <unistd.h>
#include <signal.h>
#include <string.h>
#include <pthread.h>

#include "elev.h"

void *server_function(void *ptr) {
	
	printf("\n\nServer function is under construction....\n\n");
	
	exit(0);	
	
	
	/*
		receive();
		stringToArray()
		void addReceivedOrders();
		serverSort();
		
		char backupString[BACKUP_STRING_SIZE];
		printf("bUps: b = %s\n", arrayToString("b", backupString));
		send();
	
	
	*/
}





/*


void serverSort() {
	
	
	
	int i = 0;

	printf("\n\n################# Server #################\n\n");
	
	print();
	
	// finn andre bestillingar av same sort i Q, og sett inn nye i rett rekkefølge, slik som dei står i bUQ og bDQ.
	while (i < N_Q) {
		if ()
		
		
	}
}



// find the highest elevator, and dispatch the down orders to it. find the lowest elevator and dispatch the up orders to it.
dispatchOrders() {
	 
}

if (((state == UP_STATE) && (Q[i].dir == 0) && (currentOrder.dir != 1) && (Q[i].floor < currentOrder.floor) && (Q[i].floor > currentFloor)) ||
			((state == DOWN_STATE) && (Q[i].dir == 1) && (currentOrder.dir != 0) && (Q[i].floor > currentOrder.floor) && (Q[i].floor < currentFloor))) 
		{
			printf("prioritizing number %i in Q\n", i);
			prioritize(i);
		}	
		
		i++;



*/


/*

generate_Q
listen()
if (newOrder) {
	addToQ
	sort_Q
	dispatchOrders
	selectElevator
	send()
}
if (orderCompleted) {
	deleteOrder_from_Q
	sort_Q
}
if (timeout) {
	dispatchOrders
	selectElevator
	send()
}


*/