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


void *client_function(void *ptr) {
	
	;

	// Initialize hardware
	if (!elev_init()) {
		printf(__FILE__ ": Unable to initialize elevator hardware.\n");
		exit (1);
	}
	
	
	//Fyll Q med -1.	
	initQ();
	
	initInternalOrdersQ();
	
	initButtonQ();
	
	initBackupQ();
	
	initButtonLamp(0);
		
	obstruction = 0;
	
	stop = 0;

	print();
	
	initElevator();
	
	pthread_exit(NULL);
	
}


/*








*/

/*

makeTempQ
initQ
listen()
if (buttonPushed) {
	addToTempQ
	separateInternalExternalOrders
	send(externalOrders)
	addInternalToQ
}
if(newOrderFromServer){
	addToQ
}
while(Q) {
	executeOrder
	sendOrderCompleted
}

*/
