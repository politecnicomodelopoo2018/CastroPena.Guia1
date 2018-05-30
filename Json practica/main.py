from persona import *
import json

A = Ciudad()

d = {"personas":[]}

for item in A.lista_personas:

    d["personas"].append(item.senialidar())

f=open("Personas.json", "w")

f.write(json.dumps(d))
f.close()



f = open("Personas.json","r")

d = json.loads(f.read())

f.close()

for item in d["personas"]:
    UnaPersona=Persona()
    UnaPersona.desenializar(item)
    A.lista_personas.append(UnaPersona)
