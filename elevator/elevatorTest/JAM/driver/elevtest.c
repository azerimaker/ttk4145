// Test functions for libComedi Elevator control. Connects all buttons and
// lights. Can be used for testing an elevator, or as an example of use of the
// drivers.
//
// 2008 Martin Korsgaard

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <assert.h>
#include <time.h>
#include <unistd.h>
#include <signal.h>
#include <string.h>
#include <assert.h>
#include <pthread.h>

#include "elev.h"


void prioritize(int possition);

order emptyOrder = {-1, -1, -1};

int elevatorNumber = 0;

void addToQ(int floor, int dir){
	
	int i;
	order thisOrder;
	for(i = 0; i < N_Q; i++){
		if((Q[i].floor == floor) && (Q[i].dir == dir)){
			break;
		}
		
		if ((floor == currentFloor) && (state == OPEN_STATE)) {
			if (dir == 2)
				internalOrdersQ[floor] = 0;
			break;
		}
		
		if(Q[i].floor != -1){
			continue;
		}
		
		else {
			thisOrder.floor = floor;
			thisOrder.dir = dir;
			thisOrder.elevNr = elevatorNumber;
			Q[i] = thisOrder;
			if (dir == 2)
				elev_set_button_lamp(dir, floor, 1);
			break;
			
		
		}
	}
}

void addToButtonQ(int floor, int dir) {
	
	if (dir == 0) 
		buttonUpQ[floor] = 1;
	
	if (dir == 1) {
		if (floor == 3)
			buttonDownQ[0] = 1;
		if (floor == 2)
			buttonDownQ[1] = 1;
		if (floor == 1)
			buttonDownQ[2] = 1;
	}
}

void print() {
	
	int i = 1, j = 0, k = 0, l = 0;
	
	
	printf("\nN_Q = %i", N_Q);
	
	printf("\nOrder nr: \t");
	while (i < N_Q + 1) {
		printf("%i\t", i);
		i++;
	}
	
	printf("\nFloor nr: \t");
	while (j < N_Q) {
		printf("%i\t", Q[j].floor);
		j++;
	}
	
	printf("\nDir: \t\t");
	while (k < N_Q) {
		printf("%i\t", Q[k].dir);
		k++;
	}
	
	printf("\nElevator nr: \t");
	while (l < N_Q) {
		printf("%i\t", Q[l].elevNr);
		l++;
	}
	printf("\nstate = %i\n", state);
	
	printf("buttonUpQ = %i, %i, %i\n", buttonUpQ[0], buttonUpQ[1], buttonUpQ[2]);
	printf("buttonDownQ = %i, %i, %i\n", buttonDownQ[0], buttonDownQ[1], buttonDownQ[2]);
	printf("elevatorStates = %i\n", elevatorStates[0]);
	printf("elevatorPositions = %i\n", elevatorPositions[0]);
	
	printf("\n\n------------------ Backuporders ------------------\n\n");
	printf("\nOrder nr: \t");
	
	i = 1;
	j = 0;
	k = 0;
	l = 0;
	
	while (i < N_Q + 1) {
		printf("%i\t", i);
		i++;
	}
	
	printf("\nFloor nr: \t");
	while (j < N_Q) {
		printf("%i\t", backupQ[j].floor);
		j++;
	}
	
	printf("\nDir: \t\t");
	while (k < N_Q) {
		printf("%i\t", backupQ[k].dir);
		k++;
	}
	
	printf("\nElevator nr: \t");
	while (l < N_Q) {
		printf("%i\t", backupQ[l].elevNr);
		l++;
	}

	printf("\n\n");
		
	
}

/*
 * Dir inne = 2
 * Dir opp = 0
 * Dir ned = 1
 * 
 */

void checkPriority() {
	
	
	
	int i = 0;
	
	print();
	printf("Checking Priority!\nN_Q = %i\ncurrentFloor = %i\n", N_Q, currentFloor);
	
	while (i < N_Q) {
		
		
		if (((state == UP_STATE) && (Q[i].dir == 2) && (Q[i].floor < currentOrder.floor) && (Q[i].floor > currentFloor)) ||
			((state == DOWN_STATE) && (Q[i].dir == 2) && (Q[i].floor > currentOrder.floor) && (Q[i].floor < currentFloor)))
		{
			printf("prioritizing number %i in Q\n", i);
			prioritize(i);
		}	
		
		i++;
	}
}

