# Calculatrice simple avec historique

historique = []

def ajouter_a_historique(operation, resultat):
    historique.append(f"{operation} = {resultat}")

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Erreur : division par zéro"
    return a / b


while True:
    print("\n1. Addition")
    print("2. Soustraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Historique")
    print("6. Clear historique")
    print("7. Quitter")


    choix = input("Choisissez une option (1-7) : ")

    if choix == "7":
        break

    if choix == "6":
        fichier = open("historique.txt" , "w")
        fichier.close
        continue

    if choix == "5":
        print("\nHistorique")
        if not historique:
            print("\nAucun calcul effectué.")
        else:
            for calcul in historique:
                print(f"\n{calcul}")
        continue

    try:
        num1 = float(input("Entrez le premier nombre : "))
        num2 = float(input("Entrez le deuxième nombre : "))
    except ValueError:
        print("Erreur : veuillez entrer des nombres valides.")
        continue


    if choix == "1":
        resultat = add(num1, num2)
        operation = (f"{num1} + {num2}")
    elif choix == "2":
        resultat = subtract(num1, num2)
        operation = (f"{num1} - {num2}")
    elif choix == "3":
        resultat = multiply(num1, num2)
        operation = (f"{num1} * {num2}")
    elif choix == "4":
        resultat = divide(num1, num2)
        operation = (f"{num1} / {num2}")
    else:
        print("Choix invalide.")
        continue

    print(f"Résultat : {resultat}")
    ajouter_a_historique(operation, resultat)

    fichier = open("historique.txt" , "a")
    fichier.write(f"{resultat}\n")
    fichier.close
