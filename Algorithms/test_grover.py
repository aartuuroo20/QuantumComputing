
soluciones = open("soluciones.txt", "r")
soluciones = soluciones.read()

respuestas = open("respuestas.txt", "r")
respuestas = respuestas.read()


assert(soluciones == respuestas) #If the assertion is true, the test passes
print("Test passed") #If the assertion is false, the test fails