void prioritize(int possition) {
	
	order temp;
	
	int i = 0, j = possition;
	
	while (i < possition) {
		temp = Q[j-1];
		Q[j-1] = Q[j];
		Q[j] = temp;
		i++;
		j = j-1;
		
		
		
	}
	currentOrder = Q[0];
	print();
	
}

void orderCompleted(int order) {
	
	int i = 0, m = 0;
	
	int ordersForSameFloor[N_BUTTONS];
	
	for (int j = 0; j < N_Q; j++) {
		if (Q[j].floor == Q[order].floor) {
			ordersForSameFloor[m] = j;
			m++;
		}
	}
	
	printf("ordersForSameFloor = %i, %i, %i\n", ordersForSameFloor[0], ordersForSameFloor[1], ordersForSameFloor[2]);
	
	
	for (int k = m-1; k >= 0; k--){
		i = ordersForSameFloor[k];
		if (Q[i].dir == 2) {
			internalOrdersQ[Q[i].floor] = 0;
			elev_set_button_lamp(Q[i].dir, Q[i].floor, 0);
		}
		while (i < N_Q) {
			Q[i] = Q[i+1];
			i++;	
		}
		Q[N_Q - 1] = emptyOrder;
	}
	
	print();
	
}


char* arrayToString(char* n, char* dest) {
    
    char temp[100];
    char temp2[100];
    char temp3[100];
    char orderString[ORDER_STRING_SIZE];
    char stateString[STATE_STRING_SIZE];
    char backupString[BACKUP_STRING_SIZE];
    char emptyString[20] = "-empty";
   
  
    int i = 0;
    
    if (strcmp(n, "u") == 0) {
    	
    	strcpy(orderString, n);
    	i = 0;
    	while (i < 3) {
    		sprintf(temp, "%d", buttonUpQ[i]);
    		strcat(orderString, temp);        
    		strcpy(dest, orderString);
    		i++;
    	}
    	
    	return dest;
    }
    
    if (strcmp(n, "d") == 0) {
    	strcpy(orderString, n);
		i = 0;
		while (i < 3) {
			sprintf(temp, "%d", buttonDownQ[i]);
			strcat(orderString, temp); 
			strcpy(dest, orderString);
			i++;
		}
		
		return dest;

    	
    }
    
    if (strcmp(n, "s") == 0) {
    	strcpy(stateString, n);
		sprintf(temp, "%d", state);
		strcat(stateString, temp);
		sprintf(temp, "%d", currentFloor);
		strcat(stateString, temp);
		sprintf(temp, "%d", elevatorNumber);
		strcat(stateString, temp);
		strcpy(dest, stateString);
		return dest;

    }
    
    if (strcmp(n, "b") == 0) {
		
    	strcpy(backupString, n);
    	i = 0;
		
    	if (Q[0].floor == -1) {
    		strcat(backupString, emptyString);
    		strcpy(dest, backupString);
    		return dest;    		
    	}
    	
    	
    	strcpy(temp, "\0");
		while (i < N_Q) {
			if (Q[i].floor == -1)
				break;
			sprintf(temp, "%d", Q[i].floor);
			strcat(backupString, temp);        
			i++;
		};
		
		strcat(backupString, "n");
		i = 0;
		
		strcpy(temp2, "\0");
		while (i < N_Q) {
			if (Q[i].dir == -1)
				break;
			sprintf(temp2,"%d", Q[i].dir);
			strcat(backupString, temp2);
			assert(!(i > 12 || i < 0));
			i++;
		};

		strcat(backupString, "n");
		i = 0;
		
		strcpy(temp3, "\0");
		while (i < N_Q) {
			if (Q[i].elevNr == -1)
				break;
			sprintf(temp3, "%d", Q[i].elevNr);
			strcat(backupString, temp3);
			i++;
		};
		
		strcat(backupString, "n");
		
		strcpy(dest, backupString);
		
		return dest;
	}
    
    else {
    	printf("Error: arrayToString input is: %s. Must be  u, d or s\n", n);
    	return NULL;
    }
    	
    
}

