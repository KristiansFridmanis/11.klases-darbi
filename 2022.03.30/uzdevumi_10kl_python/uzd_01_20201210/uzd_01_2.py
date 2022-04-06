# Izveidot programmu, kura prasa lietotâjam ievadît cilindra râdiusu un tâ augstumu, tiek aprçíinâts cilindra laukums un tilpums. Rezultâts tiek parâdîts konsolç.
# tilpums = 3.14 * râdiuss * râdiuss * augstums
# laukums = 2 * (3.14 * râdiuss * râdiuss) + augstums * (2 * 3.14 * râdiuss)



rad = float(input("ievadi radiusu:"))
aug = float(input("ievadi augstumu:"))

tilpums= 3.14*rad*rad*aug
laukums= 2*(3.14*rad*rad)+aug*(2*3.14*rad)

print("tilpums ir: ", tilpums, "un laukums ir: ", laukums )