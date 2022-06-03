#Declaramos una variable
calificacion = input("Introduce tu calificacion del AZ-900: ")

calificacion = int(calificacion)

# Preguntamos si la calificacion es menor a 700
if calificacion < 700 :
    print("vess, por no estudiar") # Si es menor a 700 muestra esto
elif calificacion == 700 :
    print("PANZAZOOO")
elif calificacion > 1000 :
    print("MIENTES!!! No puedes sacar mas de mil")
else : # si no se cumple el if anterior pasa a esta linea
    print("Felicidades, pasa por tu certificdo") #se ejecuta si ninguno de los if se cumple
