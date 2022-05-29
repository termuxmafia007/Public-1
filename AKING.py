import os
print(' \033[1;32m Welcome My Tolls\033[1;37m')
if __name__ == "__main__":
	try:
		__import__("Public").login()
	except Exception as e:
		exit(str(e))