void stringToArray(char* src) {
    
	int i = 0, m = 1; 
	
	
	
	char temp[BACKUP_STRING_SIZE];
	
	strcpy(temp, src);

    if (strncmp(temp,"u", 1) == 0) {
    	i = 0;
    	m = 1;
    	while (m < ORDER_STRING_SIZE) {
    		buttonUpQ[i] = src[m] - '0';
    		i++;
    		m++;
    	}
    	

    	return;
  
    }
    
    if (strncmp(temp,"d", 1) == 0) {
    	i = 0;
		m = 1;
		while (m < ORDER_STRING_SIZE) {
			buttonDownQ[i] = src[m] - '0';
			i++;
			m++;
		}
		return;
	}
    
    if (strncmp(temp,"s", 1) == 0) {
    	i = src[3] - '0';
    	elevatorStates[i] = src[1] - '0';
    	elevatorPositions[i] = src[2] - '0';
    	return;
    }
	
    
    if (strncmp(temp,"b", 1) == 0) {
    	i = 0;
       	
    	if (strcmp(temp, "b-empty") == 0) {
			for (i = 0;i < N_Q; i++) {
				backupQ[i] = emptyOrder; 
			}
			return;
    	}
    		
		i = 0;
		
	
		m = 1;
		while ((char)src[m] != 'n') {
			backupQ[i].floor = src[m] - '0';
			m++;
			i++;
				
        }
        
		
        while (i < N_Q ) {
            backupQ[i].floor = -1;
			i++;
			}
    
		m++;
		i = 0;
		
		while ((char)src[m] != 'n') {
			backupQ[i].dir = src[m] - '0';
			m++;
			i++;
				
		}
		
		
		while (i < N_Q ) {
			backupQ[i].dir = -1;
			i++;
			}
	
		m++;
		i = 0;
		
		while ((char)src[m] != 'n') {
			backupQ[i].elevNr = src[m] - '0';
			m++;
			i++;
		}
		
		while (i < N_Q ) {
			backupQ[i].elevNr = -1;
			i++;
			}
		return;
    }
 
    else {
    	printf("Error: stringToArray input src[0] is: %c. Must be  u, d, s or b\n", src[0]);
    	return;
    } 
 }

void mergeOrders() {
	initQ();
	int i = 0;
	while (backupQ[i].floor != -1) {
		if (backupQ[i].elevNr == elevatorNumber) {
			addToQ(backupQ[i].floor, backupQ[i].dir);
		}
		i++;
	}
	
	i = 0;
	
	while (i < 4) {
		if (internalOrdersQ[i] == 1)
			addToQ(i, 2);
		i++;
	}
	setButtonLamps();
	checkPriority();
}

void setButtonLamps() {
	int i = 0;
	initButtonLamp(1);
	while (backupQ[i].floor != -1) {
		elev_set_button_lamp(backupQ[i].dir, backupQ[i].floor, 1);
		i++;
	}
	
	
}


void addReceivedOrders() {
	int i = 0;
	while (i < 3) {
		if (buttonUpQ[i] == 1) {
			addToQ(i, 0);
		}
		if (buttonDownQ[i] == 1) {
			if (i == 0) {
				addToQ(3, 1);
			}
			if (i == 1) {
				addToQ(2, 1);
			}
			if (i == 2) {
				addToQ(1, 1);
			}
		}
		i++;
	}
}

void send(char* src){
	
	char temp[BACKUP_STRING_SIZE];
	strcpy(temp, src);
	
	printf("String in send function: %s\n", temp);
	
	
}


