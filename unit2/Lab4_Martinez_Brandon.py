ot = "si"

while ot == "si":
    name = input("Enter your name: ").lower()
    lst = input("Enter your last name: ").lower()
    lst2 = input("Enter your second last name: ").lower()

    def gen_em(name, lst, lst2):
        email = lst + lst2 + "@utd.edu.mx"
        return email

    generated_email = gen_em(name, lst, lst2)

    print("Your email is:", generated_email)
    print("-" * 30)
    
    ot = input("Desea volver a ejecutar el programa? (si/no): ").lower()

    def calcular_tiempo(gb, mbps):
    segundos = (gb * 8192) / mbps
    return segundos

ot = "si"

while ot == "si":
    try:
        tam = float(input("Tamaño del archivo (GB): "))
        velocidad = float(input("Velocidad (Mbps): "))
        
        segundos_totales = calcular_tiempo(tam, velocidad)
        
        print(f"Tiempo estimado: {segundos_totales:.2f} segundos.")
        
    except ValueError:
        print("Error: Ingresa solo números.")
    
    print("-" * 30)
    ot = input("¿Desea calcular otro tiempo? (si/no): ").lower()