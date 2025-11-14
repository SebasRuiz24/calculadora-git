print("Bienvenido a la calculadora desarrollada en Git para el taller")

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error: no se puede dividir entre cero"
    return a / b

print("=== CALCULADORA BÁSICA ===")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")

op = input("Seleccione una opcion (1-4): ").strip()

a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))

if op == "1":
    print("Resultado:", suma(a, b))
elif op == "2":
    print("Resultado:", resta(a, b))
elif op == "3":
    print("Resultado:", multiplicacion(a, b))
elif op == "4":
    print("Resultado:", division(a, b))
else:
    print("Opción inválida")
