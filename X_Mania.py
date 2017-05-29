#!/usr/bin/env python

#Import the GPIO and time package
import RPi.GPIO as GPIO
import time
import random

#Vars for Raspberry Pins
pin_red = 7
pin_green = 11
pin_blue = 13


#Initiate GPIO Outputs
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)

#Function for Activating LED
def activateLED(pin):

	for x in range(3):
		GPIO.output(pin, GPIO.HIGH)
		time.sleep(1)
        	GPIO.output(pin, GPIO.LOW)	
        	time.sleep(1)



#Vars for Question Totals
n_right = 0
n_wrong = 0

#Ask Students Questions
for q in range(5):

	n_mplr1 = random.randint(1,10)
	n_mplr2 = random.randint(1,15)
        n_correct = n_mplr1 * n_mplr2

	s_question = "What does " + str(n_mplr1) + " x " + str(n_mplr2) + " = "
        
        print('')
        n_answer = int(input(s_question))

	if n_answer == n_correct:
		n_right += 1
		activateLED(pin_green)
	
	else:
		n_wrong += 1
		activateLED(pin_red)




#Display Question Summary
print('')
print('')

print("Number Correct: " + str(n_right))
print('')
print("Number Incorrect: " + str(n_wrong))

print('')
print('')


#Reward the Big Dawgs
if n_right > n_wrong:
	
	activateLED(pin_blue)

       

#Clean Up GPIO assignments 
GPIO.cleanup()



