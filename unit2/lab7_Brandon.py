def nombres(mensaje):
    while True:
        entrada = input(mensaje).strip()
        
        if entrada == "":
            print("Error: El nombre no puede estar vacío.")
        elif entrada.replace(" ", "").isalpha() == False:
            print("Error: El nombre solo debe contener letras (sin números ni caracteres especiales).")
        else:
            return " ".join(entrada.split())

def calificaciones(materia):
    while True:
        entrada = input(f"{materia}: ").strip()
        
        if entrada == "":
            print("Error: El campo no puede estar vacío.")
        elif entrada.isdigit() == False:
            print("Error: Debes ingresar un número entero (positivo, sin letras ni decimales).")
        else:
            calificacion = int(entrada)
            if calificacion >= 0 and calificacion <= 100:
                return calificacion
            else:
                print("Error: La calificación debe estar en el rango de 0 a 100.")

def main():
    print("=== REGISTRO DE ESTUDIANTE ===")
    
    student = {
        "name": nombres("Nombre: "),
        "programming": calificaciones("Programming"),
        "design": calificaciones("Design"),
        "networking": calificaciones("Networking"),
        "data_analysis": calificaciones("Data Analysis")
    }
    
    print("\nName:", student["name"])
    print("Programming:", student["programming"])
    print("Design:", student["design"])
    print("Networking:", student["networking"])
    print("Data Analysis:", student["data_analysis"])
    
    carreras = {
        "programming": "Software Developer",
        "design": "UI/UX Designer",
        "networking": "Network Administrator",
        "data_analysis": "Data Analyst"
    }
    
    high_grade = "programming"
    empate = False
    
    if student["design"] > student[high_grade]:
        high_grade = "design"
        empate = False
    elif student["design"] == student[high_grade]:
        empate = True
        
    if student["networking"] > student[high_grade]:
        high_grade = "networking"
        empate = False
    elif student["networking"] == student[high_grade]:
        empate = True
        
    if student["data_analysis"] > student[high_grade]:
        high_grade = "data_analysis"
        empate = False
    elif student["data_analysis"] == student[high_grade]:
        empate = True
        
    print("\n-----------------------------------")
    if empate:
        print("Recommended Career: Multiple Career Paths Identified")
    else:
        print("Recommended Career:", carreras[high_grade])

if __name__ == "__main__":
    main()
