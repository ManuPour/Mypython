lista = [4, 7, 2, 3, 6, 1, 8, 5, 13, 16, 19]
target = 12

def summa12(lista, target):
    resultat_lista = []
    antalsokningar = 0

    for i in range(len(lista)-1):
        antalsokningar += 1
        for j in range(i+1, len(lista)):

            if lista[i] + lista[j] == target:
                resultat_lista = lista[i], lista[j]
                print("Tal i listan som är summan eller lika med target:", resultat_lista)
                return 'Antal sökningar är:', antalsokningar
            elif target == lista[i]:
                resultat_lista = lista[i]
                print("Tal i listan som är summan eller lika med target:", resultat_lista)
                return 'Antal sökningar är:', antalsokningar
    return

print(summa12(lista, target))