// Callback function that handles the elevator reaching a floor
static void signal_floor_sensor(int floor, int value)
{
    elev_set_floor_indicator(floor);
    currentFloor = floor;
    printf("Current floor = %i\n", currentFloor);
    if (state == UP_STATE)
    	nextFloor = floor + 1;
    if (state == DOWN_STATE)
    	nextFloor = floor - 1;
    printf("Next floor = %i\n", nextFloor);
    printf(__FILE__ ": Floor %d %s.\n", floor+1, value ? "arrive" : "depart");
}



// Callback for elevator buttons being pushed.
static void signal_button_pushed(int floor, int dir)
{
	if (dir == 2)
		internalOrdersQ[floor] = 1;
		
	else
		addToButtonQ(floor, dir);
	
	mergeOrders();

	printf(__FILE__ ": Button %s pushed for floor %d.\n", dir==0?"CALL UP":dir==1?"CALL DOWN":"COMMAND", floor+1);
}



// Callback for stop.
static void signal_stop(int dummy, int dummy2)
{
    static int lamp = 0;
    lamp ^= 1;
	elev_set_stop_lamp(lamp);
	stop = lamp;
	state = STOP_STATE;
	printf(__FILE__ ": Stop button pushed!\n");
}



// Callback for obstruction. Sets the stop lamp.
static void signal_obstruction(int dummy, int value)
{
    elev_set_door_open_lamp(value);
    obstruction = value;
	printf(__FILE__ ": Obstruction switch flipped!\n");
}


void ctrlc(int x)
{
    elev_set_speed(0);
    exit(0);
}


void initQ() {
	for (int i = 0; i < N_Q; i++){
		Q[i] = emptyOrder;
	}
}

void initBackupQ() {
	for (int i = 0; i < N_Q; i++){
			backupQ[i] = emptyOrder;
		}
}

void initButtonQ() {
	int i;
	for(i = 0; i < 3; i++) {
		buttonUpQ[i] = 0;
		buttonDownQ[i] = 0;
	}
}

void initInternalOrdersQ() {
	int i = 0;
	while (i < 4) {
		internalOrdersQ[i] = -1;
		i++;
	}
	
}


void initButtonLamp(int n) {
	
	elev_set_button_lamp(0, 0, 0);
	elev_set_button_lamp(0, 1, 0);
	elev_set_button_lamp(0, 2, 0);
	elev_set_button_lamp(1, 1, 0);
	elev_set_button_lamp(1, 2, 0);
	elev_set_button_lamp(1, 3, 0);
	if (n == 1)
		return;
	elev_set_button_lamp(2, 0, 0);
	elev_set_button_lamp(2, 1, 0);
	elev_set_button_lamp(2, 2, 0);
	elev_set_button_lamp(2, 3, 0);
	
}

int initElevator() {
	
	//Stopper heisen
    signal(SIGINT, ctrlc);

	elev_register_callback(SIGNAL_TYPE_CALL_UP, &signal_button_pushed);
	elev_register_callback(SIGNAL_TYPE_CALL_DOWN, &signal_button_pushed);
	elev_register_callback(SIGNAL_TYPE_COMMAND, &signal_button_pushed);
	elev_register_callback(SIGNAL_TYPE_SENSOR, &signal_floor_sensor);
	elev_register_callback(SIGNAL_TYPE_STOP, &signal_stop);
	elev_register_callback(SIGNAL_TYPE_OBSTR, &signal_obstruction);
	
	elev_reset_all_lamps();

    elev_set_speed(0);
    
    state = FREE_STATE;

    //Denne starter pollingtråden, slik at det leses hvilke signaler som blir sent inn.
	elev_enable_callbacks();
	
	

	// Loop endlessly. 
	while (1) ;

	
	return 0;
}

int main(int argc, char* argv[])
{
	if (argc < 2) {
		printf("\nFeil antal argument. Skriv: server eller client\n\n");
		exit(0);
	}
	
	if (strcmp(argv[1], "client") == 0) {
		pthread_create(&client_thread, NULL, client_function, NULL);
	}
	
	if (strcmp(argv[1], "server") == 0) {
		pthread_create(&server_thread, NULL, server_function, NULL);
	}
	
	
	pthread_exit(NULL);
	
}






