def realizar_operacion(operador, num1, num2):
    if operador == '+':
        return num1 + num2
    elif operador == '-':
        return num1 - num2
    elif operador == '*':
        return num1 * num2
    elif operador == '/':
        if num2==0:
            return 'NO SE PUEDE DIVIDIR ENTRE 0'
        else:
            return num1 / num2
def evaluar_expresion(expresion, es_prefija=False):
    pila = []
    elementos = expresion.split()
    if es_prefija:
        elementos=elementos[::-1]
    for elemento in elementos:
        if elemento.isdigit():
            pila.append(int(elemento))
        else:
            numero2 = pila.pop()
            numero1 = pila.pop()
            resultado = realizar_operacion(elemento, numero1, numero2)
            pila.append(resultado)
    return pila.pop()
while True:
    print("\nMenú:")
    print("1. Evaluar expresión en notación posfija")
    print("2. Evaluar expresión en notación prefija")
    print("3. Salir")
    opcion = input("Elige una opción: ")
    if opcion == '1':
        expresion = input("Introduce la expresión en notación posfija (separada por espacios): ")
        resultado = evaluar_expresion(expresion)
        print("Resultado:", resultado)
    elif opcion == '2':
        expresion = input("Introduce la expresión en notación prefija (separada por espacios): ")
        resultado = evaluar_expresion(expresion, es_prefija=True)
        print("Resultado:", resultado)
    elif opcion == '3':
        print("Saliendo del programa.")
        break
    else:
        print("Opción no válida. Por favor, elige una opción del menú.")