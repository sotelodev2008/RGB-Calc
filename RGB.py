from sys import exit as getout
print("1. English\n2. Español")
try:
    lang = int(input("Choose your language/Elije Tu Idioma: "))
except ValueError:
    print("You need to use one of the 2 valid options, no characters\nDebes usar una de las 2 opciones permitidas, nada de letras")
    getout()
if lang == 1:
    print("\nImGui Color Calculator")

    r = int(input("Give me the quantity of red: "))
    g = int(input("Give me the quantity of green: "))
    b = int(input("Give me the quantity of blue: "))

    print("The red color quantity is: ", ((r*100)/256)/100)
    print("The green color quantity is: ", ((g*100)/256)/100)
    print("The blue color quantity is:", ((b*100)/256)/100)
if lang == 2:
    print("\nCalculador de colores ImGui")

    r = int(input("Dame el color rojo: "))
    g = int(input("Dame el color verde: "))
    b = int(input("Dame el color azul: "))

    print("El color rojo es: ", ((r*100)/256)/100)
    print("El color verde es: ", ((g*100)/256)/100)
    print("El color azul es:", ((b*100)/256)/100)
else:
    print("You need to use one of the two valid options\nDebes usar una de las 2 opciones permitidas")
