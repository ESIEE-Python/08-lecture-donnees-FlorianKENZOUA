"""module exercice github sur les fichiers
"""

#### Imports et définition des variables globales

import csv

FILENAME = "listes.csv"

#### Fonctions secondaires

def read_data(filename):
    """retourne le contenu du fichier <filename>

    Args:
        filename (str): nom du fichier à lire

    Returns:
        list: le contenu du fichier (1 list par ligne)
    """
    with open(filename, mode='r', encoding='utf8') as fichier :
        liste = csv.reader(fichier, delimiter=';')
        data_provisoir = list(liste)
        data = []
        for liste in data_provisoir :
            data_liste =[]
            for element in liste :
                data_liste.append(int(element))
            data.append(data_liste)
    return data

def get_list_k(data, k):
    """retourne la k-ieme liste de la liste data

    Args : 
        data : liste de listes
        k : entier
    
    return :
    liste : k-ieme liste de data
    """
    liste = data[k]
    return liste

def get_first(l):
    """retourne le premier element de la liste

    Args : 
        l : liste
    
    return :
    element : int, premier element de liste
    """
    element = l[0]
    return element

def get_last(l):
    """retourne le dernier element de la liste

    Args : 
        l : liste
    
    return :
    element : int, dernier element de liste
    """
    element = l[-1]
    return element

def get_max(l):
    """retourne le plus grand element de la liste

    Args : 
        l : liste
    
    return :
    element : int, plus grand element de liste
    """
    element = max(l)
    return element

def get_min(l):
    """retourne le plus petit element de la liste

    Args : 
        l : liste
    
    return :
    element : int, plus petit element de liste
    """
    element = min(l)
    return element

def get_sum(l):
    """retourne la somme de tous les elements de la liste

    Args : 
        l : liste
    
    return :
    somme : int, somme des elements de liste
    """
    somme = 0
    for element in l :
        somme += element
    return somme


#### Fonction principale


def main():
    """retourne des tests sur nos fonctions secondaires
    """
    data = read_data(FILENAME)
    for i, l in enumerate(data):
        print(i, l)
    k = 37
    print(k, get_list_k(data, 37))


if __name__ == "__main__":
    main()
