from math import factorial as fact
import help
def perm(str):
	if len(str) < 2:
		help.helper("perm")
		return None
	total = int(str[1])
	pick = int(str[2])
	return fact(total)/fact(total-pick)

def combo(str):
	if len(str) < 2:
		help.helper("combo")
	total = int(str[1])
	pick = int(str[2])
	return fact(total)/(fact(pick)*fact(total-pick)) 
