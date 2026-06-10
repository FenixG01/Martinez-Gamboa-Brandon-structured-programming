def main():
    name = input("Nombre: ")
    
    student = {
        "name": name,
        "programming": int(input("Programming: ")),
        "design": int(input("Design: ")),
        "networking": int(input("Networking: ")),
        "data_analysis": int(input("Data Analysis: "))
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
    
 
    materia_mas_alta = "programming"
    s = False
    
    if student["design"] > student[materia_mas_alta]:
        materia_mas_alta = "design"
        tie = False
    elif student["design"] == student[materia_mas_alta]:
        tie = True
        
    if student["networking"] > student[materia_mas_alta]:
        materia_mas_alta = "networking"
        tie = False
    elif student["networking"] == student[materia_mas_alta]:
        tie = True
        
    if student["data_analysis"] > student[materia_mas_alta]:
        materia_mas_alta = "data_analysis"
        tie = False
    elif student["data_analysis"] == student[materia_mas_alta]:
        tie = True
        
   
    if tie:
        print("Recommended Career: Multiple Career Paths Identified")
    else:
        print("Recommended Career:", carreras[materia_mas_alta])

if __name__ == "__main__":
    main()