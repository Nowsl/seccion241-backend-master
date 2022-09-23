#salida de datos
print("escribe tu nombre")
#entrada de datos   
miVariable= input()
#salida de datos
print("mi nombre es: "+miVariable)
#entrada
edad= int(input("Escribe tu edad "))
print("Tu edad es:" +str(edad)+" Años")
#proceso
edad = int(edad)+1
edad += 1 #equivalente al anterior
print("En 2 años más tendras "+str(edad))

#se puede realizar muchos if, pero es ineficiente
if(edad>18):
    print("Es mayor de edad ")
if(edad==18):
    print("cumplio la mayoria de edad ")
if(edad<18):
    print("Es menor de edad ")
#otra alternativa
if(edad>18):
    print("es mayor de edad ")
    if(edad>65):
        print("es adulto mayor ")
else:
    if(edad<5):
        print("es infante ")
    print("es menor de edad ")   
print("Fin del programa ")           
i=0
while(i<10):
    print("ciclo ")
    i=i+1 #i+=1 es equivalente