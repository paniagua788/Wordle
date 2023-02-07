def verificar_palabra(palabra_secreta, chance):
    palabra_list = []
    contador = 0
    acertaste = False
    while chance > 0 and acertaste == False:
        palabra_ingresada = input()
        contador = 0
        for i in range(len(palabra_secreta)):
            if palabra_ingresada[i] == palabra_secreta[i]:
                palabra_list.append("[" + palabra_ingresada[i] + "]")
                contador += 1
            elif palabra_ingresada[i] in palabra_secreta:
                palabra_list.append("(" + palabra_ingresada[i] + ")")
            else:
                palabra_list.append(palabra_ingresada[i])
            if contador == len(palabra_secreta):
                acertaste = True
                
        print(palabra_list)
        
        palabra_list = []
        chance = chance - 1
    return acertaste
        
        
intentos = 3
secret_word = "movil"
print(f"Bienvenido a Wordle, tenes {intentos} intentos para acertar. A continuacion, ingrese una palabra:")
if verificar_palabra(secret_word, intentos) == True:
    print("Felicidades Acertaste!!")
else:
    print("Más suerte la próxima")