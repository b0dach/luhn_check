#!/usr/bin/python
 
import os
import sys
import string

class bcolors:
                BLUE = '\033[94m'
                GREEN = '\033[92m'
                YELLOW = '\033[93m'
                RED = '\033[91m'
		ENDC = '\033[0m'

def disable(self):
                        self.BLUE = ''
                        self.GREEN = ''
                        self.YELLOW = ''
                        self.RED = ''
			self.ENDC = ''


#################################################
#       Writen by Jamie Murdock 'b0dach'        #
#       --Credit Card number Luhn Check--       #
#       Checks to see if numbers in a           #
#       file or single input are valid          #
#       credit card numbers                     #
#################################################


#	Luhn check algorithm

def luhn_checksum(card_number):
    def digits_of(n):
        return [int(d) for d in str(n)]
    digits = digits_of(card_number)
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    checksum = 0
    checksum += sum(odd_digits)
    for d in even_digits:
        checksum += sum(digits_of(d*2))
    return checksum % 10
 
def is_luhn_valid(card_number):
    return luhn_checksum(card_number) == 0


#	Menu
os.system('clear')

print bcolors.BLUE +  """
-------------------------------------------------
|       --Credit Card Number Luhn Check --      |
|	       	         			|
-------------------------------------------------
|       Writen by Jamie Murdock 'b0dach'        |
|       Checks to see if numbers in a           |
|       file or single input are valid          |
|       credit card numbers                     |
-------------------------------------------------
""" + bcolors.ENDC

print """

Do you want to:
1. Enter the location and file of the list (i.e. /tmp/cards.csv)
2. Enter a single number to evaluate

* Press any other key to exit *

Please enter your selection:
"""

menu_choice = (raw_input(""))

#	Evaluate numbers in a file

if menu_choice == '1':
	try:
	# menu_1 was input
		input=raw_input("please enter the full path of the csv file: ")
		with open (input, "r") as file:
			lines=file.read().replace('\r', '\n')
			lines=string.split(lines, '\n')
		print "Do you want to save the results to a file in the current directory?"
		menu_2 = (raw_input(""))

		if menu_2 == "y" or menu_2 == "Y" or menu_2 == "Yes" or menu_2 == "yes":

				output_name=raw_input("What do you want the output file to be named? ")
				output=open(output_name,"w")
				for line in lines:
                    			card=line.strip()
                                	if len(card)>=12 and len(card)<=19:
                                        		last4=card[len(card)-4:]
                                        		first6=card[0:6]
							print " "
							if is_luhn_valid(card):
                                				print first6+"xxxxxx"+last4+"   "+bcolors.RED+"Valid card number" +bcolors.ENDC
                                				output.write(first6+"xxxxxx"+last4+"   " +"Valid card number"+"\n")
							else:
                                				print first6+"xxxxxx"+last4+"   " +bcolors.GREEN+"Not a valid card number"+bcolors.ENDC
                                				output.write(first6+"xxxxxx"+last4+"   " +"Not a valid card number"+"\n")
				print " "
	        		print "Results have been saved to "+output_name

		else:
			for line in lines:
				card=line.strip()
				if len(card)>=12 and len(card)<=19:
					last4=card[len(card)-4:]
					first6=card[0:6]
					print " "
				if is_luhn_valid(card):
                                	print first6+"xxxxxx"+last4+"   "+bcolors.RED+"Valid card number" +bcolors.ENDC
                        	else:
                                	print first6+"xxxxxx"+last4+"   " +bcolors.GREEN+"Not a valid card number"+bcolors.ENDC
				
        except Exception, error:
                print bcolors.RED + "\n\n Something went wrong, printing the error: "+ str(error) + bcolors.ENDC

#	Evaluate single number

if menu_choice == '2':
		card=raw_input (bcolors.GREEN + "Please enter the card number: " + bcolors.ENDC)
		valid=card.isdigit ()
		if (valid == False):
			print "Please enter numbers only"
#		else:

		if len(card)>=12 and len(card)<=19:
			last4=card[len(card)-4:]
			first6=card[0:6]
			print " "
			if is_luhn_valid(card):
				print first6+"xxxxxx"+last4+"   "+bcolors.RED+"Valid card number" +bcolors.ENDC
			else:
				print first6+"xxxxxx"+last4+"   " +bcolors.GREEN+"Not a valid card number"+bcolors.ENDC
		else:
			print bcolors.RED + "Credit card numbers must be 12 and 19 digits." + bcolors.ENDC

#	press any key to continue function


exit=raw_input('Press Enter to exit')

os.system('clear')
