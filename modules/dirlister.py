import os

#Ritorna tutti i file nella cartella
def run(**args):
	print "[*] In dirlister module"
	files = os.listdir(".")

	return str(files)
