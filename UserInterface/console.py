from Domain.rezervare import toString, getnume, getclasa, getpret, getcheckin
from Logic.CRUD import adaugarezervare, stergerezervare, modificarezervare, getbyid
from Logic.cerinte import cerinta4, cerinta5, cerinta6economyplus, cerinta6economy, cerinta6business, cerinta7, \
    cerinta8, Undo, Redo


def printmenu():
    print('1. Adauga rezervare')
    print('2. Sterge rezervare')
    print('3. Modifica rezervare')
    print('4. Trecerea tuturor rezervarilor la o clasa superioara')
    print('5. Ieftinirea tuturor rezervărilor la care s-a făcut checkin cu un procentaj citit')
    print('6. Determina prețul maxim pentru fiecare clasă')
    print('7. Odoneaza rezervarile in ordine descrescatoare dupa pret')
    print('8. Afișarea sumelor prețurilor pentru fiecare nume.')
    print('u. Undo')
    print('r. Redo')
    print('a. Afiseaza toate rezervarile')
    print('x. Iesire')

def UIadaugarezervare(lista ,undoList, redoList):
    try:
        id = input('Dati id-ul: ')
        nume = input('Dati un nume: ')
        clasa = input('Dati clasa: ')
        pret = float(input('Dati pretul: '))
        checkin = input('Dati checkin: ')
        rezultat = adaugarezervare(id, nume, clasa, pret, checkin, lista)
        undoList.append(lista)
        redoList.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def UIstergerezervare(lista, undoList ,redoList):
    try:
        id = input('Dati id-ul rezervarii pe care vreti sa o stergeti: ')

        rezultat = stergerezervare(id , lista)
        undoList.append(lista)
        redoList.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista

def UImodificarezervare(lista, undoList, redoList):
    try:
        id = input('Dati id-ul rezervarii de modificat: ')
        nume = input('Dati numele rezervarii de modificat: ')
        clasa = input('Dati clasa rezervarii de modificat: ')
        pret = float(input('Dati pretul rezervarii de modificat: '))
        checkin = input('Dati checkin-ul rezervarii de modificat: ')
        rezultat =  modificarezervare(id, nume, clasa, pret, checkin, lista)
        undoList.append(lista)
        redoList.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def showall(lista):
    for rezervare in lista:
        print(toString(rezervare))


def uicerinta5(lista, undoList, redoList):
    try:
        procentaj = int(input('Dati un procentaj cu care sa se reduca preturile celor care au checkin ul facut: '))
        result = cerinta5(lista, procentaj)
        undoList.append(lista)
        redoList.clear()
        return result
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def uicerinta6(lista):
    print('Pretul maxim de la economy este: {}'.format(cerinta6economy(lista)))
    print('Pretul maxim de la economy plus este: {} '.format(cerinta6economyplus(lista)))
    print('Pretul maxim de la business este: {} '.format(cerinta6business(lista)))


def uicerinta8(lista, undoList, redoList):
    try:
        result = cerinta8(lista)
        undoList.append(lista)
        redoList.clear()
        return result
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def uicerinta4(lista, undoList, redoList):
    try:
        nume = input("Dati un nume: ")
        result = cerinta4(lista, nume)
        undoList.append(lista)
        redoList.clear()
        return result
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def uicerinta7(lista, undoList, redoList):
    try:
        result = cerinta7(lista)
        undoList.append(lista)
        redoList.clear()
        return result
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista

def runmenu(lista):
    undoList = []
    redoList =[]
    while True:
        printmenu()
        optiune = input('Dati optiunea: ')
        if optiune == '1':
            lista = UIadaugarezervare(lista, undoList ,redoList)
        elif optiune == '2':
            lista = UIstergerezervare(lista, undoList ,redoList)
        elif optiune == '3':
            lista = UImodificarezervare(lista, undoList ,redoList)
        elif optiune == '4':
            lista =uicerinta4(lista, undoList, redoList)
        elif optiune == '5':
            lista=uicerinta5(lista, undoList, redoList)
        elif optiune == '6':
            uicerinta6(lista)
        elif optiune == '7':
            lista = uicerinta7(lista, undoList, redoList)
        elif optiune == '8':
            uicerinta8(lista, undoList, redoList)
        elif optiune == 'u':
            if len(undoList) > 0:
                redoList.append(lista)
                lista = undoList.pop()
            else:
                print("Nu se poate face undo!")
        elif optiune == 'r':
            if len(redoList) > 0:
                undoList.append(lista)
                lista = redoList.pop()
            else:
                print("Nu se poate face redo!")
        elif optiune == 'a':
            showall(lista)
        elif optiune == 'x':
            break
        else:
            print('Optiune gresita!. Reincercati')