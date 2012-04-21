from driver import *
from time import sleep
from channels import *

def m(floor):
	"""
	moves the elevator to the designated floor. 
	"""
	if driver.getCurrentFloor>floor:
		direction = 0
	else:
		direction = 1
	print "move"
	driver.move(direction, 250)
	while 1:
		if driver.getCurrentFloor()==floor:
			driver.stop()
			driver.setFloorIndicator(driver.getCurrentFloor())
			break
	print "move complete"	

def commandButtonsListenersInitiation():
    for light in OUTPUT.IN_LIGHTS:
        driver.setChannel(light, 0)
    for button in INPUT.IN_BUTTONS:
        driver.addListener(button, driver.setCommandButton, listento=None)

commandButtonsListenersInitiation()

"""

    MOTOR_UP       = 0
    MOTOR_DOWN     = 1

print "dang"
driver.move(0, 100)
while 1:
	if driver.getCurrentFloor()==4:
		driver.move(0, 0)
		driver.setFloorIndicator(driver.getCurrentFloor())
		break
"""

driver.stop()
m(3)

#    driver.getAccordingLight(INPUT.IN_BUTTONS, 3)
print driver.channelToFloor(driver.getAccordingLight(INPUT.IN_BUTTONS, 3))[0]
driver.setFloorIndicator(2)
print driver.channelToFloor(driver.getAccordingLight(INPUT.IN_BUTTONS, driver.getCurrentFloor()))[0]




#stops the elvator. 
driver.move(0,0)
driver.stop()
print "done"



