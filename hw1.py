import sys
line = ""
for i in range(sys.argv[1]):



	print ("How long do you want the pyramid's base to be.")

	if sys.argv[1]=="-p":
		if (int)(sys.argv[2])%2 == 0:
			c = ' '
		else:
			c = '*'
			line += c
			print line

				else:
					print ("Python hw1.py [{-p int}]")
