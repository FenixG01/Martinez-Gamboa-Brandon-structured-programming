def menu():
    print("\n=== ENEVAB50 ===")
    print("Seleccione un género:")
    print("1. Anime")
    print("2. Romance")
    print("3. Aventura")
    print("4. Thriller")
    print("5. Trágico")
    print("6. Salir")


def get_gen():
    try:
        opt = int(input("Opción: "))
        return opt
    except ValueError:
        return 0


def recom(gen):
    print("Recomendaciones:")
    match gen:
        case 1:
            print("- Demon Slayer")
            print("- Jujutsu Kaisen")
            print("- Chainsaw Man")
            print("- My Hero Academia")
        case 2:
            print("- Kaguya-sama: Love is War")
            print("- Toradora!")
            print("- Horimiya")
            print("- My Dress-Up Darling")
        case 3:
            print("- One Piece")
            print("- Attack on Titan")
            print("- Hunter x Hunter")
            print("- Black Clover")
        case 4:
            print("- Death Note")
            print("- Monster")
            print("- Cyberpunk: Edgerunners")
            print("- Steins;Gate")
        case 5:
            print("- Your Lie in April")
            print("- Anohana")
            print("- Cyberpunk: Edgerunners")
            print("- Violet Evergarden")
        case _:
            print("No hay recomendaciones disponibles.")


def main():
    while True:
        menu()
        gen = get_gen()
        
        if gen == 6:
            print("Gracias por usar ENEVAB50. ¡Adiós!")
            break
            
        if gen in [1, 2, 3, 4, 5]:
            recom(gen)
        else:
            print("Opción inválida. Intente de nuevo.")
            continue
        
        ans = input("¿Desea realizar otra búsqueda? (Y/N): ").strip().upper()
        if ans != 'Y':
            print("Gracias por usar ENEVAB50. ¡Adiós!")
            break


if __name__ == "__main__":
    main()