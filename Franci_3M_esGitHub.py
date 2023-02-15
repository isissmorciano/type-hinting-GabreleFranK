import random
#Franci Gabriele
#Es1
def descrizione(nome, eta):
    return f"{nome} ha {eta} anni."
print(descrizione("Pippo", 23))
#Es2
def numero_casuale():
    return random.randint(0, 99)
print(numero_casuale())
#Es3
def descrizione_eta_casuale(nome):
    eta = str(random.randint(1, 100))
    return nome + " ha " + eta + " anni"
print(descrizione_eta_casuale("Pippo"))

