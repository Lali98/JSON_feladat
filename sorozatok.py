import json

sorozatok = {"sorozatok": []}

file = open("lista.txt","r")
line = file.readline().strip()
folytat = True
while folytat:
    if line:
        sorozat = {}
        sorozat["datum"] = line
        line = file.readline().strip()
        sorozat["sorozat"] = line
        line = file.readline().strip()
        sorozat["epizod"] = line
        line = file.readline().strip()
        sorozat["hossz"] = line
        line = file.readline().strip()
        sorozat["latta"] = True if line == 1 else False
        sorozatok["sorozatok"].append(sorozat)
        line = file.readline().strip()
    else:
        folytat = False
file.close()
#print(sorozatok)
file = open("asdf.json","w",encoding = "utf-8")
json.dump(sorozatok,file,indent = 2)
file.close()
file = open("asdf.json","r")
adatok = json.load(file)
file.close()
for adat in adatok["sorozatok"]:
    print(adat)