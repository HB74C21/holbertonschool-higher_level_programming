#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        for i in range(x):
            if isinstance(my_list[i], int):
                print("{:d}".format(my_list[i]), end="")
                count += 1
        print()  # Ajoutez cette ligne pour imprimer une nouvelle ligne après l'affichage des entiers
    except IndexError:
        pass
    return count
