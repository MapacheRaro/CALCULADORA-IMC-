def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

def clasificacion_imc(imc):
    if imc < 18.5:
        return "Bajo peso"
    elif 18.5 <= imc < 24.9:
        return "Peso normal"
    elif 25 <= imc < 29.9:
        return "Sobrepeso"
    else:
        return "Obesidad"

peso = float(input("Introduce tu peso en kg: "))
altura = float(input("Introduce tu altura en metros: "))

imc = calcular_imc(peso, altura)
clasificacion = clasificacion_imc(imc)

print(f"Tu IMC es: {imc:.2f}")
print(f"Clasificación: {clasificacion}")
