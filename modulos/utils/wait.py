import time
import random as r

def pausa(min = 0, max =0.4):
    #Realiza una pausa durante un tiempo aleatorio
    time.sleep(r.uniform(min,max))