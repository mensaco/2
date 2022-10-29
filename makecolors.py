import json
import os

for i in range(20):
    print()



menyrat = {
    "deftore" : 210,
    "habitore" : 190,
    "lidhore" : 150,
    "kushtore" : 120,
    "deshirore" : 60,
    "urdherore" : 360,
    "format_e_pashtjelluara" : 240,
    "zgjedhimi_e_forma" : 90
}
lights = [200, 300, 800]



for key in menyrat:
    #for i in range(len(lights)):
        #l = "--tw-" + key.replace("_","-") + "-" + str(lights[i]) + ": hsl(" + str(menyrat[key]) + ", 100%, " + str(int((1000-lights[i])/10)) + "%);"
        l = "--tw-" + key.replace("_","-") + "-h:" + str(menyrat[key]) + ";"
        #l = key + ":" + str(lights[i])
        print(l)


