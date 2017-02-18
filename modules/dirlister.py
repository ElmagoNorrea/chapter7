import os
def tommalo(**args):
	print "[*] In dirlister module."
	files = os.listdir(".")
	return str(files)

