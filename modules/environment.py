import os

#Recupera tutte le variabili d'ambiente impostate sulla macchina remota
def run(**args):
	print "[*] In environment module"

	return str(os.environ)
