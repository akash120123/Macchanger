import subprocess
import optparse
import re

def get_user_input():
	parse_object = optparse.OptionParser()
	parse_object.add_option("-i","--interface",dest="interface",help="Interface to change")
	parse_object.add_option("-m","--mac",dest="mac_address",help="New mac address")	
	return	parse_object.parse_args()

def mac_changer(user_interface,user_mac_address):
	try:	
		subprocess.call(["ifconfig",user_interface,"down"])
		subprocess.call(["ifconfig",user_interface,"hw","ether",user_mac_address])
		subprocess.call(["ifconfig",user_interface,"up"])
	except Exception as e:
		print(f"!!!!FAILED TO CHANGE THE MAC ADDRESS DUE TO ERROR: {e} !!!")


def mac_validater(interface):
	try:
		ifconfig = subprocess.check_output(["ifconfig",interface])
		new_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",str(ifconfig))
	
		if new_mac:
			return new_mac.group(0)
		else:
			return None
	except subprocess.CalledProcessError as e:
		print("!!! FAILED TO RUN ifconfig: {e} !!!")
		return None


print("---------Mac-changer-is-starting-----------")
try:
	(user_input,arguments) = get_user_input()
	mac_changer(user_input.interface,user_input.mac_address)
	finalized_mac = mac_validater(str(user_input.interface))

	if finalized_mac == user_input.mac_address:
		print("MAC ADDRESS CHANGED SUCCESSFULLY!")
	else:
		print("ERROR!!!!") 
 
except Exception as e:
	print("!!! ERROR OCCURE WHILE CHANGING MAC ADDRESS: {e}")
